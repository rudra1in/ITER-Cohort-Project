# Longest Substring Without Repeating Characters

Problem ID: longest_substring_without_repeating_characters

Title: Longest Substring Without Repeating Characters

Difficulty: Medium

Topic: sliding_window

Pattern: **Variable Sliding Window**

---

## Problem Identity

This document is specifically about:

**Longest Substring Without Repeating Characters**

This knowledge chunk belongs to:

**sliding_window**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Longest Substring Without Repeating Characters** problem.

The primary problem-solving pattern is:

**Variable Sliding Window**

---

## Key Idea

Maintain a sliding window containing unique characters. Expand the right pointer and move the left pointer whenever a duplicate character appears.

### Core Invariant

The current window always contains no duplicate characters.

---

## Brute Force Approach

Generate every possible substring and check whether all characters are unique.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize left = 0 and a frequency map or set.
2. Move the right pointer through the string.
3. Add the current character to the window.
4. If the character already exists in the window, move left forward until the window becomes valid.
5. Track the maximum window length.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Variable Sliding Window**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can you maintain a window containing only unique characters?

### Hint 2

What should happen when a duplicate character enters the window?

---

## Common Mistakes

- Not moving the left pointer when a duplicate appears.
- Moving left only once instead of until the window becomes valid.
- Updating the maximum length before restoring the valid window.
- Using O(N^2) substring generation unnecessarily.

---

## Edge Cases

- Empty string.
- String with one character.
- All characters are unique.
- All characters are identical.
- Duplicate occurs immediately.
- Duplicate occurs near the end.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(K), where K is the number of distinct characters.**

---

## Interview Explanation

A concise interview explanation for **Longest Substring Without Repeating Characters** is:

> Maintain a sliding window containing unique characters. Expand the right pointer and move the left pointer whenever a duplicate character appears.

When explaining this problem in an interview, focus on:

1. The core idea behind the problem.
2. The data structure or algorithm being used.
3. The important steps of the approach.
4. Why the approach works.
5. The time and space complexity.
6. Common edge cases and mistakes.

---

## Retrieval Keywords

- sliding window
- longest substring
- no repeating characters
- HashSet
- frequency map
- variable window

---

## Problem Retrieval Identity

Problem Name: Longest Substring Without Repeating Characters

Problem ID: longest_substring_without_repeating_characters

Topic: sliding_window

Pattern: Variable Sliding Window

Difficulty: Medium

Primary Retrieval Entity:

**Longest Substring Without Repeating Characters**

This document should be preferred when a user explicitly asks about:

- sliding window
- longest substring
- no repeating characters
- HashSet
- frequency map
- variable window

Related concepts:

- sliding window
- longest substring
- no repeating characters
- HashSet
- frequency map
- variable window
