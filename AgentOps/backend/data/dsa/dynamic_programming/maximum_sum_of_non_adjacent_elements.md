# Maximum Sum of Non-Adjacent Elements

Problem ID: maximum_sum_of_non_adjacent_elements

Title: Maximum Sum of Non-Adjacent Elements

Difficulty: Medium

Topic: dynamic_programming

Pattern: **1D DP**

---

## Problem Identity

This document is specifically about:

**Maximum Sum of Non-Adjacent Elements**

This knowledge chunk belongs to:

**dynamic_programming**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Maximum Sum of Non-Adjacent Elements** problem.

The primary problem-solving pattern is:

**1D DP**

---

## Key Idea

For every element, either take it and skip the previous element, or skip it and keep the best answer from the previous position.

### Core Invariant

dp[i] represents the maximum possible sum using elements from index 0 through i without selecting adjacent elements.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use recursion to decide whether to take or skip every element.

### Brute Force Complexity

- **Time Complexity:** O(2^N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Define dp[i] as the maximum sum obtainable from elements up to index i.
2. For every index, calculate the value if the current element is taken.
3. If the current element is taken, add it to dp[i-2].
4. If it is skipped, use dp[i-1].
5. Take the maximum of these two choices.
6. Optimize space by storing only the previous two states.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**1D DP**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

At each element, what are your two choices?

### Hint 2

If you take the current element, which previous element cannot be taken?

---

## Common Mistakes

- Taking adjacent elements.
- Forgetting the skip choice.
- Using dp[i-1] when the current element is selected.
- Incorrect initialization.

---

## Edge Cases

- Empty array.
- One element.
- Two elements.
- All elements negative if allowed.
- All elements positive.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1) with two variables.**

---

## Interview Explanation

A concise interview explanation for **Maximum Sum of Non-Adjacent Elements** is:

> For every element, either take it and skip the previous element, or skip it and keep the best answer from the previous position.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- maximum sum non adjacent
- non adjacent elements
- 1D DP
- take or not take
- house robber pattern

---

## Problem Retrieval Identity

Problem Name: Maximum Sum of Non-Adjacent Elements

Problem ID: maximum_sum_of_non_adjacent_elements

Topic: dynamic_programming

Pattern: 1D DP

Difficulty: Medium

Primary Retrieval Entity:

**Maximum Sum of Non-Adjacent Elements**

This document should be preferred when a user explicitly asks about:

- maximum sum non adjacent
- non adjacent elements
- 1D DP
- take or not take
- house robber pattern

Related concepts:

- maximum sum non adjacent
- non adjacent elements
- 1D DP
- take or not take
- house robber pattern
