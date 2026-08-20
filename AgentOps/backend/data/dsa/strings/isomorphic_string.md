# Isomorphic String

Problem ID: isomorphic_string

Title: Isomorphic String

Difficulty: Easy

Topic: strings

Pattern: **Hash Map / Character Mapping**

---

## Problem Identity

This document is specifically about:

**Isomorphic String**

This knowledge chunk belongs to:

**strings**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Isomorphic String** problem.

The primary problem-solving pattern is:

**Hash Map / Character Mapping**

---

## Key Idea

Two strings are isomorphic when every character in the first string maps to exactly one character in the second string and the mapping is consistent in both directions.

### Core Invariant

At every position, the character mapping remains one-to-one and consistent with all previously processed characters.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Track mappings between characters and repeatedly check whether an existing mapping conflicts with the current pair.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a mapping from characters of the first string to the second.
2. Create a reverse mapping from the second string to the first.
3. Traverse both strings together.
4. If an existing mapping conflicts, return false.
5. Otherwise create the required mappings.
6. Return true after processing all characters.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Hash Map / Character Mapping**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can two different characters in the first string map to the same character?

### Hint 2

Why do you need to check the mapping in both directions?

---

## Common Mistakes

- Checking only one direction of mapping.
- Allowing two source characters to map to the same destination.
- Ignoring string length differences.

---

## Edge Cases

- Strings of different lengths.
- Single-character strings.
- Repeated characters.
- No repeated characters.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(K)**

---

## Interview Explanation

A concise interview explanation for **Isomorphic String** is:

> Two strings are isomorphic when every character in the first string maps to exactly one character in the second string and the mapping is consistent in both directions.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Isomorphic String
- character mapping
- hash map
- LeetCode 205

---

## Problem Retrieval Identity

Problem Name: Isomorphic String

Problem ID: isomorphic_string

Topic: strings

Pattern: Hash Map / Character Mapping

Difficulty: Easy

Primary Retrieval Entity:

**Isomorphic String**

This document should be preferred when a user explicitly asks about:

- Isomorphic String
- character mapping
- hash map
- LeetCode 205

Related concepts:

- Isomorphic String
- character mapping
- hash map
- LeetCode 205
