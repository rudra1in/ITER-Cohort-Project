# Check if Two Strings Are Anagrams

Problem ID: valid_anagram

Title: Check if Two Strings Are Anagrams

Difficulty: Easy

Topic: strings

Pattern: **Frequency Counting**

---

## Problem Identity

This document is specifically about:

**Check if Two Strings Are Anagrams**

This knowledge chunk belongs to:

**strings**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Check if Two Strings Are Anagrams** problem.

The primary problem-solving pattern is:

**Frequency Counting**

---

## Key Idea

Two strings are anagrams when they contain exactly the same characters with the same frequencies. Character frequency counting provides a direct way to verify this.

### Core Invariant

The frequency structure represents the difference between character counts in the two strings processed so far.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Sort both strings and compare the resulting character sequences.

### Brute Force Complexity

- **Time Complexity:** O(N log N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Check whether both strings have the same length.
2. Create a frequency array or hash map.
3. Increase the count for every character in the first string.
4. Decrease the count for every character in the second string.
5. If every frequency becomes zero, the strings are anagrams.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Frequency Counting**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What information must be identical in two anagrams?

### Hint 2

Can you count characters instead of sorting the entire strings?

---

## Common Mistakes

- Ignoring character frequencies.
- Checking only whether both strings contain the same unique characters.
- Forgetting to check string lengths.

---

## Edge Cases

- Empty strings.
- Different lengths.
- Repeated characters.
- Identical strings.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(K)**

---

## Interview Explanation

A concise interview explanation for **Check if Two Strings Are Anagrams** is:

> Two strings are anagrams when they contain exactly the same characters with the same frequencies. Character frequency counting provides a direct way to verify this.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Valid Anagram
- anagram
- frequency count
- character frequency
- LeetCode 242

---

## Problem Retrieval Identity

Problem Name: Check if Two Strings Are Anagrams

Problem ID: valid_anagram

Topic: strings

Pattern: Frequency Counting

Difficulty: Easy

Primary Retrieval Entity:

**Check if Two Strings Are Anagrams**

This document should be preferred when a user explicitly asks about:

- Valid Anagram
- anagram
- frequency count
- character frequency
- LeetCode 242

Related concepts:

- Valid Anagram
- anagram
- frequency count
- character frequency
- LeetCode 242
