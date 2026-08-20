# Partition Equal Subset Sum

Problem ID: partition_equal_subset_sum

Title: Partition Equal Subset Sum

Difficulty: Hard

Topic: dynamic_programming

Pattern: **0/1 Knapsack DP**

---

## Problem Identity

This document is specifically about:

**Partition Equal Subset Sum**

This knowledge chunk belongs to:

**dynamic_programming**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Partition Equal Subset Sum** problem.

The primary problem-solving pattern is:

**0/1 Knapsack DP**

---

## Key Idea

If the total sum is odd, equal partition is impossible. Otherwise the problem becomes finding whether a subset exists whose sum equals totalSum / 2.

### Core Invariant

The DP state tracks whether a subset with the required target sum can be formed using the elements processed so far.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Try every possible subset and check whether its sum equals half of the total sum.

### Brute Force Complexity

- **Time Complexity:** O(2^N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Calculate the total sum of all elements.
2. If the total sum is odd, return false.
3. Set target = totalSum / 2.
4. Use subset-sum DP to determine whether target can be formed.
5. For every element, choose either include or exclude.
6. Return whether target is achievable.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**0/1 Knapsack DP**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What must the sum of each partition be?

### Hint 2

What can you conclude if the total sum is odd?

---

## Common Mistakes

- Not checking whether total sum is odd.
- Using the entire total sum as the target.
- Reusing elements.
- Updating the 1D DP array from left to right.

---

## Edge Cases

- Single element.
- Total sum is odd.
- Total sum is zero.
- Two equal elements.
- Duplicate values.

---

## Complexity Analysis

### Time Complexity

**O(N * Target)**

### Space Complexity

**O(Target).**

---

## Interview Explanation

A concise interview explanation for **Partition Equal Subset Sum** is:

> If the total sum is odd, equal partition is impossible. Otherwise the problem becomes finding whether a subset exists whose sum equals totalSum / 2.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- partition equal subset sum
- subset sum
- 0/1 knapsack
- partition DP
- target sum

---

## Problem Retrieval Identity

Problem Name: Partition Equal Subset Sum

Problem ID: partition_equal_subset_sum

Topic: dynamic_programming

Pattern: 0/1 Knapsack DP

Difficulty: Hard

Primary Retrieval Entity:

**Partition Equal Subset Sum**

This document should be preferred when a user explicitly asks about:

- partition equal subset sum
- subset sum
- 0/1 knapsack
- partition DP
- target sum

Related concepts:

- partition equal subset sum
- subset sum
- 0/1 knapsack
- partition DP
- target sum
