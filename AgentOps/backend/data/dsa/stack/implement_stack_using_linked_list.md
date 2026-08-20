# Implement Stack using Linked List

Problem ID: implement_stack_using_linked_list

Title: Implement Stack using Linked List

Difficulty: Easy

Topic: stack

Pattern: **Stack Implementation**

---

## Problem Identity

This document is specifically about:

**Implement Stack using Linked List**

This knowledge chunk belongs to:

**stack**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Implement Stack using Linked List** problem.

The primary problem-solving pattern is:

**Stack Implementation**

---

## Key Idea

A linked list can implement a stack by treating the head node as the top of the stack. Insertion and deletion at the head are both constant-time operations.

### Core Invariant

The top reference always points to the most recently inserted node.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Maintain a linked list and perform push and pop operations at the head node.

### Brute Force Complexity

- **Time Complexity:** O(1) for push, pop, and peek.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a linked-list node containing data and next.
2. Maintain a top reference.
3. For push, create a node and connect it before the current top.
4. Update top to the new node.
5. For pop, move top to top.next.
6. For peek, return top.data.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Stack Implementation**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Which end of a linked list allows O(1) insertion and deletion?

### Hint 2

Can the head of the linked list represent the stack top?

---

## Common Mistakes

- Using the tail unnecessarily.
- Forgetting to update top.
- Accessing top.data when top is null.

---

## Edge Cases

- Empty stack.
- Single element.
- Multiple elements.
- Pop until empty.

---

## Complexity Analysis

### Time Complexity

**O(1) for push, pop, and peek.**

### Space Complexity

**O(N)**

---

## Interview Explanation

A concise interview explanation for **Implement Stack using Linked List** is:

> A linked list can implement a stack by treating the head node as the top of the stack. Insertion and deletion at the head are both constant-time operations.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- stack using linked list
- linked list stack
- stack implementation
- push pop linked list

---

## Problem Retrieval Identity

Problem Name: Implement Stack using Linked List

Problem ID: implement_stack_using_linked_list

Topic: stack

Pattern: Stack Implementation

Difficulty: Easy

Primary Retrieval Entity:

**Implement Stack using Linked List**

This document should be preferred when a user explicitly asks about:

- stack using linked list
- linked list stack
- stack implementation
- push pop linked list

Related concepts:

- stack using linked list
- linked list stack
- stack implementation
- push pop linked list
