# Search in Linked List

Problem ID: search_in_linked_list

Title: Search in Linked List

Difficulty: Easy

Topic: linked_list

Pattern: **Linked List Traversal**

---

## Problem Identity

This document is specifically about:

**Search in Linked List**

This knowledge chunk belongs to:

**linked_list**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Search in Linked List** problem.

The primary problem-solving pattern is:

**Linked List Traversal**

---

## Key Idea

Traverse the linked list from the head and compare every node's value with the target.

### Core Invariant

Every node before current has already been checked and does not contain the target.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Visit every node sequentially and compare its value with the target.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Start current at head.
2. Compare current.data with the target.
3. If they match, return true or the required position.
4. Otherwise move current to current.next.
5. Return false if the traversal reaches null.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Linked List Traversal**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can you use the normal linked-list traversal?

### Hint 2

What should you return when current becomes null?

---

## Common Mistakes

- Forgetting to move current.
- Returning true for the wrong condition.
- Dereferencing a null node.

---

## Edge Cases

- Empty linked list.
- Target at head.
- Target at tail.
- Target does not exist.
- Duplicate values.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Search in Linked List** is:

> Traverse the linked list from the head and compare every node's value with the target.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- search linked list
- find element in linked list
- linked list search
- linear search linked list

---

## Problem Retrieval Identity

Problem Name: Search in Linked List

Problem ID: search_in_linked_list

Topic: linked_list

Pattern: Linked List Traversal

Difficulty: Easy

Primary Retrieval Entity:

**Search in Linked List**

This document should be preferred when a user explicitly asks about:

- search linked list
- find element in linked list
- linked list search
- linear search linked list

Related concepts:

- search linked list
- find element in linked list
- linked list search
- linear search linked list
