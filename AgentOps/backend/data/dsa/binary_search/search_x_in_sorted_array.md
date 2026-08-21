# Search X in Sorted Array

Problem ID: search_x_in_sorted_array

Title: Search X in Sorted Array

Difficulty: Easy

Topic: binary_search

Pattern: **Binary Search**

---

## Problem Identity

This document is specifically about:

**Search X in Sorted Array**

This knowledge chunk belongs to:

**binary_search**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Search X in Sorted Array** problem.

The primary problem-solving pattern is:

**Binary Search**

---

## Key Idea

Because the array is sorted, compare the target with the middle element. If the target is smaller, search the left half. If the target is larger, search the right half.

### Core Invariant

If the target exists in the array, it always remains inside the current search range from low to high.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Scan the array from left to right and compare every element with the target until the target is found.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Set low = 0 and high = n - 1.
2. Calculate mid = low + (high - low) / 2.
3. If nums[mid] equals the target, return mid.
4. If nums[mid] is smaller than the target, search the right half by setting low = mid + 1.
5. If nums[mid] is larger than the target, search the left half by setting high = mid - 1.
6. Return -1 if the target is not found.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Binary Search**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

The array is sorted. Can you eliminate half of the search space after checking the middle element?

### Hint 2

What should happen to low and high when nums[mid] is smaller or larger than the target?

---

## Common Mistakes

- Using linear search instead of exploiting sorted order.
- Updating low or high incorrectly.
- Using mid = (low + high) / 2 without considering integer overflow in languages where it matters.
- Forgetting to return -1 when the target does not exist.

---

## Edge Cases

- Empty array.
- Single-element array.
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

A concise interview explanation for **Search X in Sorted Array** is:

> Because the array is sorted, compare the target with the middle element. If the target is smaller, search the left half. If the target is larger, search the right half.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Binary Search
- Search X in Sorted Array
- search target
- sorted array
- LeetCode binary search
- binary search basic

---

## Problem Retrieval Identity

Problem Name: Search X in Sorted Array

Problem ID: search_x_in_sorted_array

Topic: binary_search

Pattern: Binary Search

Difficulty: Easy

Primary Retrieval Entity:

**Search X in Sorted Array**

This document should be preferred when a user explicitly asks about:

- Binary Search
- Search X in Sorted Array
- search target
- sorted array
- LeetCode binary search
- binary search basic

Related concepts:

- Binary Search
- Search X in Sorted Array
- search target
- sorted array
- LeetCode binary search
- binary search basic
