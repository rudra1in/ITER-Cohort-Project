# Infix to Prefix Conversion

Problem ID: infix_to_prefix_conversion

Title: Infix to Prefix Conversion

Difficulty: Medium

Topic: stack

Pattern: **Stack Expression Conversion**

---

## Problem Identity

This document is specifically about:

**Infix to Prefix Conversion**

This knowledge chunk belongs to:

**stack**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Infix to Prefix Conversion** problem.

The primary problem-solving pattern is:

**Stack Expression Conversion**

---

## Key Idea

Convert an infix expression into prefix notation by reversing the expression, handling parentheses appropriately, and using operator precedence with a stack.

### Core Invariant

The operator stack maintains operators that cannot yet be placed into the output because of precedence or parentheses.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use operator and operand stacks while processing the infix expression according to precedence and associativity.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Reverse the infix expression.
2. Swap opening and closing parentheses.
3. Process the expression using operator precedence.
4. Use a stack for operators.
5. Build the postfix-style intermediate result.
6. Reverse the resulting expression to obtain prefix notation.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Stack Expression Conversion**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can reversing the infix expression help convert it to prefix?

### Hint 2

What happens to parentheses after reversing?

---

## Common Mistakes

- Forgetting to swap parentheses.
- Incorrect operator associativity.
- Incorrect operand order.
- Forgetting to reverse the final result.

---

## Edge Cases

- Single operand.
- Nested parentheses.
- Multiple operators.
- Different precedence levels.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(N)**

---

## Interview Explanation

A concise interview explanation for **Infix to Prefix Conversion** is:

> Convert an infix expression into prefix notation by reversing the expression, handling parentheses appropriately, and using operator precedence with a stack.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- infix to prefix
- prefix conversion
- expression conversion
- operator precedence

---

## Problem Retrieval Identity

Problem Name: Infix to Prefix Conversion

Problem ID: infix_to_prefix_conversion

Topic: stack

Pattern: Stack Expression Conversion

Difficulty: Medium

Primary Retrieval Entity:

**Infix to Prefix Conversion**

This document should be preferred when a user explicitly asks about:

- infix to prefix
- prefix conversion
- expression conversion
- operator precedence

Related concepts:

- infix to prefix
- prefix conversion
- expression conversion
- operator precedence
