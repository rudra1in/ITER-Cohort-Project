# Single Element in a Sorted Array

Problem ID: single_element_in_sorted_array

Title: Single Element in a Sorted Array

Difficulty: Medium

Topic: binary_search

Pattern: **Binary Search Using Pair Parity**

---

## Problem Identity

This document is specifically about:

**Single Element in a Sorted Array**

This knowledge chunk belongs to:

**binary_search**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Single Element in a Sorted Array** problem.

The primary problem-solving pattern is:

**Binary Search Using Pair Parity**

---

## Key Idea

In a sorted array where every element appears twice except one element, pairs occur at predictable even-odd indices before the single element. Binary search can use this parity property to locate the unique element.

### Core Invariant

The unique element always remains inside the current search range, and the pairing pattern determines which half contains it.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use a frequency map or scan neighboring elements to find the element that does not have an equal pair.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Set low = 0 and high = n - 1.
2. Calculate mid.
3. Ensure mid is even by adjusting it when necessary.
4. Compare nums[mid] with nums[mid + 1].
5. If they form a correct pair, the single element lies to the right.
6. Otherwise the single element lies at mid or to the left.
7. Continue until low equals high.
8. Return nums[low].

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Binary Search Using Pair Parity**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Before the unique element, pairs start at even indices. What happens to this pattern after the unique element?

### Hint 2

Can you use the parity of the middle index to determine which side contains the single element?

---

## Common Mistakes

- Ignoring the even-odd index pairing pattern.
- Using a frequency map when O(1) extra space is expected.
- Accessing mid + 1 without ensuring it is inside the array.
- Using the wrong direction after comparing the pair.

---

## Edge Cases

- Array contains one element.
- Unique element is at the beginning.
- Unique element is at the end.
- Unique element is in the middle.

---

## Complexity Analysis

### Time Complexity

**O(log N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Single Element in a Sorted Array** is:

> In a sorted array where every element appears twice except one element, pairs occur at predictable even-odd indices before the single element. Binary search can use this parity property to locate the unique element.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Single Element in Sorted Array
- unique element
- pair parity
- binary search
- LeetCode 540

---

## Problem Retrieval Identity

Problem Name: Single Element in a Sorted Array

Problem ID: single_element_in_sorted_array

Topic: binary_search

Pattern: Binary Search Using Pair Parity

Difficulty: Medium

Primary Retrieval Entity:

**Single Element in a Sorted Array**

This document should be preferred when a user explicitly asks about:

- Single Element in Sorted Array
- unique element
- pair parity
- binary search
- LeetCode 540

Related concepts:

- Single Element in Sorted Array
- unique element
- pair parity
- binary search
- LeetCode 540
