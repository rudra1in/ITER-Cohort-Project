# String to Integer (atoi)

Problem ID: string_to_integer_atoi

Title: String to Integer (atoi)

Difficulty: Medium

Topic: strings

Pattern: **String Parsing**

---

## Problem Identity

This document is specifically about:

**String to Integer (atoi)**

This knowledge chunk belongs to:

**strings**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **String to Integer (atoi)** problem.

The primary problem-solving pattern is:

**String Parsing**

---

## Key Idea

Parse the string carefully by skipping leading spaces, identifying the sign, reading consecutive digits, and preventing integer overflow.

### Core Invariant

After processing each digit, the accumulated result represents exactly the numeric prefix read so far while remaining within the allowed integer range.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Parse the characters manually and build the integer while checking the sign and numeric range.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Skip leading whitespace.
2. Check whether the next character is '+' or '-'.
3. Read consecutive numeric digits.
4. Build the result digit by digit.
5. Before adding a digit, check whether the next operation would overflow the integer range.
6. Clamp the result to the appropriate integer limit if overflow occurs.
7. Return the final integer.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**String Parsing**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What parts of the input should be processed before reading digits?

### Hint 2

How can you detect overflow before it happens?

---

## Common Mistakes

- Ignoring leading spaces.
- Allowing multiple signs.
- Continuing after a non-digit character.
- Not handling integer overflow.
- Incorrectly applying the negative sign.

---

## Edge Cases

- Leading whitespace.
- Positive sign.
- Negative sign.
- No digits.
- Integer overflow.
- Trailing characters.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **String to Integer (atoi)** is:

> Parse the string carefully by skipping leading spaces, identifying the sign, reading consecutive digits, and preventing integer overflow.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- String to Integer
- atoi
- string parsing
- overflow
- LeetCode 8

---

## Problem Retrieval Identity

Problem Name: String to Integer (atoi)

Problem ID: string_to_integer_atoi

Topic: strings

Pattern: String Parsing

Difficulty: Medium

Primary Retrieval Entity:

**String to Integer (atoi)**

This document should be preferred when a user explicitly asks about:

- String to Integer
- atoi
- string parsing
- overflow
- LeetCode 8

Related concepts:

- String to Integer
- atoi
- string parsing
- overflow
- LeetCode 8
