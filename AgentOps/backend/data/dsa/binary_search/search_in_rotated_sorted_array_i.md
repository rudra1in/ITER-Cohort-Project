# Search in Rotated Sorted Array I

Problem ID: search_in_rotated_sorted_array_i

Title: Search in Rotated Sorted Array I

Difficulty: Medium

Topic: binary_search

Pattern: **Modified Binary Search**

---

## Problem Identity

This document is specifically about:

**Search in Rotated Sorted Array I**

This knowledge chunk belongs to:

**binary_search**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Search in Rotated Sorted Array I** problem.

The primary problem-solving pattern is:

**Modified Binary Search**

---

## Key Idea

In a rotated sorted array with distinct values, at least one half of the current search range is always sorted. Determine which half is sorted and decide whether the target belongs to that half.

### Core Invariant

The target, if present, always remains inside the current search interval while at least one half of that interval remains sorted.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Scan every element until the target is found.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Set low = 0 and high = n - 1.
2. Calculate mid.
3. If nums[mid] equals the target, return mid.
4. Determine whether the left half is sorted by comparing nums[low] and nums[mid].
5. If the left half is sorted, check whether the target lies inside that range.
6. Otherwise determine that the right half is sorted and check whether the target lies inside it.
7. Discard the half that cannot contain the target.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Modified Binary Search**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Even after rotation, is at least one half of the current range guaranteed to be sorted?

### Hint 2

Once you identify the sorted half, can you determine whether the target belongs there?

---

## Common Mistakes

- Assuming the entire array is sorted.
- Incorrectly identifying the sorted half.
- Using the wrong inclusive boundary conditions.
- Forgetting that this version assumes distinct values.

---

## Edge Cases

- Array is not rotated.
- Array is rotated once.
- Target is the first element.
- Target is the last element.
- Target does not exist.

---

## Complexity Analysis

### Time Complexity

**O(log N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Search in Rotated Sorted Array I** is:

> In a rotated sorted array with distinct values, at least one half of the current search range is always sorted. Determine which half is sorted and decide whether the target belongs to that half.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Search in Rotated Sorted Array
- rotated sorted array
- modified binary search
- LeetCode 33

---

## Problem Retrieval Identity

Problem Name: Search in Rotated Sorted Array I

Problem ID: search_in_rotated_sorted_array_i

Topic: binary_search

Pattern: Modified Binary Search

Difficulty: Medium

Primary Retrieval Entity:

**Search in Rotated Sorted Array I**

This document should be preferred when a user explicitly asks about:

- Search in Rotated Sorted Array
- rotated sorted array
- modified binary search
- LeetCode 33

Related concepts:

- Search in Rotated Sorted Array
- rotated sorted array
- modified binary search
- LeetCode 33
