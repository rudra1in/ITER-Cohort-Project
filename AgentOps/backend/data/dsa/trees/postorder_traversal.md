# Postorder Traversal of Binary Tree

Problem ID: postorder_traversal

Title: Postorder Traversal of Binary Tree

Difficulty: Easy

Topic: trees

Pattern: **Tree Traversal**

---

## Problem Identity

This document is specifically about:

**Postorder Traversal of Binary Tree**

This knowledge chunk belongs to:

**trees**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Postorder Traversal of Binary Tree** problem.

The primary problem-solving pattern is:

**Tree Traversal**

---

## Key Idea

Postorder traversal visits the left subtree, then the right subtree, and processes the current node last.

### Core Invariant

A node is processed only after both of its subtrees have been completely processed.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use recursion to visit nodes in Left → Right → Root order.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Start from the root.
2. Recursively process the left subtree.
3. Recursively process the right subtree.
4. Process the current node after both children are processed.
5. Stop when the current node is null.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Tree Traversal**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Which node should be processed last?

### Hint 2

What does Left → Right → Root mean?

---

## Common Mistakes

- Processing the root too early.
- Swapping left and right subtree processing.
- Forgetting the base case.
- Confusing postorder with preorder.

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

A concise interview explanation for **Postorder Traversal of Binary Tree** is:

> Postorder traversal visits the left subtree, then the right subtree, and processes the current node last.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- postorder
- binary tree traversal
- left right root
- tree recursion

---

## Problem Retrieval Identity

Problem Name: Postorder Traversal of Binary Tree

Problem ID: postorder_traversal

Topic: trees

Pattern: Tree Traversal

Difficulty: Easy

Primary Retrieval Entity:

**Postorder Traversal of Binary Tree**

This document should be preferred when a user explicitly asks about:

- postorder
- binary tree traversal
- left right root
- tree recursion

Related concepts:

- postorder
- binary tree traversal
- left right root
- tree recursion
