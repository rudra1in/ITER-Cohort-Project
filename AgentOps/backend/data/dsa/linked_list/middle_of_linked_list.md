# Middle of a Linked List

Problem ID: middle_of_linked_list

Title: Middle of a Linked List

Difficulty: Easy

Topic: linked_list

Pattern: **Fast and Slow Pointers**

---

## Problem Identity

This document is specifically about:

**Middle of a Linked List**

This knowledge chunk belongs to:

**linked_list**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Middle of a Linked List** problem.

The primary problem-solving pattern is:

**Fast and Slow Pointers**

---

## Key Idea

Use a slow pointer moving one step at a time and a fast pointer moving two steps at a time. When fast reaches the end, slow is at the middle.

### Core Invariant

The fast pointer moves approximately twice as quickly as the slow pointer, so when fast reaches the end, slow has reached the middle.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

First calculate the length of the linked list, then traverse again until reaching the middle position.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize slow = head.
2. Initialize fast = head.
3. Move slow one node at a time.
4. Move fast two nodes at a time.
5. When fast reaches the end, slow points to the middle.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Fast and Slow Pointers**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can two pointers moving at different speeds find the middle?

### Hint 2

What happens if one pointer moves twice as fast as the other?

---

## Common Mistakes

- Moving slow by two nodes.
- Using incorrect fast-pointer stopping conditions.
- Not considering even-length lists.

---

## Edge Cases

- Empty linked list.
- Single node.
- Two nodes.
- Even number of nodes.
- Odd number of nodes.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Middle of a Linked List** is:

> Use a slow pointer moving one step at a time and a fast pointer moving two steps at a time. When fast reaches the end, slow is at the middle.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- middle of linked list
- tortoise hare
- fast slow pointers
- linked list middle

---

## Problem Retrieval Identity

Problem Name: Middle of a Linked List

Problem ID: middle_of_linked_list

Topic: linked_list

Pattern: Fast and Slow Pointers

Difficulty: Easy

Primary Retrieval Entity:

**Middle of a Linked List**

This document should be preferred when a user explicitly asks about:

- middle of linked list
- tortoise hare
- fast slow pointers
- linked list middle

Related concepts:

- middle of linked list
- tortoise hare
- fast slow pointers
- linked list middle
