import json


class EventIndexer:

    def __init__(
        self,
        database,
        embedding_service,
        vector_store
    ):

        self.database = database

        self.embedding_service = (
            embedding_service
        )

        self.vector_store = (
            vector_store
        )

    
    # INDEX TEST
    

    def index_test(
        self,
        test_id
    ):

        events = (
            self.database.get_events(
                test_id
            )
        )

        if not events:

            return {

                "test_id":
                    test_id,

                "events":
                    0,

                "indexed":
                    0
            }


        self.vector_store.remove_by_test(
            test_id
        )

        texts = []

        metadata = []

        for event in events:

            text = self.event_to_text(
                event
            )

            texts.append(
                text
            )

            metadata.append(
                {

                    "event_id":
                        event[
                            "event_id"
                        ],

                    "test_id":
                        event[
                            "test_id"
                        ],

                    "candidate_id":
                        event[
                            "candidate_id"
                        ],

                    "event_type":
                        event[
                            "event_type"
                        ],

                    "start_time":
                        event[
                            "start_time"
                        ],

                    "end_time":
                        event[
                            "end_time"
                        ],

                    "duration":
                        event[
                            "duration"
                        ],

                    "confidence":
                        event[
                            "confidence"
                        ],

                    "description":
                        event[
                            "description"
                        ],

                    "evidence_json":
                        event[
                            "evidence_json"
                        ],

                    "text":
                        text
                }
            )

        vectors = (
            self.embedding_service.encode_batch(
                texts
            )
        )

        self.vector_store.add(
            vectors,
            metadata
        )

        return {

            "test_id":
                test_id,

            "events":
                len(events),

            "indexed":
                len(metadata)
        }

    
    # EVENT → TEXT
    

    @staticmethod
    def event_to_text(
        event
    ):

        return f"""
Candidate {event.get("candidate_id")}

Behavior event:
{event.get("event_type")}

Description:
{event.get("description")}

Start time:
{event.get("start_time")}

End time:
{event.get("end_time")}

Duration:
{event.get("duration")} seconds

Confidence:
{event.get("confidence")}

Evidence frames:
{event.get("evidence_json")}
""".strip()