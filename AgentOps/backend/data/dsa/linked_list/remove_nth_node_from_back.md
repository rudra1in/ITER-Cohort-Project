# Remove Nth Node from the Back of the Linked List

Problem ID: remove_nth_node_from_back

Title: Remove Nth Node from the Back of the Linked List

Difficulty: Medium

Topic: linked_list

Pattern: **Two Pointers**

---

## Problem Identity

This document is specifically about:

**Remove Nth Node from the Back of the Linked List**

This knowledge chunk belongs to:

**linked_list**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Remove Nth Node from the Back of the Linked List** problem.

The primary problem-solving pattern is:

**Two Pointers**

---

## Key Idea

Use two pointers separated by n positions. When the fast pointer reaches the end, the slow pointer is positioned immediately before the node that must be removed.

### Core Invariant

The distance between fast and slow remains n nodes, so when fast reaches the end, slow is directly before the target node.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

First calculate the length of the linked list, then calculate the position of the node from the beginning and traverse to remove it.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a dummy node before head.
2. Initialize slow and fast at the dummy node.
3. Move fast forward by n positions.
4. Move slow and fast together until fast reaches the end.
5. The node after slow is the node to remove.
6. Change slow.next to skip the target node.
7. Return dummy.next.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Two Pointers**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can two pointers maintain a fixed distance of n nodes?

### Hint 2

Which node should slow point to when fast reaches the end?

---

## Common Mistakes

- Off-by-one errors.
- Not using a dummy node when the head itself may be removed.
- Moving fast the wrong number of steps.
- Forgetting to reconnect the list.

---

## Edge Cases

- Remove the head.
- Remove the tail.
- Single-node list.
- n equals list length.
- n equals 1.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Remove Nth Node from the Back of the Linked List** is:

> Use two pointers separated by n positions. When the fast pointer reaches the end, the slow pointer is positioned immediately before the node that must be removed.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- remove nth node
- remove nth node from end
- linked list two pointers
- dummy node
- two pointer linked list

---

## Problem Retrieval Identity

Problem Name: Remove Nth Node from the Back of the Linked List

Problem ID: remove_nth_node_from_back

Topic: linked_list

Pattern: Two Pointers

Difficulty: Medium

Primary Retrieval Entity:

**Remove Nth Node from the Back of the Linked List**

This document should be preferred when a user explicitly asks about:

- remove nth node
- remove nth node from end
- linked list two pointers
- dummy node
- two pointer linked list

Related concepts:

- remove nth node
- remove nth node from end
- linked list two pointers
- dummy node
- two pointer linked list
