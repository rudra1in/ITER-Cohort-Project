# Longest Common Prefix

Problem ID: longest_common_prefix

Title: Longest Common Prefix

Difficulty: Easy

Topic: strings

Pattern: **String Comparison**

---

## Problem Identity

This document is specifically about:

**Longest Common Prefix**

This knowledge chunk belongs to:

**strings**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Longest Common Prefix** problem.

The primary problem-solving pattern is:

**String Comparison**

---

## Key Idea

Compare characters at the same position across all strings. Stop as soon as one string differs or ends.

### Core Invariant

The maintained prefix is always a common prefix of all strings processed so far.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use the first string as a candidate prefix and repeatedly shorten it until every string starts with that prefix.

### Brute Force Complexity

- **Time Complexity:** O(N × M)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Take the first string as the initial prefix.
2. Compare the prefix with each remaining string.
3. While the current string does not start with the prefix, remove the last character from the prefix.
4. Continue until all strings share the prefix.
5. Return the final prefix.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**String Comparison**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What happens if you compare the first string with every other string?

### Hint 2

When should the current prefix become shorter?

---

## Common Mistakes

- Assuming the first string itself is always the answer.
- Accessing characters beyond the length of a shorter string.
- Forgetting the empty-string case.

---

## Edge Cases

- Only one string.
- No common prefix.
- All strings identical.
- One string is empty.
- Different string lengths.

---

## Complexity Analysis

### Time Complexity

**O(N × M)**

### Space Complexity

**O(M)**

---

## Interview Explanation

A concise interview explanation for **Longest Common Prefix** is:

> Compare characters at the same position across all strings. Stop as soon as one string differs or ends.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Longest Common Prefix
- common prefix
- string comparison
- LeetCode 14

---

## Problem Retrieval Identity

Problem Name: Longest Common Prefix

Problem ID: longest_common_prefix

Topic: strings

Pattern: String Comparison

Difficulty: Easy

Primary Retrieval Entity:

**Longest Common Prefix**

This document should be preferred when a user explicitly asks about:

- Longest Common Prefix
- common prefix
- string comparison
- LeetCode 14

Related concepts:

- Longest Common Prefix
- common prefix
- string comparison
- LeetCode 14
