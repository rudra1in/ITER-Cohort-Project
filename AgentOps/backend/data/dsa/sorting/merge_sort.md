# Merge Sort

Problem ID: merge_sort

Title: Merge Sort

Difficulty: Medium

Topic: sorting

Pattern: **Divide and Conquer**

---

## Problem Identity

This document is specifically about:

**Merge Sort**

This knowledge chunk belongs to:

**sorting**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Merge Sort** problem.

The primary problem-solving pattern is:

**Divide and Conquer**

---

## Key Idea

Merge sort divides the array into smaller halves, recursively sorts each half, and then merges the sorted halves into one sorted array.

### Core Invariant

Whenever two ranges are passed to the merge step, both ranges are already individually sorted.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Repeatedly divide the array into smaller parts, recursively sort both parts, and merge the resulting sorted arrays.

### Brute Force Complexity

- **Time Complexity:** O(N log N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. If the current range contains zero or one element, it is already sorted.
2. Find the middle of the current range.
3. Recursively sort the left half.
4. Recursively sort the right half.
5. Merge the two sorted halves.
6. Copy the merged result back into the original array.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Divide and Conquer**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can you divide the array into two halves?

### Hint 2

How can recursion sort each half?

---

## Common Mistakes

- Incorrect base case.
- Incorrect middle calculation.
- Losing elements during merging.
- Forgetting to copy merged elements back.
- Using incorrect left and right boundaries.
- Forgetting to process remaining elements from either half.

---

## Edge Cases

- Empty array.
- Single element.
- Already sorted array.
- Reverse sorted array.
- Duplicate values.
- All elements equal.

---

## Complexity Analysis

### Time Complexity

**O(N log N)**

### Space Complexity

**O(N) auxiliary space for merging, plus O(log N) recursion stack space.**

---

## Interview Explanation

A concise interview explanation for **Merge Sort** is:

> Merge sort divides the array into smaller halves, recursively sorts each half, and then merges the sorted halves into one sorted array.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- merge sort
- merge sorting
- divide and conquer
- recursive sorting
- merge two sorted arrays

---

## Problem Retrieval Identity

Problem Name: Merge Sort

Problem ID: merge_sort

Topic: sorting

Pattern: Divide and Conquer

Difficulty: Medium

Primary Retrieval Entity:

**Merge Sort**

This document should be preferred when a user explicitly asks about:

- merge sort
- merge sorting
- divide and conquer
- recursive sorting
- merge two sorted arrays

Related concepts:

- merge sort
- merge sorting
- divide and conquer
- recursive sorting
- merge two sorted arrays
