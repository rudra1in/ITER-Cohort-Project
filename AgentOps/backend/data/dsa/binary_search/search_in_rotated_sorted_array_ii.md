# Search in Rotated Sorted Array II

Problem ID: search_in_rotated_sorted_array_ii

Title: Search in Rotated Sorted Array II

Difficulty: Medium

Topic: binary_search

Pattern: **Modified Binary Search with Duplicates**

---

## Problem Identity

This document is specifically about:

**Search in Rotated Sorted Array II**

This knowledge chunk belongs to:

**binary_search**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Search in Rotated Sorted Array II** problem.

The primary problem-solving pattern is:

**Modified Binary Search with Duplicates**

---

## Key Idea

The presence of duplicates can make it impossible to determine which half is sorted. When nums[low], nums[mid], and nums[high] are equal, shrink the boundaries before continuing binary search.

### Core Invariant

The target remains inside the current search interval, while duplicate boundary values may be removed when they provide no information about which half is sorted.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Scan the entire array and check every element against the target.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Set low = 0 and high = n - 1.
2. Calculate mid.
3. Return true if nums[mid] equals the target.
4. If nums[low], nums[mid], and nums[high] are equal, increment low and decrement high.
5. Otherwise identify the sorted half.
6. Check whether the target belongs to the sorted half.
7. Discard the half that cannot contain the target.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Modified Binary Search with Duplicates**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What problem do duplicates create when trying to identify the sorted half?

### Hint 2

If low, mid, and high contain the same value, what information can you safely remove?

---

## Common Mistakes

- Using the exact logic of the distinct-value version without handling duplicates.
- Forgetting to shrink low and high when all three boundary values are equal.
- Claiming strict O(log N) worst-case complexity despite duplicates.

---

## Edge Cases

- Many duplicate values.
- All elements are identical.
- Array is not rotated.
- Target does not exist.

---

## Complexity Analysis

### Time Complexity

**O(log N) average, O(N) worst case**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Search in Rotated Sorted Array II** is:

> The presence of duplicates can make it impossible to determine which half is sorted. When nums[low], nums[mid], and nums[high] are equal, shrink the boundaries before continuing binary search.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Search in Rotated Sorted Array II
- rotated sorted array duplicates
- modified binary search duplicates
- LeetCode 81

---

## Problem Retrieval Identity

Problem Name: Search in Rotated Sorted Array II

Problem ID: search_in_rotated_sorted_array_ii

Topic: binary_search

Pattern: Modified Binary Search with Duplicates

Difficulty: Medium

Primary Retrieval Entity:

**Search in Rotated Sorted Array II**

This document should be preferred when a user explicitly asks about:

- Search in Rotated Sorted Array II
- rotated sorted array duplicates
- modified binary search duplicates
- LeetCode 81

Related concepts:

- Search in Rotated Sorted Array II
- rotated sorted array duplicates
- modified binary search duplicates
- LeetCode 81
