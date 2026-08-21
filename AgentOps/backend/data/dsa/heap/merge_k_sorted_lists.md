# Merge K Sorted Lists

Problem ID: merge_k_sorted_lists

Title: Merge K Sorted Lists

Difficulty: Hard

Topic: heap

Pattern: **Min Heap / K-Way Merge**

---

## Problem Identity

This document is specifically about:

**Merge K Sorted Lists**

This knowledge chunk belongs to:

**heap**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Merge K Sorted Lists** problem.

The primary problem-solving pattern is:

**Min Heap / K-Way Merge**

---

## Key Idea

Maintain a min heap containing the current smallest node from every non-empty list. Repeatedly remove the smallest node and insert its next node.

### Core Invariant

The heap contains the smallest unprocessed node from each active list.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Collect all values from all lists into one array, sort them, and reconstruct the merged list.

### Brute Force Complexity

- **Time Complexity:** O(N log N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Insert the first node of every non-empty list into a min heap.
2. Remove the smallest node from the heap.
3. Add it to the merged result.
4. If the removed node has a next node, insert that node into the heap.
5. Repeat until the heap becomes empty.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Min Heap / K-Way Merge**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

At any moment, which node from each list can be a candidate for the next result?

### Hint 2

How can a heap compare the current candidates efficiently?

---

## Common Mistakes

- Adding every node to the heap at once.
- Forgetting to add the next node from the removed list.
- Incorrectly handling empty lists.
- Creating incorrect next pointers.

---

## Edge Cases

- No lists.
- Empty lists.
- One list.
- Lists with different lengths.
- Duplicate values.

---

## Complexity Analysis

### Time Complexity

**O(N log K)**

### Space Complexity

**O(K)**

---

## Interview Explanation

A concise interview explanation for **Merge K Sorted Lists** is:

> Maintain a min heap containing the current smallest node from every non-empty list. Repeatedly remove the smallest node and insert its next node.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- merge k sorted lists
- k way merge
- min heap
- priority queue
- merge sorted lists

---

## Problem Retrieval Identity

Problem Name: Merge K Sorted Lists

Problem ID: merge_k_sorted_lists

Topic: heap

Pattern: Min Heap / K-Way Merge

Difficulty: Hard

Primary Retrieval Entity:

**Merge K Sorted Lists**

This document should be preferred when a user explicitly asks about:

- merge k sorted lists
- k way merge
- min heap
- priority queue
- merge sorted lists

Related concepts:

- merge k sorted lists
- k way merge
- min heap
- priority queue
- merge sorted lists
