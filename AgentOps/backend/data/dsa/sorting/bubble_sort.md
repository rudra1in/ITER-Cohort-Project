# Bubble Sort

Problem ID: bubble_sort

Title: Bubble Sort

Difficulty: Easy

Topic: sorting

Pattern: **Bubble Sort**

---

## Problem Identity

This document is specifically about:

**Bubble Sort**

This knowledge chunk belongs to:

**sorting**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Bubble Sort** problem.

The primary problem-solving pattern is:

**Bubble Sort**

---

## Key Idea

Bubble sort repeatedly compares adjacent elements and swaps them when they are in the wrong order, causing the largest unsorted element to move toward the end after each pass.

### Core Invariant

After each pass, the largest element in the remaining unsorted portion is placed at its final position at the end of that portion.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Perform repeated passes over the array and compare every adjacent pair, swapping whenever the left element is greater than the right element.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Start from the beginning of the array.
2. Compare each pair of adjacent elements.
3. Swap them if they are in the wrong order.
4. After one complete pass, the largest remaining element reaches the end.
5. Reduce the unsorted range by one.
6. If a complete pass performs no swaps, the array is already sorted and the algorithm can stop early.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Bubble Sort**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What happens when you repeatedly compare adjacent elements?

### Hint 2

Which element reaches the end after one complete pass?

---

## Common Mistakes

- Using incorrect loop boundaries.
- Forgetting to swap adjacent elements.
- Not reducing the inner loop range.
- Forgetting the early-stop optimization.
- Comparing non-adjacent elements.

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

**O(N^2) worst case, O(N) best case with early stopping.**

### Space Complexity

**O(1) auxiliary space.**

---

## Interview Explanation

A concise interview explanation for **Bubble Sort** is:

> Bubble sort repeatedly compares adjacent elements and swaps them when they are in the wrong order, causing the largest unsorted element to move toward the end after each pass.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- bubble sort
- adjacent swaps
- sorting
- in-place sorting
- comparison sorting

---

## Problem Retrieval Identity

Problem Name: Bubble Sort

Problem ID: bubble_sort

Topic: sorting

Pattern: Bubble Sort

Difficulty: Easy

Primary Retrieval Entity:

**Bubble Sort**

This document should be preferred when a user explicitly asks about:

- bubble sort
- adjacent swaps
- sorting
- in-place sorting
- comparison sorting

Related concepts:

- bubble sort
- adjacent swaps
- sorting
- in-place sorting
- comparison sorting
