# 3Sum

Problem ID: three_sum

Title: 3Sum

Difficulty: Medium

Topic: two_pointers

Pattern: **Sorting + Two Pointers**

---

## Problem Identity

This document is specifically about:

**3Sum**

This knowledge chunk belongs to:

**two_pointers**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **3Sum** problem.

The primary problem-solving pattern is:

**Sorting + Two Pointers**

---

## Key Idea

Sort the array and fix one element. Then use two pointers on the remaining portion to find pairs whose sum completes the target of zero.

### Core Invariant

For a fixed first element, the two-pointer range contains all remaining candidates that have not yet been eliminated.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use three nested loops to check every possible combination of three elements.

### Brute Force Complexity

- **Time Complexity:** O(N^3)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Sort the array.
2. Fix an element using index i.
3. Skip duplicate values for i.
4. Initialize left = i + 1 and right = n - 1.
5. Calculate the sum of nums[i] + nums[left] + nums[right].
6. If the sum is zero, store the triplet.
7. Move both pointers and skip duplicate values.
8. If the sum is smaller than zero, move left forward.
9. If the sum is larger than zero, move right backward.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Sorting + Two Pointers**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can you reduce 3Sum to a two-sum problem?

### Hint 2

Why should the array be sorted?

---

## Common Mistakes

- Not sorting the array.
- Not skipping duplicate values.
- Moving only one pointer after finding a valid triplet.
- Returning duplicate triplets.

---

## Edge Cases

- Array contains fewer than three elements.
- All values are zero.
- All values are positive.
- All values are negative.
- Many duplicate values.

---

## Complexity Analysis

### Time Complexity

**O(N^2)**

### Space Complexity

**O(1) excluding the output and sorting implementation.**

---

## Interview Explanation

A concise interview explanation for **3Sum** is:

> Sort the array and fix one element. Then use two pointers on the remaining portion to find pairs whose sum completes the target of zero.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- 3sum
- three sum
- sorting
- two pointers
- triplets
- duplicate handling

---

## Problem Retrieval Identity

Problem Name: 3Sum

Problem ID: three_sum

Topic: two_pointers

Pattern: Sorting + Two Pointers

Difficulty: Medium

Primary Retrieval Entity:

**3Sum**

This document should be preferred when a user explicitly asks about:

- 3sum
- three sum
- sorting
- two pointers
- triplets
- duplicate handling

Related concepts:

- 3sum
- three sum
- sorting
- two pointers
- triplets
- duplicate handling
