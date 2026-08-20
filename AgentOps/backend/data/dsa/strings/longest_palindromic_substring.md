# Longest Palindromic Substring

Problem ID: longest_palindromic_substring

Title: Longest Palindromic Substring

Difficulty: Medium

Topic: strings

Pattern: **Expand Around Center**

---

## Problem Identity

This document is specifically about:

**Longest Palindromic Substring**

This knowledge chunk belongs to:

**strings**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Longest Palindromic Substring** problem.

The primary problem-solving pattern is:

**Expand Around Center**

---

## Key Idea

Every palindrome has a center. Expand outward from every possible center while the characters remain equal, keeping track of the longest palindrome found.

### Core Invariant

During expansion, the substring between left and right remains a palindrome because matching characters are added symmetrically.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Generate every substring and check whether each substring is a palindrome.

### Brute Force Complexity

- **Time Complexity:** O(N^3)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Consider every character as a possible center of an odd-length palindrome.
2. Expand left and right while the characters match.
3. Also consider every gap between two characters as a center for an even-length palindrome.
4. Expand around that center.
5. Track the longest palindrome found.
6. Return the longest palindromic substring.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Expand Around Center**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Where is the center of a palindrome?

### Hint 2

Why do you need to consider both a character and the gap between two characters as possible centers?

---

## Common Mistakes

- Checking only odd-length palindromes.
- Checking only even-length palindromes.
- Expanding beyond the string boundaries.
- Returning the first palindrome instead of the longest one.

---

## Edge Cases

- Empty string.
- Single character.
- All characters identical.
- No palindrome longer than one character.
- Even-length palindrome.

---

## Complexity Analysis

### Time Complexity

**O(N^2)**

### Space Complexity

**O(1) auxiliary space excluding the output string.**

---

## Interview Explanation

A concise interview explanation for **Longest Palindromic Substring** is:

> Every palindrome has a center. Expand outward from every possible center while the characters remain equal, keeping track of the longest palindrome found.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Longest Palindromic Substring
- palindrome
- expand around center
- string
- LeetCode 5

---

## Problem Retrieval Identity

Problem Name: Longest Palindromic Substring

Problem ID: longest_palindromic_substring

Topic: strings

Pattern: Expand Around Center

Difficulty: Medium

Primary Retrieval Entity:

**Longest Palindromic Substring**

This document should be preferred when a user explicitly asks about:

- Longest Palindromic Substring
- palindrome
- expand around center
- string
- LeetCode 5

Related concepts:

- Longest Palindromic Substring
- palindrome
- expand around center
- string
- LeetCode 5
