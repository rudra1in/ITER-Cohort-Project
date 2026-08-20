# Sort Characters by Frequency

Problem ID: sort_characters_by_frequency

Title: Sort Characters by Frequency

Difficulty: Easy

Topic: strings

Pattern: **Hash Map + Sorting / Bucket Frequency**

---

## Problem Identity

This document is specifically about:

**Sort Characters by Frequency**

This knowledge chunk belongs to:

**strings**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Sort Characters by Frequency** problem.

The primary problem-solving pattern is:

**Hash Map + Sorting / Bucket Frequency**

---

## Key Idea

Count how frequently every character occurs, then arrange the characters from highest frequency to lowest frequency.

### Core Invariant

Characters already placed in the result have frequencies greater than or equal to the remaining characters.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Count character frequencies and sort the characters according to their frequencies.

### Brute Force Complexity

- **Time Complexity:** O(N + K log K)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Count the frequency of every character.
2. Group or sort characters according to their frequencies.
3. Process characters from highest frequency to lowest.
4. Append each character as many times as its frequency.
5. Return the resulting string.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Hash Map + Sorting / Bucket Frequency**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What information determines where each character should appear?

### Hint 2

Can you count each character first and then order them by frequency?

---

## Common Mistakes

- Sorting characters alphabetically instead of by frequency.
- Forgetting to repeat a character according to its frequency.
- Incorrectly handling characters with equal frequencies.

---

## Edge Cases

- Single character.
- All characters identical.
- All characters have the same frequency.
- Empty string.

---

## Complexity Analysis

### Time Complexity

**O(N + K log K)**

### Space Complexity

**O(N + K)**

---

## Interview Explanation

A concise interview explanation for **Sort Characters by Frequency** is:

> Count how frequently every character occurs, then arrange the characters from highest frequency to lowest frequency.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Sort Characters by Frequency
- frequency sorting
- hash map
- LeetCode 451

---

## Problem Retrieval Identity

Problem Name: Sort Characters by Frequency

Problem ID: sort_characters_by_frequency

Topic: strings

Pattern: Hash Map + Sorting / Bucket Frequency

Difficulty: Easy

Primary Retrieval Entity:

**Sort Characters by Frequency**

This document should be preferred when a user explicitly asks about:

- Sort Characters by Frequency
- frequency sorting
- hash map
- LeetCode 451

Related concepts:

- Sort Characters by Frequency
- frequency sorting
- hash map
- LeetCode 451
