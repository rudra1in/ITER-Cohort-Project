# Find How Many Times the Array Is Rotated

Problem ID: find_how_many_times_array_is_rotated

Title: Find How Many Times the Array Is Rotated

Difficulty: Easy

Topic: binary_search

Pattern: **Binary Search for Minimum / Rotation Count**

---

## Problem Identity

This document is specifically about:

**Find How Many Times the Array Is Rotated**

This knowledge chunk belongs to:

**binary_search**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Find How Many Times the Array Is Rotated** problem.

The primary problem-solving pattern is:

**Binary Search for Minimum / Rotation Count**

---

## Key Idea

For a rotated sorted array without duplicates, the index of the minimum element represents how many positions the array was rotated.

### Core Invariant

The index of the minimum element is preserved as the rotation count, and the minimum remains inside the search interval.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Scan the array to find the minimum element and return its index.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Set low = 0 and high = n - 1.
2. Track the smallest value and its index.
3. If the current range is already sorted, compare nums[low] with the best minimum.
4. Calculate mid.
5. If nums[mid] is smaller than the current minimum, update the answer.
6. If nums[mid] is greater than nums[high], search the right half.
7. Otherwise search the left half.
8. Return the index of the minimum element.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Binary Search for Minimum / Rotation Count**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What does the position of the minimum element tell you about the number of rotations?

### Hint 2

Can you find the minimum using the same binary-search idea as the rotated-array minimum problem?

---

## Common Mistakes

- Returning the minimum value instead of its index.
- Confusing rotation count with the maximum element index.
- Using linear search when binary search is expected.

---

## Edge Cases

- Array is not rotated.
- Array is rotated once.
- Array is rotated n - 1 times.
- Two-element array.

---

## Complexity Analysis

### Time Complexity

**O(log N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Find How Many Times the Array Is Rotated** is:

> For a rotated sorted array without duplicates, the index of the minimum element represents how many positions the array was rotated.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- rotation count
- number of rotations
- rotated sorted array
- minimum index
- binary search

---

## Problem Retrieval Identity

Problem Name: Find How Many Times the Array Is Rotated

Problem ID: find_how_many_times_array_is_rotated

Topic: binary_search

Pattern: Binary Search for Minimum / Rotation Count

Difficulty: Easy

Primary Retrieval Entity:

**Find How Many Times the Array Is Rotated**

This document should be preferred when a user explicitly asks about:

- rotation count
- number of rotations
- rotated sorted array
- minimum index
- binary search

Related concepts:

- rotation count
- number of rotations
- rotated sorted array
- minimum index
- binary search
