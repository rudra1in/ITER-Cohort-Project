# Rotten Oranges

Problem ID: rotten_oranges

Title: Rotten Oranges

Difficulty: Medium

Topic: queue

Pattern: **BFS Queue**

---

## Problem Identity

This document is specifically about:

**Rotten Oranges**

This knowledge chunk belongs to:

**queue**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Rotten Oranges** problem.

The primary problem-solving pattern is:

**BFS Queue**

---

## Key Idea

Use Breadth First Search with a queue to process rotten oranges level by level. Each BFS level represents one unit of time.

### Core Invariant

Every orange removed from the queue is processed in nondecreasing order of the time at which it became rotten.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Repeatedly scan the entire grid and rot adjacent fresh oranges. This may require many full-grid scans.

### Brute Force Complexity

- **Time Complexity:** O((M × N)^2) in the worst case for repeated scanning.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Add all initially rotten oranges to a queue.
2. Store their row, column, and time information.
3. Process the queue level by level.
4. Check the four neighboring cells.
5. Turn fresh oranges rotten and add them to the queue.
6. Track the maximum time.
7. Check whether any fresh orange remains.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**BFS Queue**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Why is BFS suitable when the process happens minute by minute?

### Hint 2

Which elements should enter the queue initially?

---

## Common Mistakes

- Starting BFS from only one rotten orange.
- Forgetting to count minutes.
- Visiting already processed cells repeatedly.
- Not checking for remaining fresh oranges.

---

## Edge Cases

- No oranges.
- No rotten oranges.
- No fresh oranges.
- Fresh orange that can never rot.
- All oranges initially rotten.

---

## Complexity Analysis

### Time Complexity

**O(M × N)**

### Space Complexity

**O(M × N)**

---

## Interview Explanation

A concise interview explanation for **Rotten Oranges** is:

> Use Breadth First Search with a queue to process rotten oranges level by level. Each BFS level represents one unit of time.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- rotten oranges
- BFS
- grid BFS
- queue BFS
- multi source BFS

---

## Problem Retrieval Identity

Problem Name: Rotten Oranges

Problem ID: rotten_oranges

Topic: queue

Pattern: BFS Queue

Difficulty: Medium

Primary Retrieval Entity:

**Rotten Oranges**

This document should be preferred when a user explicitly asks about:

- rotten oranges
- BFS
- grid BFS
- queue BFS
- multi source BFS

Related concepts:

- rotten oranges
- BFS
- grid BFS
- queue BFS
- multi source BFS
