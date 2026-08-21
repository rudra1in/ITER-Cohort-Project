# Power Set using Bit Manipulation

Problem ID: power_set_bit_manipulation

Title: Power Set using Bit Manipulation

Difficulty: Medium

Topic: bit_manipulation

Pattern: **Bitmasking + Subsets**

---

## Problem Identity

This document is specifically about:

**Power Set using Bit Manipulation**

This knowledge chunk belongs to:

**bit_manipulation**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Power Set using Bit Manipulation** problem.

The primary problem-solving pattern is:

**Bitmasking + Subsets**

---

## Key Idea

For an array of n elements, every subset can be represented by an n-bit mask. Bit i determines whether element i is included in the subset.

### Core Invariant

Each mask represents exactly one subset, where a set bit means the corresponding element is selected.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Generate subsets using recursive include/exclude choices.

### Brute Force Complexity

- **Time Complexity:** O(N * 2^N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. For n elements, there are 2^n possible subsets.
2. Iterate mask from 0 to (1 << n) - 1.
3. For every bit position i, check whether mask & (1 << i) is non-zero.
4. If the bit is set, include element i in the current subset.
5. Store or process the generated subset.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Bitmasking + Subsets**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How many subsets does an array of n elements have?

### Hint 2

Can each subset be represented by a binary number?

---

## Common Mistakes

- Using 1 << n incorrectly.
- Looping through the wrong mask range.
- Checking the wrong bit position.
- Forgetting that mask 0 represents the empty subset.

---

## Edge Cases

- Empty array.
- One element.
- All elements distinct.
- Duplicate values.
- Large n where 2^n becomes expensive.

---

## Complexity Analysis

### Time Complexity

**O(N * 2^N)**

### Space Complexity

**O(N * 2^N) if all subsets are stored.**

---

## Interview Explanation

A concise interview explanation for **Power Set using Bit Manipulation** is:

> For an array of n elements, every subset can be represented by an n-bit mask. Bit i determines whether element i is included in the subset.

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
- bitmask
- bit manipulation
- 2^n subsets

---

## Problem Retrieval Identity

Problem Name: Power Set using Bit Manipulation

Problem ID: power_set_bit_manipulation

Topic: bit_manipulation

Pattern: Bitmasking + Subsets

Difficulty: Medium

Primary Retrieval Entity:

**Power Set using Bit Manipulation**

This document should be preferred when a user explicitly asks about:

- power set
- subsets
- bitmask
- bit manipulation
- 2^n subsets

Related concepts:

- power set
- subsets
- bitmask
- bit manipulation
- 2^n subsets
