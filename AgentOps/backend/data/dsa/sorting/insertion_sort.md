# Insertion Sort

Problem ID: insertion_sort

Title: Insertion Sort

Difficulty: Easy

Topic: sorting

Pattern: **Insertion Sort**

---

## Problem Identity

This document is specifically about:

**Insertion Sort**

This knowledge chunk belongs to:

**sorting**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Insertion Sort** problem.

The primary problem-solving pattern is:

**Insertion Sort**

---

## Key Idea

Insertion sort builds the sorted portion of the array one element at a time by inserting each new element into its correct position within the already sorted portion.

### Core Invariant

Before processing index i, the portion from index 0 to i-1 is sorted.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

For each element, shift larger elements in the sorted portion to the right until the correct position for the current element is found.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Consider the first element as already sorted.
2. Take the next element as the current key.
3. Compare the key with elements in the sorted portion from right to left.
4. Shift elements greater than the key one position to the right.
5. Insert the key into the empty position.
6. Repeat until all elements are processed.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Insertion Sort**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can you maintain a sorted portion on the left side?

### Hint 2

What should happen to elements greater than the current element?

---

## Common Mistakes

- Forgetting to store the current element before shifting.
- Using the wrong condition while shifting.
- Forgetting to insert the key after shifting.
- Using incorrect loop boundaries.

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

**O(N^2) worst case, O(N) best case.**

### Space Complexity

**O(1) auxiliary space.**

---

## Interview Explanation

A concise interview explanation for **Insertion Sort** is:

> Insertion sort builds the sorted portion of the array one element at a time by inserting each new element into its correct position within the already sorted portion.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- insertion sort
- insertion sorting
- sorted portion
- shifting elements
- in-place sorting

---

## Problem Retrieval Identity

Problem Name: Insertion Sort

Problem ID: insertion_sort

Topic: sorting

Pattern: Insertion Sort

Difficulty: Easy

Primary Retrieval Entity:

**Insertion Sort**

This document should be preferred when a user explicitly asks about:

- insertion sort
- insertion sorting
- sorted portion
- shifting elements
- in-place sorting

Related concepts:

- insertion sort
- insertion sorting
- sorted portion
- shifting elements
- in-place sorting
