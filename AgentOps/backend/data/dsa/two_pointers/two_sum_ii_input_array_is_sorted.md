# Two Sum II – Input Array Is Sorted

Problem ID: two_sum_ii_input_array_is_sorted

Title: Two Sum II – Input Array Is Sorted

Difficulty: Easy

Topic: two_pointers

Pattern: **Left + Right Pointer**

---

## Problem Identity

This document is specifically about:

**Two Sum II – Input Array Is Sorted**

This knowledge chunk belongs to:

**two_pointers**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Two Sum II – Input Array Is Sorted** problem.

The primary problem-solving pattern is:

**Left + Right Pointer**

---

## Key Idea

Because the array is sorted, use one pointer at the beginning and another at the end. Move the left pointer when the sum is too small and the right pointer when the sum is too large.

### Core Invariant

All pairs outside the current left-right range have already been eliminated because the sorted order proves they cannot produce the required target.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Check every pair of elements using two nested loops and return the pair whose sum equals the target.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize left = 0 and right = n - 1.
2. Calculate the sum of nums[left] + nums[right].
3. If the sum equals the target, return the two positions.
4. If the sum is smaller than the target, move left forward.
5. If the sum is larger than the target, move right backward.
6. Continue until the pointers meet.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Left + Right Pointer**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

The array is already sorted. How can that help you eliminate pairs?

### Hint 2

What should you do if the current sum is too small?

---

## Common Mistakes

- Using a hash map unnecessarily.
- Moving both pointers after every comparison.
- Forgetting that the array is sorted.
- Using incorrect indexing when the problem expects 1-based positions.

---

## Edge Cases

- Array contains only two elements.
- Target equals the sum of the first and last elements.
- Negative numbers.
- Duplicate values.
- No valid pair exists.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Two Sum II – Input Array Is Sorted** is:

> Because the array is sorted, use one pointer at the beginning and another at the end. Move the left pointer when the sum is too small and the right pointer when the sum is too large.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- two sum
- sorted array
- two pointers
- left pointer
- right pointer
- target sum

---

## Problem Retrieval Identity

Problem Name: Two Sum II – Input Array Is Sorted

Problem ID: two_sum_ii_input_array_is_sorted

Topic: two_pointers

Pattern: Left + Right Pointer

Difficulty: Easy

Primary Retrieval Entity:

**Two Sum II – Input Array Is Sorted**

This document should be preferred when a user explicitly asks about:

- two sum
- sorted array
- two pointers
- left pointer
- right pointer
- target sum

Related concepts:

- two sum
- sorted array
- two pointers
- left pointer
- right pointer
- target sum
