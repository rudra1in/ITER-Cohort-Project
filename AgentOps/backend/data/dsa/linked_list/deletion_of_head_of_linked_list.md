# Deletion of the Head of Linked List

Problem ID: deletion_of_head_of_linked_list

Title: Deletion of the Head of Linked List

Difficulty: Easy

Topic: linked_list

Pattern: **Linked List Deletion**

---

## Problem Identity

This document is specifically about:

**Deletion of the Head of Linked List**

This knowledge chunk belongs to:

**linked_list**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Deletion of the Head of Linked List** problem.

The primary problem-solving pattern is:

**Linked List Deletion**

---

## Key Idea

To delete the first node, move the head reference to the second node. The old first node is then removed from the list.

### Core Invariant

After deletion, head always refers to the first remaining node of the linked list.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Check whether the list is empty. If it is not empty, move head to head.next.

### Brute Force Complexity

- **Time Complexity:** O(1)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Check whether head is null.
2. If the list is empty, return null.
3. Store or directly access head.next.
4. Update head = head.next.
5. Return the new head.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Linked List Deletion**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

If the first node is removed, which node should become the new head?

### Hint 2

What should happen when the linked list is empty?

---

## Common Mistakes

- Dereferencing head when head is null.
- Forgetting to update head.
- Trying to traverse the entire list unnecessarily.

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

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Deletion of the Head of Linked List** is:

> To delete the first node, move the head reference to the second node. The old first node is then removed from the list.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- delete head
- delete first node
- linked list deletion
- remove head

---

## Problem Retrieval Identity

Problem Name: Deletion of the Head of Linked List

Problem ID: deletion_of_head_of_linked_list

Topic: linked_list

Pattern: Linked List Deletion

Difficulty: Easy

Primary Retrieval Entity:

**Deletion of the Head of Linked List**

This document should be preferred when a user explicitly asks about:

- delete head
- delete first node
- linked list deletion
- remove head

Related concepts:

- delete head
- delete first node
- linked list deletion
- remove head
