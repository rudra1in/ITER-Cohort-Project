# First Negative Number in Every Window

Problem ID: first_negative_number_in_every_window

Title: First Negative Number in Every Window

Difficulty: Medium

Topic: queue

Pattern: **Queue + Sliding Window**

---

## Problem Identity

This document is specifically about:

**First Negative Number in Every Window**

This knowledge chunk belongs to:

**queue**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **First Negative Number in Every Window** problem.

The primary problem-solving pattern is:

**Queue + Sliding Window**

---

## Key Idea

Maintain a queue of indices of negative numbers inside the current sliding window. The front of the queue is the first negative number in that window.

### Core Invariant

The queue contains only negative-number indices that belong to the current window, in increasing index order.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

For every window of size K, scan all K elements until finding the first negative number.

### Brute Force Complexity

- **Time Complexity:** O(NK)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Maintain a queue of indices of negative numbers.
2. Expand the sliding window one element at a time.
3. Add the current index if its value is negative.
4. Remove indices that have moved outside the current window.
5. Once the window reaches size K, use the front index as the first negative number.
6. Move to the next window.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Queue + Sliding Window**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Do you need to store every element?

### Hint 2

Which elements are actually useful for answering the query?

---

## Common Mistakes

- Not removing expired indices.
- Storing positive numbers unnecessarily.
- Returning a negative number from outside the current window.
- Using O(NK) repeated scanning.

---

## Edge Cases

- No negative number in a window.
- Window size one.
- Window size equals array length.
- All numbers negative.
- All numbers positive.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(K)**

---

## Interview Explanation

A concise interview explanation for **First Negative Number in Every Window** is:

> Maintain a queue of indices of negative numbers inside the current sliding window. The front of the queue is the first negative number in that window.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- first negative number
- negative number in window
- sliding window queue
- queue indices
- first negative in every window

---

## Problem Retrieval Identity

Problem Name: First Negative Number in Every Window

Problem ID: first_negative_number_in_every_window

Topic: queue

Pattern: Queue + Sliding Window

Difficulty: Medium

Primary Retrieval Entity:

**First Negative Number in Every Window**

This document should be preferred when a user explicitly asks about:

- first negative number
- negative number in window
- sliding window queue
- queue indices
- first negative in every window

Related concepts:

- first negative number
- negative number in window
- sliding window queue
- queue indices
- first negative in every window
