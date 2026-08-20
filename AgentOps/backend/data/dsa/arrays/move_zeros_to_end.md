# Move Zeros to End

Problem ID: move_zeros_to_end

Title: Move Zeros to End

Difficulty: Easy

Topic: arrays

Pattern: **Two Pointers**

---

## Problem Identity

This document is specifically about:

**Move Zeros to End**

This knowledge chunk belongs to:

**arrays**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Move Zeros to End** problem.

The primary problem-solving pattern is:

**Two Pointers**

---

## Key Idea

Use a pointer to track the position where the next non-zero element should be placed. This keeps all non-zero elements in their original relative order while moving zeros to the end.

### Core Invariant

The portion before the write pointer contains all non-zero values encountered so far in their original relative order.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Create a separate array containing all non-zero values and fill the remaining positions with zeros.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Maintain a pointer for the next non-zero position.
2. Scan the array from left to right.
3. Whenever a non-zero value is found, place it at the next available position.
4. After all non-zero values are placed, fill the remaining positions with zeros.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Two Pointers**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can you separate non-zero values from zeros using a write pointer?

### Hint 2

How can you preserve the relative order of non-zero elements?

---

## Common Mistakes

- Changing the relative order of non-zero elements.
- Using unnecessary extra space.
- Forgetting to fill remaining positions with zero.

---

## Edge Cases

- All zeros.
- No zeros.
- Zeros at the beginning.
- Zeros at the end.
- Single element.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Move Zeros to End** is:

> Use a pointer to track the position where the next non-zero element should be placed. This keeps all non-zero elements in their original relative order while moving zeros to the end.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Move Zeros to End
- move zeroes
- two pointers
- stable partition
- LeetCode 283

---

## Problem Retrieval Identity

Problem Name: Move Zeros to End

Problem ID: move_zeros_to_end

Topic: arrays

Pattern: Two Pointers

Difficulty: Easy

Primary Retrieval Entity:

**Move Zeros to End**

This document should be preferred when a user explicitly asks about:

- Move Zeros to End
- move zeroes
- two pointers
- stable partition
- LeetCode 283

Related concepts:

- Move Zeros to End
- move zeroes
- two pointers
- stable partition
- LeetCode 283
