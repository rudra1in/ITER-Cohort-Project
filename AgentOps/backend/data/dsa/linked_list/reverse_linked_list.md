# Reverse a Linked List

Problem ID: reverse_linked_list

Title: Reverse a Linked List

Difficulty: Medium

Topic: linked_list

Pattern: **Pointer Manipulation**

---

## Problem Identity

This document is specifically about:

**Reverse a Linked List**

This knowledge chunk belongs to:

**linked_list**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Reverse a Linked List** problem.

The primary problem-solving pattern is:

**Pointer Manipulation**

---

## Key Idea

Reverse every next pointer so that each node points to its previous node. Maintain previous, current, and next references to avoid losing the remaining list.

### Core Invariant

All nodes before current have already been reversed and form the reversed portion of the list.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Store the nodes or values in another structure and reconstruct the linked list in reverse order.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize prev = null.
2. Set current = head.
3. Store current.next in next.
4. Reverse the pointer using current.next = prev.
5. Move prev to current.
6. Move current to next.
7. Repeat until current becomes null.
8. Return prev as the new head.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Pointer Manipulation**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How can you reverse a next pointer without losing the rest of the list?

### Hint 2

Which three references are useful during iterative reversal?

---

## Common Mistakes

- Changing current.next before saving the original next node.
- Losing the remaining list.
- Returning the old head instead of prev.
- Incorrectly updating prev and current.

---

## Edge Cases

- Empty linked list.
- Single node.
- Two nodes.
- Long linked list.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Reverse a Linked List** is:

> Reverse every next pointer so that each node points to its previous node. Maintain previous, current, and next references to avoid losing the remaining list.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- reverse linked list
- reverse a linked list
- iterative linked list reversal
- pointer manipulation

---

## Problem Retrieval Identity

Problem Name: Reverse a Linked List

Problem ID: reverse_linked_list

Topic: linked_list

Pattern: Pointer Manipulation

Difficulty: Medium

Primary Retrieval Entity:

**Reverse a Linked List**

This document should be preferred when a user explicitly asks about:

- reverse linked list
- reverse a linked list
- iterative linked list reversal
- pointer manipulation

Related concepts:

- reverse linked list
- reverse a linked list
- iterative linked list reversal
- pointer manipulation
