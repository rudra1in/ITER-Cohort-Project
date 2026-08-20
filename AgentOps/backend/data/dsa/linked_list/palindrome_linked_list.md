# Check if Linked List is Palindrome

Problem ID: palindrome_linked_list

Title: Check if Linked List is Palindrome

Difficulty: Medium

Topic: linked_list

Pattern: **Fast Slow + Reverse**

---

## Problem Identity

This document is specifically about:

**Check if Linked List is Palindrome**

This knowledge chunk belongs to:

**linked_list**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Check if Linked List is Palindrome** problem.

The primary problem-solving pattern is:

**Fast Slow + Reverse**

---

## Key Idea

Find the middle of the list, reverse the second half, and compare the first half with the reversed second half.

### Core Invariant

During comparison, every pair of nodes examined so far has equal values from opposite sides of the original list.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Copy all node values into an array and compare the array from both ends.

### Brute Force Complexity

- **Time Complexity:** O(N) time and O(N) space
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Find the middle using slow and fast pointers.
2. Reverse the second half of the linked list.
3. Compare nodes from the first half and reversed second half.
4. If all corresponding values match, the list is a palindrome.
5. Optionally restore the second half if required.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Fast Slow + Reverse**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can you compare the two halves after reversing one of them?

### Hint 2

How can fast and slow pointers help divide the list?

---

## Common Mistakes

- Finding the wrong middle.
- Comparing the wrong nodes.
- Forgetting to reverse the second half.
- Using unnecessary O(N) extra space.

---

## Edge Cases

- Empty list.
- Single node.
- Two nodes.
- Odd number of nodes.
- Even number of nodes.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Check if Linked List is Palindrome** is:

> Find the middle of the list, reverse the second half, and compare the first half with the reversed second half.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- palindrome linked list
- linked list palindrome
- reverse second half
- fast slow pointers

---

## Problem Retrieval Identity

Problem Name: Check if Linked List is Palindrome

Problem ID: palindrome_linked_list

Topic: linked_list

Pattern: Fast Slow + Reverse

Difficulty: Medium

Primary Retrieval Entity:

**Check if Linked List is Palindrome**

This document should be preferred when a user explicitly asks about:

- palindrome linked list
- linked list palindrome
- reverse second half
- fast slow pointers

Related concepts:

- palindrome linked list
- linked list palindrome
- reverse second half
- fast slow pointers
