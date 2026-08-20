# Floor and Ceil in Sorted Array

Problem ID: floor_and_ceil_in_sorted_array

Title: Floor and Ceil in Sorted Array

Difficulty: Easy

Topic: binary_search

Pattern: **Binary Search for Floor and Ceil**

---

## Problem Identity

This document is specifically about:

**Floor and Ceil in Sorted Array**

This knowledge chunk belongs to:

**binary_search**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Floor and Ceil in Sorted Array** problem.

The primary problem-solving pattern is:

**Binary Search for Floor and Ceil**

---

## Key Idea

The floor is the largest value less than or equal to the target, while the ceil is the smallest value greater than or equal to the target. Both can be found using binary search.

### Core Invariant

For floor search, every valid candidate is at or before the current right boundary; for ceil search, every valid candidate is at or after the current left boundary.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Scan the entire sorted array and keep track of the largest value not exceeding the target and the smallest value not smaller than the target.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Use binary search to find the floor candidate.
2. When nums[mid] is less than or equal to the target, store nums[mid] as a floor candidate and move right.
3. When nums[mid] is greater than the target, move left.
4. Use binary search to find the ceil candidate.
5. When nums[mid] is greater than or equal to the target, store nums[mid] as a ceil candidate and move left.
6. When nums[mid] is smaller than the target, move right.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Binary Search for Floor and Ceil**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

For floor, what is the largest value that can still be less than or equal to the target?

### Hint 2

For ceil, what is the smallest value that can still be greater than or equal to the target?

---

## Common Mistakes

- Reversing the floor and ceil conditions.
- Returning the nearest value without checking the required inequality.
- Forgetting that floor or ceil may not exist.

---

## Edge Cases

- Target smaller than all elements.
- Target larger than all elements.
- Target exactly exists.
- Duplicate values.

---

## Complexity Analysis

### Time Complexity

**O(log N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Floor and Ceil in Sorted Array** is:

> The floor is the largest value less than or equal to the target, while the ceil is the smallest value greater than or equal to the target. Both can be found using binary search.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Floor and Ceil
- floor in sorted array
- ceil in sorted array
- binary search

---

## Problem Retrieval Identity

Problem Name: Floor and Ceil in Sorted Array

Problem ID: floor_and_ceil_in_sorted_array

Topic: binary_search

Pattern: Binary Search for Floor and Ceil

Difficulty: Easy

Primary Retrieval Entity:

**Floor and Ceil in Sorted Array**

This document should be preferred when a user explicitly asks about:

- Floor and Ceil
- floor in sorted array
- ceil in sorted array
- binary search

Related concepts:

- Floor and Ceil
- floor in sorted array
- ceil in sorted array
- binary search
