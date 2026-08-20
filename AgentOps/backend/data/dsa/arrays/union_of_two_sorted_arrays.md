# Union of Two Sorted Arrays

Problem ID: union_of_two_sorted_arrays

Title: Union of Two Sorted Arrays

Difficulty: Easy

Topic: arrays

Pattern: **Two Pointers / Merge**

---

## Problem Identity

This document is specifically about:

**Union of Two Sorted Arrays**

This knowledge chunk belongs to:

**arrays**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Union of Two Sorted Arrays** problem.

The primary problem-solving pattern is:

**Two Pointers / Merge**

---

## Key Idea

Because both arrays are sorted, use two pointers to compare their current values and add the smaller value while skipping duplicates.

### Core Invariant

All values before pointers i and j have already been considered, and the result contains the unique values processed so far in sorted order.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Insert all elements from both arrays into a set and then produce the sorted unique result.

### Brute Force Complexity

- **Time Complexity:** O((N + M) log(N + M))
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize pointers i and j at the beginning of the two arrays.
2. Compare the current values.
3. Add the smaller value to the result while avoiding duplicates.
4. If the values are equal, add the value once and move both pointers.
5. Process remaining elements from either array.
6. Return the union.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Two Pointers / Merge**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Both arrays are sorted. Can you merge them like merge sort?

### Hint 2

What should you do when both pointers contain the same value?

---

## Common Mistakes

- Adding duplicates.
- Moving only one pointer when both values are equal.
- Ignoring remaining elements after one array is exhausted.

---

## Edge Cases

- One array is empty.
- Both arrays are empty.
- No common elements.
- All elements are common.
- Duplicate values within an array.

---

## Complexity Analysis

### Time Complexity

**O(N + M)**

### Space Complexity

**O(N + M) for the output.**

---

## Interview Explanation

A concise interview explanation for **Union of Two Sorted Arrays** is:

> Because both arrays are sorted, use two pointers to compare their current values and add the smaller value while skipping duplicates.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Union of Two Sorted Arrays
- union array
- two pointers
- merge sorted arrays
- unique sorted elements

---

## Problem Retrieval Identity

Problem Name: Union of Two Sorted Arrays

Problem ID: union_of_two_sorted_arrays

Topic: arrays

Pattern: Two Pointers / Merge

Difficulty: Easy

Primary Retrieval Entity:

**Union of Two Sorted Arrays**

This document should be preferred when a user explicitly asks about:

- Union of Two Sorted Arrays
- union array
- two pointers
- merge sorted arrays
- unique sorted elements

Related concepts:

- Union of Two Sorted Arrays
- union array
- two pointers
- merge sorted arrays
- unique sorted elements
