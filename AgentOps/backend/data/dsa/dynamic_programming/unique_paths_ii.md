# Unique Paths II

Problem ID: unique_paths_ii

Title: Unique Paths II

Difficulty: Medium

Topic: dynamic_programming

Pattern: **Grid DP with Obstacles**

---

## Problem Identity

This document is specifically about:

**Unique Paths II**

This knowledge chunk belongs to:

**dynamic_programming**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Unique Paths II** problem.

The primary problem-solving pattern is:

**Grid DP with Obstacles**

---

## Key Idea

This is the unique-paths problem with blocked cells. If a cell contains an obstacle, there are zero ways to reach it. Otherwise its number of paths comes from the top and left cells.

### Core Invariant

Every DP state counts only paths that avoid all obstacles encountered before reaching that cell.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use recursion to explore right and down paths while stopping whenever an obstacle is encountered.

### Brute Force Complexity

- **Time Complexity:** Exponential
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Define dp[i][j] as the number of valid paths to cell (i, j).
2. If the current cell contains an obstacle, set its value to zero.
3. Otherwise add the number of paths from the top and left.
4. Initialize the starting cell only if it is not blocked.
5. Continue until the destination.
6. Return the destination state.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Grid DP with Obstacles**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What should happen when you reach an obstacle?

### Hint 2

Can you use the same top-plus-left recurrence as Unique Paths?

---

## Common Mistakes

- Counting paths through obstacles.
- Incorrectly initializing the first row.
- Forgetting that an obstacle makes the current state zero.
- Ignoring a blocked starting cell.

---

## Edge Cases

- Starting cell blocked.
- Destination blocked.
- No obstacles.
- Entire row blocked.
- 1 x 1 grid.

---

## Complexity Analysis

### Time Complexity

**O(M * N)**

### Space Complexity

**O(N) using a one-dimensional DP array.**

---

## Interview Explanation

A concise interview explanation for **Unique Paths II** is:

> This is the unique-paths problem with blocked cells. If a cell contains an obstacle, there are zero ways to reach it. Otherwise its number of paths comes from the top and left cells.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- unique paths II
- grid DP
- obstacles
- 2D DP
- path counting

---

## Problem Retrieval Identity

Problem Name: Unique Paths II

Problem ID: unique_paths_ii

Topic: dynamic_programming

Pattern: Grid DP with Obstacles

Difficulty: Medium

Primary Retrieval Entity:

**Unique Paths II**

This document should be preferred when a user explicitly asks about:

- unique paths II
- grid DP
- obstacles
- 2D DP
- path counting

Related concepts:

- unique paths II
- grid DP
- obstacles
- 2D DP
- path counting
