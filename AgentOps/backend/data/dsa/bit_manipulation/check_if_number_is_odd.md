# Check if a Number is Odd or Not

Problem ID: check_if_number_is_odd

Title: Check if a Number is Odd or Not

Difficulty: Easy

Topic: bit_manipulation

Pattern: **Bitwise AND**

---

## Problem Identity

This document is specifically about:

**Check if a Number is Odd or Not**

This knowledge chunk belongs to:

**bit_manipulation**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Check if a Number is Odd or Not** problem.

The primary problem-solving pattern is:

**Bitwise AND**

---

## Key Idea

The least significant bit determines whether an integer is odd or even. An odd number always has its least significant bit set to 1.

### Core Invariant

The least significant bit is 1 for odd numbers and 0 for even numbers.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use the modulo operator and check whether num % 2 is equal to 1.

### Brute Force Complexity

- **Time Complexity:** O(1)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Perform num & 1.
2. If the result is 1, the number is odd.
3. If the result is 0, the number is even.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Bitwise AND**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Which binary bit tells you whether a number is odd?

### Hint 2

What is the value of the least significant bit for an odd number?

---

## Common Mistakes

- Checking the wrong bit.
- Using OR instead of AND.
- Confusing the least significant bit with the most significant bit.

---

## Edge Cases

- 0.
- 1.
- Negative odd number.
- Negative even number.
- Large integer.

---

## Complexity Analysis

### Time Complexity

**O(1)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Check if a Number is Odd or Not** is:

> The least significant bit determines whether an integer is odd or even. An odd number always has its least significant bit set to 1.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- odd number
- even number
- least significant bit
- LSB
- bitwise AND

---

## Problem Retrieval Identity

Problem Name: Check if a Number is Odd or Not

Problem ID: check_if_number_is_odd

Topic: bit_manipulation

Pattern: Bitwise AND

Difficulty: Easy

Primary Retrieval Entity:

**Check if a Number is Odd or Not**

This document should be preferred when a user explicitly asks about:

- odd number
- even number
- least significant bit
- LSB
- bitwise AND

Related concepts:

- odd number
- even number
- least significant bit
- LSB
- bitwise AND
