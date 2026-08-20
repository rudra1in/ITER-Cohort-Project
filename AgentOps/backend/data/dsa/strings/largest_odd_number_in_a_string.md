# Largest Odd Number in a String

Problem ID: largest_odd_number_in_a_string

Title: Largest Odd Number in a String

Difficulty: Easy

Topic: strings

Pattern: **String Traversal + Last Odd Digit**

---

## Problem Identity

This document is specifically about:

**Largest Odd Number in a String**

This knowledge chunk belongs to:

**strings**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Largest Odd Number in a String** problem.

The primary problem-solving pattern is:

**String Traversal + Last Odd Digit**

---

## Key Idea

The largest odd substring must end at the rightmost odd digit. Once that digit is found, the prefix from the beginning through that position forms the largest possible odd number.

### Core Invariant

The rightmost odd digit gives the longest and therefore largest valid prefix that ends with an odd digit.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Generate possible substrings, check which represent odd numbers, and select the largest one.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Start from the last character of the string.
2. Check whether the current digit is odd.
3. When the first odd digit from the right is found, return the substring from index 0 through that digit.
4. If no odd digit exists, return an empty string.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**String Traversal + Last Odd Digit**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What property must the last digit of an odd number have?

### Hint 2

Why should you search for the odd digit from the right?

---

## Common Mistakes

- Searching for the first odd digit instead of the last.
- Converting a very large numeric string into an integer.
- Returning a substring ending with an even digit.

---

## Edge Cases

- All digits are even.
- Only one digit.
- The last digit is odd.
- Leading zeroes.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(N) for the returned substring.**

---

## Interview Explanation

A concise interview explanation for **Largest Odd Number in a String** is:

> The largest odd substring must end at the rightmost odd digit. Once that digit is found, the prefix from the beginning through that position forms the largest possible odd number.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Largest Odd Number
- odd number string
- last odd digit
- LeetCode 1903

---

## Problem Retrieval Identity

Problem Name: Largest Odd Number in a String

Problem ID: largest_odd_number_in_a_string

Topic: strings

Pattern: String Traversal + Last Odd Digit

Difficulty: Easy

Primary Retrieval Entity:

**Largest Odd Number in a String**

This document should be preferred when a user explicitly asks about:

- Largest Odd Number
- odd number string
- last odd digit
- LeetCode 1903

Related concepts:

- Largest Odd Number
- odd number string
- last odd digit
- LeetCode 1903
