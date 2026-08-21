# Prefix to Infix Conversion

Problem ID: prefix_to_infix_conversion

Title: Prefix to Infix Conversion

Difficulty: Medium

Topic: stack

Pattern: **Stack Expression Conversion**

---

## Problem Identity

This document is specifically about:

**Prefix to Infix Conversion**

This knowledge chunk belongs to:

**stack**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Prefix to Infix Conversion** problem.

The primary problem-solving pattern is:

**Stack Expression Conversion**

---

## Key Idea

Scan a prefix expression from right to left. Operands are pushed onto a stack, while operators combine the top two operands into an infix expression.

### Core Invariant

Every stack element represents a valid infix expression corresponding to a processed portion of the prefix expression.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use a stack of strings and process the prefix expression from right to left.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Scan the prefix expression from right to left.
2. If the character is an operand, push it onto the stack.
3. If the character is an operator, pop two operands.
4. Combine them as left operator right.
5. Push the resulting expression back.
6. The final stack element is the infix expression.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Stack Expression Conversion**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Which direction should prefix notation be scanned?

### Hint 2

What should happen when an operator is encountered?

---

## Common Mistakes

- Scanning in the wrong direction.
- Reversing operand order.
- Popping operands in the wrong order.
- Forgetting parentheses.

---

## Edge Cases

- Single operand.
- Single operator.
- Multiple operators.
- Nested expressions.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(N)**

---

## Interview Explanation

A concise interview explanation for **Prefix to Infix Conversion** is:

> Scan a prefix expression from right to left. Operands are pushed onto a stack, while operators combine the top two operands into an infix expression.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- prefix to infix
- prefix conversion
- stack expression conversion

---

## Problem Retrieval Identity

Problem Name: Prefix to Infix Conversion

Problem ID: prefix_to_infix_conversion

Topic: stack

Pattern: Stack Expression Conversion

Difficulty: Medium

Primary Retrieval Entity:

**Prefix to Infix Conversion**

This document should be preferred when a user explicitly asks about:

- prefix to infix
- prefix conversion
- stack expression conversion

Related concepts:

- prefix to infix
- prefix conversion
- stack expression conversion
