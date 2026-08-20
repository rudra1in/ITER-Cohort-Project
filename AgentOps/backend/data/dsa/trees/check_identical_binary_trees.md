# Check if Two Trees are Identical

Problem ID: check_identical_binary_trees

Title: Check if Two Trees are Identical

Difficulty: Medium

Topic: trees

Pattern: **Tree DFS / Recursion**

---

## Problem Identity

This document is specifically about:

**Check if Two Trees are Identical**

This knowledge chunk belongs to:

**trees**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Check if Two Trees are Identical** problem.

The primary problem-solving pattern is:

**Tree DFS / Recursion**

---

## Key Idea

Two binary trees are identical when corresponding nodes contain the same values and their left and right subtree structures are also identical.

### Core Invariant

At every recursive call, the two current subtrees are identical exactly when their roots and corresponding subtrees match.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Traverse both trees simultaneously and compare corresponding nodes.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. If both nodes are null, return true.
2. If exactly one node is null, return false.
3. Compare the values of the current nodes.
4. Recursively compare their left children.
5. Recursively compare their right children.
6. Return true only when all comparisons succeed.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Tree DFS / Recursion**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What should happen when both current nodes are null?

### Hint 2

What if only one current node is null?

---

## Common Mistakes

- Comparing only node values.
- Forgetting to compare one of the subtrees.
- Handling null nodes incorrectly.
- Comparing nodes from different positions.

---

## Edge Cases

- Both trees empty.
- One tree empty.
- Single-node trees.
- Same values but different structure.
- Different node values.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(H) recursion stack space.**

---

## Interview Explanation

A concise interview explanation for **Check if Two Trees are Identical** is:

> Two binary trees are identical when corresponding nodes contain the same values and their left and right subtree structures are also identical.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- identical binary trees
- same tree
- tree comparison
- DFS
- recursion

---

## Problem Retrieval Identity

Problem Name: Check if Two Trees are Identical

Problem ID: check_identical_binary_trees

Topic: trees

Pattern: Tree DFS / Recursion

Difficulty: Medium

Primary Retrieval Entity:

**Check if Two Trees are Identical**

This document should be preferred when a user explicitly asks about:

- identical binary trees
- same tree
- tree comparison
- DFS
- recursion

Related concepts:

- identical binary trees
- same tree
- tree comparison
- DFS
- recursion
