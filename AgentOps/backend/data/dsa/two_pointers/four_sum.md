# 4Sum

Problem ID: four_sum

Title: 4Sum

Difficulty: Medium

Topic: two_pointers

Pattern: **Sorting + Multiple Pointers**

---

## Problem Identity

This document is specifically about:

**4Sum**

This knowledge chunk belongs to:

**two_pointers**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **4Sum** problem.

The primary problem-solving pattern is:

**Sorting + Multiple Pointers**

---

## Key Idea

Sort the array, fix two elements, and reduce the remaining two elements to a two-pointer problem.

### Core Invariant

For each fixed pair of elements, the two-pointer range contains all remaining candidate pairs that have not been eliminated.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use four nested loops to examine every possible group of four elements.

### Brute Force Complexity

- **Time Complexity:** O(N^4)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Sort the array.
2. Fix the first element using i.
3. Fix the second element using j.
4. Initialize left = j + 1 and right = n - 1.
5. Calculate the four-element sum.
6. If the sum equals the target, store the quadruplet.
7. Skip duplicate values.
8. Move left or right based on whether the sum is smaller or larger than the target.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Sorting + Multiple Pointers**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can 4Sum be reduced to 2Sum after fixing two elements?

### Hint 2

Why must the array be sorted?

---

## Common Mistakes

- Not sorting the array.
- Not skipping duplicates.
- Integer overflow when calculating the sum.
- Incorrect pointer movement.

---

## Edge Cases

- Fewer than four elements.
- All elements are identical.
- Negative values.
- Very large values.
- No valid quadruplet.

---

## Complexity Analysis

### Time Complexity

**O(N^3)**

### Space Complexity

**O(1) excluding the output and sorting implementation.**

---

## Interview Explanation

A concise interview explanation for **4Sum** is:

> Sort the array, fix two elements, and reduce the remaining two elements to a two-pointer problem.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- 4sum
- four sum
- quadruplets
- two pointers
- sorting

---

## Problem Retrieval Identity

Problem Name: 4Sum

Problem ID: four_sum

Topic: two_pointers

Pattern: Sorting + Multiple Pointers

Difficulty: Medium

Primary Retrieval Entity:

**4Sum**

This document should be preferred when a user explicitly asks about:

- 4sum
- four sum
- quadruplets
- two pointers
- sorting

Related concepts:

- 4sum
- four sum
- quadruplets
- two pointers
- sorting
