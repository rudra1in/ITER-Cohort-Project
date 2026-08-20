# Insertion at the Head of Linked List

Problem ID: insertion_at_head_of_linked_list

Title: Insertion at the Head of Linked List

Difficulty: Easy

Topic: linked_list

Pattern: **Linked List Insertion**

---

## Problem Identity

This document is specifically about:

**Insertion at the Head of Linked List**

This knowledge chunk belongs to:

**linked_list**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Insertion at the Head of Linked List** problem.

The primary problem-solving pattern is:

**Linked List Insertion**

---

## Key Idea

To insert a node at the beginning, make the new node point to the current head and then update head to the new node.

### Core Invariant

After insertion, the new node becomes the first node and the complete previous list remains connected through newNode.next.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

For insertion at the head, no traversal is actually required. Create a node, connect it to the current head, and update the head.

### Brute Force Complexity

- **Time Complexity:** O(1)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a new node.
2. Set newNode.next = head.
3. Update head = newNode.
4. Return the updated head.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Linked List Insertion**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Where should the new node point before changing head?

### Hint 2

Which reference must be updated after connecting the new node?

---

## Common Mistakes

- Changing head before connecting the new node.
- Losing the original linked list.
- Forgetting to set newNode.next.

---

## Edge Cases

- Empty linked list.
- Single-node linked list.
- Multiple-node linked list.

---

## Complexity Analysis

### Time Complexity

**O(1)**

### Space Complexity

**O(1) auxiliary space excluding the newly created node.**

---

## Interview Explanation

A concise interview explanation for **Insertion at the Head of Linked List** is:

> To insert a node at the beginning, make the new node point to the current head and then update head to the new node.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- insert at head
- insertion at head
- linked list insertion
- add node at beginning

---

## Problem Retrieval Identity

Problem Name: Insertion at the Head of Linked List

Problem ID: insertion_at_head_of_linked_list

Topic: linked_list

Pattern: Linked List Insertion

Difficulty: Easy

Primary Retrieval Entity:

**Insertion at the Head of Linked List**

This document should be preferred when a user explicitly asks about:

- insert at head
- insertion at head
- linked list insertion
- add node at beginning

Related concepts:

- insert at head
- insertion at head
- linked list insertion
- add node at beginning
