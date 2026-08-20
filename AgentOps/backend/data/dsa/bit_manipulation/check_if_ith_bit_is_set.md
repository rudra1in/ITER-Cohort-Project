# Check if the i-th Bit is Set or Not

Problem ID: check_if_ith_bit_is_set

Title: Check if the i-th Bit is Set or Not

Difficulty: Easy

Topic: bit_manipulation

Pattern: **Bit Masking**

---

## Problem Identity

This document is specifically about:

**Check if the i-th Bit is Set or Not**

This knowledge chunk belongs to:

**bit_manipulation**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Check if the i-th Bit is Set or Not** problem.

The primary problem-solving pattern is:

**Bit Masking**

---

## Key Idea

To check whether the i-th bit is set, create a mask with only the i-th bit set and use bitwise AND with the number.

### Core Invariant

The mask contains exactly one set bit at position i, so AND isolates only the bit being checked.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Convert the number to binary and inspect the i-th position.

### Brute Force Complexity

- **Time Complexity:** O(log N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a mask using 1 << i.
2. Perform num & mask.
3. If the result is non-zero, the i-th bit is set.
4. Otherwise, the i-th bit is not set.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Bit Masking**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How can you create a number with only the i-th bit set?

### Hint 2

What happens when you AND the number with that mask?

---

## Common Mistakes

- Using 1 << (i - 1) when the problem uses zero-based indexing.
- Using OR instead of AND.
- Forgetting that a non-zero AND result means the bit is set.

---

## Edge Cases

- i equals 0.
- Number equals 0.
- Checking the highest relevant bit.
- Bit is set.
- Bit is not set.

---

## Complexity Analysis

### Time Complexity

**O(1)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Check if the i-th Bit is Set or Not** is:

> To check whether the i-th bit is set, create a mask with only the i-th bit set and use bitwise AND with the number.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- check ith bit
- set bit
- bit masking
- bit manipulation
- 1 << i

---

## Problem Retrieval Identity

Problem Name: Check if the i-th Bit is Set or Not

Problem ID: check_if_ith_bit_is_set

Topic: bit_manipulation

Pattern: Bit Masking

Difficulty: Easy

Primary Retrieval Entity:

**Check if the i-th Bit is Set or Not**

This document should be preferred when a user explicitly asks about:

- check ith bit
- set bit
- bit masking
- bit manipulation
- 1 << i

Related concepts:

- check ith bit
- set bit
- bit masking
- bit manipulation
- 1 << i
