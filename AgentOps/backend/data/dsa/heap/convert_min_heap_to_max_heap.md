# Convert Min Heap to Max Heap

Problem ID: convert_min_heap_to_max_heap

Title: Convert Min Heap to Max Heap

Difficulty: Medium

Topic: heap

Pattern: **Heapify**

---

## Problem Identity

This document is specifically about:

**Convert Min Heap to Max Heap**

This knowledge chunk belongs to:

**heap**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Convert Min Heap to Max Heap** problem.

The primary problem-solving pattern is:

**Heapify**

---

## Key Idea

A max heap can be built from the same array by applying max heapify from the last non-leaf node toward the root.

### Core Invariant

After processing an index, the subtree rooted at that index satisfies the max heap property.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Extract all elements from the min heap and repeatedly insert them into a new max heap.

### Brute Force Complexity

- **Time Complexity:** O(N log N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Keep the elements in the same array.
2. Find the last non-leaf node using n/2 - 1.
3. Apply max heapify from the last non-leaf node toward index 0.
4. During heapify, compare the node with its children.
5. Move the larger child upward when necessary.
6. Continue until the max heap property is restored.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Heapify**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Which nodes actually need heapify?

### Hint 2

Can you build the max heap bottom-up?

---

## Common Mistakes

- Starting heapify from the root only.
- Using min heap comparisons instead of max heap comparisons.
- Incorrect child index calculation.
- Ignoring the bottom-up construction.

---

## Edge Cases

- Empty array.
- Single element.
- Already a max heap.
- Duplicate values.
- Reverse ordered values.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(log N) for recursive heapify or O(1) for iterative heapify.**

---

## Interview Explanation

A concise interview explanation for **Convert Min Heap to Max Heap** is:

> A max heap can be built from the same array by applying max heapify from the last non-leaf node toward the root.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- convert min heap to max heap
- max heapify
- heapify
- build max heap

---

## Problem Retrieval Identity

Problem Name: Convert Min Heap to Max Heap

Problem ID: convert_min_heap_to_max_heap

Topic: heap

Pattern: Heapify

Difficulty: Medium

Primary Retrieval Entity:

**Convert Min Heap to Max Heap**

This document should be preferred when a user explicitly asks about:

- convert min heap to max heap
- max heapify
- heapify
- build max heap

Related concepts:

- convert min heap to max heap
- max heapify
- heapify
- build max heap
