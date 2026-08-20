# Coin Change 2

Problem ID: coin_change_2

Title: Coin Change 2

Difficulty: Hard

Topic: dynamic_programming

Pattern: **Unbounded Knapsack DP**

---

## Problem Identity

This document is specifically about:

**Coin Change 2**

This knowledge chunk belongs to:

**dynamic_programming**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Coin Change 2** problem.

The primary problem-solving pattern is:

**Unbounded Knapsack DP**

---

## Key Idea

For each coin, we can either skip it or use it again because coins can be used unlimited times. The DP counts the number of combinations that form the target amount.

### Core Invariant

After processing a coin, dp[amount] represents the number of combinations to form that amount using the processed coins without counting different orders as different combinations.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use recursion to try including or excluding each coin. Since a coin can be reused, the same coin can be selected multiple times.

### Brute Force Complexity

- **Time Complexity:** Exponential
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Define dp[amount] as the number of combinations that form that amount.
2. Initialize dp[0] = 1 because there is one way to make amount zero: choose no coins.
3. Process coins one by one.
4. For every coin, iterate amounts from coin value to the target.
5. Add dp[amount - coin] to dp[amount].
6. Return dp[target].

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Unbounded Knapsack DP**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can each coin be used more than once?

### Hint 2

What should dp[0] represent?

---

## Common Mistakes

- Counting permutations instead of combinations.
- Iterating coins and amounts in the wrong order.
- Forgetting dp[0] = 1.
- Treating the problem as 0/1 knapsack.
- Using a coin only once when unlimited usage is allowed.

---

## Edge Cases

- Amount = 0.
- No combination can form the amount.
- One coin denomination.
- Coin value greater than target.
- Duplicate denominations if input permits them.

---

## Complexity Analysis

### Time Complexity

**O(N * Amount)**

### Space Complexity

**O(Amount).**

---

## Interview Explanation

A concise interview explanation for **Coin Change 2** is:

> For each coin, we can either skip it or use it again because coins can be used unlimited times. The DP counts the number of combinations that form the target amount.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- coin change 2
- coin change II
- unbounded knapsack
- number of combinations
- 1D DP

---

## Problem Retrieval Identity

Problem Name: Coin Change 2

Problem ID: coin_change_2

Topic: dynamic_programming

Pattern: Unbounded Knapsack DP

Difficulty: Hard

Primary Retrieval Entity:

**Coin Change 2**

This document should be preferred when a user explicitly asks about:

- coin change 2
- coin change II
- unbounded knapsack
- number of combinations
- 1D DP

Related concepts:

- coin change 2
- coin change II
- unbounded knapsack
- number of combinations
- 1D DP
