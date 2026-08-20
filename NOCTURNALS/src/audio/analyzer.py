# ============================================================
# FILE: src/audio/analyzer.py
# ============================================================

from pathlib import Path
from typing import Any, Dict

import librosa
import numpy as np


LABELS = {
    "KEYBOARD",
    "HUMAN_SPEECH",
    "MULTIPLE_VOICES",
    "VEHICLE_NOISE",
    "ENVIRONMENTAL_NOISE",
    "SILENCE",
    "OTHER",
}


# ============================================================
# SAFE NUMERIC HELPERS
# ============================================================

def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        result = float(value)

        if not np.isfinite(result):
            return default

        return result

    except (TypeError, ValueError):
        return default


def _round(value: Any, digits: int = 4) -> float:
    return round(_safe_float(value), digits)


def _normalize(
    value: float,
    lo: float,
    hi: float,
) -> float:

    value = _safe_float(value)

    if hi <= lo:
        return 0.0

    return float(
        np.clip(
            (value - lo) / (hi - lo),
            0.0,
            1.0,
        )
    )


def _load_audio(path: str):
    """
    Load audio as mono 16 kHz.
    """

    audio_path = Path(path)

    if not audio_path.exists():
        raise FileNotFoundError(
            f"Audio chunk does not exist: {audio_path}"
        )

    y, sr = librosa.load(
        str(audio_path),
        sr=16000,
        mono=True,
    )

    y = np.asarray(
        y,
        dtype=np.float32,
    )

    if y.size:
        y = np.nan_to_num(
            y,
            nan=0.0,
            posinf=0.0,
            neginf=0.0,
        )

    return y, int(sr)


# ============================================================
# COMMON FEATURES
# ============================================================

def _extract_features(
    y: np.ndarray,
    sr: int,
) -> Dict[str, float]:

    if len(y) == 0:
        return {
            "rms": 0.0,
            "rms_db": -80.0,
            "zcr": 0.0,
            "spectral_centroid": 0.0,
            "spectral_bandwidth": 0.0,
            "spectral_rolloff": 0.0,
            "spectral_flatness": 0.0,
            "low_band_ratio": 0.0,
            "mid_band_ratio": 0.0,
            "high_band_ratio": 0.0,
            "spectral_flux": 0.0,
            "harmonic_ratio": 0.0,
        }

    rms_value = float(
        np.sqrt(
            np.mean(
                np.square(y)
            )
        )
        + 1e-12
    )

    rms_db = float(
        20.0
        * np.log10(
            rms_value + 1e-12
        )
    )

    zcr = float(
        np.mean(
            librosa.feature.zero_crossing_rate(
                y=y
            )
        )
    )

    centroid = float(
        np.mean(
            librosa.feature.spectral_centroid(
                y=y,
                sr=sr,
            )
        )
    )

    bandwidth = float(
        np.mean(
            librosa.feature.spectral_bandwidth(
                y=y,
                sr=sr,
            )
        )
    )

    rolloff = float(
        np.mean(
            librosa.feature.spectral_rolloff(
                y=y,
                sr=sr,
                roll_percent=0.85,
            )
        )
    )

    flatness = float(
        np.mean(
            librosa.feature.spectral_flatness(
                y=y
            )
        )
    )

    stft = librosa.stft(
        y,
        n_fft=1024,
        hop_length=256,
    )

    magnitude = np.abs(stft) + 1e-12

    frequencies = librosa.fft_frequencies(
        sr=sr,
        n_fft=1024,
    )

    total_energy = float(
        np.sum(magnitude)
        + 1e-12
    )

    low_energy = float(
        np.sum(
            magnitude[
                frequencies < 300
            ]
        )
    )

    mid_energy = float(
        np.sum(
            magnitude[
                (frequencies >= 300)
                & (frequencies < 3000)
            ]
        )
    )

    high_energy = float(
        np.sum(
            magnitude[
                frequencies >= 3000
            ]
        )
    )

    low_band_ratio = low_energy / total_energy
    mid_band_ratio = mid_energy / total_energy
    high_band_ratio = high_energy / total_energy

    # Spectral flux.
    normalized_mag = (
        magnitude
        / (
            np.sum(
                magnitude,
                axis=0,
                keepdims=True,
            )
            + 1e-12
        )
    )

    diff = np.diff(
        normalized_mag,
        axis=1,
    )

    spectral_flux = float(
        np.mean(
            np.sqrt(
                np.sum(
                    np.square(diff),
                    axis=0,
                )
            )
        )
    )

    # Harmonic ratio.
    try:
        harmonic, _ = librosa.effects.hpss(y)

        harmonic_energy = float(
            np.mean(
                np.square(harmonic)
            )
            + 1e-12
        )

        total_signal_energy = float(
            np.mean(
                np.square(y)
            )
            + 1e-12
        )

        harmonic_ratio = float(
            np.clip(
                harmonic_energy
                / total_signal_energy,
                0.0,
                1.0,
            )
        )

    except Exception:
        harmonic_ratio = 0.0

    return {
        "rms": rms_value,
        "rms_db": rms_db,
        "zcr": zcr,
        "spectral_centroid": centroid,
        "spectral_bandwidth": bandwidth,
        "spectral_rolloff": rolloff,
        "spectral_flatness": flatness,
        "low_band_ratio": low_band_ratio,
        "mid_band_ratio": mid_band_ratio,
        "high_band_ratio": high_band_ratio,
        "spectral_flux": spectral_flux,
        "harmonic_ratio": harmonic_ratio,
    }


