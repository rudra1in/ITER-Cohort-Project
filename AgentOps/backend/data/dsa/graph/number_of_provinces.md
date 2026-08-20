# Number of Provinces

Problem ID: number_of_provinces

Title: Number of Provinces

Difficulty: Medium

Topic: graph

Pattern: **Connected Components + DFS/BFS**

---

## Problem Identity

This document is specifically about:

**Number of Provinces**

This knowledge chunk belongs to:

**graph**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Number of Provinces** problem.

The primary problem-solving pattern is:

**Connected Components + DFS/BFS**

---

## Key Idea

Each province represents a connected component. Run DFS or BFS from every unvisited city and count how many times a new traversal is started.

### Core Invariant

Every city visited during one DFS/BFS belongs to the same connected component or province.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Repeatedly compare every city with every other city to determine connectivity.

### Brute Force Complexity

- **Time Complexity:** O(V^2) because the input is represented as an adjacency matrix.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a visited array for all cities.
2. Initialize provinces = 0.
3. For every city, check whether it has been visited.
4. If it has not been visited, increment the province count.
5. Run DFS or BFS from that city.
6. Mark every city reachable from it as visited.
7. Continue until every city has been processed.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Connected Components + DFS/BFS**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What does a province represent in graph terminology?

### Hint 2

How can connected components be counted?

---

## Common Mistakes

- Counting every city as a separate province.
- Not marking all reachable cities visited.
- Starting DFS/BFS from already visited cities.
- Confusing direct connections with indirect connections.

---

## Edge Cases

- One city.
- No connections between cities.
- All cities connected.
- Multiple disconnected components.

---

## Complexity Analysis

### Time Complexity

**O(V^2)**

### Space Complexity

**O(V) for the visited array and traversal structure.**

---

## Interview Explanation

A concise interview explanation for **Number of Provinces** is:

> Each province represents a connected component. Run DFS or BFS from every unvisited city and count how many times a new traversal is started.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- number of provinces
- connected components
- dfs provinces
- bfs provinces
- graph connectivity

---

## Problem Retrieval Identity

Problem Name: Number of Provinces

Problem ID: number_of_provinces

Topic: graph

Pattern: Connected Components + DFS/BFS

Difficulty: Medium

Primary Retrieval Entity:

**Number of Provinces**

This document should be preferred when a user explicitly asks about:

- number of provinces
- connected components
- dfs provinces
- bfs provinces
- graph connectivity

Related concepts:

- number of provinces
- connected components
- dfs provinces
- bfs provinces
- graph connectivity
