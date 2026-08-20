# Check if a Number is Power of 2

Problem ID: check_if_number_is_power_of_two

Title: Check if a Number is Power of 2

Difficulty: Easy

Topic: bit_manipulation

Pattern: **Bit Trick**

---

## Problem Identity

This document is specifically about:

**Check if a Number is Power of 2**

This knowledge chunk belongs to:

**bit_manipulation**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Check if a Number is Power of 2** problem.

The primary problem-solving pattern is:

**Bit Trick**

---

## Key Idea

A positive power of two has exactly one set bit. For such a number n, n & (n - 1) equals 0.

### Core Invariant

For a positive power of two, exactly one bit is set; subtracting one clears that bit and sets all lower bits, making the AND result zero.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Repeatedly divide the number by 2 and check whether it can be reduced to 1 without a remainder.

### Brute Force Complexity

- **Time Complexity:** O(log N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Check that n is greater than 0.
2. Calculate n & (n - 1).
3. If the result is 0, n is a power of two.
4. Otherwise, n is not a power of two.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Bit Trick**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How many set bits does a power of two have?

### Hint 2

What happens to the binary representation when you subtract 1?

---

## Common Mistakes

- Forgetting that 0 is not a power of two.
- Not checking that n is positive.
- Confusing n & (n - 1) with n & (n + 1).

---

## Edge Cases

- 0.
- 1.
- 2.
- Large power of two.
- Negative number.
- Number just above or below a power of two.

---

## Complexity Analysis

### Time Complexity

**O(1)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Check if a Number is Power of 2** is:

> A positive power of two has exactly one set bit. For such a number n, n & (n - 1) equals 0.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- power of two
- n & n-1
- bit trick
- set bits
- bit manipulation

---

## Problem Retrieval Identity

Problem Name: Check if a Number is Power of 2

Problem ID: check_if_number_is_power_of_two

Topic: bit_manipulation

Pattern: Bit Trick

Difficulty: Easy

Primary Retrieval Entity:

**Check if a Number is Power of 2**

This document should be preferred when a user explicitly asks about:

- power of two
- n & n-1
- bit trick
- set bits
- bit manipulation

Related concepts:

- power of two
- n & n-1
- bit trick
- set bits
- bit manipulation
