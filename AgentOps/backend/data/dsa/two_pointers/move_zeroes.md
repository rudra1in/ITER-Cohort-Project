# Move Zeroes

Problem ID: move_zeroes

Title: Move Zeroes

Difficulty: Easy

Topic: two_pointers

Pattern: **Slow + Fast Pointer**

---

## Problem Identity

This document is specifically about:

**Move Zeroes**

This knowledge chunk belongs to:

**two_pointers**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Move Zeroes** problem.

The primary problem-solving pattern is:

**Slow + Fast Pointer**

---

## Key Idea

Use a slow pointer to track the position where the next non-zero element should go while the fast pointer scans the array.

### Core Invariant

All positions before slow contain non-zero elements in their original relative order.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Create a separate array containing all non-zero values followed by the required number of zeroes.

### Brute Force Complexity

- **Time Complexity:** O(N) time and O(N) space.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize slow = 0.
2. Traverse the array using fast.
3. Whenever nums[fast] is non-zero, swap nums[fast] with nums[slow].
4. Increment slow.
5. Continue until the array is fully processed.
6. All zeroes will naturally move toward the end.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Slow + Fast Pointer**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can you treat zeroes as elements that should be skipped?

### Hint 2

Where should the next non-zero element be placed?

---

## Common Mistakes

- Using extra space.
- Changing the relative order of non-zero elements.
- Performing unnecessary swaps.
- Forgetting arrays should be modified in-place.

---

## Edge Cases

- No zeroes.
- All zeroes.
- Zero at the beginning.
- Zero at the end.
- Alternating zero and non-zero values.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Move Zeroes** is:

> Use a slow pointer to track the position where the next non-zero element should go while the fast pointer scans the array.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- move zeroes
- slow fast pointer
- in-place
- stable order
- two pointers

---

## Problem Retrieval Identity

Problem Name: Move Zeroes

Problem ID: move_zeroes

Topic: two_pointers

Pattern: Slow + Fast Pointer

Difficulty: Easy

Primary Retrieval Entity:

**Move Zeroes**

This document should be preferred when a user explicitly asks about:

- move zeroes
- slow fast pointer
- in-place
- stable order
- two pointers

Related concepts:

- move zeroes
- slow fast pointer
- in-place
- stable order
- two pointers
