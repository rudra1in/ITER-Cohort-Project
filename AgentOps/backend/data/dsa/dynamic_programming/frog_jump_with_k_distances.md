# Frog Jump with K Distances

Problem ID: frog_jump_with_k_distances

Title: Frog Jump with K Distances

Difficulty: Medium

Topic: dynamic_programming

Pattern: **1D DP**

---

## Problem Identity

This document is specifically about:

**Frog Jump with K Distances**

This knowledge chunk belongs to:

**dynamic_programming**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Frog Jump with K Distances** problem.

The primary problem-solving pattern is:

**1D DP**

---

## Key Idea

The frog can jump up to K positions backward. For every stone, try all possible jump lengths from 1 to K and choose the jump that results in minimum total energy.

### Core Invariant

After computing dp[i], it represents the minimum energy required to reach stone i using any valid sequence of jumps of length at most K.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use recursion to try every possible jump length at every stone. This creates a large number of repeated subproblems.

### Brute Force Complexity

- **Time Complexity:** Exponential
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Define dp[i] as the minimum energy needed to reach stone i.
2. Initialize dp[0] = 0.
3. For each stone i, try jump lengths from 1 to K.
4. Check whether i - jump is a valid previous stone.
5. Calculate the energy using the height difference.
6. Take the minimum among all valid jumps.
7. Return dp[n-1].

### Why This Works

The optimized solution works because it exploits the structure provided by:

**1D DP**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How many previous stones can reach the current stone?

### Hint 2

Can you try every jump length from 1 to K?

---

## Common Mistakes

- Checking more than K previous positions.
- Using an invalid previous index.
- Forgetting to take the minimum over all jump lengths.
- Incorrectly calculating height difference.

---

## Edge Cases

- K = 1.
- K = 2.
- K >= N.
- Single stone.
- Repeated heights.

---

## Complexity Analysis

### Time Complexity

**O(N * K)**

### Space Complexity

**O(N) for the DP array.**

---

## Interview Explanation

A concise interview explanation for **Frog Jump with K Distances** is:

> The frog can jump up to K positions backward. For every stone, try all possible jump lengths from 1 to K and choose the jump that results in minimum total energy.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- frog jump k distances
- k jumps
- 1D DP
- minimum energy
- dynamic programming

---

## Problem Retrieval Identity

Problem Name: Frog Jump with K Distances

Problem ID: frog_jump_with_k_distances

Topic: dynamic_programming

Pattern: 1D DP

Difficulty: Medium

Primary Retrieval Entity:

**Frog Jump with K Distances**

This document should be preferred when a user explicitly asks about:

- frog jump k distances
- k jumps
- 1D DP
- minimum energy
- dynamic programming

Related concepts:

- frog jump k distances
- k jumps
- 1D DP
- minimum energy
- dynamic programming
