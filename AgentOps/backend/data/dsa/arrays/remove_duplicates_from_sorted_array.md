# Remove Duplicates from Sorted Array

Problem ID: remove_duplicates_from_sorted_array

Title: Remove Duplicates from Sorted Array

Difficulty: Easy

Topic: arrays

Pattern: **Two Pointers**

---

## Problem Identity

This document is specifically about:

**Remove Duplicates from Sorted Array**

This knowledge chunk belongs to:

**arrays**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Remove Duplicates from Sorted Array** problem.

The primary problem-solving pattern is:

**Two Pointers**

---

## Key Idea

Because the array is sorted, duplicates appear next to each other. Use one pointer to track the position for the next unique value and another pointer to scan the array.

### Core Invariant

The portion before the write pointer contains the unique elements found so far in sorted order.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use an additional data structure such as a set to store unique values and then copy them back into the array.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. If the array is empty, return zero.
2. Keep a write pointer at index 1.
3. Scan the array from index 1 onward.
4. Whenever the current value differs from the previous value, place it at the write pointer.
5. Increment the write pointer.
6. Return the number of unique elements.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Two Pointers**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What does sorting tell you about where duplicate values occur?

### Hint 2

Can one pointer scan while another marks where the next unique value should go?

---

## Common Mistakes

- Using extra space unnecessarily.
- Comparing against the wrong element.
- Returning the last index instead of the number of unique elements.

---

## Edge Cases

- Empty array.
- Single element.
- All elements are duplicates.
- No duplicates.
- Multiple groups of duplicates.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Remove Duplicates from Sorted Array** is:

> Because the array is sorted, duplicates appear next to each other. Use one pointer to track the position for the next unique value and another pointer to scan the array.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Remove Duplicates from Sorted Array
- remove duplicates
- two pointers
- unique elements
- LeetCode 26

---

## Problem Retrieval Identity

Problem Name: Remove Duplicates from Sorted Array

Problem ID: remove_duplicates_from_sorted_array

Topic: arrays

Pattern: Two Pointers

Difficulty: Easy

Primary Retrieval Entity:

**Remove Duplicates from Sorted Array**

This document should be preferred when a user explicitly asks about:

- Remove Duplicates from Sorted Array
- remove duplicates
- two pointers
- unique elements
- LeetCode 26

Related concepts:

- Remove Duplicates from Sorted Array
- remove duplicates
- two pointers
- unique elements
- LeetCode 26