def _feature_evidence(
    features: Dict[str, float],
) -> Dict[str, float]:

    return {
        key: (
            _round(
                value,
                4,
            )
            if key
            not in {
                "rms_db",
                "spectral_centroid",
                "spectral_bandwidth",
                "spectral_rolloff",
            }
            else _round(
                value,
                2,
            )
        )
        for key, value in features.items()
    }


# ============================================================
# PRIMARY HEURISTIC ANALYZER
# ============================================================

def _primary_classification(
    features: Dict[str, float],
) -> Dict[str, Any]:

    rms_db = features["rms_db"]
    zcr = features["zcr"]
    centroid = features["spectral_centroid"]
    bandwidth = features["spectral_bandwidth"]
    activity = _normalize(
        rms_db,
        -55.0,
        -12.0,
    )

    evidence = _feature_evidence(
        features
    )

    evidence["activity"] = _round(
        activity,
        3,
    )

    # --------------------------------------------------------
    # SILENCE
    # --------------------------------------------------------

    if rms_db < -48.0:

        confidence = min(
            0.99,
            0.78
            + (
                (-48.0 - rms_db)
                / 80.0
            ),
        )

        return {
            "event": "SILENCE",
            "confidence": round(
                confidence,
                3,
            ),
            "analysis_method": (
                "primary_heuristic"
            ),
            "evidence": evidence,
        }

    # --------------------------------------------------------
    # KEYBOARD / CLICK-LIKE
    # --------------------------------------------------------

    if (
        zcr > 0.08
        and centroid > 2500
        and bandwidth > 1800
        and rms_db < -18
        and features["spectral_flux"] > 0.015
    ):

        confidence = min(
            0.90,
            0.56
            + _normalize(
                zcr,
                0.08,
                0.20,
            )
            * 0.12
            + _normalize(
                centroid,
                2500,
                6000,
            )
            * 0.16
            + _normalize(
                features["spectral_flux"],
                0.015,
                0.08,
            )
            * 0.08,
        )

        return {
            "event": "KEYBOARD",
            "confidence": round(
                confidence,
                3,
            ),
            "analysis_method": (
                "primary_heuristic"
            ),
            "evidence": evidence,
        }

    # --------------------------------------------------------
    # HUMAN SPEECH PROXY
    # --------------------------------------------------------

    if (
        500 <= centroid <= 3000
        and 0.02 <= zcr <= 0.12
        and activity > 0.20
        and features["mid_band_ratio"] > 0.30
    ):

        confidence = min(
            0.88,
            0.54
            + _normalize(
                centroid,
                500,
                3000,
            )
            * 0.08
            + _normalize(
                activity,
                0.20,
                0.90,
            )
            * 0.12
            + _normalize(
                features["harmonic_ratio"],
                0.15,
                0.70,
            )
            * 0.12,
        )

        return {
            "event": "HUMAN_SPEECH",
            "confidence": round(
                confidence,
                3,
            ),
            "analysis_method": (
                "primary_heuristic"
            ),
            "evidence": evidence,
        }

    # --------------------------------------------------------
    # VEHICLE / LOW-FREQUENCY PROXY
    # --------------------------------------------------------

    if (
        centroid < 900
        and rms_db > -30
        and features["low_band_ratio"] > 0.25
    ):

        confidence = min(
            0.84,
            0.50
            + _normalize(
                features["low_band_ratio"],
                0.25,
                0.65,
            )
            * 0.16
            + _normalize(
                -rms_db,
                10,
                35,
            )
            * 0.12
            + _normalize(
                1.0
                - features["spectral_flatness"],
                0.20,
                0.80,
            )
            * 0.08,
        )

        return {
            "event": "VEHICLE_NOISE",
            "confidence": round(
                confidence,
                3,
            ),
            "analysis_method": (
                "primary_heuristic"
            ),
            "evidence": evidence,
        }

    # --------------------------------------------------------
    # DEFAULT
    # --------------------------------------------------------

    return {
        "event": "ENVIRONMENTAL_NOISE",
        "confidence": 0.52,
        "analysis_method": (
            "primary_heuristic"
        ),
        "evidence": evidence,
    }


