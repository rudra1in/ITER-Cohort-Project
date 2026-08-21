# Search Insert Position

Problem ID: search_insert_position

Title: Search Insert Position

Difficulty: Easy

Topic: binary_search

Pattern: **Binary Search / Lower Bound**

---

## Problem Identity

This document is specifically about:

**Search Insert Position**

This knowledge chunk belongs to:

**binary_search**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Search Insert Position** problem.

The primary problem-solving pattern is:

**Binary Search / Lower Bound**

---

## Key Idea

Find the position where the target exists or where it should be inserted while keeping the sorted array order. This is equivalent to finding the lower bound of the target.

### Core Invariant

The answer remains within the current binary-search range and represents the first position where the target can be inserted without breaking sorted order.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Scan from left to right and return the first index where nums[i] is greater than or equal to the target.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Set low = 0 and high = n - 1.
2. Calculate mid.
3. If nums[mid] is greater than or equal to the target, store mid as the possible insertion position and search left.
4. Otherwise search right.
5. Return the first valid insertion position.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Binary Search / Lower Bound**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What position would the target occupy if it does not already exist?

### Hint 2

Can this problem be treated as a lower-bound problem?

---

## Common Mistakes

- Returning the nearest value instead of the insertion position.
- Forgetting that the answer can be n.
- Stopping at any equal value instead of finding the correct insertion position.

---

## Edge Cases

- Empty array.
- Target smaller than every element.
- Target greater than every element.
- Target already exists.

---

## Complexity Analysis

### Time Complexity

**O(log N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Search Insert Position** is:

> Find the position where the target exists or where it should be inserted while keeping the sorted array order. This is equivalent to finding the lower bound of the target.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Search Insert Position
- insert position
- lower bound
- binary search

---

## Problem Retrieval Identity

Problem Name: Search Insert Position

Problem ID: search_insert_position

Topic: binary_search

Pattern: Binary Search / Lower Bound

Difficulty: Easy

Primary Retrieval Entity:

**Search Insert Position**

This document should be preferred when a user explicitly asks about:

- Search Insert Position
- insert position
- lower bound
- binary search

Related concepts:

- Search Insert Position
- insert position
- lower bound
- binary search
