# Distance of Nearest Cell Having 1

Problem ID: distance_of_nearest_cell_having_one

Title: Distance of Nearest Cell Having 1

Difficulty: Medium

Topic: graph

Pattern: **Multi-Source BFS**

---

## Problem Identity

This document is specifically about:

**Distance of Nearest Cell Having 1**

This knowledge chunk belongs to:

**graph**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Distance of Nearest Cell Having 1** problem.

The primary problem-solving pattern is:

**Multi-Source BFS**

---

## Key Idea

Treat every cell containing 1 as a source and perform multi-source BFS. The first time a cell is reached gives its shortest distance from any 1.

### Core Invariant

When a cell is first visited by BFS, the assigned distance is the shortest possible distance from any cell containing 1.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

For every zero cell, search outward until a cell containing 1 is found.

### Brute Force Complexity

- **Time Complexity:** Can take O((R * C)^2) in the worst case.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Add every cell containing 1 to the queue.
2. Set the distance of these source cells to zero.
3. Mark all source cells visited.
4. Process the queue using BFS.
5. For each neighboring cell, if it is unvisited, assign distance = current distance + 1.
6. Add the neighboring cell to the queue.
7. Continue until all cells have their nearest-source distance.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Multi-Source BFS**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What if every 1 is considered a starting point?

### Hint 2

Which traversal finds the shortest distance in an unweighted graph?

---

## Common Mistakes

- Running BFS separately for every zero.
- Using only one source cell.
- Incorrectly initializing source distances.
- Visiting a cell multiple times unnecessarily.

---

## Edge Cases

- All cells are 1.
- Only one cell contains 1.
- Single-cell matrix.
- Large matrix.
- Multiple source cells.

---

## Complexity Analysis

### Time Complexity

**O(R * C)**

### Space Complexity

**O(R * C).**

---

## Interview Explanation

A concise interview explanation for **Distance of Nearest Cell Having 1** is:

> Treat every cell containing 1 as a source and perform multi-source BFS. The first time a cell is reached gives its shortest distance from any 1.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- nearest one
- distance matrix
- multi source bfs
- shortest distance grid
- bfs matrix

---

## Problem Retrieval Identity

Problem Name: Distance of Nearest Cell Having 1

Problem ID: distance_of_nearest_cell_having_one

Topic: graph

Pattern: Multi-Source BFS

Difficulty: Medium

Primary Retrieval Entity:

**Distance of Nearest Cell Having 1**

This document should be preferred when a user explicitly asks about:

- nearest one
- distance matrix
- multi source bfs
- shortest distance grid
- bfs matrix

Related concepts:

- nearest one
- distance matrix
- multi source bfs
- shortest distance grid
- bfs matrix
