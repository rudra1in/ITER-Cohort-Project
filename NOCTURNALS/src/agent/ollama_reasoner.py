# ============================================================
# FILE: src/agent/ollama_reasoner.py
# ============================================================

import json
import time
from typing import Any, Dict, Optional

import requests


# ============================================================
# CONFIGURATION
# ============================================================

DEFAULT_BASE_URL = "http://localhost:11434"

DEFAULT_MODEL = "qwen3:8b"

DEFAULT_TIMEOUT = 90

MAX_RETRIES = 2

TEMPERATURE = 0

MAX_PREDICT = 220


# ============================================================
# REASONER
# ============================================================

class OllamaReasoner:
    """
    Local Ollama reasoning component.

    IMPORTANT:

    Confidence is NOT treated as proof.

    The reasoning flow is:

        current observation
                +
        confidence
                +
        student-specific historical evidence
                ↓
        contextual decision

    High confidence can be accepted only when the historical
    evidence does not contradict the observation.

    Decisions stored by the agent are NOT supplied as evidence.
    """

    def __init__(
        self,
        model: str = DEFAULT_MODEL,
        base_url: str = DEFAULT_BASE_URL,
        ollama_url: Optional[str] = None,
        timeout: int = DEFAULT_TIMEOUT,
        max_retries: int = MAX_RETRIES,
    ):

        self.model = model

        if ollama_url:

            self.base_url = ollama_url

        else:

            self.base_url = base_url

        self.base_url = (
            self.base_url.rstrip("/")
        )

        if self.base_url.endswith(
            "/api/chat"
        ):

            self.ollama_url = (
                self.base_url
            )

        else:

            self.ollama_url = (
                f"{self.base_url}/api/chat"
            )

        self.timeout = timeout

        self.max_retries = (
            max_retries
        )

    # ========================================================
    # REASON
    # ========================================================

    def reason(
        self,
        detected_event: str,
        confidence_score: float,
        context: Optional[list] = None,
        previous_labels: Optional[list] = None,
        recent_events: Optional[list] = None,
        reanalyzed: bool = False,
        context_retrieved: bool = False,
        student_id: Optional[str] = None,
    ) -> Dict[str, Any]:

        context = context or []

        previous_labels = (
            previous_labels or []
        )

        recent_events = (
            recent_events or []
        )

        confidence_band = (
            self._confidence_band(
                confidence_score
            )
        )

        prompt = self._build_prompt(
            student_id=student_id,
            detected_event=detected_event,
            confidence_score=confidence_score,
            confidence_band=confidence_band,
            context=context,
            previous_labels=previous_labels,
            recent_events=recent_events,
            reanalyzed=reanalyzed,
            context_retrieved=context_retrieved,
        )

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        self._system_prompt()
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            "think": False,
            "stream": False,
            "format": "json",
            "options": {
                "temperature": TEMPERATURE,
                "num_predict": MAX_PREDICT,
            },
        }

        last_error = None

        for attempt in range(
            1,
            self.max_retries + 1,
        ):

            print(
                f"[Ollama] Attempt "
                f"{attempt}/{self.max_retries}"
            )

            start_time = (
                time.perf_counter()
            )

            try:

                response = requests.post(
                    self.ollama_url,
                    json=payload,
                    timeout=self.timeout,
                )

                elapsed = (
                    time.perf_counter()
                    - start_time
                )

                response.raise_for_status()

                data = response.json()

                print(
                    f"[Ollama] Response received "
                    f"in {elapsed:.2f}s."
                )

                result = (
                    self._parse_response(
                        data
                    )
                )

                print(
                    "[Ollama] Decision:"
                )

                print(
                    json.dumps(
                        result,
                        indent=2,
                        ensure_ascii=False,
                    )
                )

                return result

            except requests.exceptions.Timeout as exc:

                last_error = exc

                print(
                    f"[ERROR] Ollama timed out "
                    f"after {self.timeout}s."
                )

            except requests.exceptions.RequestException as exc:

                last_error = exc

                print(
                    f"[ERROR] Ollama request failed: "
                    f"{exc}"
                )

            except Exception as exc:

                last_error = exc

                print(
                    f"[ERROR] Ollama response "
                    f"processing failed: {exc}"
                )

        return {
            "action": "REVIEW",
            "reasoning": (
                "Ollama reasoning failed. "
                "The observation cannot be safely "
                "validated automatically."
            ),
            "review_required": True,
        }

    # ========================================================
    # COMPATIBILITY API
    # ========================================================

    def decide(
        self,
        detected_event: str,
        confidence_score: float,
        context: Optional[list] = None,
        previous_labels: Optional[list] = None,
        recent_events: Optional[list] = None,
        reanalyzed: bool = False,
        context_retrieved: bool = False,
        student_id: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:

        return self.reason(
            detected_event=detected_event,
            confidence_score=confidence_score,
            context=context,
            previous_labels=previous_labels,
            recent_events=recent_events,
            reanalyzed=reanalyzed,
            context_retrieved=context_retrieved,
            student_id=student_id,
        )

    # ========================================================
    # SYSTEM PROMPT
    # ========================================================

    def _system_prompt(self) -> str:

        return """
You are the reasoning component of a local audio evidence
validation agent.

You do NOT perform raw audio analysis.

You must NOT invent audio evidence.

The audio analyzer has already produced the current
observation.

Your job is to determine whether the current observation is
supported by the historical evidence retrieved from the same
student.

CRITICAL PRINCIPLE:

A confidence score is NOT proof.

A HIGH confidence score means only that the detector produced
a strong observation under its own heuristic rules.

HIGH confidence does NOT automatically mean the observation is
genuine.

The historical semantic evidence must be considered.

VALID ACTIONS:

RETRIEVE_CONTEXT
REANALYZE
LABEL
REVIEW

DECISION FRAMEWORK:

1. If semantic context has NOT been retrieved:

   RETRIEVE_CONTEXT

2. If semantic context HAS been retrieved:

   Compare the current observation against the retrieved
   historical observations.

3. Classify the relationship between current evidence and
   historical evidence as one of:

   SUPPORTING
   CONTRADICTORY
   NEUTRAL
   IRRELEVANT
   INSUFFICIENT

4. HIGH confidence + SUPPORTING evidence:

   LABEL

5. HIGH confidence + CONTRADICTORY evidence:

   REVIEW

6. HIGH confidence + NEUTRAL or IRRELEVANT evidence:

   REVIEW

   Do NOT call the observation automatically genuine.

7. MEDIUM confidence:

   Use historical evidence to determine whether the event
   is supported. If evidence is insufficient, REVIEW.

8. LOW confidence:

   Use historical evidence and, when useful, REANALYZE.
   If uncertainty remains, REVIEW.

9. REANALYZE is allowed only once.

10. Never use another agent decision as evidence.

11. Historical observations are evidence, not absolute truth.

12. Do not assume that two observations are the same event
    simply because they have similar labels.

13. Do not invent student behavior, identity, intent,
    conversations, speakers, or cheating.

14. REVIEW is required when evidence is contradictory or
    insufficient.

MOST IMPORTANT EXAMPLE:

Student A:

Current observation:
HUMAN_SPEECH, confidence 0.91

Historical evidence:
Repeated unusual/suspicious audio observations.

Result:
Do NOT automatically accept the 0.91.
The historical evidence conflicts with the assumption that
the current observation is normal/genuine.
Choose REVIEW.

Student B:

Current observation:
HUMAN_SPEECH, confidence 0.91

Historical evidence:
Repeated consistent HUMAN_SPEECH observations with no
contradictory evidence.

Result:
The historical evidence supports the current observation.
Choose LABEL.

The confidence score itself must never be changed merely
because context was retrieved.

The original detector confidence remains the detector's
confidence.

OUTPUT:

Return ONLY valid JSON.

Required format:

{
  "action": "RETRIEVE_CONTEXT | REANALYZE | LABEL | REVIEW",
  "reasoning": "specific evidence-based explanation",
  "review_required": true
}

Do not output markdown.
Do not output code fences.
Do not output additional fields.
""".strip()

    # ========================================================
    # USER PROMPT
    # ========================================================

    def _build_prompt(
        self,
        student_id: Optional[str],
        detected_event: str,
        confidence_score: float,
        confidence_band: str,
        context: list,
        previous_labels: list,
        recent_events: list,
        reanalyzed: bool,
        context_retrieved: bool,
    ) -> str:

        return f"""
CURRENT STUDENT
===============

Student ID:
{student_id or "UNKNOWN"}

CURRENT AUDIO OBSERVATION
=========================

Detected event:
{detected_event}

Detector confidence:
{confidence_score:.3f}

Confidence band:
{confidence_band}

PROCESSING STATE
================

Semantic context retrieved:
{context_retrieved}

Independent re-analysis completed:
{reanalyzed}

PREVIOUS LABELS
===============

{self._safe_json(previous_labels)}

RECENT OPERATIONAL HISTORY
==========================

{self._safe_json(recent_events)}

HISTORICAL AUDIO EVIDENCE
=========================

{self._safe_json(context)}

TASK
====

Determine whether the CURRENT observation is supported by
historical evidence belonging to THIS SAME STUDENT.

Do not confuse:

1. Current detector evidence
2. Historical observations
3. Agent decisions

Historical observations are the only RAG evidence.

Agent decisions are NOT evidence.

First determine whether the historical evidence is:

SUPPORTING
CONTRADICTORY
NEUTRAL
IRRELEVANT
INSUFFICIENT

Then select the appropriate action.

Remember:

HIGH confidence is NOT automatically genuine.

A high-confidence current observation can still require
REVIEW if the student's historical evidence contradicts it.

A high-confidence observation can be LABELed when relevant
historical observations consistently support it.

Do not change the detector confidence score.

Explain specifically WHY the historical evidence supports,
contradicts, or fails to validate the current observation.

Return ONLY JSON.
""".strip()

    # ========================================================
    # PARSER
    # ========================================================

    def _parse_response(
        self,
        response_data: Dict[str, Any],
    ) -> Dict[str, Any]:

        if not isinstance(
            response_data,
            dict,
        ):
            raise ValueError(
                "Invalid Ollama response."
            )

        message = response_data.get(
            "message"
        )

        if not isinstance(
            message,
            dict,
        ):
            raise ValueError(
                "Missing Ollama message."
            )

        content = message.get(
            "content"
        )

        if not isinstance(
            content,
            str,
        ):
            raise ValueError(
                "Ollama content is not a string."
            )

        content = content.strip()

        try:

            result = json.loads(
                content
            )

        except json.JSONDecodeError:

            cleaned = (
                self._extract_json_object(
                    content
                )
            )

            if cleaned is None:

                raise ValueError(
                    "Invalid JSON returned by Ollama."
                )

            result = json.loads(
                cleaned
            )

        if not isinstance(
            result,
            dict,
        ):
            raise ValueError(
                "Ollama decision is not an object."
            )

        action = str(
            result.get(
                "action",
                "REVIEW",
            )
        ).strip().upper()

        reasoning = str(
            result.get(
                "reasoning",
                "",
            )
        ).strip()

        review_required = result.get(
            "review_required",
            False,
        )

        valid_actions = {
            "RETRIEVE_CONTEXT",
            "REANALYZE",
            "LABEL",
            "REVIEW",
        }

        if action not in valid_actions:

            raise ValueError(
                f"Unsupported action: {action}"
            )

        if not reasoning:

            reasoning = (
                "No reasoning explanation "
                "was supplied."
            )

        if not isinstance(
            review_required,
            bool,
        ):

            review_required = (
                str(
                    review_required
                ).lower()
                == "true"
            )

        if action == "REVIEW":

            review_required = True

        if action == "LABEL":

            review_required = False

        return {
            "action": action,
            "reasoning": reasoning,
            "review_required": (
                review_required
            ),
        }

    # ========================================================
    # JSON EXTRACTION
    # ========================================================

    @staticmethod
    def _extract_json_object(
        text: str,
    ) -> Optional[str]:

        start = text.find("{")

        end = text.rfind("}")

        if start == -1 or end == -1:
            return None

        if end <= start:
            return None

        return text[
            start:end + 1
        ]

    # ========================================================
    # CONFIDENCE BAND
    # ========================================================

    @staticmethod
    def _confidence_band(
        confidence_score: float,
    ) -> str:

        if confidence_score >= 0.80:
            return "HIGH"

        if confidence_score >= 0.60:
            return "MEDIUM"

        return "LOW"

    # ========================================================
    # SAFE JSON
    # ========================================================

    @staticmethod
    def _safe_json(
        value: Any,
    ) -> str:

        try:

            return json.dumps(
                value,
                indent=2,
                ensure_ascii=False,
                default=str,
            )

        except Exception:

            return "[]"


# ============================================================
# DEFAULT REASONER
# ============================================================

_default_reasoner = None


def get_ollama_reasoner(
    model: str = DEFAULT_MODEL,
    base_url: str = DEFAULT_BASE_URL,
    timeout: int = DEFAULT_TIMEOUT,
    max_retries: int = MAX_RETRIES,
) -> OllamaReasoner:

    global _default_reasoner

    if _default_reasoner is None:

        _default_reasoner = (
            OllamaReasoner(
                model=model,
                base_url=base_url,
                timeout=timeout,
                max_retries=max_retries,
            )
        )

    return _default_reasoner


# ============================================================
# SIMPLE FUNCTION API
# ============================================================

def ask_ollama(
    detected_event: str,
    confidence_score: float,
    context: Optional[list] = None,
    previous_labels: Optional[list] = None,
    recent_events: Optional[list] = None,
    reanalyzed: bool = False,
    context_retrieved: bool = False,
    student_id: Optional[str] = None,
    model: str = DEFAULT_MODEL,
    base_url: str = DEFAULT_BASE_URL,
    timeout: int = DEFAULT_TIMEOUT,
) -> Dict[str, Any]:

    reasoner = OllamaReasoner(
        model=model,
        base_url=base_url,
        timeout=timeout,
        max_retries=MAX_RETRIES,
    )

    return reasoner.reason(
        detected_event=detected_event,
        confidence_score=confidence_score,
        context=context,
        previous_labels=previous_labels,
        recent_events=recent_events,
        reanalyzed=reanalyzed,
        context_retrieved=context_retrieved,
        student_id=student_id,
    )