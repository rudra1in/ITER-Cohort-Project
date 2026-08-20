# Subarrays with K Different Integers

Problem ID: subarrays_with_k_different_integers

Title: Subarrays with K Different Integers

Difficulty: Hard

Topic: sliding_window

Pattern: **AtMost(K) - AtMost(K-1)**

---

## Problem Identity

This document is specifically about:

**Subarrays with K Different Integers**

This knowledge chunk belongs to:

**sliding_window**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Subarrays with K Different Integers** problem.

The primary problem-solving pattern is:

**AtMost(K) - AtMost(K-1)**

---

## Key Idea

Count subarrays with exactly K distinct integers by calculating atMost(K) - atMost(K - 1).

### Core Invariant

The helper window contains at most K distinct integers.

---

## Brute Force Approach

Generate every subarray and count its distinct integers.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a helper function that counts subarrays with at most K distinct integers.
2. Maintain a frequency map for the current window.
3. Expand the right pointer.
4. If the number of distinct integers exceeds K, move left forward.
5. Add right - left + 1 to the count.
6. Return atMost(K) - atMost(K - 1).

### Why This Works

The optimized solution works because it exploits the structure provided by:

**AtMost(K) - AtMost(K-1)**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can exactly K be expressed using two atMost calculations?

### Hint 2

How do you maintain distinct integer count?

---

## Common Mistakes

- Trying to count exactly K directly.
- Forgetting the atMost(K - 1) subtraction.
- Not deleting zero-frequency elements.
- Counting frequencies instead of distinct values.

---

## Edge Cases

- K equals 1.
- K equals number of distinct values.
- All elements are identical.
- All elements are different.
- K is greater than the number of distinct elements.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(K)**

---

## Interview Explanation

A concise interview explanation for **Subarrays with K Different Integers** is:

> Count subarrays with exactly K distinct integers by calculating atMost(K) - atMost(K - 1).

When explaining this problem in an interview, focus on:

1. The core idea behind the problem.
2. The data structure or algorithm being used.
3. The important steps of the approach.
4. Why the approach works.
5. The time and space complexity.
6. Common edge cases and mistakes.

---

## Retrieval Keywords

- subarrays with K distinct
- exactly K
- at most K
- frequency map
- sliding window

---

## Problem Retrieval Identity

Problem Name: Subarrays with K Different Integers

Problem ID: subarrays_with_k_different_integers

Topic: sliding_window

Pattern: AtMost(K) - AtMost(K-1)

Difficulty: Hard

Primary Retrieval Entity:

**Subarrays with K Different Integers**

This document should be preferred when a user explicitly asks about:

- subarrays with K distinct
- exactly K
- at most K
- frequency map
- sliding window

Related concepts:

- subarrays with K distinct
- exactly K
- at most K
- frequency map
- sliding window