# ============================================================
# INDEPENDENT SECOND-PASS ANALYZER
# ============================================================

def _independent_classification(
    features: Dict[str, float],
) -> Dict[str, Any]:

    rms_db = features["rms_db"]
    centroid = features["spectral_centroid"]
    zcr = features["zcr"]

    low_ratio = features[
        "low_band_ratio"
    ]

    mid_ratio = features[
        "mid_band_ratio"
    ]

    high_ratio = features[
        "high_band_ratio"
    ]

    flux = features[
        "spectral_flux"
    ]

    harmonic_ratio = features[
        "harmonic_ratio"
    ]

    flatness = features[
        "spectral_flatness"
    ]

    evidence = _feature_evidence(
        features
    )

    # --------------------------------------------------------
    # SILENCE
    # --------------------------------------------------------

    if (
        rms_db < -47.0
        and low_ratio < 0.40
    ):

        return {
            "event": "SILENCE",
            "confidence": 0.93,
            "analysis_method": (
                "independent_spectral_pass"
            ),
            "evidence": evidence,
        }

    # --------------------------------------------------------
    # KEYBOARD
    # --------------------------------------------------------

    keyboard_score = (
        0.35
        * _normalize(
            high_ratio,
            0.25,
            0.75,
        )
        + 0.30
        * _normalize(
            flux,
            0.01,
            0.08,
        )
        + 0.20
        * _normalize(
            zcr,
            0.06,
            0.18,
        )
        + 0.15
        * _normalize(
            centroid,
            2500,
            6500,
        )
    )

    if keyboard_score >= 0.55:
        return {
            "event": "KEYBOARD",
            "confidence": round(
                min(
                    0.86,
                    0.50
                    + keyboard_score * 0.40,
                ),
                3,
            ),
            "analysis_method": (
                "independent_spectral_pass"
            ),
            "evidence": evidence,
        }

    # --------------------------------------------------------
    # HUMAN SPEECH
    # --------------------------------------------------------

    speech_score = (
        0.30
        * _normalize(
            mid_ratio,
            0.30,
            0.75,
        )
        + 0.25
        * _normalize(
            harmonic_ratio,
            0.15,
            0.75,
        )
        + 0.20
        * (
            1.0
            - abs(
                _normalize(
                    centroid,
                    300,
                    4500,
                )
                - 0.50
            )
        )
        + 0.25
        * _normalize(
            zcr,
            0.015,
            0.12,
        )
    )

    if (
        speech_score >= 0.48
        and 350 <= centroid <= 3500
        and rms_db > -45
    ):

        return {
            "event": "HUMAN_SPEECH",
            "confidence": round(
                min(
                    0.84,
                    0.46
                    + speech_score * 0.42,
                ),
                3,
            ),
            "analysis_method": (
                "independent_spectral_pass"
            ),
            "evidence": evidence,
        }

    # --------------------------------------------------------
    # VEHICLE / LOW-FREQUENCY
    # --------------------------------------------------------

    vehicle_score = (
        0.45
        * _normalize(
            low_ratio,
            0.20,
            0.70,
        )
        + 0.25
        * _normalize(
            -rms_db,
            8,
            38,
        )
        + 0.15
        * (
            1.0
            - _normalize(
                centroid,
                500,
                2500,
            )
        )
        + 0.15
        * (
            1.0
            - _normalize(
                flatness,
                0.15,
                0.90,
            )
        )
    )

    if (
        vehicle_score >= 0.44
        and low_ratio > 0.22
    ):

        return {
            "event": "VEHICLE_NOISE",
            "confidence": round(
                min(
                    0.85,
                    0.46
                    + vehicle_score * 0.42,
                ),
                3,
            ),
            "analysis_method": (
                "independent_spectral_pass"
            ),
            "evidence": evidence,
        }

    # --------------------------------------------------------
    # ENVIRONMENTAL
    # --------------------------------------------------------

    environmental_score = (
        0.45
        * _normalize(
            flatness,
            0.20,
            0.90,
        )
        + 0.30
        * _normalize(
            high_ratio,
            0.10,
            0.60,
        )
        + 0.25
        * _normalize(
            flux,
            0.01,
            0.10,
        )
    )

    return {
        "event": (
            "ENVIRONMENTAL_NOISE"
            if environmental_score >= 0.25
            else "OTHER"
        ),
        "confidence": round(
            min(
                0.76,
                0.44
                + environmental_score
                * 0.30,
            ),
            3,
        ),
        "analysis_method": (
            "independent_spectral_pass"
        ),
        "evidence": evidence,
    }


