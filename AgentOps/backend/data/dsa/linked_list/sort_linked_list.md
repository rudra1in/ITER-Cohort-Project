# Sort a Linked List

Problem ID: sort_linked_list

Title: Sort a Linked List

Difficulty: Medium

Topic: linked_list

Pattern: **Merge Sort on Linked List**

---

## Problem Identity

This document is specifically about:

**Sort a Linked List**

This knowledge chunk belongs to:

**linked_list**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Sort a Linked List** problem.

The primary problem-solving pattern is:

**Merge Sort on Linked List**

---

## Key Idea

Merge sort is well suited for linked lists because the list can be divided using fast and slow pointers and two sorted linked lists can be merged by changing pointers.

### Core Invariant

At every merge step, the two input lists are already sorted, allowing the smallest available node to be selected and appended to the result.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Copy all values into an array, sort the array, and then use the sorted values to rebuild or update the linked list.

### Brute Force Complexity

- **Time Complexity:** O(N log N) time and O(N) extra space
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Find the middle of the linked list using slow and fast pointers.
2. Split the list into two halves.
3. Recursively sort both halves.
4. Merge the two sorted halves.
5. Return the merged sorted list.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Merge Sort on Linked List**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Which sorting algorithm works naturally with linked lists?

### Hint 2

How can fast and slow pointers divide the list into two halves?

---

## Common Mistakes

- Incorrectly splitting the linked list.
- Creating cycles while merging.
- Forgetting the base case for recursion.
- Losing one of the two halves.
- Incorrectly connecting the remaining nodes.

---

## Edge Cases

- Empty list.
- Single node.
- Already sorted list.
- Reverse sorted list.
- Duplicate values.
- All values equal.

---

## Complexity Analysis

### Time Complexity

**O(N log N)**

### Space Complexity

**O(log N) recursion stack space.**

---

## Interview Explanation

A concise interview explanation for **Sort a Linked List** is:

> Merge sort is well suited for linked lists because the list can be divided using fast and slow pointers and two sorted linked lists can be merged by changing pointers.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- sort linked list
- merge sort linked list
- linked list sorting
- merge two sorted lists
- divide and conquer

---

## Problem Retrieval Identity

Problem Name: Sort a Linked List

Problem ID: sort_linked_list

Topic: linked_list

Pattern: Merge Sort on Linked List

Difficulty: Medium

Primary Retrieval Entity:

**Sort a Linked List**

This document should be preferred when a user explicitly asks about:

- sort linked list
- merge sort linked list
- linked list sorting
- merge two sorted lists
- divide and conquer

Related concepts:

- sort linked list
- merge sort linked list
- linked list sorting
- merge two sorted lists
- divide and conquer
