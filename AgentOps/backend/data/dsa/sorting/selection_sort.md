# Selection Sort

Problem ID: selection_sort

Title: Selection Sort

Difficulty: Easy

Topic: sorting

Pattern: **Selection Sort**

---

## Problem Identity

This document is specifically about:

**Selection Sort**

This knowledge chunk belongs to:

**sorting**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Selection Sort** problem.

The primary problem-solving pattern is:

**Selection Sort**

---

## Key Idea

Selection sort repeatedly finds the smallest element from the unsorted portion of the array and places it at the current position.

### Core Invariant

Before processing index i, all elements before i are already sorted and contain the smallest i elements in their correct positions.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

For every position, scan the remaining unsorted portion to find the minimum element and swap it into that position.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Start from the first index.
2. Assume the current index contains the minimum value.
3. Scan the remaining unsorted portion to find the actual minimum.
4. Swap the minimum element with the element at the current index.
5. Move to the next index and repeat.
6. After all positions are processed, the array is sorted.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Selection Sort**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

For each position, can you find the smallest element in the remaining array?

### Hint 2

Where should the smallest element be placed?

---

## Common Mistakes

- Finding the minimum from the wrong range.
- Forgetting to update the minimum index.
- Swapping values instead of indices incorrectly.
- Running the inner loop from index 0 every time.
- Using unnecessary extra space.

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

**O(N^2)**

### Space Complexity

**O(1) auxiliary space.**

---

## Interview Explanation

A concise interview explanation for **Selection Sort** is:

> Selection sort repeatedly finds the smallest element from the unsorted portion of the array and places it at the current position.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- selection sort
- sorting
- minimum element
- in-place sorting
- comparison sorting

---

## Problem Retrieval Identity

Problem Name: Selection Sort

Problem ID: selection_sort

Topic: sorting

Pattern: Selection Sort

Difficulty: Easy

Primary Retrieval Entity:

**Selection Sort**

This document should be preferred when a user explicitly asks about:

- selection sort
- sorting
- minimum element
- in-place sorting
- comparison sorting

Related concepts:

- selection sort
- sorting
- minimum element
- in-place sorting
- comparison sorting
