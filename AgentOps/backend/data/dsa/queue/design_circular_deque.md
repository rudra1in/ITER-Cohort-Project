# Design Circular Deque

Problem ID: design_circular_deque

Title: Design Circular Deque

Difficulty: Medium

Topic: queue

Pattern: **Circular Queue**

---

## Problem Identity

This document is specifically about:

**Design Circular Deque**

This knowledge chunk belongs to:

**queue**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Design Circular Deque** problem.

The primary problem-solving pattern is:

**Circular Queue**

---

## Key Idea

A circular deque allows insertion and deletion from both the front and rear while efficiently reusing array positions through circular indexing.

### Core Invariant

The deque maintains its elements in circular order while front and rear correctly identify both ends.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use an array and shift elements whenever insertion or deletion occurs away from the end.

### Brute Force Complexity

- **Time Complexity:** O(N) for operations that require shifting.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Maintain a fixed-size circular array.
2. Track front and rear positions.
3. Insert at the front using circular decrement.
4. Insert at the rear using circular increment.
5. Delete from the front.
6. Delete from the rear.
7. Track the current number of elements.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Circular Queue**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How can both ends be updated using modulo?

### Hint 2

How can you detect whether the deque is full?

---

## Common Mistakes

- Incorrect wraparound.
- Incorrect full/empty conditions.
- Confusing front insertion with rear insertion.

---

## Edge Cases

- Empty deque.
- Full deque.
- Single element.
- Insert from both ends.
- Delete from both ends.

---

## Complexity Analysis

### Time Complexity

**O(1) per operation.**

### Space Complexity

**O(N)**

---

## Interview Explanation

A concise interview explanation for **Design Circular Deque** is:

> A circular deque allows insertion and deletion from both the front and rear while efficiently reusing array positions through circular indexing.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- circular deque
- deque
- double ended queue
- circular queue

---

## Problem Retrieval Identity

Problem Name: Design Circular Deque

Problem ID: design_circular_deque

Topic: queue

Pattern: Circular Queue

Difficulty: Medium

Primary Retrieval Entity:

**Design Circular Deque**

This document should be preferred when a user explicitly asks about:

- circular deque
- deque
- double ended queue
- circular queue

Related concepts:

- circular deque
- deque
- double ended queue
- circular queue
