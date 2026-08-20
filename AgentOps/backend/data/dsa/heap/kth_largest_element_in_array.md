# K-th Largest Element in an Array

Problem ID: kth_largest_element_in_array

Title: K-th Largest Element in an Array

Difficulty: Medium

Topic: heap

Pattern: **Min Heap / Top K**

---

## Problem Identity

This document is specifically about:

**K-th Largest Element in an Array**

This knowledge chunk belongs to:

**heap**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **K-th Largest Element in an Array** problem.

The primary problem-solving pattern is:

**Min Heap / Top K**

---

## Key Idea

Maintain a min heap containing the k largest elements seen so far. The smallest element inside this heap is the k-th largest element overall.

### Core Invariant

The heap contains exactly the k largest elements encountered so far, and its root is the smallest among them.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Sort the complete array and return the element at index n - k.

### Brute Force Complexity

- **Time Complexity:** O(N log N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a min heap.
2. Traverse every element in the array.
3. Insert the current element into the heap.
4. If the heap size becomes greater than k, remove the minimum element.
5. After processing all elements, the root of the heap is the k-th largest element.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Min Heap / Top K**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Do you really need to keep all N elements?

### Hint 2

If you want the k largest elements, which heap is useful?

---

## Common Mistakes

- Using a max heap unnecessarily.
- Allowing the heap to grow beyond k.
- Returning the wrong heap element.
- Forgetting that duplicates are allowed.

---

## Edge Cases

- k = 1.
- k = n.
- Duplicate values.
- Negative values.
- All elements equal.

---

## Complexity Analysis

### Time Complexity

**O(N log K)**

### Space Complexity

**O(K)**

---

## Interview Explanation

A concise interview explanation for **K-th Largest Element in an Array** is:

> Maintain a min heap containing the k largest elements seen so far. The smallest element inside this heap is the k-th largest element overall.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- kth largest
- k-th largest element
- top k
- min heap
- priority queue

---

## Problem Retrieval Identity

Problem Name: K-th Largest Element in an Array

Problem ID: kth_largest_element_in_array

Topic: heap

Pattern: Min Heap / Top K

Difficulty: Medium

Primary Retrieval Entity:

**K-th Largest Element in an Array**

This document should be preferred when a user explicitly asks about:

- kth largest
- k-th largest element
- top k
- min heap
- priority queue

Related concepts:

- kth largest
- k-th largest element
- top k
- min heap
- priority queue
