# Count Occurrences in a Sorted Array

Problem ID: count_occurrences_in_sorted_array

Title: Count Occurrences in a Sorted Array

Difficulty: Easy

Topic: binary_search

Pattern: **First and Last Occurrence / Binary Search**

---

## Problem Identity

This document is specifically about:

**Count Occurrences in a Sorted Array**

This knowledge chunk belongs to:

**binary_search**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Count Occurrences in a Sorted Array** problem.

The primary problem-solving pattern is:

**First and Last Occurrence / Binary Search**

---

## Key Idea

In a sorted array, the number of occurrences of a target can be calculated from its first and last positions.

### Core Invariant

The binary searches maintain the boundary positions of all occurrences of the target.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Scan the complete array and count every element equal to the target.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Find the first occurrence of the target using binary search.
2. Find the last occurrence of the target using binary search.
3. If the target does not exist, return zero.
4. Otherwise calculate count = last - first + 1.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**First and Last Occurrence / Binary Search**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

If you know the first and last occurrence, can you calculate the number of occurrences directly?

### Hint 2

Which two binary-search boundary problems are useful here?

---

## Common Mistakes

- Counting by scanning the entire array.
- Forgetting the +1 in last - first + 1.
- Assuming the target exists.

---

## Edge Cases

- Target does not exist.
- Target appears once.
- Target appears everywhere.
- Target appears only at one boundary.

---

## Complexity Analysis

### Time Complexity

**O(log N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Count Occurrences in a Sorted Array** is:

> In a sorted array, the number of occurrences of a target can be calculated from its first and last positions.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Count Occurrences
- count frequency sorted array
- first occurrence
- last occurrence
- binary search

---

## Problem Retrieval Identity

Problem Name: Count Occurrences in a Sorted Array

Problem ID: count_occurrences_in_sorted_array

Topic: binary_search

Pattern: First and Last Occurrence / Binary Search

Difficulty: Easy

Primary Retrieval Entity:

**Count Occurrences in a Sorted Array**

This document should be preferred when a user explicitly asks about:

- Count Occurrences
- count frequency sorted array
- first occurrence
- last occurrence
- binary search

Related concepts:

- Count Occurrences
- count frequency sorted array
- first occurrence
- last occurrence
- binary search
