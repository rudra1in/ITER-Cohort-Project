# Binary Subarrays With Sum

Problem ID: binary_subarrays_with_sum

Title: Binary Subarrays With Sum

Difficulty: Medium

Topic: sliding_window

Pattern: **AtMost Sliding Window**

---

## Problem Identity

This document is specifically about:

**Binary Subarrays With Sum**

This knowledge chunk belongs to:

**sliding_window**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Binary Subarrays With Sum** problem.

The primary problem-solving pattern is:

**AtMost Sliding Window**

---

## Key Idea

For a binary array, count subarrays with sum exactly goal using atMost(goal) - atMost(goal - 1).

### Core Invariant

The sliding window maintained by atMost contains a sum less than or equal to the specified goal.

---

## Brute Force Approach

Generate every subarray and calculate its sum. Count subarrays whose sum equals the target.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a helper function atMost(goal).
2. Maintain a sliding window whose sum is at most goal.
3. Expand the right pointer and add nums[right].
4. While the sum is greater than goal, move left forward.
5. Every valid window ending at right contributes right - left + 1 subarrays.
6. Return atMost(goal) - atMost(goal - 1).

### Why This Works

The optimized solution works because it exploits the structure provided by:

**AtMost Sliding Window**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can you count subarrays with sum at most goal?

### Hint 2

How can exactly goal be obtained from two atMost counts?

---

## Common Mistakes

- Trying to directly count exact sums using a normal shrinking window.
- Forgetting the atMost(goal - 1) term.
- Not handling goal = 0 correctly.
- Using this exact technique on arbitrary negative numbers.

---

## Edge Cases

- Goal equals 0.
- All elements are zero.
- All elements are one.
- Single-element array.
- Goal is larger than total sum.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Binary Subarrays With Sum** is:

> For a binary array, count subarrays with sum exactly goal using atMost(goal) - atMost(goal - 1).

When explaining this problem in an interview, focus on:

1. The core idea behind the problem.
2. The data structure or algorithm being used.
3. The important steps of the approach.
4. Why the approach works.
5. The time and space complexity.
6. Common edge cases and mistakes.

---

## Retrieval Keywords

- binary subarray
- exact sum
- at most
- sliding window
- prefix sum alternative

---

## Problem Retrieval Identity

Problem Name: Binary Subarrays With Sum

Problem ID: binary_subarrays_with_sum

Topic: sliding_window

Pattern: AtMost Sliding Window

Difficulty: Medium

Primary Retrieval Entity:

**Binary Subarrays With Sum**

This document should be preferred when a user explicitly asks about:

- binary subarray
- exact sum
- at most
- sliding window
- prefix sum alternative

Related concepts:

- binary subarray
- exact sum
- at most
- sliding window
- prefix sum alternative
