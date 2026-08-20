class HybridRetriever:

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

    
    # SEARCH
    

    def search(
        self,
        test_id,
        query,
        top_k=8,
        candidate_id=None
    ):

         
        # VECTOR SEARCH
         

        query_vector = (
            self.embedding_service.encode(
                query
            )
        )

        vector_results = (
            self.vector_store.search(
                query_vector,
                top_k=top_k * 2
            )
        )

        # Only retain events from this test.

        vector_results = [

            item

            for item in vector_results

            if item.get(
                "test_id"
            ) == test_id

        ]

         
        # KEYWORD SEARCH
         

        keyword_results = (
            self.database.keyword_search_events(
                test_id=test_id,
                query=query,
                limit=top_k * 2
            )
        )

         
        # METADATA FILTER
         

        if candidate_id:

            vector_results = [

                item

                for item in vector_results

                if item.get(
                    "candidate_id"
                ) == candidate_id

            ]

            keyword_results = [

                item

                for item in keyword_results

                if item.get(
                    "candidate_id"
                ) == candidate_id

            ]

         
        # FUSION
         

        scores = {}

        records = {}

        # Vector contribution.

        for rank, item in enumerate(
            vector_results
        ):

            event_id = item[
                "event_id"
            ]

            score = (
                1.0
                / (rank + 1)
            )

            scores.setdefault(
                event_id,
                0.0
            )

            scores[
                event_id
            ] += (
                0.65 * score
            )

            records[
                event_id
            ] = item

        # Keyword contribution.

        for rank, item in enumerate(
            keyword_results
        ):

            event_id = item[
                "event_id"
            ]

            score = (
                1.0
                / (rank + 1)
            )

            scores.setdefault(
                event_id,
                0.0
            )

            scores[
                event_id
            ] += (
                0.35 * score
            )

            records[
                event_id
            ] = item

         
        # SORT
         

        ranked_ids = sorted(
            scores.keys(),
            key=lambda event_id:
            scores[event_id],
            reverse=True
        )

        results = []

        for event_id in ranked_ids:

            item = dict(
                records[event_id]
            )

            item[
                "hybrid_score"
            ] = round(
                scores[event_id],
                6
            )

            results.append(
                item
            )

            if len(results) >= top_k:

                break

        return results