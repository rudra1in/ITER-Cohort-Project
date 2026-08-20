# Single Number - I

Problem ID: single_number_i

Title: Single Number - I

Difficulty: Medium

Topic: bit_manipulation

Pattern: **XOR**

---

## Problem Identity

This document is specifically about:

**Single Number - I**

This knowledge chunk belongs to:

**bit_manipulation**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Single Number - I** problem.

The primary problem-solving pattern is:

**XOR**

---

## Key Idea

If every number appears twice except one number, XORing all elements cancels every duplicate and leaves the unique number.

### Core Invariant

After processing each element, result contains the XOR of all processed values, with duplicate pairs effectively cancelled.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use a hash map to count the frequency of every number and return the number whose frequency is one.

### Brute Force Complexity

- **Time Complexity:** O(N) time and O(N) space.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize result = 0.
2. XOR every element with result.
3. Equal numbers cancel because x ^ x = 0.
4. XOR with zero leaves the number unchanged.
5. The remaining result is the unique number.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**XOR**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What happens when a number is XORed with itself?

### Hint 2

What happens when a number is XORed with zero?

---

## Common Mistakes

- Using addition instead of XOR.
- Using a hash map unnecessarily.
- Assuming the approach works when numbers do not appear exactly twice except the unique one.

---

## Edge Cases

- Only one element.
- Negative values.
- Large values.
- Unique number appears first.
- Unique number appears last.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Single Number - I** is:

> If every number appears twice except one number, XORing all elements cancels every duplicate and leaves the unique number.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- single number
- unique element
- XOR
- duplicate cancellation
- bit manipulation

---

## Problem Retrieval Identity

Problem Name: Single Number - I

Problem ID: single_number_i

Topic: bit_manipulation

Pattern: XOR

Difficulty: Medium

Primary Retrieval Entity:

**Single Number - I**

This document should be preferred when a user explicitly asks about:

- single number
- unique element
- XOR
- duplicate cancellation
- bit manipulation

Related concepts:

- single number
- unique element
- XOR
- duplicate cancellation
- bit manipulation
