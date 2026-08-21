# Fractional Knapsack

Problem ID: fractional_knapsack

Title: Fractional Knapsack

Difficulty: Medium

Topic: greedy

Pattern: **Greedy by Value-to-Weight Ratio**

---

## Problem Identity

This document is specifically about:

**Fractional Knapsack**

This knowledge chunk belongs to:

**greedy**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Fractional Knapsack** problem.

The primary problem-solving pattern is:

**Greedy by Value-to-Weight Ratio**

---

## Key Idea

For fractional knapsack, calculate the value-to-weight ratio of every item and take items in decreasing order of this ratio. Fractions of an item are allowed.

### Core Invariant

At every step, the chosen items have the highest available value per unit of weight among all remaining items.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Consider different combinations of items and calculate their total value. This becomes inefficient because many combinations must be explored.

### Brute Force Complexity

- **Time Complexity:** O(2^N) for the basic subset-based approach.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Calculate value divided by weight for every item.
2. Sort items by decreasing value-to-weight ratio.
3. Take the complete item if its weight fits in the remaining capacity.
4. Otherwise take the fraction that fits.
5. Stop when the knapsack becomes full.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Greedy by Value-to-Weight Ratio**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

If you can take a fraction of an item, what should determine which item is most valuable?

### Hint 2

Can you compare items using value per unit weight?

---

## Common Mistakes

- Sorting only by value.
- Sorting only by weight.
- Forgetting that fractions are allowed.
- Using 0/1 knapsack logic for a fractional problem.

---

## Edge Cases

- Capacity is zero.
- Only one item.
- An item is heavier than the complete capacity.
- Multiple items have the same ratio.
- An item can be taken completely.

---

## Complexity Analysis

### Time Complexity

**O(N log N)**

### Space Complexity

**O(N) depending on how item ratios are stored.**

---

## Interview Explanation

A concise interview explanation for **Fractional Knapsack** is:

> For fractional knapsack, calculate the value-to-weight ratio of every item and take items in decreasing order of this ratio. Fractions of an item are allowed.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- fractional knapsack
- knapsack greedy
- value weight ratio
- greedy knapsack
- fractional item

---

## Problem Retrieval Identity

Problem Name: Fractional Knapsack

Problem ID: fractional_knapsack

Topic: greedy

Pattern: Greedy by Value-to-Weight Ratio

Difficulty: Medium

Primary Retrieval Entity:

**Fractional Knapsack**

This document should be preferred when a user explicitly asks about:

- fractional knapsack
- knapsack greedy
- value weight ratio
- greedy knapsack
- fractional item

Related concepts:

- fractional knapsack
- knapsack greedy
- value weight ratio
- greedy knapsack
- fractional item
