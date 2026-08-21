# Subsets I

Problem ID: subsets_i

Title: Subsets I

Difficulty: Medium

Topic: recursion

Pattern: **Recursion + Include Exclude**

---

## Problem Identity

This document is specifically about:

**Subsets I**

This knowledge chunk belongs to:

**recursion**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Subsets I** problem.

The primary problem-solving pattern is:

**Recursion + Include Exclude**

---

## Key Idea

Generate every subset by making an include or exclude decision for each element.

### Core Invariant

The current subset contains only decisions made for indices before the current recursive index.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Enumerate all possible combinations of elements and collect them as subsets.

### Brute Force Complexity

- **Time Complexity:** O(2^N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Start recursion from index 0.
2. Maintain a current subset.
3. Choose to include the current element.
4. Recursively process the next index.
5. Remove the element to backtrack.
6. Choose to exclude the current element.
7. Continue until all elements are processed.
8. Add every completed subset to the answer.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Recursion + Include Exclude**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

For each element, can you make an include and exclude choice?

### Hint 2

What should happen when index reaches the array length?

---

## Common Mistakes

- Forgetting backtracking.
- Not adding the empty subset.
- Adding duplicate references instead of copies.

---

## Edge Cases

- Empty array.
- Single element.
- Multiple elements.

---

## Complexity Analysis

### Time Complexity

**O(2^N) subsets are generated.**

### Space Complexity

**O(N) recursion depth excluding output.**

---

## Interview Explanation

A concise interview explanation for **Subsets I** is:

> Generate every subset by making an include or exclude decision for each element.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- subsets
- subsets I
- power set
- recursion
- include exclude

---

## Problem Retrieval Identity

Problem Name: Subsets I

Problem ID: subsets_i

Topic: recursion

Pattern: Recursion + Include Exclude

Difficulty: Medium

Primary Retrieval Entity:

**Subsets I**

This document should be preferred when a user explicitly asks about:

- subsets
- subsets I
- power set
- recursion
- include exclude

Related concepts:

- subsets
- subsets I
- power set
- recursion
- include exclude
