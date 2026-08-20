# Letter Combinations of a Phone Number

Problem ID: letter_combinations_of_phone_number

Title: Letter Combinations of a Phone Number

Difficulty: Medium

Topic: recursion

Pattern: **Backtracking**

---

## Problem Identity

This document is specifically about:

**Letter Combinations of a Phone Number**

This knowledge chunk belongs to:

**recursion**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Letter Combinations of a Phone Number** problem.

The primary problem-solving pattern is:

**Backtracking**

---

## Key Idea

Map each digit to its possible letters and recursively choose one letter for each digit.

### Core Invariant

At recursion depth i, the current string contains exactly one selected letter for each of the first i digits.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Generate all possible letter combinations from the digit-to-letter mappings.

### Brute Force Complexity

- **Time Complexity:** O(4^N) in the worst case.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a mapping from each digit to its corresponding letters.
2. Start recursion from the first digit.
3. Retrieve the letters associated with the current digit.
4. Try each possible letter.
5. Append the letter to the current string.
6. Recursively process the next digit.
7. Backtrack by removing the chosen letter.
8. Store the string when all digits are processed.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Backtracking**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What does each phone digit map to?

### Hint 2

At each digit, how many choices can you make?

---

## Common Mistakes

- Using the wrong digit-to-letter mapping.
- Forgetting to backtrack.
- Processing the same digit repeatedly.
- Adding incomplete strings to the result.

---

## Edge Cases

- Empty digit string.
- Single digit.
- Digits containing 7 or 9.
- Multiple digits.

---

## Complexity Analysis

### Time Complexity

**O(4^N * N) including construction of output strings.**

### Space Complexity

**O(N) recursion depth excluding output.**

---

## Interview Explanation

A concise interview explanation for **Letter Combinations of a Phone Number** is:

> Map each digit to its possible letters and recursively choose one letter for each digit.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- letter combinations
- phone number
- phone keypad
- backtracking
- recursion

---

## Problem Retrieval Identity

Problem Name: Letter Combinations of a Phone Number

Problem ID: letter_combinations_of_phone_number

Topic: recursion

Pattern: Backtracking

Difficulty: Medium

Primary Retrieval Entity:

**Letter Combinations of a Phone Number**

This document should be preferred when a user explicitly asks about:

- letter combinations
- phone number
- phone keypad
- backtracking
- recursion

Related concepts:

- letter combinations
- phone number
- phone keypad
- backtracking
- recursion
