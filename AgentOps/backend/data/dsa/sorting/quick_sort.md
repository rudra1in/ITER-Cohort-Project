# Quick Sort

Problem ID: quick_sort

Title: Quick Sort

Difficulty: Easy

Topic: sorting

Pattern: **Divide and Conquer**

---

## Problem Identity

This document is specifically about:

**Quick Sort**

This knowledge chunk belongs to:

**sorting**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Quick Sort** problem.

The primary problem-solving pattern is:

**Divide and Conquer**

---

## Key Idea

Quick sort chooses a pivot, partitions the array so that smaller elements are placed on one side and larger elements on the other, and recursively sorts both partitions.

### Core Invariant

After partitioning, the pivot is in its final sorted position, with elements on the left satisfying the partition condition and elements on the right satisfying the opposite condition.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Choose a pivot and create separate arrays for elements smaller than, equal to, and greater than the pivot before recursively sorting the smaller and greater portions.

### Brute Force Complexity

- **Time Complexity:** O(N log N) average time but uses O(N) extra space for auxiliary arrays.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Choose a pivot element.
2. Partition the array around the pivot.
3. Place the pivot in its correct final position.
4. Recursively sort the elements before the pivot.
5. Recursively sort the elements after the pivot.
6. Stop when the subarray contains zero or one element.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Divide and Conquer**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What element can divide the array into two parts?

### Hint 2

How can you place the pivot into its correct position?

---

## Common Mistakes

- Incorrect partition logic.
- Forgetting to place the pivot correctly.
- Using incorrect left and right boundaries.
- Infinite recursion due to incorrect partition indices.
- Choosing a poor pivot repeatedly.
- Forgetting the base case.

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

**O(N log N) average, O(N^2) worst case.**

### Space Complexity

**O(log N) average recursion stack space, O(N) worst-case recursion stack space.**

---

## Interview Explanation

A concise interview explanation for **Quick Sort** is:

> Quick sort chooses a pivot, partitions the array so that smaller elements are placed on one side and larger elements on the other, and recursively sorts both partitions.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- quick sort
- quick sorting
- partition
- pivot
- divide and conquer
- recursive sorting

---

## Problem Retrieval Identity

Problem Name: Quick Sort

Problem ID: quick_sort

Topic: sorting

Pattern: Divide and Conquer

Difficulty: Easy

Primary Retrieval Entity:

**Quick Sort**

This document should be preferred when a user explicitly asks about:

- quick sort
- quick sorting
- partition
- pivot
- divide and conquer
- recursive sorting

Related concepts:

- quick sort
- quick sorting
- partition
- pivot
- divide and conquer
- recursive sorting
