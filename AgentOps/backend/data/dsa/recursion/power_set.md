# Power Set

Problem ID: power_set

Title: Power Set

Difficulty: Medium

Topic: recursion

Pattern: **Recursion + Subsequence**

---

## Problem Identity

This document is specifically about:

**Power Set**

This knowledge chunk belongs to:

**recursion**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Power Set** problem.

The primary problem-solving pattern is:

**Recursion + Subsequence**

---

## Key Idea

For every element, make two recursive choices: include the current element in the subset or exclude it. When all elements have been processed, the current collection represents one subset.

### Core Invariant

At every recursive call, the current subset contains exactly the elements selected from the indices processed so far.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Generate every possible subset by repeatedly making include and exclude choices for each element.

### Brute Force Complexity

- **Time Complexity:** O(2^N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Start recursion from index 0 with an empty current subset.
2. At each index, choose to include the current element.
3. Recursively process the next index.
4. Backtrack by removing the current element.
5. Choose to exclude the current element.
6. Recursively process the next index.
7. When the index reaches n, add the current subset to the result.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Recursion + Subsequence**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

For every element, what are the two possible choices?

### Hint 2

Can you recursively solve the remaining elements after making an include or exclude decision?

---

## Common Mistakes

- Forgetting to backtrack after including an element.
- Not adding the current subset at the base case.
- Starting recursion from the wrong index.
- Modifying the same subset reference without copying it.

---

## Edge Cases

- Empty array.
- Single element.
- All elements are equal.
- Array contains negative values.
- Array contains duplicate values.

---

## Complexity Analysis

### Time Complexity

**O(2^N) subsets are generated, with additional O(N) work to copy each subset.**

### Space Complexity

**O(N) recursion depth excluding the output list.**

---

## Interview Explanation

A concise interview explanation for **Power Set** is:

> For every element, make two recursive choices: include the current element in the subset or exclude it. When all elements have been processed, the current collection represents one subset.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- power set
- subsets
- subsequence
- recursion
- include exclude
- backtracking

---

## Problem Retrieval Identity

Problem Name: Power Set

Problem ID: power_set

Topic: recursion

Pattern: Recursion + Subsequence

Difficulty: Medium

Primary Retrieval Entity:

**Power Set**

This document should be preferred when a user explicitly asks about:

- power set
- subsets
- subsequence
- recursion
- include exclude
- backtracking

Related concepts:

- power set
- subsets
- subsequence
- recursion
- include exclude
- backtracking
