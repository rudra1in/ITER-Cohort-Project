# Combination Sum II

Problem ID: combination_sum_ii

Title: Combination Sum II

Difficulty: Medium

Topic: recursion

Pattern: **Backtracking + Duplicate Handling**

---

## Problem Identity

This document is specifically about:

**Combination Sum II**

This knowledge chunk belongs to:

**recursion**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Combination Sum II** problem.

The primary problem-solving pattern is:

**Backtracking + Duplicate Handling**

---

## Key Idea

Sort the candidates and use backtracking. Each element can be used at most once, and duplicate values at the same recursion level are skipped to avoid duplicate combinations.

### Core Invariant

Each recursive level considers candidates from a non-decreasing index, ensuring that every input element is used at most once.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Generate every subset of candidates and keep those whose sum equals the target, removing duplicates afterward.

### Brute Force Complexity

- **Time Complexity:** O(2^N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Sort the candidates.
2. Start backtracking from index 0.
3. If the remaining target is zero, store the combination.
4. Skip duplicate values at the same recursion level.
5. Choose the current candidate.
6. Recursively continue from the next index because each element can be used only once.
7. Backtrack by removing the chosen candidate.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Backtracking + Duplicate Handling**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Why is sorting useful here?

### Hint 2

Why does recursion move to index + 1?

---

## Common Mistakes

- Reusing the same element.
- Forgetting to sort.
- Skipping duplicates incorrectly.
- Not moving to the next index after choosing an element.

---

## Edge Cases

- Duplicate candidates.
- No valid combination.
- Target equals zero.
- Candidate larger than target.

---

## Complexity Analysis

### Time Complexity

**O(2^N * N) in the worst case.**

### Space Complexity

**O(N) recursion depth excluding output.**

---

## Interview Explanation

A concise interview explanation for **Combination Sum II** is:

> Sort the candidates and use backtracking. Each element can be used at most once, and duplicate values at the same recursion level are skipped to avoid duplicate combinations.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- combination sum II
- backtracking
- subsets
- duplicate handling
- recursion

---

## Problem Retrieval Identity

Problem Name: Combination Sum II

Problem ID: combination_sum_ii

Topic: recursion

Pattern: Backtracking + Duplicate Handling

Difficulty: Medium

Primary Retrieval Entity:

**Combination Sum II**

This document should be preferred when a user explicitly asks about:

- combination sum II
- backtracking
- subsets
- duplicate handling
- recursion

Related concepts:

- combination sum II
- backtracking
- subsets
- duplicate handling
- recursion
