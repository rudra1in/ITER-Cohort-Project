# K-th Smallest Element in an Array

Problem ID: kth_smallest_element_in_array

Title: K-th Smallest Element in an Array

Difficulty: Medium

Topic: heap

Pattern: **Max Heap / Top K**

---

## Problem Identity

This document is specifically about:

**K-th Smallest Element in an Array**

This knowledge chunk belongs to:

**heap**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **K-th Smallest Element in an Array** problem.

The primary problem-solving pattern is:

**Max Heap / Top K**

---

## Key Idea

Maintain a max heap containing the k smallest elements. The largest element inside this heap is the k-th smallest element.

### Core Invariant

The heap contains the k smallest elements encountered so far, and its root is the largest among them.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Sort the complete array and return the element at index k - 1.

### Brute Force Complexity

- **Time Complexity:** O(N log N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a max heap.
2. Traverse every element.
3. Insert the current element into the max heap.
4. If the heap size becomes greater than k, remove the maximum element.
5. After processing all elements, the root is the k-th smallest element.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Max Heap / Top K**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Which heap keeps the smallest k elements?

### Hint 2

What should be removed when the heap grows beyond k?

---

## Common Mistakes

- Using a min heap.
- Keeping more than k elements.
- Returning the wrong element.
- Incorrectly handling duplicate values.

---

## Edge Cases

- k = 1.
- k = n.
- Duplicate values.
- Negative numbers.
- All values equal.

---

## Complexity Analysis

### Time Complexity

**O(N log K)**

### Space Complexity

**O(K)**

---

## Interview Explanation

A concise interview explanation for **K-th Smallest Element in an Array** is:

> Maintain a max heap containing the k smallest elements. The largest element inside this heap is the k-th smallest element.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- kth smallest
- k-th smallest
- max heap
- priority queue
- top k smallest

---

## Problem Retrieval Identity

Problem Name: K-th Smallest Element in an Array

Problem ID: kth_smallest_element_in_array

Topic: heap

Pattern: Max Heap / Top K

Difficulty: Medium

Primary Retrieval Entity:

**K-th Smallest Element in an Array**

This document should be preferred when a user explicitly asks about:

- kth smallest
- k-th smallest
- max heap
- priority queue
- top k smallest

Related concepts:

- kth smallest
- k-th smallest
- max heap
- priority queue
- top k smallest
