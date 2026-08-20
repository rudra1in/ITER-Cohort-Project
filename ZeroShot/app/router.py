class QueryRouter:

    COMPLEX_TERMS = [

        "investigate",

        "strongest evidence",

        "most suspicious",

        "compare",

        "compare candidates",

        "why",

        "overall",

        "multiple",

        "all evidence",

        "review",

        "rank",

        "who should be flagged",

        "pattern"
    ]

    def should_use_agents(
        self,
        question
    ):

        question = (
            question.lower()
        )

        for term in self.COMPLEX_TERMS:

            if term in question:

                return True

        return False