# Find Missing Number

Problem ID: find_missing_number

Title: Find Missing Number

Difficulty: Easy

Topic: arrays

Pattern: **XOR / Mathematical Sum**

---

## Problem Identity

This document is specifically about:

**Find Missing Number**

This knowledge chunk belongs to:

**arrays**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Find Missing Number** problem.

The primary problem-solving pattern is:

**XOR / Mathematical Sum**

---

## Key Idea

The array contains numbers from 0 to n with one missing. XOR can be used because equal numbers cancel each other, leaving exactly the missing number.

### Core Invariant

After XORing the corresponding values from the expected range and the array, every present value cancels with its duplicate.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Calculate the expected sum from 0 to n and subtract the sum of the array.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize xor with n or zero depending on the implementation.
2. XOR all array values.
3. XOR all numbers from 0 through n.
4. Equal numbers cancel because x XOR x is zero.
5. The remaining value is the missing number.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**XOR / Mathematical Sum**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What operation makes equal numbers cancel each other?

### Hint 2

Can you combine the array values with the complete range from 0 to n?

---

## Common Mistakes

- Using an incorrect range.
- Forgetting that zero is part of the range.
- Using a data structure unnecessarily.

---

## Edge Cases

- Missing zero.
- Missing n.
- Single-element array.
- Missing number from the middle.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Find Missing Number** is:

> The array contains numbers from 0 to n with one missing. XOR can be used because equal numbers cancel each other, leaving exactly the missing number.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Find Missing Number
- missing number
- XOR
- LeetCode 268
- 0 to n

---

## Problem Retrieval Identity

Problem Name: Find Missing Number

Problem ID: find_missing_number

Topic: arrays

Pattern: XOR / Mathematical Sum

Difficulty: Easy

Primary Retrieval Entity:

**Find Missing Number**

This document should be preferred when a user explicitly asks about:

- Find Missing Number
- missing number
- XOR
- LeetCode 268
- 0 to n

Related concepts:

- Find Missing Number
- missing number
- XOR
- LeetCode 268
- 0 to n
