# ============================================================
# FILE: src/rag/store.py
# ============================================================

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

import chromadb
import requests


# ============================================================
# PROJECT CONFIGURATION
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

CHROMA_PATH = (
    PROJECT_ROOT
    / "data"
    / "chroma"
)

OLLAMA_BASE_URL = "http://localhost:11434"

# Local embedding model.
#
# Install once:
#
#     ollama pull nomic-embed-text
#
EMBEDDING_MODEL = "nomic-embed-text"

EMBEDDING_TIMEOUT = 60


# ============================================================
# COLLECTION NAMES
# ============================================================

CHUNKS_COLLECTION = "audio_chunks_v3"

OBSERVATIONS_COLLECTION = "audio_observations_v3"

DECISIONS_COLLECTION = "audio_decisions_v3"


# ============================================================
# LOCAL OLLAMA EMBEDDER
# ============================================================

class LocalOllamaEmbedder:
    """
    Local embedding client for Ollama.

    Primary endpoint:
        POST /api/embed

    Legacy fallback:
        POST /api/embeddings

    The modern /api/embed endpoint is preferred because current
    Ollama versions expose embedding generation through this API.

    This class intentionally performs no external API calls.
    Everything remains local.
    """

    def __init__(
        self,
        base_url: str = OLLAMA_BASE_URL,
        model: str = EMBEDDING_MODEL,
        timeout: int = EMBEDDING_TIMEOUT,
    ):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout

        # Modern Ollama endpoint.
        self.embed_url = (
            f"{self.base_url}/api/embed"
        )

        # Older Ollama endpoint.
        self.legacy_embedding_url = (
            f"{self.base_url}/api/embeddings"
        )

    # ========================================================
    # NORMALIZE EMBEDDING RESPONSE
    # ========================================================

    @staticmethod
    def _extract_embedding(
        data: Dict[str, Any],
    ) -> List[float]:
        """
        Extract a single embedding vector from an Ollama
        response.

        Supported response shapes:

        Modern /api/embed:

            {
                "embeddings": [
                    [0.1, 0.2, ...]
                ]
            }

        Legacy /api/embeddings:

            {
                "embedding": [
                    0.1,
                    0.2,
                    ...
                ]
            }
        """

        # ----------------------------------------------------
        # Modern API
        # ----------------------------------------------------

        embeddings = data.get("embeddings")

        if isinstance(embeddings, list):

            if not embeddings:
                raise ValueError(
                    "Ollama returned an empty "
                    "'embeddings' array."
                )

            first = embeddings[0]

            if isinstance(first, list):

                return [
                    float(value)
                    for value in first
                ]

            # Some implementations may return a flat list.
            if all(
                isinstance(
                    value,
                    (int, float),
                )
                for value in embeddings
            ):

                return [
                    float(value)
                    for value in embeddings
                ]

        # ----------------------------------------------------
        # Legacy API
        # ----------------------------------------------------

        embedding = data.get("embedding")

        if isinstance(
            embedding,
            list,
        ):

            return [
                float(value)
                for value in embedding
            ]

        raise ValueError(
            "Ollama response does not contain "
            "a valid embedding vector."
        )

    # ========================================================
    # MODERN EMBEDDING ENDPOINT
    # ========================================================

    def _embed_modern(
        self,
        text: str,
    ) -> List[float]:

        payload = {
            "model": self.model,
            "input": text,
        }

        response = requests.post(
            self.embed_url,
            json=payload,
            timeout=self.timeout,
        )

        response.raise_for_status()

        data = response.json()

        return self._extract_embedding(
            data
        )

    # ========================================================
    # LEGACY EMBEDDING ENDPOINT
    # ========================================================

    def _embed_legacy(
        self,
        text: str,
    ) -> List[float]:

        payload = {
            "model": self.model,
            "prompt": text,
        }

        response = requests.post(
            self.legacy_embedding_url,
            json=payload,
            timeout=self.timeout,
        )

        response.raise_for_status()

        data = response.json()

        return self._extract_embedding(
            data
        )

    # ========================================================
    # PUBLIC EMBEDDING METHOD
    # ========================================================

    def embed(
        self,
        text: str,
    ) -> List[float]:
        """
        Generate one semantic embedding.

        Modern Ollama endpoint is attempted first.

        If the modern endpoint is unavailable, the legacy
        endpoint is attempted as a compatibility fallback.

        Raises RuntimeError if neither endpoint succeeds.
        """

        text = str(text).strip()

        if not text:
            text = "empty audio observation"

        modern_error = None

        # ----------------------------------------------------
        # Attempt 1: modern /api/embed
        # ----------------------------------------------------

        try:

            embedding = self._embed_modern(
                text
            )

            if not embedding:
                raise ValueError(
                    "Modern Ollama embedding "
                    "returned an empty vector."
                )

            return embedding

        except Exception as exc:

            modern_error = exc

            print(
                "[Embedding] Modern endpoint "
                "/api/embed failed."
            )

            print(
                f"[Embedding] Reason: {exc}"
            )

        # ----------------------------------------------------
        # Attempt 2: legacy /api/embeddings
        # ----------------------------------------------------

        try:

            embedding = self._embed_legacy(
                text
            )

            if not embedding:
                raise ValueError(
                    "Legacy Ollama embedding "
                    "returned an empty vector."
                )

            print(
                "[Embedding] Legacy endpoint "
                "/api/embeddings succeeded."
            )

            return embedding

        except Exception as legacy_error:

            raise RuntimeError(
                "Unable to generate Ollama embedding.\n"
                f"Modern endpoint error: {modern_error}\n"
                f"Legacy endpoint error: {legacy_error}"
            ) from legacy_error


