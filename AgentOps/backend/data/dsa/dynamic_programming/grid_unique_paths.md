# Grid Unique Paths

Problem ID: grid_unique_paths

Title: Grid Unique Paths

Difficulty: Medium

Topic: dynamic_programming

Pattern: **2D Grid DP**

---

## Problem Identity

This document is specifically about:

**Grid Unique Paths**

This knowledge chunk belongs to:

**dynamic_programming**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Grid Unique Paths** problem.

The primary problem-solving pattern is:

**2D Grid DP**

---

## Key Idea

To reach a cell, the path must come either from the cell above or from the cell to the left. Therefore the number of paths to a cell is the sum of these two states.

### Core Invariant

dp[i][j] always represents the total number of valid paths from the starting cell to cell (i, j).

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use recursion to move either right or down from every cell until reaching the destination.

### Brute Force Complexity

- **Time Complexity:** O(2^(M+N))
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Define dp[i][j] as the number of ways to reach cell (i, j).
2. Initialize the starting cell with one way.
3. For each cell, add the number of ways from the top.
4. Add the number of ways from the left.
5. Continue until reaching the destination.
6. Return dp[m-1][n-1].

### Why This Works

The optimized solution works because it exploits the structure provided by:

**2D Grid DP**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

From which two directions can you enter a cell?

### Hint 2

What should be the number of ways to reach the starting cell?

---

## Common Mistakes

- Allowing diagonal movement.
- Using the wrong base case.
- Mixing row and column indices.
- Forgetting boundary conditions.

---

## Edge Cases

- 1 x 1 grid.
- One row.
- One column.
- Large grid.

---

## Complexity Analysis

### Time Complexity

**O(M * N)**

### Space Complexity

**O(N) using a single-row DP array.**

---

## Interview Explanation

A concise interview explanation for **Grid Unique Paths** is:

> To reach a cell, the path must come either from the cell above or from the cell to the left. Therefore the number of paths to a cell is the sum of these two states.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- unique paths
- grid DP
- 2D DP
- path counting
- dynamic programming

---

## Problem Retrieval Identity

Problem Name: Grid Unique Paths

Problem ID: grid_unique_paths

Topic: dynamic_programming

Pattern: 2D Grid DP

Difficulty: Medium

Primary Retrieval Entity:

**Grid Unique Paths**

This document should be preferred when a user explicitly asks about:

- unique paths
- grid DP
- 2D DP
- path counting
- dynamic programming

Related concepts:

- unique paths
- grid DP
- 2D DP
- path counting
- dynamic programming
