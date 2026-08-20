# Generate Parentheses

Problem ID: generate_parentheses

Title: Generate Parentheses

Difficulty: Medium

Topic: recursion

Pattern: **Backtracking + Valid State**

---

## Problem Identity

This document is specifically about:

**Generate Parentheses**

This knowledge chunk belongs to:

**recursion**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Generate Parentheses** problem.

The primary problem-solving pattern is:

**Backtracking + Valid State**

---

## Key Idea

Build the parentheses string recursively while maintaining the number of opening and closing brackets used. A closing bracket can only be added when there are more opening brackets already placed than closing brackets.

### Core Invariant

At every recursive step, the partial parentheses string remains valid: closing brackets never exceed opening brackets.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Generate all possible strings containing 2N parentheses and keep only those that form valid parentheses sequences.

### Brute Force Complexity

- **Time Complexity:** O(2^(2N)) candidates before validation.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Start with an empty string.
2. Track the number of opening brackets used.
3. Track the number of closing brackets used.
4. Add an opening bracket if the number of opening brackets is less than n.
5. Add a closing bracket only when closing brackets are fewer than opening brackets.
6. Continue recursively until 2n characters are created.
7. Add the completed valid string to the result.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Backtracking + Valid State**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

When is it safe to add an opening parenthesis?

### Hint 2

When is it safe to add a closing parenthesis?

---

## Common Mistakes

- Allowing more closing brackets than opening brackets.
- Using exactly n opening and n closing brackets incorrectly.
- Adding a result before the string is complete.
- Forgetting to backtrack.

---

## Edge Cases

- n = 0.
- n = 1.
- n = 2.
- Larger values of n.

---

## Complexity Analysis

### Time Complexity

**O(Cn * N), where Cn is the nth Catalan number.**

### Space Complexity

**O(N) recursion depth excluding the output.**

---

## Interview Explanation

A concise interview explanation for **Generate Parentheses** is:

> Build the parentheses string recursively while maintaining the number of opening and closing brackets used. A closing bracket can only be added when there are more opening brackets already placed than closing brackets.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- generate parentheses
- valid parentheses
- backtracking
- recursion
- Catalan

---

## Problem Retrieval Identity

Problem Name: Generate Parentheses

Problem ID: generate_parentheses

Topic: recursion

Pattern: Backtracking + Valid State

Difficulty: Medium

Primary Retrieval Entity:

**Generate Parentheses**

This document should be preferred when a user explicitly asks about:

- generate parentheses
- valid parentheses
- backtracking
- recursion
- Catalan

Related concepts:

- generate parentheses
- valid parentheses
- backtracking
- recursion
- Catalan
