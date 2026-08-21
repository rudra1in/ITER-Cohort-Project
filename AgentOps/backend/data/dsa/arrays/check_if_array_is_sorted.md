# Check if the Array is Sorted

Problem ID: check_if_array_is_sorted

Title: Check if the Array is Sorted

Difficulty: Easy

Topic: arrays

Pattern: **Adjacent Comparison**

---

## Problem Identity

This document is specifically about:

**Check if the Array is Sorted**

This knowledge chunk belongs to:

**arrays**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Check if the Array is Sorted** problem.

The primary problem-solving pattern is:

**Adjacent Comparison**

---

## Key Idea

A non-decreasing array must have every element greater than or equal to the previous element. Scan adjacent pairs and return false when an order violation is found.

### Core Invariant

Every adjacent pair processed so far satisfies the required sorted order.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Compare every pair of elements and check whether an earlier element is greater than a later element.

### Brute Force Complexity

- **Time Complexity:** O(N²)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Start from the second element.
2. Compare each element with the previous element.
3. If the current element is smaller than the previous element, the array is not sorted.
4. If no violation is found, the array is sorted.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Adjacent Comparison**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What must be true for every adjacent pair in a sorted array?

### Hint 2

Can one incorrect adjacent pair prove that the entire array is unsorted?

---

## Common Mistakes

- Using the wrong comparison.
- Forgetting that duplicate values are allowed.
- Checking only the first and last elements.

---

## Edge Cases

- Empty array.
- Single element.
- All elements equal.
- Already sorted array.
- Descending array.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Check if the Array is Sorted** is:

> A non-decreasing array must have every element greater than or equal to the previous element. Scan adjacent pairs and return false when an order violation is found.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Check if Array is Sorted
- sorted array
- array sorted
- non decreasing
- adjacent comparison

---

## Problem Retrieval Identity

Problem Name: Check if the Array is Sorted

Problem ID: check_if_array_is_sorted

Topic: arrays

Pattern: Adjacent Comparison

Difficulty: Easy

Primary Retrieval Entity:

**Check if the Array is Sorted**

This document should be preferred when a user explicitly asks about:

- Check if Array is Sorted
- sorted array
- array sorted
- non decreasing
- adjacent comparison

Related concepts:

- Check if Array is Sorted
- sorted array
- array sorted
- non decreasing
- adjacent comparison
