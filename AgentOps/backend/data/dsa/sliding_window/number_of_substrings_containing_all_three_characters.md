# Number of Substrings Containing All Three Characters

Problem ID: number_of_substrings_containing_all_three_characters

Title: Number of Substrings Containing All Three Characters

Difficulty: Medium

Topic: sliding_window

Pattern: **Frequency + Sliding Window**

---

## Problem Identity

This document is specifically about:

**Number of Substrings Containing All Three Characters**

This knowledge chunk belongs to:

**sliding_window**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Number of Substrings Containing All Three Characters** problem.

The primary problem-solving pattern is:

**Frequency + Sliding Window**

---

## Key Idea

Maintain a window containing characters a, b, and c. Once the window contains all three characters, every extension to the right remains valid.

### Core Invariant

Whenever the window contains all three required characters, the counted substrings satisfy the requirement.

---

## Brute Force Approach

Generate every substring and check whether it contains a, b, and c.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Maintain the last occurrence or frequency of a, b, and c.
2. Move the right pointer through the string.
3. Update the position or frequency of the current character.
4. When all three characters have appeared, count all valid starting positions.
5. Continue expanding the right pointer.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Frequency + Sliding Window**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What are the required characters?

### Hint 2

Can you track their latest positions?

---

## Common Mistakes

- Counting only the current window.
- Forgetting that extending the substring to the right preserves validity.
- Using O(N^2) substring creation.
- Incorrectly handling the first occurrence of each character.

---

## Edge Cases

- String shorter than three characters.
- Only one distinct character.
- Exactly one occurrence of each character.
- Repeated characters.
- All three characters appear near the end.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Number of Substrings Containing All Three Characters** is:

> Maintain a window containing characters a, b, and c. Once the window contains all three characters, every extension to the right remains valid.

When explaining this problem in an interview, focus on:

1. The core idea behind the problem.
2. The data structure or algorithm being used.
3. The important steps of the approach.
4. Why the approach works.
5. The time and space complexity.
6. Common edge cases and mistakes.

---

## Retrieval Keywords

- substrings
- all three characters
- a b c
- sliding window
- frequency
- last occurrence

---

## Problem Retrieval Identity

Problem Name: Number of Substrings Containing All Three Characters

Problem ID: number_of_substrings_containing_all_three_characters

Topic: sliding_window

Pattern: Frequency + Sliding Window

Difficulty: Medium

Primary Retrieval Entity:

**Number of Substrings Containing All Three Characters**

This document should be preferred when a user explicitly asks about:

- substrings
- all three characters
- a b c
- sliding window
- frequency
- last occurrence

Related concepts:

- substrings
- all three characters
- a b c
- sliding window
- frequency
- last occurrence
