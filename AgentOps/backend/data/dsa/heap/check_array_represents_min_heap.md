# Check if an Array Represents a Min Heap

Problem ID: check_array_represents_min_heap

Title: Check if an Array Represents a Min Heap

Difficulty: Medium

Topic: heap

Pattern: **Heap Property Validation**

---

## Problem Identity

This document is specifically about:

**Check if an Array Represents a Min Heap**

This knowledge chunk belongs to:

**heap**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Check if an Array Represents a Min Heap** problem.

The primary problem-solving pattern is:

**Heap Property Validation**

---

## Key Idea

An array represents a min heap if every parent is smaller than or equal to its children. Only non-leaf nodes need to be checked.

### Core Invariant

Every parent processed so far satisfies the min heap property with respect to all of its existing children.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Construct the corresponding tree and inspect every parent-child relationship.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Start from index 0.
2. Only indices from 0 to (n/2) - 1 can have children.
3. For every parent, calculate its left and right child indices.
4. Check that the parent is less than or equal to each existing child.
5. Return false immediately if any heap property is violated.
6. Return true if every parent satisfies the condition.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Heap Property Validation**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Which elements in a heap can actually have children?

### Hint 2

Do you need to check leaf nodes?

---

## Common Mistakes

- Checking leaf nodes unnecessarily.
- Using incorrect child indices.
- Forgetting that the right child may not exist.
- Checking only the root.

---

## Edge Cases

- Empty array.
- Single element.
- Two elements.
- Duplicate values.
- Invalid parent-child relationship.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Check if an Array Represents a Min Heap** is:

> An array represents a min heap if every parent is smaller than or equal to its children. Only non-leaf nodes need to be checked.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- check min heap
- array min heap
- heap property
- validate heap

---

## Problem Retrieval Identity

Problem Name: Check if an Array Represents a Min Heap

Problem ID: check_array_represents_min_heap

Topic: heap

Pattern: Heap Property Validation

Difficulty: Medium

Primary Retrieval Entity:

**Check if an Array Represents a Min Heap**

This document should be preferred when a user explicitly asks about:

- check min heap
- array min heap
- heap property
- validate heap

Related concepts:

- check min heap
- array min heap
- heap property
- validate heap
