# Count Number of Nice Subarrays

Problem ID: count_number_of_nice_subarrays

Title: Count Number of Nice Subarrays

Difficulty: Medium

Topic: sliding_window

Pattern: **AtMost Sliding Window**

---

## Problem Identity

This document is specifically about:

**Count Number of Nice Subarrays**

This knowledge chunk belongs to:

**sliding_window**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Count Number of Nice Subarrays** problem.

The primary problem-solving pattern is:

**AtMost Sliding Window**

---

## Key Idea

A nice subarray contains exactly K odd numbers. Count subarrays with at most K odd numbers and subtract those with at most K - 1 odd numbers.

### Core Invariant

The current window contains at most K odd numbers.

---

## Brute Force Approach

Generate every subarray and count the number of odd elements.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a helper function that counts subarrays with at most K odd numbers.
2. Maintain a sliding window.
3. Increment oddCount whenever an odd number enters.
4. If oddCount exceeds K, move left forward.
5. Add right - left + 1 to the answer.
6. Return atMost(K) - atMost(K - 1).

### Why This Works

The optimized solution works because it exploits the structure provided by:

**AtMost Sliding Window**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What property makes a subarray nice?

### Hint 2

Can you convert exactly K into two atMost problems?

---

## Common Mistakes

- Counting exactly K directly with an incorrect shrinking rule.
- Forgetting K - 1.
- Checking even numbers instead of odd numbers.
- Incorrectly counting valid windows.

---

## Edge Cases

- K equals 0 if allowed.
- K equals 1.
- No odd numbers.
- All numbers are odd.
- K is greater than the number of odd elements.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Count Number of Nice Subarrays** is:

> A nice subarray contains exactly K odd numbers. Count subarrays with at most K odd numbers and subtract those with at most K - 1 odd numbers.

When explaining this problem in an interview, focus on:

1. The core idea behind the problem.
2. The data structure or algorithm being used.
3. The important steps of the approach.
4. Why the approach works.
5. The time and space complexity.
6. Common edge cases and mistakes.

---

## Retrieval Keywords

- nice subarrays
- exactly K odd
- at most K
- sliding window
- two pointers

---

## Problem Retrieval Identity

Problem Name: Count Number of Nice Subarrays

Problem ID: count_number_of_nice_subarrays

Topic: sliding_window

Pattern: AtMost Sliding Window

Difficulty: Medium

Primary Retrieval Entity:

**Count Number of Nice Subarrays**

This document should be preferred when a user explicitly asks about:

- nice subarrays
- exactly K odd
- at most K
- sliding window
- two pointers

Related concepts:

- nice subarrays
- exactly K odd
- at most K
- sliding window
- two pointers
