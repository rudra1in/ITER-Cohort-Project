# Maximum Path Sum in Binary Tree

Problem ID: maximum_path_sum_binary_tree

Title: Maximum Path Sum in Binary Tree

Difficulty: Medium

Topic: trees

Pattern: **Tree DFS / Dynamic Programming**

---

## Problem Identity

This document is specifically about:

**Maximum Path Sum in Binary Tree**

This knowledge chunk belongs to:

**trees**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Maximum Path Sum in Binary Tree** problem.

The primary problem-solving pattern is:

**Tree DFS / Dynamic Programming**

---

## Key Idea

For every node, calculate the maximum downward path that can be extended to its parent while separately updating the best path that passes through the node.

### Core Invariant

The recursive return value represents the maximum path sum starting at the current node and extending downward through at most one child.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Consider possible paths through nodes and calculate their sums recursively.

### Brute Force Complexity

- **Time Complexity:** O(N^2) or worse depending on implementation
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Recursively calculate the best downward path from the left subtree.
2. Recursively calculate the best downward path from the right subtree.
3. Ignore negative contributions by taking zero when appropriate.
4. Calculate the path passing through the current node.
5. Update the global maximum.
6. Return the best one-sided path to the parent.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Tree DFS / Dynamic Programming**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can a path going upward to the parent use both children?

### Hint 2

What should you do with a negative subtree contribution?

---

## Common Mistakes

- Allowing a node to return paths through both children.
- Ignoring negative subtree sums.
- Initializing the answer incorrectly for all-negative trees.
- Confusing downward path with the complete maximum path.

---

## Edge Cases

- Empty tree.
- Single-node tree.
- All positive values.
- All negative values.
- Mixed positive and negative values.
- Maximum path not passing through root.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(H) recursion stack space.**

---

## Interview Explanation

A concise interview explanation for **Maximum Path Sum in Binary Tree** is:

> For every node, calculate the maximum downward path that can be extended to its parent while separately updating the best path that passes through the node.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- maximum path sum
- binary tree maximum path
- tree DP
- DFS
- recursion

---

## Problem Retrieval Identity

Problem Name: Maximum Path Sum in Binary Tree

Problem ID: maximum_path_sum_binary_tree

Topic: trees

Pattern: Tree DFS / Dynamic Programming

Difficulty: Medium

Primary Retrieval Entity:

**Maximum Path Sum in Binary Tree**

This document should be preferred when a user explicitly asks about:

- maximum path sum
- binary tree maximum path
- tree DP
- DFS
- recursion

Related concepts:

- maximum path sum
- binary tree maximum path
- tree DP
- DFS
- recursion
