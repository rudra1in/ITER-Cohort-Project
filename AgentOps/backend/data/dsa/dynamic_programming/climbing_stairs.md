# Climbing Stairs

Problem ID: climbing_stairs

Title: Climbing Stairs

Difficulty: Easy

Topic: dynamic_programming

Pattern: **1D DP**

---

## Problem Identity

This document is specifically about:

**Climbing Stairs**

This knowledge chunk belongs to:

**dynamic_programming**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Climbing Stairs** problem.

The primary problem-solving pattern is:

**1D DP**

---

## Key Idea

To reach step n, the last move must come from either step n-1 or step n-2. Therefore the number of ways to reach n is the sum of the ways to reach n-1 and n-2.

### Core Invariant

At every step i, the stored state represents the number of distinct ways to reach exactly step i.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use recursion to try taking either one step or two steps at every position. This creates many repeated subproblems.

### Brute Force Complexity

- **Time Complexity:** O(2^N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Define dp[i] as the number of ways to reach step i.
2. Initialize dp[0] = 1 and dp[1] = 1.
3. For every step from 2 to n, calculate dp[i] = dp[i - 1] + dp[i - 2].
4. Return dp[n].
5. The array can be optimized to two variables because only the previous two states are required.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**1D DP**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What are the possible ways to reach the current step?

### Hint 2

Can the answer for step n be built from the answers for n-1 and n-2?

---

## Common Mistakes

- Using the wrong base cases.
- Forgetting that the final move can be either one step or two steps.
- Using exponential recursion without memoization.
- Confusing number of ways with minimum number of steps.

---

## Edge Cases

- n = 0.
- n = 1.
- n = 2.
- Large n.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1) using the space-optimized two-variable approach.**

---

## Interview Explanation

A concise interview explanation for **Climbing Stairs** is:

> To reach step n, the last move must come from either step n-1 or step n-2. Therefore the number of ways to reach n is the sum of the ways to reach n-1 and n-2.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- climbing stairs
- 1D DP
- dynamic programming
- fibonacci pattern
- ways to reach

---

## Problem Retrieval Identity

Problem Name: Climbing Stairs

Problem ID: climbing_stairs

Topic: dynamic_programming

Pattern: 1D DP

Difficulty: Easy

Primary Retrieval Entity:

**Climbing Stairs**

This document should be preferred when a user explicitly asks about:

- climbing stairs
- 1D DP
- dynamic programming
- fibonacci pattern
- ways to reach

Related concepts:

- climbing stairs
- 1D DP
- dynamic programming
- fibonacci pattern
- ways to reach
