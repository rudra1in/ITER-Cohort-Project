# Sort K-Sorted Array

Problem ID: sort_k_sorted_array

Title: Sort K-Sorted Array

Difficulty: Easy

Topic: heap

Pattern: **Min Heap / Nearly Sorted Array**

---

## Problem Identity

This document is specifically about:

**Sort K-Sorted Array**

This knowledge chunk belongs to:

**heap**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Sort K-Sorted Array** problem.

The primary problem-solving pattern is:

**Min Heap / Nearly Sorted Array**

---

## Key Idea

In a k-sorted array, every element is at most k positions away from its correct position. A min heap of size k + 1 can therefore produce the sorted order efficiently.

### Core Invariant

The minimum element among the next k + 1 candidates is always the next element in sorted order.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Sort the complete array using a comparison-based sorting algorithm.

### Brute Force Complexity

- **Time Complexity:** O(N log N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a min heap.
2. Insert the first k + 1 elements.
3. Take the minimum element from the heap and place it in the output.
4. Insert the next array element into the heap.
5. Continue extracting the minimum and adding the next element.
6. After processing the array, remove the remaining heap elements in sorted order.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Min Heap / Nearly Sorted Array**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How far can an element be from its correct position?

### Hint 2

How many elements need to be considered for the next smallest value?

---

## Common Mistakes

- Using heap size k instead of k + 1.
- Forgetting remaining heap elements.
- Using a max heap.
- Incorrect output index.

---

## Edge Cases

- k = 0.
- k = 1.
- k >= n.
- Duplicate values.
- Already sorted array.

---

## Complexity Analysis

### Time Complexity

**O(N log K)**

### Space Complexity

**O(K)**

---

## Interview Explanation

A concise interview explanation for **Sort K-Sorted Array** is:

> In a k-sorted array, every element is at most k positions away from its correct position. A min heap of size k + 1 can therefore produce the sorted order efficiently.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- k sorted array
- nearly sorted array
- sort k sorted array
- min heap
- priority queue

---

## Problem Retrieval Identity

Problem Name: Sort K-Sorted Array

Problem ID: sort_k_sorted_array

Topic: heap

Pattern: Min Heap / Nearly Sorted Array

Difficulty: Easy

Primary Retrieval Entity:

**Sort K-Sorted Array**

This document should be preferred when a user explicitly asks about:

- k sorted array
- nearly sorted array
- sort k sorted array
- min heap
- priority queue

Related concepts:

- k sorted array
- nearly sorted array
- sort k sorted array
- min heap
- priority queue
