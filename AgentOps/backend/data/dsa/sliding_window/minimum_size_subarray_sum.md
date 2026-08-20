# Minimum Size Subarray Sum

Problem ID: minimum_size_subarray_sum

Title: Minimum Size Subarray Sum

Difficulty: Medium

Topic: sliding_window

Pattern: **Variable Sliding Window**

---

## Problem Identity

This document is specifically about:

**Minimum Size Subarray Sum**

This knowledge chunk belongs to:

**sliding_window**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Minimum Size Subarray Sum** problem.

The primary problem-solving pattern is:

**Variable Sliding Window**

---

## Key Idea

For an array of positive integers, expand the window until its sum reaches the target, then shrink it from the left to find the smallest valid window.

### Core Invariant

The current window is adjusted so that when its sum reaches the target, shrinking from the left finds the smallest valid window ending at right.

---

## Brute Force Approach

Generate every subarray and calculate its sum. Track the shortest subarray whose sum is at least the target.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize left = 0, currentSum = 0, and minimumLength = infinity.
2. Expand the right pointer and add nums[right] to currentSum.
3. While currentSum is at least target, update the minimum length.
4. Remove nums[left] from currentSum and move left forward.
5. Continue until the right pointer reaches the end.
6. If no valid subarray exists, return 0.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Variable Sliding Window**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Why does positivity of the array matter?

### Hint 2

When should you expand the window?

---

## Common Mistakes

- Using this sliding window approach when negative numbers are present.
- Shrinking only once instead of while the sum is valid.
- Forgetting to update the answer before shrinking.
- Returning infinity instead of 0 when no valid subarray exists.

---

## Edge Cases

- No subarray reaches the target.
- One element equals the target.
- The entire array is required.
- Target is smaller than the first element.
- Single-element array.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Minimum Size Subarray Sum** is:

> For an array of positive integers, expand the window until its sum reaches the target, then shrink it from the left to find the smallest valid window.

When explaining this problem in an interview, focus on:

1. The core idea behind the problem.
2. The data structure or algorithm being used.
3. The important steps of the approach.
4. Why the approach works.
5. The time and space complexity.
6. Common edge cases and mistakes.

---

## Retrieval Keywords

- minimum size subarray
- minimum length
- target sum
- positive integers
- variable sliding window

---

## Problem Retrieval Identity

Problem Name: Minimum Size Subarray Sum

Problem ID: minimum_size_subarray_sum

Topic: sliding_window

Pattern: Variable Sliding Window

Difficulty: Medium

Primary Retrieval Entity:

**Minimum Size Subarray Sum**

This document should be preferred when a user explicitly asks about:

- minimum size subarray
- minimum length
- target sum
- positive integers
- variable sliding window

Related concepts:

- minimum size subarray
- minimum length
- target sum
- positive integers
- variable sliding window
