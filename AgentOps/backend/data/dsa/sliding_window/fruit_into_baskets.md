# Fruit Into Baskets

Problem ID: fruit_into_baskets

Title: Fruit Into Baskets

Difficulty: Medium

Topic: sliding_window

Pattern: **At Most 2 Distinct Sliding Window**

---

## Problem Identity

This document is specifically about:

**Fruit Into Baskets**

This knowledge chunk belongs to:

**sliding_window**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Fruit Into Baskets** problem.

The primary problem-solving pattern is:

**At Most 2 Distinct Sliding Window**

---

## Key Idea

Find the longest contiguous subarray containing at most two distinct fruit types.

### Core Invariant

The current window contains at most two distinct fruit types.

---

## Brute Force Approach

Generate every subarray and count the number of distinct fruit types.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize left = 0 and a frequency map.
2. Expand the right pointer.
3. Add fruits[right] to the frequency map.
4. If the number of distinct fruit types becomes greater than 2, move left forward.
5. Remove elements from the frequency map as they leave the window.
6. Track the maximum window length.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**At Most 2 Distinct Sliding Window**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How many distinct fruit types can the window contain?

### Hint 2

What data structure can count distinct values?

---

## Common Mistakes

- Allowing three fruit types in the window.
- Forgetting to remove a fruit when its frequency becomes zero.
- Counting total fruits instead of distinct types.
- Resetting the entire window unnecessarily.

---

## Edge Cases

- Empty array.
- One fruit type.
- Exactly two fruit types.
- Every fruit is different.
- All fruits are identical.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Fruit Into Baskets** is:

> Find the longest contiguous subarray containing at most two distinct fruit types.

When explaining this problem in an interview, focus on:

1. The core idea behind the problem.
2. The data structure or algorithm being used.
3. The important steps of the approach.
4. Why the approach works.
5. The time and space complexity.
6. Common edge cases and mistakes.

---

## Retrieval Keywords

- fruit into baskets
- at most two distinct
- sliding window
- frequency map
- variable window

---

## Problem Retrieval Identity

Problem Name: Fruit Into Baskets

Problem ID: fruit_into_baskets

Topic: sliding_window

Pattern: At Most 2 Distinct Sliding Window

Difficulty: Medium

Primary Retrieval Entity:

**Fruit Into Baskets**

This document should be preferred when a user explicitly asks about:

- fruit into baskets
- at most two distinct
- sliding window
- frequency map
- variable window

Related concepts:

- fruit into baskets
- at most two distinct
- sliding window
- frequency map
- variable window
