# Merge Sorted Array

Problem ID: merge_sorted_array

Title: Merge Sorted Array

Difficulty: Easy

Topic: two_pointers

Pattern: **Two Pointers from End**

---

## Problem Identity

This document is specifically about:

**Merge Sorted Array**

This knowledge chunk belongs to:

**two_pointers**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Merge Sorted Array** problem.

The primary problem-solving pattern is:

**Two Pointers from End**

---

## Key Idea

Merge two sorted arrays into the first array by comparing elements from the end, placing the largest remaining element at the end of the available space.

### Core Invariant

The positions after k contain the largest elements from both arrays in sorted order.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Copy all elements into a separate array, sort the combined array, and place the result back.

### Brute Force Complexity

- **Time Complexity:** O((M + N) log(M + N))
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Set i = m - 1 for the last valid element of nums1.
2. Set j = n - 1 for the last element of nums2.
3. Set k = m + n - 1 for the last position in nums1.
4. Compare nums1[i] and nums2[j].
5. Place the larger value at nums1[k].
6. Move the corresponding pointer backward.
7. Continue until nums2 is completely merged.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Two Pointers from End**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Why is it safer to merge from the end?

### Hint 2

Which element should occupy the last available position?

---

## Common Mistakes

- Merging from the beginning and overwriting values.
- Forgetting that m represents valid elements in nums1.
- Not copying remaining elements from nums2.
- Using unnecessary extra space.

---

## Edge Cases

- nums1 has no valid elements.
- nums2 is empty.
- All nums1 values are smaller.
- All nums2 values are smaller.
- Duplicate values.

---

## Complexity Analysis

### Time Complexity

**O(M + N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Merge Sorted Array** is:

> Merge two sorted arrays into the first array by comparing elements from the end, placing the largest remaining element at the end of the available space.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- merge sorted array
- two pointers
- merge
- sorted arrays
- pointer from end

---

## Problem Retrieval Identity

Problem Name: Merge Sorted Array

Problem ID: merge_sorted_array

Topic: two_pointers

Pattern: Two Pointers from End

Difficulty: Easy

Primary Retrieval Entity:

**Merge Sorted Array**

This document should be preferred when a user explicitly asks about:

- merge sorted array
- two pointers
- merge
- sorted arrays
- pointer from end

Related concepts:

- merge sorted array
- two pointers
- merge
- sorted arrays
- pointer from end
