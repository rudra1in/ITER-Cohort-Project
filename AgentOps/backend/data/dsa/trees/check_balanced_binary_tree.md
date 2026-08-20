# Check for Balanced Binary Tree

Problem ID: check_balanced_binary_tree

Title: Check for Balanced Binary Tree

Difficulty: Medium

Topic: trees

Pattern: **Tree DFS / Height**

---

## Problem Identity

This document is specifically about:

**Check for Balanced Binary Tree**

This knowledge chunk belongs to:

**trees**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Check for Balanced Binary Tree** problem.

The primary problem-solving pattern is:

**Tree DFS / Height**

---

## Key Idea

A binary tree is balanced when the height difference between the left and right subtrees of every node is at most one.

### Core Invariant

The recursive function simultaneously determines subtree height and whether that subtree is balanced.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

For every node, separately calculate the height of its left and right subtrees and check their difference.

### Brute Force Complexity

- **Time Complexity:** O(N^2) in the worst case
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Recursively calculate the height of the left subtree.
2. Recursively calculate the height of the right subtree.
3. If either subtree is already unbalanced, propagate a failure value.
4. Check whether the height difference is greater than one.
5. Return the height of the current subtree if balanced.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Tree DFS / Height**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can height calculation and balance checking be combined?

### Hint 2

What should happen if a subtree is already unbalanced?

---

## Common Mistakes

- Calculating height separately for every node.
- Forgetting to check both subtrees.
- Using an incorrect height difference condition.
- Continuing expensive calculations after detecting an imbalance.

---

## Edge Cases

- Empty tree.
- Single-node tree.
- Perfectly balanced tree.
- Completely skewed tree.
- Imbalance near the root.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(H) recursion stack space.**

---

## Interview Explanation

A concise interview explanation for **Check for Balanced Binary Tree** is:

> A binary tree is balanced when the height difference between the left and right subtrees of every node is at most one.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- balanced binary tree
- height balanced
- tree height
- DFS
- recursion

---

## Problem Retrieval Identity

Problem Name: Check for Balanced Binary Tree

Problem ID: check_balanced_binary_tree

Topic: trees

Pattern: Tree DFS / Height

Difficulty: Medium

Primary Retrieval Entity:

**Check for Balanced Binary Tree**

This document should be preferred when a user explicitly asks about:

- balanced binary tree
- height balanced
- tree height
- DFS
- recursion

Related concepts:

- balanced binary tree
- height balanced
- tree height
- DFS
- recursion
