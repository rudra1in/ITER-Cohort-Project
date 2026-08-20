# Longest Repeating Character Replacement

Problem ID: longest_repeating_character_replacement

Title: Longest Repeating Character Replacement

Difficulty: Medium

Topic: sliding_window

Pattern: **Frequency + Variable Sliding Window**

---

## Problem Identity

This document is specifically about:

**Longest Repeating Character Replacement**

This knowledge chunk belongs to:

**sliding_window**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Longest Repeating Character Replacement** problem.

The primary problem-solving pattern is:

**Frequency + Variable Sliding Window**

---

## Key Idea

Maintain a window where the number of characters that must be replaced is at most K. The number of replacements needed is window length minus the frequency of the most frequent character.

### Core Invariant

The current window can be converted into a string of identical characters using at most K replacements.

---

## Brute Force Approach

Generate every substring and determine how many characters need to be replaced to make all characters equal.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize left = 0 and a frequency array.
2. Expand the right pointer.
3. Update the frequency of the current character.
4. Track the highest frequency inside the window.
5. Calculate replacements as windowLength - maxFrequency.
6. If replacements exceed K, move left forward.
7. Track the largest valid window.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Frequency + Variable Sliding Window**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Which character should remain unchanged?

### Hint 2

How many characters need replacement?

---

## Common Mistakes

- Using the total frequency instead of maximum frequency.
- Shrinking the window at the wrong condition.
- Forgetting to update the maximum frequency.
- Recomputing all character frequencies for every window.

---

## Edge Cases

- K equals 0.
- K is greater than or equal to string length.
- All characters are identical.
- All characters are different.
- Single-character string.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Longest Repeating Character Replacement** is:

> Maintain a window where the number of characters that must be replaced is at most K. The number of replacements needed is window length minus the frequency of the most frequent character.

When explaining this problem in an interview, focus on:

1. The core idea behind the problem.
2. The data structure or algorithm being used.
3. The important steps of the approach.
4. Why the approach works.
5. The time and space complexity.
6. Common edge cases and mistakes.

---

## Retrieval Keywords

- character replacement
- sliding window
- frequency
- maximum frequency
- K replacements

---

## Problem Retrieval Identity

Problem Name: Longest Repeating Character Replacement

Problem ID: longest_repeating_character_replacement

Topic: sliding_window

Pattern: Frequency + Variable Sliding Window

Difficulty: Medium

Primary Retrieval Entity:

**Longest Repeating Character Replacement**

This document should be preferred when a user explicitly asks about:

- character replacement
- sliding window
- frequency
- maximum frequency
- K replacements

Related concepts:

- character replacement
- sliding window
- frequency
- maximum frequency
- K replacements
