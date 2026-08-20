# Maximum Depth in Binary Tree

Problem ID: maximum_depth_of_binary_tree

Title: Maximum Depth in Binary Tree

Difficulty: Medium

Topic: trees

Pattern: **Tree DFS / Recursion**

---

## Problem Identity

This document is specifically about:

**Maximum Depth in Binary Tree**

This knowledge chunk belongs to:

**trees**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Maximum Depth in Binary Tree** problem.

The primary problem-solving pattern is:

**Tree DFS / Recursion**

---

## Key Idea

The maximum depth of a binary tree is one plus the larger depth of its left and right subtrees.

### Core Invariant

The recursive function returns the maximum depth of the subtree rooted at the current node.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Recursively calculate the depth of both subtrees and return the larger value plus one.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. If the current node is null, return 0.
2. Recursively calculate the left subtree depth.
3. Recursively calculate the right subtree depth.
4. Take the maximum of the two depths.
5. Add one for the current node.
6. Return the result.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Tree DFS / Recursion**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What is the depth of a null tree?

### Hint 2

How can the depth of a tree be expressed using its left and right subtree depths?

---

## Common Mistakes

- Returning the minimum instead of maximum.
- Forgetting to add one.
- Using the wrong base case.
- Confusing height with number of edges versus number of nodes.

---

## Edge Cases

- Empty tree.
- Single-node tree.
- Skewed tree.
- Balanced tree.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(H) recursion stack space.**

---

## Interview Explanation

A concise interview explanation for **Maximum Depth in Binary Tree** is:

> The maximum depth of a binary tree is one plus the larger depth of its left and right subtrees.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- maximum depth
- tree height
- binary tree depth
- DFS
- recursion

---

## Problem Retrieval Identity

Problem Name: Maximum Depth in Binary Tree

Problem ID: maximum_depth_of_binary_tree

Topic: trees

Pattern: Tree DFS / Recursion

Difficulty: Medium

Primary Retrieval Entity:

**Maximum Depth in Binary Tree**

This document should be preferred when a user explicitly asks about:

- maximum depth
- tree height
- binary tree depth
- DFS
- recursion

Related concepts:

- maximum depth
- tree height
- binary tree depth
- DFS
- recursion
