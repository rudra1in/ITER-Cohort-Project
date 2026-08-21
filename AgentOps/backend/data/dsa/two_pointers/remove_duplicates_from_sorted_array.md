# Remove Duplicates from Sorted Array

Problem ID: remove_duplicates_from_sorted_array

Title: Remove Duplicates from Sorted Array

Difficulty: Easy

Topic: two_pointers

Pattern: **Slow + Fast Pointer**

---

## Problem Identity

This document is specifically about:

**Remove Duplicates from Sorted Array**

This knowledge chunk belongs to:

**two_pointers**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Remove Duplicates from Sorted Array** problem.

The primary problem-solving pattern is:

**Slow + Fast Pointer**

---

## Key Idea

Use a slow pointer to represent the position where the next unique element should be written and a fast pointer to scan the array.

### Core Invariant

The portion from index 0 through slow contains only unique elements in sorted order.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use an additional data structure such as a set to store unique elements and then copy them back into the array.

### Brute Force Complexity

- **Time Complexity:** O(N) time and O(N) space.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. If the array is empty, return 0.
2. Initialize slow = 0.
3. Start fast from index 1.
4. If nums[fast] differs from nums[slow], increment slow.
5. Copy nums[fast] to nums[slow].
6. Continue until fast reaches the end.
7. Return slow + 1.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Slow + Fast Pointer**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Because the array is sorted, where will duplicate values appear?

### Hint 2

Which pointer should scan the array?

---

## Common Mistakes

- Using extra space unnecessarily.
- Incrementing slow at the wrong time.
- Returning slow instead of slow + 1.
- Not handling an empty array.

---

## Edge Cases

- Empty array.
- One element.
- All elements are duplicates.
- No duplicates.
- Many repeated values.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Remove Duplicates from Sorted Array** is:

> Use a slow pointer to represent the position where the next unique element should be written and a fast pointer to scan the array.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- remove duplicates
- sorted array
- slow fast pointer
- in-place
- two pointers

---

## Problem Retrieval Identity

Problem Name: Remove Duplicates from Sorted Array

Problem ID: remove_duplicates_from_sorted_array

Topic: two_pointers

Pattern: Slow + Fast Pointer

Difficulty: Easy

Primary Retrieval Entity:

**Remove Duplicates from Sorted Array**

This document should be preferred when a user explicitly asks about:

- remove duplicates
- sorted array
- slow fast pointer
- in-place
- two pointers

Related concepts:

- remove duplicates
- sorted array
- slow fast pointer
- in-place
- two pointers
