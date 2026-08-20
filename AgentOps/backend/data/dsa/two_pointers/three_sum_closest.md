# 3Sum Closest

Problem ID: three_sum_closest

Title: 3Sum Closest

Difficulty: Medium

Topic: two_pointers

Pattern: **Sorting + Two Pointers**

---

## Problem Identity

This document is specifically about:

**3Sum Closest**

This knowledge chunk belongs to:

**two_pointers**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **3Sum Closest** problem.

The primary problem-solving pattern is:

**Sorting + Two Pointers**

---

## Key Idea

Sort the array, fix one element, and use two pointers to find the three-element sum closest to the target.

### Core Invariant

For every fixed first element, the pointer movement eliminates sums that cannot be closer because the array is sorted.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Check every combination of three elements and keep the sum with the smallest absolute difference from the target.

### Brute Force Complexity

- **Time Complexity:** O(N^3)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Sort the array.
2. Fix the first element using i.
3. Initialize left = i + 1 and right = n - 1.
4. Calculate the current three-element sum.
5. Update the closest answer if the current sum is closer to the target.
6. If the sum is smaller than the target, move left forward.
7. If the sum is larger than the target, move right backward.
8. If the sum equals the target, return immediately.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Sorting + Two Pointers**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How can sorting help decide which pointer to move?

### Hint 2

What value should you compare with the current best answer?

---

## Common Mistakes

- Comparing the sums instead of their absolute differences.
- Moving both pointers without checking the sum.
- Forgetting to sort.
- Incorrect initialization of the closest sum.

---

## Edge Cases

- Exactly three elements.
- Target is smaller than all possible sums.
- Target is larger than all possible sums.
- Exact target exists.
- Negative values.

---

## Complexity Analysis

### Time Complexity

**O(N^2)**

### Space Complexity

**O(1) excluding sorting implementation.**

---

## Interview Explanation

A concise interview explanation for **3Sum Closest** is:

> Sort the array, fix one element, and use two pointers to find the three-element sum closest to the target.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- 3sum closest
- three sum
- closest sum
- sorting
- two pointers

---

## Problem Retrieval Identity

Problem Name: 3Sum Closest

Problem ID: three_sum_closest

Topic: two_pointers

Pattern: Sorting + Two Pointers

Difficulty: Medium

Primary Retrieval Entity:

**3Sum Closest**

This document should be preferred when a user explicitly asks about:

- 3sum closest
- three sum
- closest sum
- sorting
- two pointers

Related concepts:

- 3sum closest
- three sum
- closest sum
- sorting
- two pointers
