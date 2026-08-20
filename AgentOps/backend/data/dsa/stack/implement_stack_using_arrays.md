# Implement Stack using Arrays

Problem ID: implement_stack_using_arrays

Title: Implement Stack using Arrays

Difficulty: Easy

Topic: stack

Pattern: **Stack Implementation**

---

## Problem Identity

This document is specifically about:

**Implement Stack using Arrays**

This knowledge chunk belongs to:

**stack**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Implement Stack using Arrays** problem.

The primary problem-solving pattern is:

**Stack Implementation**

---

## Key Idea

A stack follows the Last In First Out (LIFO) principle. An array can implement a stack by maintaining a top index that points to the most recently inserted element.

### Core Invariant

The top index always points to the current top element of the stack, and elements below it remain in LIFO order.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use an array and maintain the top position. Push adds an element at the top, pop removes the top element, and peek returns the top element without removing it.

### Brute Force Complexity

- **Time Complexity:** O(1) for push, pop, and peek
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create an array to store stack elements.
2. Maintain a top index initialized appropriately.
3. For push, increment top and insert the element.
4. For pop, return the element at top and decrement top.
5. For peek, return the element at top without removing it.
6. Check whether the stack is empty before pop or peek.
7. Check capacity if implementing a fixed-size stack.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Stack Implementation**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What property does a stack follow?

### Hint 2

Which index should represent the top of the stack?

---

## Common Mistakes

- Using the wrong initial value for top.
- Incrementing or decrementing top at the wrong time.
- Popping from an empty stack.
- Ignoring stack overflow in a fixed-size implementation.

---

## Edge Cases

- Empty stack.
- Single element.
- Multiple push operations.
- Multiple pop operations.
- Stack overflow.
- Stack underflow.

---

## Complexity Analysis

### Time Complexity

**O(1) per push, pop, and peek operation**

### Space Complexity

**O(N) for storing N stack elements.**

---

## Interview Explanation

A concise interview explanation for **Implement Stack using Arrays** is:

> A stack follows the Last In First Out (LIFO) principle. An array can implement a stack by maintaining a top index that points to the most recently inserted element.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- implement stack
- stack using array
- array stack
- LIFO
- push
- pop
- peek

---

## Problem Retrieval Identity

Problem Name: Implement Stack using Arrays

Problem ID: implement_stack_using_arrays

Topic: stack

Pattern: Stack Implementation

Difficulty: Easy

Primary Retrieval Entity:

**Implement Stack using Arrays**

This document should be preferred when a user explicitly asks about:

- implement stack
- stack using array
- array stack
- LIFO
- push
- pop
- peek

Related concepts:

- implement stack
- stack using array
- array stack
- LIFO
- push
- pop
- peek
