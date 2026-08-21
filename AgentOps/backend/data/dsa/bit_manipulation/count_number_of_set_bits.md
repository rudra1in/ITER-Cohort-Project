# Count the Number of Set Bits

Problem ID: count_number_of_set_bits

Title: Count the Number of Set Bits

Difficulty: Easy

Topic: bit_manipulation

Pattern: **Bit Manipulation**

---

## Problem Identity

This document is specifically about:

**Count the Number of Set Bits**

This knowledge chunk belongs to:

**bit_manipulation**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Count the Number of Set Bits** problem.

The primary problem-solving pattern is:

**Bit Manipulation**

---

## Key Idea

Count the number of 1s in the binary representation of a number. Brian Kernighan's algorithm repeatedly removes the rightmost set bit using n & (n - 1).

### Core Invariant

Every iteration removes exactly one set bit from n, so count represents the number of set bits removed so far.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Check every bit one by one using n & 1 and repeatedly right shift the number.

### Brute Force Complexity

- **Time Complexity:** O(log N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize count = 0.
2. While n is not zero, perform n = n & (n - 1).
3. Increment count after removing each set bit.
4. Return count.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Bit Manipulation**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What operation removes the rightmost set bit?

### Hint 2

How many times must n & (n - 1) be performed?

---

## Common Mistakes

- Using n & 1 without shifting.
- Forgetting to increment count.
- Using n & (n + 1) incorrectly.
- Not handling zero correctly.

---

## Edge Cases

- 0.
- 1.
- All bits are set.
- Only one bit is set.
- Large integer.

---

## Complexity Analysis

### Time Complexity

**O(K), where K is the number of set bits.**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Count the Number of Set Bits** is:

> Count the number of 1s in the binary representation of a number. Brian Kernighan's algorithm repeatedly removes the rightmost set bit using n & (n - 1).

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- count set bits
- number of 1 bits
- Brian Kernighan
- n & n-1
- popcount

---

## Problem Retrieval Identity

Problem Name: Count the Number of Set Bits

Problem ID: count_number_of_set_bits

Topic: bit_manipulation

Pattern: Bit Manipulation

Difficulty: Easy

Primary Retrieval Entity:

**Count the Number of Set Bits**

This document should be preferred when a user explicitly asks about:

- count set bits
- number of 1 bits
- Brian Kernighan
- n & n-1
- popcount

Related concepts:

- count set bits
- number of 1 bits
- Brian Kernighan
- n & n-1
- popcount
