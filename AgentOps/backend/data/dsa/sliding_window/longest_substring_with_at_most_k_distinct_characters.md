# Longest Substring With At Most K Distinct Characters

Problem ID: longest_substring_with_at_most_k_distinct_characters

Title: Longest Substring With At Most K Distinct Characters

Difficulty: Medium

Topic: sliding_window

Pattern: **At Most K Distinct Sliding Window**

---

## Problem Identity

This document is specifically about:

**Longest Substring With At Most K Distinct Characters**

This knowledge chunk belongs to:

**sliding_window**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Longest Substring With At Most K Distinct Characters** problem.

The primary problem-solving pattern is:

**At Most K Distinct Sliding Window**

---

## Key Idea

Maintain a window containing at most K distinct characters and maximize its length.

### Core Invariant

The current window always contains at most K distinct characters.

---

## Brute Force Approach

Generate every substring and count the number of distinct characters.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize left = 0 and a frequency map.
2. Expand the right pointer.
3. Add the current character to the frequency map.
4. If the number of distinct characters exceeds K, move left forward.
5. Remove characters whose frequency becomes zero.
6. Track the maximum window length.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**At Most K Distinct Sliding Window**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What exactly does K limit?

### Hint 2

How can a frequency map track distinct characters?

---

## Common Mistakes

- Counting character frequency instead of distinct characters.
- Not deleting characters when their frequency reaches zero.
- Allowing K + 1 distinct characters.
- Using nested loops unnecessarily.

---

## Edge Cases

- K equals 0.
- K equals 1.
- K is greater than the number of distinct characters.
- Empty string.
- All characters are identical.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(K)**

---

## Interview Explanation

A concise interview explanation for **Longest Substring With At Most K Distinct Characters** is:

> Maintain a window containing at most K distinct characters and maximize its length.

When explaining this problem in an interview, focus on:

1. The core idea behind the problem.
2. The data structure or algorithm being used.
3. The important steps of the approach.
4. Why the approach works.
5. The time and space complexity.
6. Common edge cases and mistakes.

---

## Retrieval Keywords

- at most K distinct
- longest substring
- sliding window
- frequency map
- variable window

---

## Problem Retrieval Identity

Problem Name: Longest Substring With At Most K Distinct Characters

Problem ID: longest_substring_with_at_most_k_distinct_characters

Topic: sliding_window

Pattern: At Most K Distinct Sliding Window

Difficulty: Medium

Primary Retrieval Entity:

**Longest Substring With At Most K Distinct Characters**

This document should be preferred when a user explicitly asks about:

- at most K distinct
- longest substring
- sliding window
- frequency map
- variable window

Related concepts:

- at most K distinct
- longest substring
- sliding window
- frequency map
- variable window
