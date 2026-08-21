# Flood Fill Algorithm

Problem ID: flood_fill_algorithm

Title: Flood Fill Algorithm

Difficulty: Medium

Topic: graph

Pattern: **Grid DFS/BFS**

---

## Problem Identity

This document is specifically about:

**Flood Fill Algorithm**

This knowledge chunk belongs to:

**graph**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Flood Fill Algorithm** problem.

The primary problem-solving pattern is:

**Grid DFS/BFS**

---

## Key Idea

Starting from a source cell, change its color and recursively or iteratively visit all connected cells having the original color.

### Core Invariant

Every cell recolored so far belongs to the same connected component of the original source color.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Change cells individually without systematically exploring the connected region.

### Brute Force Complexity

- **Time Complexity:** May require repeated scanning of the grid.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Store the original color of the starting cell.
2. If the original color equals the new color, return the image unchanged.
3. Change the starting cell to the new color.
4. Explore its four valid neighboring cells.
5. Only continue into cells having the original color.
6. Repeat until the entire connected region is recolored.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Grid DFS/BFS**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Which cells should receive the new color?

### Hint 2

How can DFS or BFS explore the connected region?

---

## Common Mistakes

- Forgetting the old-color check.
- Creating infinite recursion when oldColor equals newColor.
- Going outside grid boundaries.
- Changing cells that are not connected to the source.

---

## Edge Cases

- Source cell already has the new color.
- Single-cell image.
- Entire image has the same color.
- Source lies at a corner.
- No neighboring cell has the same color.

---

## Complexity Analysis

### Time Complexity

**O(R * C)**

### Space Complexity

**O(R * C) in the worst case for recursion or queue storage.**

---

## Interview Explanation

A concise interview explanation for **Flood Fill Algorithm** is:

> Starting from a source cell, change its color and recursively or iteratively visit all connected cells having the original color.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- flood fill
- dfs grid
- bfs grid
- connected component
- image recoloring

---

## Problem Retrieval Identity

Problem Name: Flood Fill Algorithm

Problem ID: flood_fill_algorithm

Topic: graph

Pattern: Grid DFS/BFS

Difficulty: Medium

Primary Retrieval Entity:

**Flood Fill Algorithm**

This document should be preferred when a user explicitly asks about:

- flood fill
- dfs grid
- bfs grid
- connected component
- image recoloring

Related concepts:

- flood fill
- dfs grid
- bfs grid
- connected component
- image recoloring
