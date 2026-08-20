# Squares of a Sorted Array

Problem ID: squares_of_a_sorted_array

Title: Squares of a Sorted Array

Difficulty: Easy

Topic: two_pointers

Pattern: **Two Pointers**

---

## Problem Identity

This document is specifically about:

**Squares of a Sorted Array**

This knowledge chunk belongs to:

**two_pointers**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Squares of a Sorted Array** problem.

The primary problem-solving pattern is:

**Two Pointers**

---

## Key Idea

In a sorted array containing negative and positive numbers, the largest square comes from the number with the largest absolute value. Compare both ends and fill the result from the back.

### Core Invariant

The positions after the current result index contain the largest squares in sorted order.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Square every element and then sort the resulting array.

### Brute Force Complexity

- **Time Complexity:** O(N log N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize left = 0 and right = n - 1.
2. Create a result array of the same size.
3. Start filling the result from index n - 1.
4. Compare the absolute values of nums[left] and nums[right].
5. Place the larger square at the current result position.
6. Move the corresponding pointer.
7. Continue until all elements are processed.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Two Pointers**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Which values can produce the largest square?

### Hint 2

Why are the largest candidates always at the two ends?

---

## Common Mistakes

- Squaring and then sorting unnecessarily.
- Comparing the raw values instead of their absolute values.
- Filling the result from the wrong direction.
- Forgetting negative values can have the largest square.

---

## Edge Cases

- All negative values.
- All positive values.
- Array contains zero.
- Only one element.
- Equal absolute values on both sides.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(N) for the output array.**

---

## Interview Explanation

A concise interview explanation for **Squares of a Sorted Array** is:

> In a sorted array containing negative and positive numbers, the largest square comes from the number with the largest absolute value. Compare both ends and fill the result from the back.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- squares of sorted array
- two pointers
- absolute value
- sorted array
- negative numbers

---

## Problem Retrieval Identity

Problem Name: Squares of a Sorted Array

Problem ID: squares_of_a_sorted_array

Topic: two_pointers

Pattern: Two Pointers

Difficulty: Easy

Primary Retrieval Entity:

**Squares of a Sorted Array**

This document should be preferred when a user explicitly asks about:

- squares of sorted array
- two pointers
- absolute value
- sorted array
- negative numbers

Related concepts:

- squares of sorted array
- two pointers
- absolute value
- sorted array
- negative numbers
