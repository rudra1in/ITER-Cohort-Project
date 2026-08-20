# Valid Palindrome

Problem ID: valid_palindrome

Title: Valid Palindrome

Difficulty: Easy

Topic: two_pointers

Pattern: **Left + Right Pointer**

---

## Problem Identity

This document is specifically about:

**Valid Palindrome**

This knowledge chunk belongs to:

**two_pointers**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Valid Palindrome** problem.

The primary problem-solving pattern is:

**Left + Right Pointer**

---

## Key Idea

Compare characters from both ends of the string using left and right pointers while ignoring non-alphanumeric characters and case when required.

### Core Invariant

All characters outside the current left-right range have already been verified as matching palindrome pairs.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Create a cleaned and reversed version of the string and compare it with the original cleaned string.

### Brute Force Complexity

- **Time Complexity:** O(N) time and O(N) space.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize left = 0 and right = n - 1.
2. Skip characters from the left that are not alphanumeric.
3. Skip characters from the right that are not alphanumeric.
4. Compare the lowercase versions of the two characters.
5. If they differ, return false.
6. Move both pointers toward the center.
7. Return true when the pointers cross.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Left + Right Pointer**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Do you need to create a reversed string?

### Hint 2

What should happen to spaces and punctuation?

---

## Common Mistakes

- Not ignoring punctuation.
- Not ignoring spaces.
- Forgetting case-insensitive comparison.
- Moving pointers incorrectly after skipping characters.

---

## Edge Cases

- Empty string.
- Single character.
- Only punctuation.
- Mixed uppercase and lowercase characters.
- String containing spaces.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Valid Palindrome** is:

> Compare characters from both ends of the string using left and right pointers while ignoring non-alphanumeric characters and case when required.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- palindrome
- left right pointer
- two pointers
- string
- character comparison

---

## Problem Retrieval Identity

Problem Name: Valid Palindrome

Problem ID: valid_palindrome

Topic: two_pointers

Pattern: Left + Right Pointer

Difficulty: Easy

Primary Retrieval Entity:

**Valid Palindrome**

This document should be preferred when a user explicitly asks about:

- palindrome
- left right pointer
- two pointers
- string
- character comparison

Related concepts:

- palindrome
- left right pointer
- two pointers
- string
- character comparison
