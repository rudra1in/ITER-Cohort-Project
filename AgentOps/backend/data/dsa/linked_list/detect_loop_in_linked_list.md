# Detect a Loop in Linked List

Problem ID: detect_loop_in_linked_list

Title: Detect a Loop in Linked List

Difficulty: Medium

Topic: linked_list

Pattern: **Fast and Slow Pointers**

---

## Problem Identity

This document is specifically about:

**Detect a Loop in Linked List**

This knowledge chunk belongs to:

**linked_list**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Detect a Loop in Linked List** problem.

The primary problem-solving pattern is:

**Fast and Slow Pointers**

---

## Key Idea

Use slow and fast pointers. If a cycle exists, the fast pointer will eventually meet the slow pointer.

### Core Invariant

If a cycle exists, the faster pointer repeatedly gains distance on the slower pointer inside the cycle and eventually meets it.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Store every visited node in a hash set. If a node is encountered again, a cycle exists.

### Brute Force Complexity

- **Time Complexity:** O(N) time and O(N) space
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize slow = head.
2. Initialize fast = head.
3. Move slow by one node.
4. Move fast by two nodes.
5. If slow and fast meet, a cycle exists.
6. If fast or fast.next becomes null, no cycle exists.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Fast and Slow Pointers**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What happens if two pointers move at different speeds inside a cycle?

### Hint 2

Can you detect a cycle without storing every visited node?

---

## Common Mistakes

- Accessing fast.next when fast is null.
- Incorrect loop condition.
- Using extra space unnecessarily.
- Checking only whether fast becomes null without checking whether the pointers meet.

---

## Edge Cases

- Empty linked list.
- Single node without cycle.
- Single node pointing to itself.
- Cycle starting at head.
- Cycle starting in the middle.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Detect a Loop in Linked List** is:

> Use slow and fast pointers. If a cycle exists, the fast pointer will eventually meet the slow pointer.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- detect cycle
- detect loop
- linked list cycle
- floyd cycle detection
- fast slow pointers

---

## Problem Retrieval Identity

Problem Name: Detect a Loop in Linked List

Problem ID: detect_loop_in_linked_list

Topic: linked_list

Pattern: Fast and Slow Pointers

Difficulty: Medium

Primary Retrieval Entity:

**Detect a Loop in Linked List**

This document should be preferred when a user explicitly asks about:

- detect cycle
- detect loop
- linked list cycle
- floyd cycle detection
- fast slow pointers

Related concepts:

- detect cycle
- detect loop
- linked list cycle
- floyd cycle detection
- fast slow pointers
