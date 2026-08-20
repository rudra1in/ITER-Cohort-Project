# Diameter of Binary Tree

Problem ID: diameter_of_binary_tree

Title: Diameter of Binary Tree

Difficulty: Easy

Topic: trees

Pattern: **Tree DFS / Height**

---

## Problem Identity

This document is specifically about:

**Diameter of Binary Tree**

This knowledge chunk belongs to:

**trees**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Diameter of Binary Tree** problem.

The primary problem-solving pattern is:

**Tree DFS / Height**

---

## Key Idea

The diameter is the longest path between any two nodes. For each node, a candidate diameter is the height of its left subtree plus the height of its right subtree.

### Core Invariant

For every processed node, the stored maximum represents the largest diameter found in the processed subtree.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Calculate the height of the left and right subtrees for every node and use their sum to determine the maximum path.

### Brute Force Complexity

- **Time Complexity:** O(N^2) in the worst case
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Use a recursive height function.
2. For each node, calculate the left subtree height.
3. Calculate the right subtree height.
4. Update the maximum diameter using leftHeight + rightHeight.
5. Return 1 + max(leftHeight, rightHeight) to the parent.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Tree DFS / Height**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How is the diameter related to the heights of the left and right subtrees?

### Hint 2

Can you calculate height and diameter in the same DFS?

---

## Common Mistakes

- Returning the diameter instead of height from recursion.
- Forgetting to update the global maximum.
- Confusing number of edges with number of nodes.
- Calculating height repeatedly.

---

## Edge Cases

- Empty tree.
- Single-node tree.
- Two-node tree.
- Skewed tree.
- Diameter passing through the root.
- Diameter not passing through the root.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(H) recursion stack space.**

---

## Interview Explanation

A concise interview explanation for **Diameter of Binary Tree** is:

> The diameter is the longest path between any two nodes. For each node, a candidate diameter is the height of its left subtree plus the height of its right subtree.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- diameter binary tree
- tree diameter
- maximum path
- tree height
- DFS

---

## Problem Retrieval Identity

Problem Name: Diameter of Binary Tree

Problem ID: diameter_of_binary_tree

Topic: trees

Pattern: Tree DFS / Height

Difficulty: Easy

Primary Retrieval Entity:

**Diameter of Binary Tree**

This document should be preferred when a user explicitly asks about:

- diameter binary tree
- tree diameter
- maximum path
- tree height
- DFS

Related concepts:

- diameter binary tree
- tree diameter
- maximum path
- tree height
- DFS
