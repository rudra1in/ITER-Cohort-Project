# Cycle Detection in Directed Graph

Problem ID: cycle_detection_directed_graph

Title: Cycle Detection in Directed Graph

Difficulty: Hard

Topic: graph

Pattern: **DFS + Recursion Stack**

---

## Problem Identity

This document is specifically about:

**Cycle Detection in Directed Graph**

This knowledge chunk belongs to:

**graph**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Cycle Detection in Directed Graph** problem.

The primary problem-solving pattern is:

**DFS + Recursion Stack**

---

## Key Idea

In a directed graph, a cycle exists if DFS encounters a vertex that is already present in the current recursion path. This is tracked using a recursion-stack array.

### Core Invariant

pathVisited contains exactly the vertices currently present in the active DFS recursion path.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Run searches from vertices without tracking the current DFS path, repeatedly exploring reachable vertices.

### Brute Force Complexity

- **Time Complexity:** Can become inefficient due to repeated traversal.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a visited array.
2. Create a pathVisited or recursion-stack array.
3. For every unvisited vertex, start DFS.
4. Mark the current vertex as visited and pathVisited.
5. Explore every outgoing neighbor.
6. If the neighbor is unvisited, recursively explore it.
7. If the neighbor is already pathVisited, a directed cycle exists.
8. After processing all neighbors, remove the current vertex from pathVisited.
9. Repeat for all disconnected components.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**DFS + Recursion Stack**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Why is normal visited tracking not enough for directed cycle detection?

### Hint 2

What does it mean if DFS reaches a vertex already in the current recursion path?

---

## Common Mistakes

- Using only a visited array.
- Forgetting to remove a vertex from pathVisited after DFS finishes.
- Confusing directed and undirected cycle detection.
- Not checking all disconnected components.
- Marking pathVisited permanently.

---

## Edge Cases

- No edges.
- Single vertex without self-loop.
- Self-loop.
- Simple directed cycle.
- Disconnected graph.
- Directed acyclic graph.

---

## Complexity Analysis

### Time Complexity

**O(V + E)**

### Space Complexity

**O(V) for visited, recursion-stack tracking, and recursion depth.**

---

## Interview Explanation

A concise interview explanation for **Cycle Detection in Directed Graph** is:

> In a directed graph, a cycle exists if DFS encounters a vertex that is already present in the current recursion path. This is tracked using a recursion-stack array.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- directed graph cycle
- cycle detection directed graph
- dfs cycle detection
- recursion stack
- path visited

---

## Problem Retrieval Identity

Problem Name: Cycle Detection in Directed Graph

Problem ID: cycle_detection_directed_graph

Topic: graph

Pattern: DFS + Recursion Stack

Difficulty: Hard

Primary Retrieval Entity:

**Cycle Detection in Directed Graph**

This document should be preferred when a user explicitly asks about:

- directed graph cycle
- cycle detection directed graph
- dfs cycle detection
- recursion stack
- path visited

Related concepts:

- directed graph cycle
- cycle detection directed graph
- dfs cycle detection
- recursion stack
- path visited
