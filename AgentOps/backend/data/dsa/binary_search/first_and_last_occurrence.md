# First and Last Occurrence

Problem ID: first_and_last_occurrence

Title: First and Last Occurrence

Difficulty: Easy

Topic: binary_search

Pattern: **Two Binary Searches / Lower and Upper Bound**

---

## Problem Identity

This document is specifically about:

**First and Last Occurrence**

This knowledge chunk belongs to:

**binary_search**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **First and Last Occurrence** problem.

The primary problem-solving pattern is:

**Two Binary Searches / Lower and Upper Bound**

---

## Key Idea

Find the first and last positions of a target in a sorted array by performing binary searches for the first position greater than or equal to the target and the first position greater than the target.

### Core Invariant

Each binary search maintains a range that contains the boundary occurrence being searched for.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Scan the entire array and record the first and last index where the target appears.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Perform a binary search for the first occurrence.
2. When nums[mid] is greater than or equal to the target, move left while recording mid when it equals the target.
3. Perform another binary search for the last occurrence.
4. When nums[mid] is less than or equal to the target, move right while recording mid when it equals the target.
5. Return the first and last positions.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Two Binary Searches / Lower and Upper Bound**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Finding one occurrence is easy. How can you modify binary search to find the leftmost occurrence?

### Hint 2

How can the same idea be modified to find the rightmost occurrence?

---

## Common Mistakes

- Returning the first occurrence found by ordinary binary search.
- Not continuing left after finding a target for the first occurrence.
- Not continuing right after finding a target for the last occurrence.
- Returning invalid indices when the target does not exist.

---

## Edge Cases

- Target does not exist.
- Target appears once.
- Target appears at every position.
- Target appears at the beginning.
- Target appears at the end.

---

## Complexity Analysis

### Time Complexity

**O(log N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **First and Last Occurrence** is:

> Find the first and last positions of a target in a sorted array by performing binary searches for the first position greater than or equal to the target and the first position greater than the target.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- First and Last Occurrence
- first occurrence
- last occurrence
- search range
- lower bound
- upper bound

---

## Problem Retrieval Identity

Problem Name: First and Last Occurrence

Problem ID: first_and_last_occurrence

Topic: binary_search

Pattern: Two Binary Searches / Lower and Upper Bound

Difficulty: Easy

Primary Retrieval Entity:

**First and Last Occurrence**

This document should be preferred when a user explicitly asks about:

- First and Last Occurrence
- first occurrence
- last occurrence
- search range
- lower bound
- upper bound

Related concepts:

- First and Last Occurrence
- first occurrence
- last occurrence
- search range
- lower bound
- upper bound