# ============================================================
# PUBLIC PRIMARY API
# ============================================================

def analyze_audio_chunk(
    path: str,
) -> dict:

    y, sr = _load_audio(
        path
    )

    if len(y) == 0:
        return {
            "event": "SILENCE",
            "confidence": 1.0,
            "analysis_method": (
                "primary_heuristic"
            ),
            "evidence": {
                "reason": "empty_audio"
            },
        }

    features = _extract_features(
        y,
        sr,
    )

    result = _primary_classification(
        features
    )

    # Make sure all values are JSON-safe.
    return _sanitize_analysis(
        result
    )


# ============================================================
# PUBLIC INDEPENDENT API
# ============================================================

def analyze_audio_chunk_independent(
    path: str,
) -> dict:
    """
    Independent second analytical pass.

    It intentionally uses a separate feature interpretation
    from the primary classifier. It does not simply call
    analyze_audio_chunk() internally.
    """

    y, sr = _load_audio(
        path
    )

    if len(y) == 0:
        return {
            "event": "SILENCE",
            "confidence": 1.0,
            "analysis_method": (
                "independent_spectral_pass"
            ),
            "evidence": {
                "reason": "empty_audio"
            },
        }

    features = _extract_features(
        y,
        sr,
    )

    result = _independent_classification(
        features
    )

    return _sanitize_analysis(
        result
    )


