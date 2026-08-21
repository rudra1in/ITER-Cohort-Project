# Subset Sum Equal to Target

Problem ID: subset_sum_equal_to_target

Title: Subset Sum Equal to Target

Difficulty: Hard

Topic: dynamic_programming

Pattern: **0/1 Knapsack DP**

---

## Problem Identity

This document is specifically about:

**Subset Sum Equal to Target**

This knowledge chunk belongs to:

**dynamic_programming**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Subset Sum Equal to Target** problem.

The primary problem-solving pattern is:

**0/1 Knapsack DP**

---

## Key Idea

For every element, either include it in the subset or exclude it. The DP state determines whether a particular sum can be formed using the processed elements.

### Core Invariant

dp[i][target] is true exactly when the target sum can be formed using the first i elements.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use recursion to make an include-or-exclude decision for every element.

### Brute Force Complexity

- **Time Complexity:** O(2^N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Define dp[i][target] as whether target can be formed using the first i elements.
2. Initialize dp[i][0] = true because sum zero is always possible by choosing no elements.
3. For every element, consider excluding it.
4. If the element is not greater than the current target, also consider including it.
5. The state is true if either choice can form the target.
6. Return whether the target state is true after processing all elements.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**0/1 Knapsack DP**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

For every number, what are the two choices?

### Hint 2

Can the target be formed without using the current element?

---

## Common Mistakes

- Reusing an element multiple times.
- Updating the 1D DP array in the wrong direction.
- Forgetting dp[0] = true.
- Confusing subset sum with unbounded knapsack.

---

## Edge Cases

- Target = 0.
- Single element.
- Target larger than total sum.
- Duplicate values.
- Zero-valued elements.

---

## Complexity Analysis

### Time Complexity

**O(N * Target)**

### Space Complexity

**O(Target) using a one-dimensional DP array.**

---

## Interview Explanation

A concise interview explanation for **Subset Sum Equal to Target** is:

> For every element, either include it in the subset or exclude it. The DP state determines whether a particular sum can be formed using the processed elements.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- subset sum
- 0/1 knapsack
- subsequence DP
- boolean DP
- target sum

---

## Problem Retrieval Identity

Problem Name: Subset Sum Equal to Target

Problem ID: subset_sum_equal_to_target

Topic: dynamic_programming

Pattern: 0/1 Knapsack DP

Difficulty: Hard

Primary Retrieval Entity:

**Subset Sum Equal to Target**

This document should be preferred when a user explicitly asks about:

- subset sum
- 0/1 knapsack
- subsequence DP
- boolean DP
- target sum

Related concepts:

- subset sum
- 0/1 knapsack
- subsequence DP
- boolean DP
- target sum
