# Implement Min Heap

Problem ID: implement_min_heap

Title: Implement Min Heap

Difficulty: Medium

Topic: heap

Pattern: **Heap Implementation**

---

## Problem Identity

This document is specifically about:

**Implement Min Heap**

This knowledge chunk belongs to:

**heap**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Implement Min Heap** problem.

The primary problem-solving pattern is:

**Heap Implementation**

---

## Key Idea

A min heap is a complete binary tree where every parent is smaller than or equal to its children. It can be efficiently represented using an array.

### Core Invariant

Every parent node remains less than or equal to its children after every heap operation.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Maintain the elements in an ordinary array and scan the array whenever the minimum element needs to be found.

### Brute Force Complexity

- **Time Complexity:** O(N) for finding the minimum element.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Represent the complete binary tree using an array.
2. For an element at index i, its left child is at 2*i + 1.
3. Its right child is at 2*i + 2.
4. Its parent is at (i - 1) / 2.
5. For insertion, add the element at the end and move it upward while it is smaller than its parent.
6. For deletion of the minimum, replace the root with the last element.
7. Remove the last element and move the new root downward until the heap property is restored.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Heap Implementation**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How can a complete binary tree be represented using an array?

### Hint 2

Where is the minimum element located in a min heap?

---

## Common Mistakes

- Using incorrect parent or child index formulas.
- Forgetting to restore the heap property after insertion.
- Comparing with only one child during heapify down.
- Ignoring empty heap cases.

---

## Edge Cases

- Empty heap.
- Single element.
- Duplicate values.
- Already ordered values.
- Deleting the last element.

---

## Complexity Analysis

### Time Complexity

**O(log N) for insertion and deletion; O(1) for accessing the minimum.**

### Space Complexity

**O(N) for storing the heap.**

---

## Interview Explanation

A concise interview explanation for **Implement Min Heap** is:

> A min heap is a complete binary tree where every parent is smaller than or equal to its children. It can be efficiently represented using an array.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- min heap
- implement min heap
- heap implementation
- heapify
- priority queue

---

## Problem Retrieval Identity

Problem Name: Implement Min Heap

Problem ID: implement_min_heap

Topic: heap

Pattern: Heap Implementation

Difficulty: Medium

Primary Retrieval Entity:

**Implement Min Heap**

This document should be preferred when a user explicitly asks about:

- min heap
- implement min heap
- heap implementation
- heapify
- priority queue

Related concepts:

- min heap
- implement min heap
- heap implementation
- heapify
- priority queue
