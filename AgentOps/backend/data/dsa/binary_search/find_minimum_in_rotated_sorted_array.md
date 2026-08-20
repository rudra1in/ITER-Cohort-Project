# Find Minimum in Rotated Sorted Array

Problem ID: find_minimum_in_rotated_sorted_array

Title: Find Minimum in Rotated Sorted Array

Difficulty: Easy

Topic: binary_search

Pattern: **Binary Search on Rotation Point**

---

## Problem Identity

This document is specifically about:

**Find Minimum in Rotated Sorted Array**

This knowledge chunk belongs to:

**binary_search**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Find Minimum in Rotated Sorted Array** problem.

The primary problem-solving pattern is:

**Binary Search on Rotation Point**

---

## Key Idea

The minimum element is the rotation point. Compare the middle element with the rightmost element to determine which side contains the minimum.

### Core Invariant

The minimum element always remains inside the current search interval.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Scan every element and keep track of the smallest value.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Set low = 0 and high = n - 1.
2. If nums[low] is less than nums[high], the current range is already sorted and nums[low] is the minimum.
3. Calculate mid.
4. If nums[mid] is greater than nums[high], the minimum lies to the right of mid.
5. Otherwise the minimum lies at mid or to its left.
6. Continue until low equals high.
7. Return nums[low].

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Binary Search on Rotation Point**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

The minimum is the point where the sorted order breaks. How can you locate that point?

### Hint 2

Compare nums[mid] with nums[high]. What does that tell you?

---

## Common Mistakes

- Searching for the maximum instead of the minimum.
- Discarding mid when mid could itself be the minimum.
- Using incorrect comparisons with high.

---

## Edge Cases

- Array is not rotated.
- Array is rotated once.
- Minimum is at the beginning.
- Two-element array.

---

## Complexity Analysis

### Time Complexity

**O(log N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Find Minimum in Rotated Sorted Array** is:

> The minimum element is the rotation point. Compare the middle element with the rightmost element to determine which side contains the minimum.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Find Minimum in Rotated Sorted Array
- minimum rotated array
- rotation point
- LeetCode 153

---

## Problem Retrieval Identity

Problem Name: Find Minimum in Rotated Sorted Array

Problem ID: find_minimum_in_rotated_sorted_array

Topic: binary_search

Pattern: Binary Search on Rotation Point

Difficulty: Easy

Primary Retrieval Entity:

**Find Minimum in Rotated Sorted Array**

This document should be preferred when a user explicitly asks about:

- Find Minimum in Rotated Sorted Array
- minimum rotated array
- rotation point
- LeetCode 153

Related concepts:

- Find Minimum in Rotated Sorted Array
- minimum rotated array
- rotation point
- LeetCode 153
