# Bipartite Graph

Problem ID: bipartite_graph

Title: Bipartite Graph

Difficulty: Hard

Topic: graph

Pattern: **Graph Coloring + BFS/DFS**

---

## Problem Identity

This document is specifically about:

**Bipartite Graph**

This knowledge chunk belongs to:

**graph**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Bipartite Graph** problem.

The primary problem-solving pattern is:

**Graph Coloring + BFS/DFS**

---

## Key Idea

A graph is bipartite if its vertices can be divided into two groups such that no edge connects vertices within the same group. This can be checked by coloring adjacent vertices with opposite colors.

### Core Invariant

Every edge processed so far connects vertices assigned opposite colors.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Try different two-group assignments for vertices and verify whether every edge connects vertices from different groups.

### Brute Force Complexity

- **Time Complexity:** Can become exponential without graph-coloring optimization.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a color array initialized to an uncolored state.
2. For every uncolored vertex, start BFS or DFS.
3. Assign the starting vertex one color.
4. For every neighbor, assign the opposite color.
5. If an uncolored neighbor is found, color it accordingly.
6. If a neighbor already has the same color as the current vertex, the graph is not bipartite.
7. Continue for all disconnected components.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Graph Coloring + BFS/DFS**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can you assign every vertex one of two colors?

### Hint 2

What color should a neighbor receive?

---

## Common Mistakes

- Using only one connected component.
- Failing to color the starting vertex.
- Assigning the same color to adjacent vertices.
- Not checking already-colored neighbors.
- Forgetting that an odd cycle makes a graph non-bipartite.

---

## Edge Cases

- Empty graph.
- Single vertex.
- Disconnected graph.
- Graph with an even cycle.
- Graph with an odd cycle.

---

## Complexity Analysis

### Time Complexity

**O(V + E)**

### Space Complexity

**O(V) for the color array and traversal structure.**

---

## Interview Explanation

A concise interview explanation for **Bipartite Graph** is:

> A graph is bipartite if its vertices can be divided into two groups such that no edge connects vertices within the same group. This can be checked by coloring adjacent vertices with opposite colors.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- bipartite graph
- graph coloring
- two coloring
- bfs bipartite
- dfs bipartite

---

## Problem Retrieval Identity

Problem Name: Bipartite Graph

Problem ID: bipartite_graph

Topic: graph

Pattern: Graph Coloring + BFS/DFS

Difficulty: Hard

Primary Retrieval Entity:

**Bipartite Graph**

This document should be preferred when a user explicitly asks about:

- bipartite graph
- graph coloring
- two coloring
- bfs bipartite
- dfs bipartite

Related concepts:

- bipartite graph
- graph coloring
- two coloring
- bfs bipartite
- dfs bipartite
