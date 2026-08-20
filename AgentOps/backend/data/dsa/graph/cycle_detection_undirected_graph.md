# Cycle Detection in Undirected Graph

Problem ID: cycle_detection_undirected_graph

Title: Cycle Detection in Undirected Graph

Difficulty: Medium

Topic: graph

Pattern: **BFS/DFS + Parent Tracking**

---

## Problem Identity

This document is specifically about:

**Cycle Detection in Undirected Graph**

This knowledge chunk belongs to:

**graph**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Cycle Detection in Undirected Graph** problem.

The primary problem-solving pattern is:

**BFS/DFS + Parent Tracking**

---

## Key Idea

In an undirected graph, if a visited neighbor is encountered that is not the parent of the current vertex, a cycle exists.

### Core Invariant

The parent edge of a vertex is ignored because it represents the same undirected edge through which the vertex was reached.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Explore the graph without tracking parent information and treat every visited neighbor as a cycle.

### Brute Force Complexity

- **Time Complexity:** Incorrect for undirected graphs because every edge appears in both directions.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a visited array.
2. For every unvisited vertex, start BFS or DFS.
3. Store the parent of each vertex.
4. For every neighbor, if it is unvisited, continue traversal and set the current vertex as its parent.
5. If the neighbor is already visited and is not the parent, a cycle exists.
6. Repeat for all disconnected components.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**BFS/DFS + Parent Tracking**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Why can't we simply say a visited neighbor means a cycle?

### Hint 2

What is special about the edge leading back to the parent?

---

## Common Mistakes

- Not tracking the parent.
- Treating the parent edge as a cycle.
- Forgetting disconnected components.
- Using directed-graph cycle logic for an undirected graph.

---

## Edge Cases

- No edges.
- Tree with no cycle.
- Single cycle.
- Multiple cycles.
- Disconnected graph.

---

## Complexity Analysis

### Time Complexity

**O(V + E)**

### Space Complexity

**O(V) for visited, parent, and traversal storage.**

---

## Interview Explanation

A concise interview explanation for **Cycle Detection in Undirected Graph** is:

> In an undirected graph, if a visited neighbor is encountered that is not the parent of the current vertex, a cycle exists.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- cycle detection
- undirected graph cycle
- bfs cycle detection
- dfs cycle detection
- parent tracking

---

## Problem Retrieval Identity

Problem Name: Cycle Detection in Undirected Graph

Problem ID: cycle_detection_undirected_graph

Topic: graph

Pattern: BFS/DFS + Parent Tracking

Difficulty: Medium

Primary Retrieval Entity:

**Cycle Detection in Undirected Graph**

This document should be preferred when a user explicitly asks about:

- cycle detection
- undirected graph cycle
- bfs cycle detection
- dfs cycle detection
- parent tracking

Related concepts:

- cycle detection
- undirected graph cycle
- bfs cycle detection
- dfs cycle detection
- parent tracking
