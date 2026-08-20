# Rotten Oranges

Problem ID: rotten_oranges

Title: Rotten Oranges

Difficulty: Medium

Topic: graph

Pattern: **Multi-Source BFS**

---

## Problem Identity

This document is specifically about:

**Rotten Oranges**

This knowledge chunk belongs to:

**graph**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Rotten Oranges** problem.

The primary problem-solving pattern is:

**Multi-Source BFS**

---

## Key Idea

All initially rotten oranges spread rot simultaneously. Put every rotten orange into a queue initially and use BFS level by level to calculate the minimum time.

### Core Invariant

At the start of each BFS level, all oranges in the queue represent oranges that became rotten at the same elapsed time.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Run a separate traversal from every rotten orange and repeatedly simulate the spreading process.

### Brute Force Complexity

- **Time Complexity:** Can become inefficient because the same cells may be processed repeatedly.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Add all initially rotten oranges to the queue.
2. Count the fresh oranges.
3. Process the queue level by level.
4. For every rotten orange, check its four neighbors.
5. If a neighboring orange is fresh, mark it rotten and add it to the queue.
6. Increase the elapsed time after processing one BFS level.
7. If fresh oranges remain, return -1.
8. Otherwise return the elapsed time.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Multi-Source BFS**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Why should all initially rotten oranges enter the queue at the beginning?

### Hint 2

What does one BFS level represent?

---

## Common Mistakes

- Starting BFS from only one rotten orange.
- Incrementing time for every orange instead of every level.
- Forgetting to count fresh oranges.
- Returning the wrong result when fresh oranges remain.

---

## Edge Cases

- No fresh oranges.
- All oranges are fresh.
- All oranges are rotten.
- Fresh orange completely surrounded by empty cells.
- Single-cell grid.

---

## Complexity Analysis

### Time Complexity

**O(R * C)**

### Space Complexity

**O(R * C) for the queue in the worst case.**

---

## Interview Explanation

A concise interview explanation for **Rotten Oranges** is:

> All initially rotten oranges spread rot simultaneously. Put every rotten orange into a queue initially and use BFS level by level to calculate the minimum time.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- rotten oranges
- multi source bfs
- bfs grid
- minimum time
- level order bfs

---

## Problem Retrieval Identity

Problem Name: Rotten Oranges

Problem ID: rotten_oranges

Topic: graph

Pattern: Multi-Source BFS

Difficulty: Medium

Primary Retrieval Entity:

**Rotten Oranges**

This document should be preferred when a user explicitly asks about:

- rotten oranges
- multi source bfs
- bfs grid
- minimum time
- level order bfs

Related concepts:

- rotten oranges
- multi source bfs
- bfs grid
- minimum time
- level order bfs
