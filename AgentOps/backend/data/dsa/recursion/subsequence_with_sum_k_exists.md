# Check if There Exists a Subsequence with Sum K

Problem ID: subsequence_with_sum_k_exists

Title: Check if There Exists a Subsequence with Sum K

Difficulty: Easy

Topic: recursion

Pattern: **Recursion + Boolean Backtracking**

---

## Problem Identity

This document is specifically about:

**Check if There Exists a Subsequence with Sum K**

This knowledge chunk belongs to:

**recursion**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Check if There Exists a Subsequence with Sum K** problem.

The primary problem-solving pattern is:

**Recursion + Boolean Backtracking**

---

## Key Idea

Recursively explore include and exclude choices for each element and return true as soon as a subsequence with the required sum is found.

### Core Invariant

The running sum represents the sum of the selected elements on the current recursion path.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Generate all subsequences and check whether any of them has sum K.

### Brute Force Complexity

- **Time Complexity:** O(2^N * N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Start from index 0 with running sum zero.
2. If the running sum becomes K, return true.
3. If all elements are processed, return false.
4. Try including the current element.
5. If that branch succeeds, return true.
6. Otherwise try excluding the current element.
7. Return the result of the two choices.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Recursion + Boolean Backtracking**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can you return a boolean from each recursive branch?

### Hint 2

What happens when either the include or exclude branch finds a valid subsequence?

---

## Common Mistakes

- Forgetting one of the two branches.
- Returning false too early.
- Incorrectly handling the base case.
- Not stopping once a valid subsequence is found.

---

## Edge Cases

- Empty array.
- K = 0.
- No valid subsequence.
- Entire array forms the required sum.

---

## Complexity Analysis

### Time Complexity

**O(2^N) in the worst case.**

### Space Complexity

**O(N) recursion depth.**

---

## Interview Explanation

A concise interview explanation for **Check if There Exists a Subsequence with Sum K** is:

> Recursively explore include and exclude choices for each element and return true as soon as a subsequence with the required sum is found.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- subsequence sum K
- exists subsequence
- recursion
- backtracking
- boolean recursion

---

## Problem Retrieval Identity

Problem Name: Check if There Exists a Subsequence with Sum K

Problem ID: subsequence_with_sum_k_exists

Topic: recursion

Pattern: Recursion + Boolean Backtracking

Difficulty: Easy

Primary Retrieval Entity:

**Check if There Exists a Subsequence with Sum K**

This document should be preferred when a user explicitly asks about:

- subsequence sum K
- exists subsequence
- recursion
- backtracking
- boolean recursion

Related concepts:

- subsequence sum K
- exists subsequence
- recursion
- backtracking
- boolean recursion
