# Triangle

Problem ID: triangle

Title: Triangle

Difficulty: Medium

Topic: dynamic_programming

Pattern: **DP on Triangular Grid**

---

## Problem Identity

This document is specifically about:

**Triangle**

This knowledge chunk belongs to:

**dynamic_programming**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Triangle** problem.

The primary problem-solving pattern is:

**DP on Triangular Grid**

---

## Key Idea

From each triangle cell, the next position can be directly below or diagonally below. The minimum path sum can be calculated from the bottom of the triangle upward.

### Core Invariant

At every processed cell, the stored value represents the minimum path sum from that cell to the bottom of the triangle.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use recursion to try both possible downward directions at every triangle position.

### Brute Force Complexity

- **Time Complexity:** O(2^N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Start from the second-last row.
2. For every element, consider the two possible cells directly below it.
3. Add the current value to the minimum of these two states.
4. Continue upward until reaching the top.
5. The top element becomes the minimum path sum.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**DP on Triangular Grid**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

From a triangle cell, how many cells can you move to?

### Hint 2

Can you start from the bottom instead of the top?

---

## Common Mistakes

- Using invalid triangle indices.
- Forgetting the diagonal option.
- Starting from the wrong row.
- Using the maximum instead of minimum.

---

## Edge Cases

- Triangle with one element.
- Two rows.
- Negative values.
- Large triangle.

---

## Complexity Analysis

### Time Complexity

**O(N^2)**

### Space Complexity

**O(N) using a one-dimensional bottom-up DP array.**

---

## Interview Explanation

A concise interview explanation for **Triangle** is:

> From each triangle cell, the next position can be directly below or diagonally below. The minimum path sum can be calculated from the bottom of the triangle upward.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- triangle
- minimum path sum
- triangle DP
- bottom up DP
- dynamic programming

---

## Problem Retrieval Identity

Problem Name: Triangle

Problem ID: triangle

Topic: dynamic_programming

Pattern: DP on Triangular Grid

Difficulty: Medium

Primary Retrieval Entity:

**Triangle**

This document should be preferred when a user explicitly asks about:

- triangle
- minimum path sum
- triangle DP
- bottom up DP
- dynamic programming

Related concepts:

- triangle
- minimum path sum
- triangle DP
- bottom up DP
- dynamic programming
