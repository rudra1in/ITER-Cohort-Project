# Linear Search

Problem ID: linear_search

Title: Linear Search

Difficulty: Easy

Topic: arrays

Pattern: **Linear Scan**

---

## Problem Identity

This document is specifically about:

**Linear Search**

This knowledge chunk belongs to:

**arrays**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Linear Search** problem.

The primary problem-solving pattern is:

**Linear Scan**

---

## Key Idea

Check each element sequentially until the target is found. Linear search works even when the array is unsorted.

### Core Invariant

All elements before the current index have already been checked and do not contain the target.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Check each element sequentially. Since linear search is already the direct approach, there is no substantially faster general approach for an unsorted array.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Start from the first element.
2. Compare each element with the target.
3. Return the index when the target is found.
4. Return -1 if the target does not exist.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Linear Scan**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

If the array is unsorted, can you eliminate half the elements at once?

### Hint 2

What is the simplest way to check every possible position?

---

## Common Mistakes

- Returning the value instead of its index.
- Forgetting the not-found case.
- Accessing an index outside the array.

---

## Edge Cases

- Empty array.
- Single element.
- Target at first position.
- Target at last position.
- Target absent.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Linear Search** is:

> Check each element sequentially until the target is found. Linear search works even when the array is unsorted.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Linear Search
- sequential search
- array search
- find element
- linear scan

---

## Problem Retrieval Identity

Problem Name: Linear Search

Problem ID: linear_search

Topic: arrays

Pattern: Linear Scan

Difficulty: Easy

Primary Retrieval Entity:

**Linear Search**

This document should be preferred when a user explicitly asks about:

- Linear Search
- sequential search
- array search
- find element
- linear scan

Related concepts:

- Linear Search
- sequential search
- array search
- find element
- linear scan
