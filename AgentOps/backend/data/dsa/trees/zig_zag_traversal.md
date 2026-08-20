# Zig Zag or Spiral Traversal

Problem ID: zig_zag_traversal

Title: Zig Zag or Spiral Traversal

Difficulty: Medium

Topic: trees

Pattern: **BFS / Queue**

---

## Problem Identity

This document is specifically about:

**Zig Zag or Spiral Traversal**

This knowledge chunk belongs to:

**trees**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Zig Zag or Spiral Traversal** problem.

The primary problem-solving pattern is:

**BFS / Queue**

---

## Key Idea

Zigzag traversal visits the tree level by level but alternates the direction of traversal between consecutive levels.

### Core Invariant

All nodes in the current level are processed before moving to the next level, and the output direction alternates between levels.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Perform level order traversal using a queue and reverse every alternate level.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Use a queue for level order traversal.
2. Process one complete level at a time.
3. Store the nodes of the current level.
4. If the level direction is left-to-right, store normally.
5. If the direction is right-to-left, store in reverse order.
6. Toggle the direction for the next level.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**BFS / Queue**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How is zigzag traversal different from normal level order?

### Hint 2

Can you keep track of the current level?

---

## Common Mistakes

- Reversing every level.
- Reversing the entire final result.
- Not processing levels separately.
- Incorrectly toggling the direction.

---

## Edge Cases

- Empty tree.
- Single-node tree.
- Two-level tree.
- Skewed tree.
- Balanced tree.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(N) for the queue and level result.**

---

## Interview Explanation

A concise interview explanation for **Zig Zag or Spiral Traversal** is:

> Zigzag traversal visits the tree level by level but alternates the direction of traversal between consecutive levels.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- zigzag traversal
- spiral traversal
- level order
- BFS
- queue

---

## Problem Retrieval Identity

Problem Name: Zig Zag or Spiral Traversal

Problem ID: zig_zag_traversal

Topic: trees

Pattern: BFS / Queue

Difficulty: Medium

Primary Retrieval Entity:

**Zig Zag or Spiral Traversal**

This document should be preferred when a user explicitly asks about:

- zigzag traversal
- spiral traversal
- level order
- BFS
- queue

Related concepts:

- zigzag traversal
- spiral traversal
- level order
- BFS
- queue
