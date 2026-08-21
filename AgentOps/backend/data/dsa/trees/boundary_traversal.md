# Boundary Traversal of Binary Tree

Problem ID: boundary_traversal

Title: Boundary Traversal of Binary Tree

Difficulty: Medium

Topic: trees

Pattern: **Tree Traversal**

---

## Problem Identity

This document is specifically about:

**Boundary Traversal of Binary Tree**

This knowledge chunk belongs to:

**trees**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Boundary Traversal of Binary Tree** problem.

The primary problem-solving pattern is:

**Tree Traversal**

---

## Key Idea

Boundary traversal visits the root, left boundary, all leaf nodes, and the right boundary in reverse order while avoiding duplicate nodes.

### Core Invariant

Each boundary component contributes nodes exactly once, and leaf nodes are not duplicated in the left or right boundary.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Traverse the tree and separately collect the left boundary, leaf nodes, and right boundary.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. If the tree is empty, return an empty result.
2. Add the root if it is not a leaf.
3. Traverse the left boundary excluding leaf nodes.
4. Traverse all leaf nodes from left to right.
5. Traverse the right boundary excluding leaf nodes.
6. Add the right boundary in reverse order.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Tree Traversal**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Which four parts make up the boundary?

### Hint 2

Why should leaf nodes be excluded from the left and right boundary?

---

## Common Mistakes

- Adding leaf nodes multiple times.
- Including leaf nodes in the left or right boundary.
- Forgetting to reverse the right boundary.
- Incorrectly handling a tree where the root is also a leaf.
- Missing nodes when a subtree has only one child.

---

## Edge Cases

- Empty tree.
- Single-node tree.
- Only left subtree.
- Only right subtree.
- Complete binary tree.
- Skewed tree.
- Tree with missing children.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(H) auxiliary recursion stack space, excluding the output.**

---

## Interview Explanation

A concise interview explanation for **Boundary Traversal of Binary Tree** is:

> Boundary traversal visits the root, left boundary, all leaf nodes, and the right boundary in reverse order while avoiding duplicate nodes.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- boundary traversal
- binary tree boundary
- left boundary
- right boundary
- leaf nodes
- tree traversal

---

## Problem Retrieval Identity

Problem Name: Boundary Traversal of Binary Tree

Problem ID: boundary_traversal

Topic: trees

Pattern: Tree Traversal

Difficulty: Medium

Primary Retrieval Entity:

**Boundary Traversal of Binary Tree**

This document should be preferred when a user explicitly asks about:

- boundary traversal
- binary tree boundary
- left boundary
- right boundary
- leaf nodes
- tree traversal

Related concepts:

- boundary traversal
- binary tree boundary
- left boundary
- right boundary
- leaf nodes
- tree traversal
