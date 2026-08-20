# Rotate String

Problem ID: rotate_string

Title: Rotate String

Difficulty: Easy

Topic: strings

Pattern: **String Rotation / Concatenation**

---

## Problem Identity

This document is specifically about:

**Rotate String**

This knowledge chunk belongs to:

**strings**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Rotate String** problem.

The primary problem-solving pattern is:

**String Rotation / Concatenation**

---

## Key Idea

A string can be rotated into another string if and only if the goal string has the same length and appears as a substring of the original string concatenated with itself.

### Core Invariant

Every possible rotation of a string appears as a substring of the string concatenated with itself.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Perform every possible rotation and compare each resulting string with the goal.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Check whether the two strings have the same length.
2. Concatenate the original string with itself.
3. Check whether the goal string occurs inside the concatenated string.
4. Return true if it occurs; otherwise return false.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**String Rotation / Concatenation**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What string do you get when you concatenate the original string with itself?

### Hint 2

Where would every possible rotation appear?

---

## Common Mistakes

- Forgetting to check equal lengths.
- Trying only one rotation.
- Concatenating the wrong strings.

---

## Edge Cases

- Both strings are empty.
- Single character.
- Strings are identical.
- Different lengths.

---

## Complexity Analysis

### Time Complexity

**O(N^2) with straightforward substring search.**

### Space Complexity

**O(N)**

---

## Interview Explanation

A concise interview explanation for **Rotate String** is:

> A string can be rotated into another string if and only if the goal string has the same length and appears as a substring of the original string concatenated with itself.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Rotate String
- string rotation
- string concatenation
- LeetCode 796

---

## Problem Retrieval Identity

Problem Name: Rotate String

Problem ID: rotate_string

Topic: strings

Pattern: String Rotation / Concatenation

Difficulty: Easy

Primary Retrieval Entity:

**Rotate String**

This document should be preferred when a user explicitly asks about:

- Rotate String
- string rotation
- string concatenation
- LeetCode 796

Related concepts:

- Rotate String
- string rotation
- string concatenation
- LeetCode 796
