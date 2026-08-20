# Preorder Traversal of Binary Tree

Problem ID: preorder_traversal

Title: Preorder Traversal of Binary Tree

Difficulty: Easy

Topic: trees

Pattern: **Tree Traversal**

---

## Problem Identity

This document is specifically about:

**Preorder Traversal of Binary Tree**

This knowledge chunk belongs to:

**trees**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Preorder Traversal of Binary Tree** problem.

The primary problem-solving pattern is:

**Tree Traversal**

---

## Key Idea

Preorder traversal visits the current node first, then recursively visits the left subtree and finally the right subtree.

### Core Invariant

Whenever a node is processed, its value is added before any of its descendants.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use recursion to visit nodes in Root → Left → Right order.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Start from the root.
2. Process the current node.
3. Recursively process the left subtree.
4. Recursively process the right subtree.
5. Stop when the current node is null.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Tree Traversal**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Which node should be processed first?

### Hint 2

What does Root → Left → Right mean?

---

## Common Mistakes

- Visiting the left child before processing the root.
- Swapping left and right traversal.
- Forgetting the null base case.
- Adding nodes to the result more than once.

---

## Edge Cases

- Empty tree.
- Single-node tree.
- Only left subtree.
- Only right subtree.
- Balanced tree.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(H) recursion stack space.**

---

## Interview Explanation

A concise interview explanation for **Preorder Traversal of Binary Tree** is:

> Preorder traversal visits the current node first, then recursively visits the left subtree and finally the right subtree.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- preorder
- binary tree traversal
- root left right
- tree recursion

---

## Problem Retrieval Identity

Problem Name: Preorder Traversal of Binary Tree

Problem ID: preorder_traversal

Topic: trees

Pattern: Tree Traversal

Difficulty: Easy

Primary Retrieval Entity:

**Preorder Traversal of Binary Tree**

This document should be preferred when a user explicitly asks about:

- preorder
- binary tree traversal
- root left right
- tree recursion

Related concepts:

- preorder
- binary tree traversal
- root left right
- tree recursion
