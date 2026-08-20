# Minimum Window Substring

Problem ID: minimum_window_substring

Title: Minimum Window Substring

Difficulty: Hard

Topic: sliding_window

Pattern: **Required Frequency + Variable Sliding Window**

---

## Problem Identity

This document is specifically about:

**Minimum Window Substring**

This knowledge chunk belongs to:

**sliding_window**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Minimum Window Substring** problem.

The primary problem-solving pattern is:

**Required Frequency + Variable Sliding Window**

---

## Key Idea

Find the smallest substring of s that contains all characters of t with the required frequencies. Expand until valid, then shrink from the left while validity is maintained.

### Core Invariant

Whenever the window is considered valid, it contains every required character with at least the required frequency.

---

## Brute Force Approach

Generate every substring of s and check whether it contains all required characters with sufficient frequency.

### Brute Force Complexity

- **Time Complexity:** O(N^2 * K)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Build a frequency map for the required characters in t.
2. Initialize left = 0 and track how many required characters are satisfied.
3. Expand the right pointer and update the window frequency.
4. When the window satisfies all required frequencies, record its length.
5. Move left forward to make the window as small as possible.
6. Stop shrinking when the window becomes invalid.
7. Continue expanding right until the entire string is processed.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Required Frequency + Variable Sliding Window**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How can you track required frequencies?

### Hint 2

When is the current window valid?

---

## Common Mistakes

- Checking only whether characters exist instead of checking frequencies.
- Not shrinking the window after it becomes valid.
- Updating the answer after the window becomes invalid.
- Incorrectly handling duplicate characters in t.
- Returning an invalid window when no solution exists.

---

## Edge Cases

- t is longer than s.
- No valid window exists.
- s equals t.
- t contains duplicate characters.
- Multiple valid windows have the same size.
- Single-character strings.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(K)**

---

## Interview Explanation

A concise interview explanation for **Minimum Window Substring** is:

> Find the smallest substring of s that contains all characters of t with the required frequencies. Expand until valid, then shrink from the left while validity is maintained.

When explaining this problem in an interview, focus on:

1. The core idea behind the problem.
2. The data structure or algorithm being used.
3. The important steps of the approach.
4. Why the approach works.
5. The time and space complexity.
6. Common edge cases and mistakes.

---

## Retrieval Keywords

- minimum window substring
- required frequency
- sliding window
- HashMap
- variable window
- frequency matching

---

## Problem Retrieval Identity

Problem Name: Minimum Window Substring

Problem ID: minimum_window_substring

Topic: sliding_window

Pattern: Required Frequency + Variable Sliding Window

Difficulty: Hard

Primary Retrieval Entity:

**Minimum Window Substring**

This document should be preferred when a user explicitly asks about:

- minimum window substring
- required frequency
- sliding window
- HashMap
- variable window
- frequency matching

Related concepts:

- minimum window substring
- required frequency
- sliding window
- HashMap
- variable window
- frequency matching