# ============================================================
# COMPARISON
# ============================================================

def compare_analyses(
    primary: Dict[str, Any],
    independent: Dict[str, Any],
) -> Dict[str, Any]:

    primary_event = str(
        primary.get(
            "event",
            "OTHER",
        )
    )

    independent_event = str(
        independent.get(
            "event",
            "OTHER",
        )
    )

    primary_confidence = _safe_float(
        primary.get(
            "confidence",
            0.0,
        )
    )

    independent_confidence = _safe_float(
        independent.get(
            "confidence",
            0.0,
        )
    )

    agreement = (
        primary_event
        == independent_event
    )

    confidence_delta = (
        independent_confidence
        - primary_confidence
    )

    confidence_gap = abs(
        confidence_delta
    )

    # Strong agreement.
    if agreement and min(
        primary_confidence,
        independent_confidence,
    ) >= 0.60:

        relation = "AGREEMENT"

    # Strong event disagreement.
    elif (
        confidence_gap >= 0.12
        and max(
            primary_confidence,
            independent_confidence,
        ) >= 0.60
    ):

        relation = "STRONG_DISAGREEMENT"

    # Weak disagreement.
    elif not agreement:

        relation = "DISAGREEMENT"

    else:

        relation = "WEAK_AGREEMENT"

    # Select a final event only when there is meaningful support.
    if agreement:
        selected_event = (
            primary_event
        )

    elif (
        independent_confidence
        >= primary_confidence
        + 0.10
        and independent_confidence
        >= 0.60
    ):

        selected_event = (
            independent_event
        )

    elif primary_confidence >= 0.70:
        selected_event = (
            primary_event
        )

    else:
        selected_event = "OTHER"

    if relation == "AGREEMENT":
        recommendation = (
            "ACCEPT"
        )

    elif (
        independent_confidence
        >= 0.75
        and primary_confidence
        < 0.60
    ):
        recommendation = (
            "ACCEPT_WITH_SECOND_PASS_SUPPORT"
        )

    else:
        recommendation = (
            "REVIEW"
        )

    return {
        "primary_event": primary_event,
        "independent_event": independent_event,
        "primary_confidence": round(
            primary_confidence,
            3,
        ),
        "independent_confidence": round(
            independent_confidence,
            3,
        ),
        "confidence_delta": round(
            confidence_delta,
            3,
        ),
        "confidence_gap": round(
            confidence_gap,
            3,
        ),
        "agreement": agreement,
        "relation": relation,
        "selected_event": selected_event,
        "recommendation": recommendation,
    }


# ============================================================
# JSON-SAFE SANITIZATION
# ============================================================

def _sanitize_analysis(
    analysis: Dict[str, Any],
) -> Dict[str, Any]:

    event = str(
        analysis.get(
            "event",
            "OTHER",
        )
    )

    if event not in LABELS:
        event = "OTHER"

    confidence = _safe_float(
        analysis.get(
            "confidence",
            0.0,
        )
    )

    confidence = float(
        np.clip(
            confidence,
            0.0,
            1.0,
        )
    )

    evidence = analysis.get(
        "evidence",
        {},
    )

    safe_evidence = {}

    if isinstance(
        evidence,
        dict,
    ):

        for key, value in evidence.items():

            if isinstance(
                value,
                (int, float, np.integer, np.floating),
            ):

                safe_evidence[str(key)] = (
                    float(value)
                    if np.isfinite(
                        float(value)
                    )
                    else 0.0
                )

            else:
                safe_evidence[str(key)] = (
                    str(value)
                )

    return {
        "event": event,
        "confidence": round(
            confidence,
            3,
        ),
        "analysis_method": str(
            analysis.get(
                "analysis_method",
                "unknown",
            )
        ),
        "evidence": safe_evidence,
    }