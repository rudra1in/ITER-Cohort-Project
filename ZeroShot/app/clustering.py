"""
Clusters behavior_events to separate suspicious (rare / outlier) behavior
from common, repeated baseline behavior.

Approach: build one feature vector per event, then run density-based clustering (DBSCAN or HDBSCAN):
  - Points that fall in a small/rare cluster, or are pure noise (label -1),
    are flagged as suspicious - they don't match a common pattern.
  - Points in a large, dense cluster are common/baseline behavior.

"""

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

try:
    import hdbscan as hdbscan_lib
    HDBSCAN_AVAILABLE = True
except ImportError:
    HDBSCAN_AVAILABLE = False


EVENT_TYPES = [
    "phone_visible",
    "repeated_side_looking",
]


class EventClusterer:

    def __init__(
        self,
        algorithm="dbscan",
        eps=1.2,
        min_samples=2,
        min_cluster_size=2,
        small_cluster_threshold=2
    ):

        self.algorithm = algorithm
        self.eps = eps
        self.min_samples = min_samples
        self.min_cluster_size = min_cluster_size
        self.small_cluster_threshold = small_cluster_threshold

        if algorithm == "hdbscan" and not HDBSCAN_AVAILABLE:
            raise ImportError(
                "hdbscan is not installed. Run: pip install hdbscan"
            )

     
    # FEATURE EXTRACTION
     

    def extract_features(
        self,
        events
    ):
        """
        Builds a numeric feature matrix from a list of event dicts
        (as returned by Database.get_events).

        Features per event:
          - one-hot event_type
          - duration (seconds)
          - confidence
          - evidence_count (frames of evidence backing the event)
        """

        import json

        rows = []

        for event in events:

            one_hot = [
                1.0 if event.get("event_type") == event_type else 0.0
                for event_type in EVENT_TYPES
            ]

            duration = float(event.get("duration") or 0.0)
            confidence = float(event.get("confidence") or 0.0)

            evidence_json = event.get("evidence_json") or "[]"

            try:
                evidence_count = len(json.loads(evidence_json))
            except (ValueError, TypeError):
                evidence_count = 0

            rows.append(
                one_hot + [duration, confidence, float(evidence_count)]
            )

        return np.array(rows, dtype="float32")

     
    # FIT + PREDICT
     

    def cluster(
        self,
        events
    ):
        """
        Returns a list of dicts (same order as `events`), one per event:
            {
                "event_id": ...,
                "cluster_id": int (-1 = noise / no cluster),
                "cluster_label": "common" | "suspicious",
                "is_suspicious": bool
            }
        """

        if not events:
            return []

        features = self.extract_features(events)

        # Guard: with only 1 event there's nothing to compare against - flag it suspicious by default (conservative: when in doubt,
        # surface it for review).
        if len(events) == 1:

            return [{
                "event_id": events[0]["event_id"],
                "cluster_id": -1,
                "cluster_label": "suspicious",
                "is_suspicious": True
            }]

        scaler = StandardScaler()
        scaled = scaler.fit_transform(features)

        if self.algorithm == "hdbscan":

            clusterer = hdbscan_lib.HDBSCAN(
                min_cluster_size=max(2, min(self.min_cluster_size, len(events)))
            )
            labels = clusterer.fit_predict(scaled)

        else:

            clusterer = DBSCAN(
                eps=self.eps,
                min_samples=min(self.min_samples, len(events))
            )
            labels = clusterer.fit_predict(scaled)

        # Cluster sizes (excluding noise, label == -1)
        cluster_sizes = {}
        for label in labels:
            if label == -1:
                continue
            cluster_sizes[label] = cluster_sizes.get(label, 0) + 1

        results = []

        for event, label in zip(events, labels):

            label_int = int(label)

            is_noise = label_int == -1
            is_small_cluster = (
                cluster_sizes.get(label_int, 0) <= self.small_cluster_threshold
            )

            is_suspicious = is_noise or is_small_cluster

            results.append({
                "event_id": event["event_id"],
                "cluster_id": label_int,
                "cluster_label": "suspicious" if is_suspicious else "common",
                "is_suspicious": is_suspicious
            })

        return results
