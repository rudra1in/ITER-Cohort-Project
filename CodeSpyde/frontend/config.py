import os

# Backend API Configuration
API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")

# App Metadata
APP_NAME = "CodeMentor"
APP_SUBTITLE = "AI DSA COACH"
APP_VERSION = "v2.4.0"

# Default Python Starter Templates
DEFAULT_TEMPLATES = {
    "two-sum": '''class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Hash map to store index of seen numbers
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
''',
    "reverse-array": '''def reverseArray(arr: list[int]) -> list[int]:
    # Reverse the array in-place or return a new reversed array
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
''',
    "default": '''def solution(nums):
    # Write your solution here
    pass
'''
}

# Initial Mock Student Stats (when backend stats endpoint is unavailable)
INITIAL_STUDENT_STATS = {
    "solved_count": 14,
    "total_problems": 48,
    "streak": 5,
    "accuracy": "82%",
    "recent_mistake": "Off-by-one boundary check"
}

# Supported Editor Themes
EDITOR_THEMES = [
    "monokai",
    "twilight",
    "dracula",
    "one_dark",
    "github",
    "tomorrow_night"
]
