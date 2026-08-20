# Swap Two Numbers

Problem ID: swap_two_numbers_using_xor

Title: Swap Two Numbers

Difficulty: Easy

Topic: bit_manipulation

Pattern: **XOR Trick**

---

## Problem Identity

This document is specifically about:

**Swap Two Numbers**

This knowledge chunk belongs to:

**bit_manipulation**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Swap Two Numbers** problem.

The primary problem-solving pattern is:

**XOR Trick**

---

## Key Idea

Two integers can be swapped without a temporary variable using XOR because a ^ b ^ b equals a and a ^ a equals zero.

### Core Invariant

XOR is reversible because applying the same value twice cancels it: x ^ y ^ y = x.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use a temporary variable to store one number while exchanging the two values.

### Brute Force Complexity

- **Time Complexity:** O(1)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Set a = a ^ b.
2. Set b = a ^ b.
3. Set a = a ^ b.
4. The values of a and b are now swapped.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**XOR Trick**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What property does XOR have when the same number is XORed twice?

### Hint 2

Can XOR preserve enough information to recover both values?

---

## Common Mistakes

- Using the XOR swap when both variables refer to the same memory location in languages where that causes issues.
- Writing the three XOR operations incorrectly.
- Assuming XOR is always preferable to a temporary variable.

---

## Edge Cases

- Both numbers are equal.
- One number is zero.
- Negative numbers.
- Large integers.

---

## Complexity Analysis

### Time Complexity

**O(1)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Swap Two Numbers** is:

> Two integers can be swapped without a temporary variable using XOR because a ^ b ^ b equals a and a ^ a equals zero.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- swap numbers
- XOR swap
- XOR trick
- bit manipulation

---

## Problem Retrieval Identity

Problem Name: Swap Two Numbers

Problem ID: swap_two_numbers_using_xor

Topic: bit_manipulation

Pattern: XOR Trick

Difficulty: Easy

Primary Retrieval Entity:

**Swap Two Numbers**

This document should be preferred when a user explicitly asks about:

- swap numbers
- XOR swap
- XOR trick
- bit manipulation

Related concepts:

- swap numbers
- XOR swap
- XOR trick
- bit manipulation
