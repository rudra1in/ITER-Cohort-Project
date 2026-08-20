# Find the Starting Point of a Loop in Linked List

Problem ID: find_starting_point_of_loop

Title: Find the Starting Point of a Loop in Linked List

Difficulty: Medium

Topic: linked_list

Pattern: **Floyd Cycle Detection**

---

## Problem Identity

This document is specifically about:

**Find the Starting Point of a Loop in Linked List**

This knowledge chunk belongs to:

**linked_list**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Find the Starting Point of a Loop in Linked List** problem.

The primary problem-solving pattern is:

**Floyd Cycle Detection**

---

## Key Idea

After slow and fast pointers meet inside a cycle, move one pointer back to head. Move both pointers one step at a time. Their next meeting point is the start of the cycle.

### Core Invariant

After the first meeting inside the cycle, resetting one pointer to head makes the distance to the cycle entry equal for both pointers under Floyd's cycle property.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Store visited nodes in a hash set and return the first node that appears more than once.

### Brute Force Complexity

- **Time Complexity:** O(N) time and O(N) space
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Use slow and fast pointers to detect a cycle.
2. Move slow one step and fast two steps until they meet.
3. If they never meet, there is no cycle.
4. Move one pointer back to head.
5. Move both pointers one step at a time.
6. The node where they meet is the cycle starting point.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Floyd Cycle Detection**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Once you know a cycle exists, can you find where the cycle begins?

### Hint 2

What happens if one pointer is moved back to head after the first meeting?

---

## Common Mistakes

- Returning the first meeting point as the cycle start.
- Forgetting to reset one pointer to head.
- Using the wrong pointer movement after the first meeting.

---

## Edge Cases

- No cycle.
- Cycle begins at head.
- Cycle begins near the tail.
- Single-node self-cycle.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Find the Starting Point of a Loop in Linked List** is:

> After slow and fast pointers meet inside a cycle, move one pointer back to head. Move both pointers one step at a time. Their next meeting point is the start of the cycle.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- starting point of loop
- cycle entry
- linked list cycle II
- floyd cycle
- cycle detection

---

## Problem Retrieval Identity

Problem Name: Find the Starting Point of a Loop in Linked List

Problem ID: find_starting_point_of_loop

Topic: linked_list

Pattern: Floyd Cycle Detection

Difficulty: Medium

Primary Retrieval Entity:

**Find the Starting Point of a Loop in Linked List**

This document should be preferred when a user explicitly asks about:

- starting point of loop
- cycle entry
- linked list cycle II
- floyd cycle
- cycle detection

Related concepts:

- starting point of loop
- cycle entry
- linked list cycle II
- floyd cycle
- cycle detection
