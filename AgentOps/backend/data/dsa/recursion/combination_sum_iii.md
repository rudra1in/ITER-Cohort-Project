# Combination Sum III

Problem ID: combination_sum_iii

Title: Combination Sum III

Difficulty: Medium

Topic: recursion

Pattern: **Backtracking + Fixed Length**

---

## Problem Identity

This document is specifically about:

**Combination Sum III**

This knowledge chunk belongs to:

**recursion**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Combination Sum III** problem.

The primary problem-solving pattern is:

**Backtracking + Fixed Length**

---

## Key Idea

Choose exactly k distinct numbers from 1 to 9 whose sum equals the target. Backtracking explores choices while ensuring numbers are not reused.

### Core Invariant

The combination always contains distinct increasing numbers, and all future choices are greater than the last selected number.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Generate combinations of numbers from 1 to 9 and keep those containing exactly k numbers with the required sum.

### Brute Force Complexity

- **Time Complexity:** O(2^9)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Start from number 1.
2. Maintain the current combination and remaining target.
3. Choose a number between the current start and 9.
4. Add it to the combination.
5. Recursively choose the next number starting from current + 1.
6. Backtrack after returning.
7. Store the combination when exactly k numbers have been chosen and the target becomes zero.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Backtracking + Fixed Length**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How can you guarantee that numbers are not reused?

### Hint 2

Why should the next recursive call start from current + 1?

---

## Common Mistakes

- Using the same number more than once.
- Accepting combinations with the wrong number of elements.
- Ignoring the target condition.
- Not backtracking.

---

## Edge Cases

- k = 1.
- k = 9.
- Target is too small.
- Target is too large.
- No valid combination.

---

## Complexity Analysis

### Time Complexity

**O(C(9,k) * k) in the worst case.**

### Space Complexity

**O(k) recursion depth excluding output.**

---

## Interview Explanation

A concise interview explanation for **Combination Sum III** is:

> Choose exactly k distinct numbers from 1 to 9 whose sum equals the target. Backtracking explores choices while ensuring numbers are not reused.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- combination sum III
- choose k numbers
- backtracking
- recursion
- 1 to 9

---

## Problem Retrieval Identity

Problem Name: Combination Sum III

Problem ID: combination_sum_iii

Topic: recursion

Pattern: Backtracking + Fixed Length

Difficulty: Medium

Primary Retrieval Entity:

**Combination Sum III**

This document should be preferred when a user explicitly asks about:

- combination sum III
- choose k numbers
- backtracking
- recursion
- 1 to 9

Related concepts:

- combination sum III
- choose k numbers
- backtracking
- recursion
- 1 to 9