# ============================================================
# AUDIO RAG STORE
# ============================================================

class AudioRAGStore:
    """
    Persistent local ChromaDB evidence store.

    Architectural rule:

        OBSERVATIONS = evidence

        DECISIONS = conclusions

    Decisions are NEVER retrieved as evidence.

    Semantic retrieval is performed over actual historical
    audio observations belonging to the same student.
    """

    def __init__(
        self,
        persist_directory: Optional[str] = None,
        ollama_base_url: str = OLLAMA_BASE_URL,
        embedding_model: str = EMBEDDING_MODEL,
    ):

        self.persist_directory = Path(
            persist_directory
            if persist_directory
            else CHROMA_PATH
        )

        self.persist_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        # ====================================================
        # CHROMADB
        # ====================================================

        self.client = chromadb.PersistentClient(
            path=str(
                self.persist_directory
            )
        )

        # ====================================================
        # LOCAL EMBEDDING CLIENT
        # ====================================================

        self.embedder = LocalOllamaEmbedder(
            base_url=ollama_base_url,
            model=embedding_model,
        )

        # ====================================================
        # COLLECTIONS
        # ====================================================

        self.chunks = (
            self.client.get_or_create_collection(
                name=CHUNKS_COLLECTION
            )
        )

        self.observations = (
            self.client.get_or_create_collection(
                name=OBSERVATIONS_COLLECTION
            )
        )

        self.decisions = (
            self.client.get_or_create_collection(
                name=DECISIONS_COLLECTION
            )
        )

    # ========================================================
    # SERIALIZATION HELPERS
    # ========================================================

    @staticmethod
    def _safe_string(
        value: Any,
    ) -> str:

        if value is None:
            return ""

        if isinstance(
            value,
            str,
        ):
            return value

        try:

            return json.dumps(
                value,
                ensure_ascii=False,
                sort_keys=True,
                default=str,
            )

        except Exception:

            return str(value)

    @staticmethod
    def _safe_metadata(
        metadata: Dict[str, Any],
    ) -> Dict[str, Any]:

        result = {}

        for key, value in metadata.items():

            if value is None:
                continue

            if isinstance(
                value,
                (
                    str,
                    int,
                    float,
                    bool,
                ),
            ):

                result[str(key)] = value

            else:

                result[str(key)] = str(value)

        return result

    # ========================================================
    # BUILD SEMANTIC DOCUMENT
    # ========================================================

    @staticmethod
    def build_observation_document(
        student_id: str,
        audio_file_id: str,
        chunk_id: str,
        chunk_index: int,
        start_timestamp: float,
        end_timestamp: float,
        event: str,
        confidence: float,
        analysis: Dict[str, Any],
    ) -> str:
        """
        Convert a structured audio observation into the text
        representation that will be embedded.

        The document contains actual acoustic evidence and
        detector information.

        Agent conclusions are intentionally excluded.
        """

        acoustic_features = {}

        if isinstance(
            analysis,
            dict,
        ):

            feature_keys = [
                "rms",
                "rms_db",
                "zcr",
                "spectral_centroid",
                "spectral_bandwidth",
                "spectral_rolloff",
            ]

            for key in feature_keys:

                if key in analysis:

                    acoustic_features[key] = (
                        analysis[key]
                    )

        acoustic_json = json.dumps(
            acoustic_features,
            ensure_ascii=False,
            sort_keys=True,
            default=str,
        )

        document = (
            f"Student ID: {student_id}\n"
            f"Audio file: {audio_file_id}\n"
            f"Chunk: {chunk_id}\n"
            f"Chunk index: {chunk_index}\n"
            f"Time: {start_timestamp:.3f} "
            f"to {end_timestamp:.3f} seconds\n"
            f"Detected audio event: {event}\n"
            f"Detector confidence: {confidence:.3f}\n"
            f"Acoustic evidence: {acoustic_json}"
        )

        return document

    # ========================================================
    # REGISTER CHUNKS
    # ========================================================

    def register_chunks(
        self,
        chunks: List[Dict[str, Any]],
        audio_file_id: str,
        student_id: str,
    ) -> None:

        if not chunks:
            return

        ids = []

        documents = []

        metadatas = []

        for chunk in chunks:

            chunk_id = str(
                chunk["chunk_id"]
            )

            ids.append(
                chunk_id
            )

            document = (
                f"Student ID: {student_id}\n"
                f"Audio file: {audio_file_id}\n"
                f"Chunk: {chunk_id}\n"
                f"Chunk index: "
                f"{chunk.get('chunk_index', 0)}\n"
                f"Time: "
                f"{chunk.get('start_timestamp', 0.0)} "
                f"to "
                f"{chunk.get('end_timestamp', 0.0)} seconds"
            )

            documents.append(
                document
            )

            metadata = {
                "student_id": str(
                    student_id
                ),
                "audio_file_id": str(
                    audio_file_id
                ),
                "chunk_id": chunk_id,
                "chunk_index": int(
                    chunk.get(
                        "chunk_index",
                        0,
                    )
                ),
                "start_timestamp": float(
                    chunk.get(
                        "start_timestamp",
                        0.0,
                    )
                ),
                "end_timestamp": float(
                    chunk.get(
                        "end_timestamp",
                        0.0,
                    )
                ),
                "duration": float(
                    chunk.get(
                        "duration",
                        0.0,
                    )
                ),
                "storage_path": str(
                    chunk.get(
                        "storage_path",
                        "",
                    )
                ),
                "processing_status": str(
                    chunk.get(
                        "processing_status",
                        "PENDING",
                    )
                ),
            }

            metadatas.append(
                self._safe_metadata(
                    metadata
                )
            )

        self.chunks.upsert(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
        )

    # ========================================================
    # UPSERT CHUNK + OBSERVATION
    # ========================================================

    def upsert_chunk(
        self,
        chunk: Dict[str, Any],
        analysis: Optional[
            Dict[str, Any]
        ] = None,
        student_id: Optional[str] = None,
    ) -> None:

        resolved_student_id = str(
            student_id
            or chunk.get(
                "student_id",
                "unknown_student",
            )
        )

        audio_file_id = str(
            chunk.get(
                "audio_file_id",
                "",
            )
        )

        chunk_id = str(
            chunk["chunk_id"]
        )

        # ====================================================
        # STRUCTURAL CHUNK RECORD
        # ====================================================

        chunk_metadata = {
            "student_id": resolved_student_id,
            "audio_file_id": audio_file_id,
            "chunk_id": chunk_id,
            "chunk_index": int(
                chunk.get(
                    "chunk_index",
                    0,
                )
            ),
            "start_timestamp": float(
                chunk.get(
                    "start_timestamp",
                    0.0,
                )
            ),
            "end_timestamp": float(
                chunk.get(
                    "end_timestamp",
                    0.0,
                )
            ),
            "duration": float(
                chunk.get(
                    "duration",
                    0.0,
                )
            ),
            "storage_path": str(
                chunk.get(
                    "storage_path",
                    "",
                )
            ),
            "processing_status": str(
                chunk.get(
                    "processing_status",
                    "PENDING",
                )
            ),
        }

        chunk_document = (
            f"Student ID: {resolved_student_id}\n"
            f"Audio file: {audio_file_id}\n"
            f"Chunk ID: {chunk_id}\n"
            f"Chunk index: "
            f"{chunk_metadata['chunk_index']}\n"
            f"Timestamp: "
            f"{chunk_metadata['start_timestamp']}"
            f"-"
            f"{chunk_metadata['end_timestamp']}"
        )

        self.chunks.upsert(
            ids=[chunk_id],
            documents=[chunk_document],
            metadatas=[
                self._safe_metadata(
                    chunk_metadata
                )
            ],
        )

        # ====================================================
        # NO ANALYSIS = NO OBSERVATION
        # ====================================================

        if analysis is None:
            return

        # ====================================================
        # OBSERVATION
        # ====================================================

        event = str(
            analysis.get(
                "event",
                "OTHER",
            )
        )

        confidence = float(
            analysis.get(
                "confidence",
                0.0,
            )
        )

        observation_document = (
            self.build_observation_document(
                student_id=resolved_student_id,
                audio_file_id=audio_file_id,
                chunk_id=chunk_id,
                chunk_index=int(
                    chunk.get(
                        "chunk_index",
                        0,
                    )
                ),
                start_timestamp=float(
                    chunk.get(
                        "start_timestamp",
                        0.0,
                    )
                ),
                end_timestamp=float(
                    chunk.get(
                        "end_timestamp",
                        0.0,
                    )
                ),
                event=event,
                confidence=confidence,
                analysis=analysis,
            )
        )

        observation_metadata = {
            "student_id": resolved_student_id,
            "audio_file_id": audio_file_id,
            "chunk_id": chunk_id,
            "chunk_index": int(
                chunk.get(
                    "chunk_index",
                    0,
                )
            ),
            "start_timestamp": float(
                chunk.get(
                    "start_timestamp",
                    0.0,
                )
            ),
            "end_timestamp": float(
                chunk.get(
                    "end_timestamp",
                    0.0,
                )
            ),
            "event": event,
            "confidence": confidence,
            "processing_status": str(
                chunk.get(
                    "processing_status",
                    "COMPLETED",
                )
            ),
            "analysis_json": self._safe_string(
                analysis
            ),
        }

        # ====================================================
        # EMBEDDING
        # ====================================================

        try:

            embedding = self.embedder.embed(
                observation_document
            )

        except Exception as exc:

            # ------------------------------------------------
            # IMPORTANT:
            #
            # Do not destroy the entire ReAct pipeline just
            # because semantic embedding failed.
            #
            # The structural chunk remains stored.
            # ------------------------------------------------

            print(
                "[RAG] WARNING: Could not generate "
                "semantic embedding."
            )

            print(
                f"[RAG] Reason: {exc}"
            )

            print(
                "[RAG] Observation will not be "
                "inserted into semantic collection."
            )

            return

        # ====================================================
        # STORE OBSERVATION
        # ====================================================

        self.observations.upsert(
            ids=[chunk_id],
            embeddings=[embedding],
            documents=[
                observation_document
            ],
            metadatas=[
                self._safe_metadata(
                    observation_metadata
                )
            ],
        )

        print(
            "[RAG] Observation stored "
            f"successfully: {chunk_id}"
        )

    # ========================================================
    # SEMANTIC SEARCH
    # ========================================================

    def semantic_search(
        self,
        query_text: str,
        student_id: str,
        current_chunk_id: Optional[str] = None,
        current_audio_file_id: Optional[str] = None,
        top_k: int = 5,
    ) -> List[Dict[str, Any]]:
        """
        Semantic search over historical AUDIO OBSERVATIONS.

        Rules:

        1. Same student only.
        2. Current chunk excluded.
        3. Decisions are never searched.
        4. Historical observations are the evidence source.

        The current audio file is NOT automatically excluded,
        because earlier chunks from the same recording can be
        useful temporal evidence.
        """

        # ====================================================
        # QUERY EMBEDDING
        # ====================================================

        try:

            query_embedding = (
                self.embedder.embed(
                    query_text
                )
            )

        except Exception as exc:

            print(
                "[RAG] Semantic search failed "
                "during embedding."
            )

            print(
                f"[RAG] Reason: {exc}"
            )

            return []

        # ====================================================
        # STUDENT FILTER
        # ====================================================

        where_filter: Dict[str, Any] = {
            "student_id": str(
                student_id
            )
        }

        # ====================================================
        # CHROMA QUERY
        # ====================================================

        try:

            results = (
                self.observations.query(
                    query_embeddings=[
                        query_embedding
                    ],
                    n_results=max(
                        int(top_k),
                        1,
                    ),
                    where=where_filter,
                    include=[
                        "documents",
                        "metadatas",
                        "distances",
                    ],
                )
            )

        except Exception as exc:

            print(
                "[RAG] ChromaDB semantic "
                "search failed:"
            )

            print(
                f"[RAG] Reason: {exc}"
            )

            return []

        # ====================================================
        # EXTRACT RESULTS
        # ====================================================

        documents = (
            results.get(
                "documents",
                [[]],
            )[0]
            or []
        )

        metadatas = (
            results.get(
                "metadatas",
                [[]],
            )[0]
            or []
        )

        distances = (
            results.get(
                "distances",
                [[]],
            )[0]
            or []
        )

        output = []

        # ====================================================
        # BUILD OUTPUT
        # ====================================================

        for index, metadata in enumerate(
            metadatas
        ):

            metadata = dict(
                metadata or {}
            )

            chunk_id = str(
                metadata.get(
                    "chunk_id",
                    "",
                )
            )

            # -----------------------------------------------
            # Never retrieve the current chunk.
            # -----------------------------------------------

            if (
                current_chunk_id
                and chunk_id
                == str(
                    current_chunk_id
                )
            ):

                continue

            document = (
                documents[index]
                if index < len(documents)
                else ""
            )

            distance = (
                float(
                    distances[index]
                )
                if index < len(distances)
                else None
            )

            # -----------------------------------------------
            # Chroma distance:
            #
            # lower = more similar
            #
            # This is only a normalized reporting value.
            # It is NOT treated as detector confidence.
            # -----------------------------------------------

            similarity = None

            if distance is not None:

                similarity = (
                    1.0
                    / (
                        1.0
                        + max(
                            distance,
                            0.0,
                        )
                    )
                )

            output.append(
                {
                    "student_id": metadata.get(
                        "student_id"
                    ),
                    "audio_file_id": metadata.get(
                        "audio_file_id"
                    ),
                    "chunk_id": metadata.get(
                        "chunk_id"
                    ),
                    "chunk_index": metadata.get(
                        "chunk_index"
                    ),
                    "start_timestamp": metadata.get(
                        "start_timestamp"
                    ),
                    "end_timestamp": metadata.get(
                        "end_timestamp"
                    ),
                    "event": metadata.get(
                        "event"
                    ),
                    "confidence": metadata.get(
                        "confidence"
                    ),
                    "processing_status": metadata.get(
                        "processing_status"
                    ),
                    "similarity": similarity,
                    "distance": distance,
                    "document": document,
                    "analysis": self._parse_analysis(
                        metadata.get(
                            "analysis_json"
                        )
                    ),
                }
            )

        return output

    # ========================================================
    # SEMANTIC CONTEXT HELPER
    # ========================================================

    def retrieve_semantic_context(
        self,
        student_id: str,
        current_chunk_id: str,
        current_audio_file_id: str,
        current_event: str,
        current_confidence: float,
        current_analysis: Dict[str, Any],
        top_k: int = 5,
    ) -> List[Dict[str, Any]]:
        """
        Build a semantic query from the current observation
        and retrieve historical evidence for the same student.
        """

        query_document = (
            self.build_observation_document(
                student_id=student_id,
                audio_file_id=current_audio_file_id,
                chunk_id=current_chunk_id,
                chunk_index=-1,
                start_timestamp=0.0,
                end_timestamp=0.0,
                event=current_event,
                confidence=current_confidence,
                analysis=current_analysis,
            )
        )

        return self.semantic_search(
            query_text=query_document,
            student_id=student_id,
            current_chunk_id=current_chunk_id,
            current_audio_file_id=current_audio_file_id,
            top_k=top_k,
        )

    # ========================================================
    # DECISION STORAGE
    # ========================================================

    def store_decision(
        self,
        decision: Dict[str, Any],
    ) -> None:

        decision_id = (
            f"{decision.get('audio_file_id', '')}"
            f"__"
            f"{decision.get('chunk_id', '')}"
        )

        document = self._safe_string(
            decision
        )

        metadata = {}

        for key, value in decision.items():

            if key in {
                "reasoning",
                "context_observations",
                "analysis_result",
            }:

                continue

            if value is None:
                continue

            if isinstance(
                value,
                (
                    str,
                    int,
                    float,
                    bool,
                ),
            ):

                metadata[key] = value

            else:

                metadata[key] = str(
                    value
                )

        self.decisions.upsert(
            ids=[decision_id],
            documents=[document],
            metadatas=[
                self._safe_metadata(
                    metadata
                )
            ],
        )

    # ========================================================
    # LEGACY TEMPORAL RETRIEVAL
    # ========================================================

    def retrieve_context(
        self,
        audio_file_id: str,
        chunk_index: int,
        radius: int = 1,
        student_id: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        Compatibility method for older code.

        New architecture should use semantic retrieval.
        """

        if student_id is None:
            return []

        try:

            results = (
                self.observations.get(
                    where={
                        "$and": [
                            {
                                "student_id": str(
                                    student_id
                                )
                            },
                            {
                                "audio_file_id": str(
                                    audio_file_id
                                )
                            },
                        ]
                    },
                    include=[
                        "documents",
                        "metadatas",
                    ],
                )
            )

        except Exception:

            return []

        output = []

        for metadata in (
            results.get(
                "metadatas",
                [],
            )
            or []
        ):

            metadata = dict(
                metadata or {}
            )

            index = int(
                metadata.get(
                    "chunk_index",
                    -999999,
                )
            )

            if index == chunk_index:
                continue

            if (
                abs(
                    index - chunk_index
                )
                > radius
            ):
                continue

            output.append(
                {
                    "metadata": metadata
                }
            )

        output.sort(
            key=lambda item: abs(
                int(
                    item["metadata"].get(
                        "chunk_index",
                        0,
                    )
                )
                - chunk_index
            )
        )

        return output

    # ========================================================
    # LIST STUDENT OBSERVATIONS
    # ========================================================

    def list_student_observations(
        self,
        student_id: str,
        limit: int = 100,
    ) -> List[Dict[str, Any]]:

        try:

            results = (
                self.observations.get(
                    where={
                        "student_id": str(
                            student_id
                        )
                    },
                    limit=int(limit),
                    include=[
                        "documents",
                        "metadatas",
                    ],
                )
            )

        except Exception as exc:

            print(
                "[RAG] Failed to list "
                "student observations:"
            )

            print(
                f"[RAG] Reason: {exc}"
            )

            return []

        output = []

        metadatas = (
            results.get(
                "metadatas",
                [],
            )
            or []
        )

        documents = (
            results.get(
                "documents",
                [],
            )
            or []
        )

        for index, metadata in enumerate(
            metadatas
        ):

            item = dict(
                metadata or {}
            )

            if index < len(
                documents
            ):

                item["document"] = (
                    documents[index]
                )

            output.append(
                item
            )

        return output

    # ========================================================
    # COUNT STUDENT OBSERVATIONS
    # ========================================================

    def count_student_observations(
        self,
        student_id: str,
    ) -> int:

        try:

            results = (
                self.observations.get(
                    where={
                        "student_id": str(
                            student_id
                        )
                    },
                    include=[],
                )
            )

            return len(
                results.get(
                    "ids",
                    [],
                )
                or []
            )

        except Exception:

            return 0

    # ========================================================
    # PARSE ANALYSIS
    # ========================================================

    @staticmethod
    def _parse_analysis(
        value: Any,
    ) -> Dict[str, Any]:

        if not value:
            return {}

        if isinstance(
            value,
            dict,
        ):

            return value

        try:

            parsed = json.loads(
                str(value)
            )

            if isinstance(
                parsed,
                dict,
            ):

                return parsed

        except Exception:

            pass

        return {}


# ============================================================
# FACTORY
# ============================================================

_default_store: Optional[
    AudioRAGStore
] = None


def get_audio_rag_store(
    persist_directory: Optional[str] = None,
    ollama_base_url: str = OLLAMA_BASE_URL,
    embedding_model: str = EMBEDDING_MODEL,
) -> AudioRAGStore:

    global _default_store

    if _default_store is None:

        _default_store = AudioRAGStore(
            persist_directory=(
                persist_directory
            ),
            ollama_base_url=(
                ollama_base_url
            ),
            embedding_model=(
                embedding_model
            ),
        )

    return _default_store
