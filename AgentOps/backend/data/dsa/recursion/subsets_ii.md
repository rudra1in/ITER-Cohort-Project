# Subsets II

Problem ID: subsets_ii

Title: Subsets II

Difficulty: Medium

Topic: recursion

Pattern: **Backtracking + Duplicate Handling**

---

## Problem Identity

This document is specifically about:

**Subsets II**

This knowledge chunk belongs to:

**recursion**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Subsets II** problem.

The primary problem-solving pattern is:

**Backtracking + Duplicate Handling**

---

## Key Idea

Sort the array first and use backtracking while skipping duplicate values at the same recursion level so that duplicate subsets are not generated.

### Core Invariant

At each recursion level, equal values are used only once as starting choices, preventing duplicate subsets.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Generate all subsets and use a set to remove duplicate subsets.

### Brute Force Complexity

- **Time Complexity:** O(2^N) generation plus additional space for duplicate removal.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Sort the array.
2. Start backtracking from index 0.
3. Add the current subset to the result.
4. Iterate through possible choices.
5. Skip an element when it is equal to the previous element at the same recursion level.
6. Include the current element.
7. Recursively continue.
8. Backtrack by removing the element.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Backtracking + Duplicate Handling**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Why should the array be sorted before handling duplicates?

### Hint 2

When should two equal values be skipped?

---

## Common Mistakes

- Forgetting to sort.
- Skipping duplicates at every recursion level.
- Not skipping duplicates at the same level.
- Forgetting to backtrack.

---

## Edge Cases

- All elements are equal.
- No duplicate values.
- Empty array.
- Single element.

---

## Complexity Analysis

### Time Complexity

**O(2^N * N) in the worst case due to generating and copying subsets.**

### Space Complexity

**O(N) recursion depth excluding output.**

---

## Interview Explanation

A concise interview explanation for **Subsets II** is:

> Sort the array first and use backtracking while skipping duplicate values at the same recursion level so that duplicate subsets are not generated.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- subsets II
- subsets with duplicates
- duplicate subsets
- backtracking
- recursion

---

## Problem Retrieval Identity

Problem Name: Subsets II

Problem ID: subsets_ii

Topic: recursion

Pattern: Backtracking + Duplicate Handling

Difficulty: Medium

Primary Retrieval Entity:

**Subsets II**

This document should be preferred when a user explicitly asks about:

- subsets II
- subsets with duplicates
- duplicate subsets
- backtracking
- recursion

Related concepts:

- subsets II
- subsets with duplicates
- duplicate subsets
- backtracking
- recursion
