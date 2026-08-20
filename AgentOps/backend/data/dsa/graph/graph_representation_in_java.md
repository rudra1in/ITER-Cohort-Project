# Graph Representation in Java

Problem ID: graph_representation_in_java

Title: Graph Representation in Java

Difficulty: Easy

Topic: graph

Pattern: **Graph Representation**

---

## Problem Identity

This document is specifically about:

**Graph Representation in Java**

This knowledge chunk belongs to:

**graph**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Graph Representation in Java** problem.

The primary problem-solving pattern is:

**Graph Representation**

---

## Key Idea

An adjacency list stores, for every vertex, the vertices directly connected to it. It is usually preferred for sparse graphs because it uses O(V + E) space.

### Core Invariant

The adjacency list of every vertex contains exactly the vertices directly connected to that vertex.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use an adjacency matrix where graph[u][v] indicates whether an edge exists between u and v.

### Brute Force Complexity

- **Time Complexity:** O(V^2) space for an adjacency matrix.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create an ArrayList for every vertex.
2. For every edge u-v, add v to u's adjacency list.
3. For an undirected graph, also add u to v's adjacency list.
4. For a directed graph, add only the directed connection.
5. Traverse the adjacency list whenever neighbors of a vertex are required.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Graph Representation**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How can you store all neighbors of each vertex?

### Hint 2

For an undirected edge u-v, where should the edge be stored?

---

## Common Mistakes

- Forgetting to add both directions for an undirected graph.
- Using incorrect vertex indexing.
- Creating only one adjacency list instead of one for every vertex.
- Confusing directed and undirected representation.

---

## Edge Cases

- No edges.
- Single vertex.
- Disconnected graph.
- Self-loop.
- Multiple edges.

---

## Complexity Analysis

### Time Complexity

**O(V + E) to construct the adjacency list.**

### Space Complexity

**O(V + E).**

---

## Interview Explanation

A concise interview explanation for **Graph Representation in Java** is:

> An adjacency list stores, for every vertex, the vertices directly connected to it. It is usually preferred for sparse graphs because it uses O(V + E) space.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- graph representation
- adjacency list
- adjacency matrix
- java graph
- graph implementation

---

## Problem Retrieval Identity

Problem Name: Graph Representation in Java

Problem ID: graph_representation_in_java

Topic: graph

Pattern: Graph Representation

Difficulty: Easy

Primary Retrieval Entity:

**Graph Representation in Java**

This document should be preferred when a user explicitly asks about:

- graph representation
- adjacency list
- adjacency matrix
- java graph
- graph implementation

Related concepts:

- graph representation
- adjacency list
- adjacency matrix
- java graph
- graph implementation
