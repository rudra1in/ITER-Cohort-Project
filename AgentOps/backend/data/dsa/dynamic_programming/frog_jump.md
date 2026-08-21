# Frog Jump

Problem ID: frog_jump

Title: Frog Jump

Difficulty: Medium

Topic: dynamic_programming

Pattern: **1D DP**

---

## Problem Identity

This document is specifically about:

**Frog Jump**

This knowledge chunk belongs to:

**dynamic_programming**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Frog Jump** problem.

The primary problem-solving pattern is:

**1D DP**

---

## Key Idea

The frog can jump from the previous stone or the stone before it. The minimum energy required to reach a stone is the minimum of these two previous possibilities plus the current jump cost.

### Core Invariant

dp[i] always stores the minimum energy needed to reach stone i from the starting stone.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use recursion to try both possible jumps at every stone and return the minimum energy among all paths.

### Brute Force Complexity

- **Time Complexity:** O(2^N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Define dp[i] as the minimum energy required to reach stone i.
2. The first stone requires zero energy.
3. For every stone i, calculate the cost of jumping from i-1.
4. If i > 1, also calculate the cost of jumping from i-2.
5. Take the minimum of the available options.
6. Return dp[n-1].

### Why This Works

The optimized solution works because it exploits the structure provided by:

**1D DP**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

From which stones can the frog reach the current stone?

### Hint 2

What is the energy cost of a jump?

---

## Common Mistakes

- Using the jump cost in the wrong direction.
- Forgetting the second jump option.
- Incorrectly handling the first or second stone.
- Using maximum instead of minimum.

---

## Edge Cases

- One stone.
- Two stones.
- All heights equal.
- Large height differences.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1) using only the previous two DP states.**

---

## Interview Explanation

A concise interview explanation for **Frog Jump** is:

> The frog can jump from the previous stone or the stone before it. The minimum energy required to reach a stone is the minimum of these two previous possibilities plus the current jump cost.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- frog jump
- minimum energy
- 1D DP
- dynamic programming
- memoization

---

## Problem Retrieval Identity

Problem Name: Frog Jump

Problem ID: frog_jump

Topic: dynamic_programming

Pattern: 1D DP

Difficulty: Medium

Primary Retrieval Entity:

**Frog Jump**

This document should be preferred when a user explicitly asks about:

- frog jump
- minimum energy
- 1D DP
- dynamic programming
- memoization

Related concepts:

- frog jump
- minimum energy
- 1D DP
- dynamic programming
- memoization
