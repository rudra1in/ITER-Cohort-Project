
class RubricGenerator:
    def __init__(self):
        self.criteria = {
            "Correctness": "Produces correct output and handles edge cases.",
            "Efficiency": "Uses appropriate time and space complexity.",
            "Readability": "Uses clear names, structure and maintainable code.",
            "Approach": "Uses a suitable DSA strategy and explains the reasoning.",
        }

    def generate_rubric(self):
        return {
            "criteria": [
                {
                    "name": name,
                    "description": description,
                }
                for name, description in self.criteria.items()
            ],
            "total": 10,
        }
