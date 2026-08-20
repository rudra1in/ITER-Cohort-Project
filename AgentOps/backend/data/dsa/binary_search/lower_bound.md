# Lower Bound

Problem ID: lower_bound

Title: Lower Bound

Difficulty: Easy

Topic: binary_search

Pattern: **Binary Search on First Valid Position**

---

## Problem Identity

This document is specifically about:

**Lower Bound**

This knowledge chunk belongs to:

**binary_search**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Lower Bound** problem.

The primary problem-solving pattern is:

**Binary Search on First Valid Position**

---

## Key Idea

Lower bound finds the first index whose value is greater than or equal to the target. Binary search can eliminate half the search space while maintaining the first valid position found so far.

### Core Invariant

Whenever nums[mid] is greater than or equal to the target, mid is a valid candidate, but an earlier valid position may still exist on the left.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Scan the sorted array from left to right and return the first index where nums[i] is greater than or equal to the target.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Set low = 0 and high = n - 1.
2. Maintain an answer initialized to n.
3. Calculate mid.
4. If nums[mid] is greater than or equal to the target, record mid as a possible answer and search the left half.
5. Otherwise search the right half.
6. Return the first valid index, or n if no such index exists.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Binary Search on First Valid Position**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Instead of asking whether the target exists, can you find the first position where the value becomes greater than or equal to the target?

### Hint 2

When nums[mid] is valid, should you stop or continue searching toward the left?

---

## Common Mistakes

- Returning any matching index instead of the first valid index.
- Moving right when nums[mid] is already greater than or equal to the target.
- Incorrect handling when every element is smaller than the target.

---

## Edge Cases

- Empty array.
- Target smaller than every element.
- Target larger than every element.
- Many duplicate values.
- Target appears multiple times.

---

## Complexity Analysis

### Time Complexity

**O(log N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Lower Bound** is:

> Lower bound finds the first index whose value is greater than or equal to the target. Binary search can eliminate half the search space while maintaining the first valid position found so far.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Lower Bound
- lower_bound
- first greater or equal
- first position
- binary search lower bound

---

## Problem Retrieval Identity

Problem Name: Lower Bound

Problem ID: lower_bound

Topic: binary_search

Pattern: Binary Search on First Valid Position

Difficulty: Easy

Primary Retrieval Entity:

**Lower Bound**

This document should be preferred when a user explicitly asks about:

- Lower Bound
- lower_bound
- first greater or equal
- first position
- binary search lower bound

Related concepts:

- Lower Bound
- lower_bound
- first greater or equal
- first position
- binary search lower bound
