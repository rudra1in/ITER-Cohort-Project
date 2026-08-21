# Minimum Falling Path Sum

Problem ID: minimum_falling_path_sum

Title: Minimum Falling Path Sum

Difficulty: Medium

Topic: dynamic_programming

Pattern: **Grid DP**

---

## Problem Identity

This document is specifically about:

**Minimum Falling Path Sum**

This knowledge chunk belongs to:

**dynamic_programming**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Minimum Falling Path Sum** problem.

The primary problem-solving pattern is:

**Grid DP**

---

## Key Idea

For each cell, the previous cell can come from directly above, above-left, or above-right. The minimum falling path ending at a cell is its value plus the minimum of these valid previous states.

### Core Invariant

dp[i][j] stores the minimum path sum for a valid falling path that ends exactly at cell (i, j).

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use recursion from every possible starting position in the first row and try all three downward directions.

### Brute Force Complexity

- **Time Complexity:** Exponential
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Define dp[i][j] as the minimum falling-path sum ending at cell (i, j).
2. Initialize the first row with the original matrix values.
3. For every subsequent row, consider the three possible cells from the previous row.
4. Add the current cell value to the minimum valid previous value.
5. Take the minimum among all cells in the last row.
6. Return that minimum.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Grid DP**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

From which three cells can the current cell be reached?

### Hint 2

What should happen at the left and right boundaries?

---

## Common Mistakes

- Accessing outside the matrix boundaries.
- Forgetting the diagonal moves.
- Taking the maximum instead of minimum.
- Returning only the bottom-right cell.

---

## Edge Cases

- 1 x 1 matrix.
- Single row.
- Negative values.
- Matrix with equal values.

---

## Complexity Analysis

### Time Complexity

**O(N^2)**

### Space Complexity

**O(N) using the previous row only.**

---

## Interview Explanation

A concise interview explanation for **Minimum Falling Path Sum** is:

> For each cell, the previous cell can come from directly above, above-left, or above-right. The minimum falling path ending at a cell is its value plus the minimum of these valid previous states.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- minimum falling path sum
- grid DP
- matrix DP
- minimum path
- dynamic programming

---

## Problem Retrieval Identity

Problem Name: Minimum Falling Path Sum

Problem ID: minimum_falling_path_sum

Topic: dynamic_programming

Pattern: Grid DP

Difficulty: Medium

Primary Retrieval Entity:

**Minimum Falling Path Sum**

This document should be preferred when a user explicitly asks about:

- minimum falling path sum
- grid DP
- matrix DP
- minimum path
- dynamic programming

Related concepts:

- minimum falling path sum
- grid DP
- matrix DP
- minimum path
- dynamic programming
