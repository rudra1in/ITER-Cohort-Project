# Replace Elements by Their Rank

Problem ID: replace_elements_by_rank

Title: Replace Elements by Their Rank

Difficulty: Easy

Topic: heap

Pattern: **Min Heap / Ranking**

---

## Problem Identity

This document is specifically about:

**Replace Elements by Their Rank**

This knowledge chunk belongs to:

**heap**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Replace Elements by Their Rank** problem.

The primary problem-solving pattern is:

**Min Heap / Ranking**

---

## Key Idea

Assign ranks according to sorted order while ensuring equal values receive the same rank.

### Core Invariant

The rank assigned to every processed distinct value correctly represents its position among all distinct values in sorted order.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

For every element, count how many distinct values are smaller than it.

### Brute Force Complexity

- **Time Complexity:** O(N²)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Copy the elements into a separate collection.
2. Sort the values or place them into a min heap.
3. Process values in increasing order.
4. Assign a new rank only when the value changes.
5. Store the rank of each value in a map.
6. Replace every original value using its stored rank.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Min Heap / Ranking**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Should duplicate values receive different ranks?

### Hint 2

Can you first determine the sorted order of distinct values?

---

## Common Mistakes

- Assigning different ranks to duplicate values.
- Losing the original array order.
- Ranking duplicate elements separately.
- Using O(N²) unnecessary comparisons.

---

## Edge Cases

- All values equal.
- All values distinct.
- Negative values.
- Duplicate values.
- Single element.

---

## Complexity Analysis

### Time Complexity

**O(N log N)**

### Space Complexity

**O(N)**

---

## Interview Explanation

A concise interview explanation for **Replace Elements by Their Rank** is:

> Assign ranks according to sorted order while ensuring equal values receive the same rank.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- replace elements by rank
- rank array
- heap ranking
- coordinate compression

---

## Problem Retrieval Identity

Problem Name: Replace Elements by Their Rank

Problem ID: replace_elements_by_rank

Topic: heap

Pattern: Min Heap / Ranking

Difficulty: Easy

Primary Retrieval Entity:

**Replace Elements by Their Rank**

This document should be preferred when a user explicitly asks about:

- replace elements by rank
- rank array
- heap ranking
- coordinate compression

Related concepts:

- replace elements by rank
- rank array
- heap ranking
- coordinate compression
