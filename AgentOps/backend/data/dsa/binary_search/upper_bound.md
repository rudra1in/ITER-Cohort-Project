# Upper Bound

Problem ID: upper_bound

Title: Upper Bound

Difficulty: Easy

Topic: binary_search

Pattern: **Binary Search on First Greater Position**

---

## Problem Identity

This document is specifically about:

**Upper Bound**

This knowledge chunk belongs to:

**binary_search**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Upper Bound** problem.

The primary problem-solving pattern is:

**Binary Search on First Greater Position**

---

## Key Idea

Upper bound finds the first index whose value is strictly greater than the target.

### Core Invariant

If nums[mid] is greater than the target, mid is a valid upper-bound candidate, but an earlier valid position may exist.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Scan the sorted array from left to right and return the first index where nums[i] is greater than the target.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Set low = 0 and high = n - 1.
2. Maintain an answer initialized to n.
3. Calculate mid.
4. If nums[mid] is greater than the target, record mid and search the left half.
5. Otherwise search the right half.
6. Return the first position containing a value greater than the target.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Binary Search on First Greater Position**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How is upper bound different from lower bound?

### Hint 2

When nums[mid] is equal to the target, can mid still be the answer?

---

## Common Mistakes

- Using >= instead of >.
- Confusing upper bound with lower bound.
- Returning the last occurrence instead of the first greater position.

---

## Edge Cases

- Empty array.
- All elements equal to the target.
- Target smaller than every element.
- Target greater than every element.

---

## Complexity Analysis

### Time Complexity

**O(log N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Upper Bound** is:

> Upper bound finds the first index whose value is strictly greater than the target.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Upper Bound
- upper_bound
- first greater
- binary search upper bound

---

## Problem Retrieval Identity

Problem Name: Upper Bound

Problem ID: upper_bound

Topic: binary_search

Pattern: Binary Search on First Greater Position

Difficulty: Easy

Primary Retrieval Entity:

**Upper Bound**

This document should be preferred when a user explicitly asks about:

- Upper Bound
- upper_bound
- first greater
- binary search upper bound

Related concepts:

- Upper Bound
- upper_bound
- first greater
- binary search upper bound
