# Balanced Parentheses

Problem ID: balanced_parentheses

Title: Balanced Parentheses

Difficulty: Easy

Topic: stack

Pattern: **Stack**

---

## Problem Identity

This document is specifically about:

**Balanced Parentheses**

This knowledge chunk belongs to:

**stack**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Balanced Parentheses** problem.

The primary problem-solving pattern is:

**Stack**

---

## Key Idea

A stack can match every closing bracket with the most recently encountered unmatched opening bracket.

### Core Invariant

The stack contains exactly the unmatched opening brackets encountered so far, with the most recent one at the top.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Scan the string and use a stack to store opening brackets. Whenever a closing bracket appears, check whether it matches the stack top.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create an empty stack.
2. For every character, push opening brackets.
3. For a closing bracket, check whether the stack is empty.
4. Check whether the top opening bracket matches the closing bracket.
5. Pop the matching opening bracket.
6. After processing the string, the stack must be empty.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Stack**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Which data structure naturally handles the most recently opened bracket?

### Hint 2

What should happen when a closing bracket does not match the stack top?

---

## Common Mistakes

- Ignoring an empty stack before accessing its top.
- Matching the wrong bracket types.
- Forgetting to pop after a successful match.
- Returning true without checking whether the stack is empty.

---

## Edge Cases

- Empty string.
- Only opening brackets.
- Only closing brackets.
- Nested brackets.
- Multiple bracket types.
- Mismatched brackets.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(N)**

---

## Interview Explanation

A concise interview explanation for **Balanced Parentheses** is:

> A stack can match every closing bracket with the most recently encountered unmatched opening bracket.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- balanced parentheses
- valid parentheses
- balanced brackets
- stack parentheses
- valid brackets

---

## Problem Retrieval Identity

Problem Name: Balanced Parentheses

Problem ID: balanced_parentheses

Topic: stack

Pattern: Stack

Difficulty: Easy

Primary Retrieval Entity:

**Balanced Parentheses**

This document should be preferred when a user explicitly asks about:

- balanced parentheses
- valid parentheses
- balanced brackets
- stack parentheses
- valid brackets

Related concepts:

- balanced parentheses
- valid parentheses
- balanced brackets
- stack parentheses
- valid brackets
