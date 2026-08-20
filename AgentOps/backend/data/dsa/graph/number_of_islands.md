# Number of Islands

Problem ID: number_of_islands

Title: Number of Islands

Difficulty: Medium

Topic: graph

Pattern: **Grid DFS/BFS**

---

## Problem Identity

This document is specifically about:

**Number of Islands**

This knowledge chunk belongs to:

**graph**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Number of Islands** problem.

The primary problem-solving pattern is:

**Grid DFS/BFS**

---

## Key Idea

Every group of connected land cells forms one island. Scan the grid and start DFS/BFS whenever an unvisited land cell is found.

### Core Invariant

Once a DFS/BFS finishes from a land cell, every land cell belonging to that connected island has been marked visited.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

For every land cell, repeatedly search surrounding cells without marking visited cells, causing repeated exploration.

### Brute Force Complexity

- **Time Complexity:** Can become inefficient due to repeated traversal.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Traverse every cell of the grid.
2. When an unvisited land cell is found, increment the island count.
3. Run DFS or BFS from that cell.
4. Visit its valid neighboring land cells.
5. Mark all cells belonging to the same island as visited.
6. Continue scanning the grid.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Grid DFS/BFS**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What does one island correspond to in graph terms?

### Hint 2

How can you explore all connected land cells?

---

## Common Mistakes

- Forgetting to mark land cells visited.
- Counting every land cell as an island.
- Going outside grid boundaries.
- Using diagonal movement when only four-directional movement is allowed.

---

## Edge Cases

- Empty grid.
- All water.
- All land.
- Single land cell.
- Multiple disconnected islands.

---

## Complexity Analysis

### Time Complexity

**O(R * C)**

### Space Complexity

**O(R * C) in the worst case for visited/recursion/traversal storage.**

---

## Interview Explanation

A concise interview explanation for **Number of Islands** is:

> Every group of connected land cells forms one island. Scan the grid and start DFS/BFS whenever an unvisited land cell is found.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- number of islands
- grid dfs
- grid bfs
- connected components matrix
- island problem

---

## Problem Retrieval Identity

Problem Name: Number of Islands

Problem ID: number_of_islands

Topic: graph

Pattern: Grid DFS/BFS

Difficulty: Medium

Primary Retrieval Entity:

**Number of Islands**

This document should be preferred when a user explicitly asks about:

- number of islands
- grid dfs
- grid bfs
- connected components matrix
- island problem

Related concepts:

- number of islands
- grid dfs
- grid bfs
- connected components matrix
- island problem
