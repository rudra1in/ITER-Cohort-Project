# Recursive Bubble Sort

Problem ID: recursive_bubble_sort

Title: Recursive Bubble Sort

Difficulty: Easy

Topic: sorting

Pattern: **Recursion + Bubble Sort**

---

## Problem Identity

This document is specifically about:

**Recursive Bubble Sort**

This knowledge chunk belongs to:

**sorting**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Recursive Bubble Sort** problem.

The primary problem-solving pattern is:

**Recursion + Bubble Sort**

---

## Key Idea

Recursive bubble sort performs one bubble-sort pass to place the largest element at the end, then recursively sorts the remaining unsorted portion.

### Core Invariant

After each recursive level's bubbling pass, the largest element in the current unsorted portion is fixed at its final position.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Perform the standard bubble sort iteratively using nested loops.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. For the current unsorted range, compare adjacent elements.
2. Swap adjacent elements when they are in the wrong order.
3. After one pass, the largest element reaches the end of the range.
4. Reduce the range by one.
5. Recursively sort the remaining portion.
6. Stop when the range contains one or zero elements.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Recursion + Bubble Sort**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What does one normal bubble-sort pass accomplish?

### Hint 2

Can the remaining unsorted portion be solved recursively?

---

## Common Mistakes

- Forgetting the recursive call.
- Using the wrong reduced array size.
- Incorrect base case.
- Forgetting to swap adjacent elements.
- Making the recursive call before completing the current pass.

---

## Edge Cases

- Empty array.
- Single element.
- Already sorted array.
- Reverse sorted array.
- Duplicate values.

---

## Complexity Analysis

### Time Complexity

**O(N^2)**

### Space Complexity

**O(N) recursion stack space in the worst case.**

---

## Interview Explanation

A concise interview explanation for **Recursive Bubble Sort** is:

> Recursive bubble sort performs one bubble-sort pass to place the largest element at the end, then recursively sorts the remaining unsorted portion.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- recursive bubble sort
- bubble sort recursion
- recursion
- sorting
- recursive sorting

---

## Problem Retrieval Identity

Problem Name: Recursive Bubble Sort

Problem ID: recursive_bubble_sort

Topic: sorting

Pattern: Recursion + Bubble Sort

Difficulty: Easy

Primary Retrieval Entity:

**Recursive Bubble Sort**

This document should be preferred when a user explicitly asks about:

- recursive bubble sort
- bubble sort recursion
- recursion
- sorting
- recursive sorting

Related concepts:

- recursive bubble sort
- bubble sort recursion
- recursion
- sorting
- recursive sorting
