# Circular Queue

Problem ID: circular_queue

Title: Circular Queue

Difficulty: Medium

Topic: queue

Pattern: **Circular Queue**

---

## Problem Identity

This document is specifically about:

**Circular Queue**

This knowledge chunk belongs to:

**queue**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Circular Queue** problem.

The primary problem-solving pattern is:

**Circular Queue**

---

## Key Idea

A circular queue reuses empty positions created after dequeue by wrapping the rear and front positions around the array.

### Core Invariant

Front points to the oldest element, rear identifies the next insertion position, and size represents the number of elements currently stored.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use a normal array queue and shift elements after removal to reuse space.

### Brute Force Complexity

- **Time Complexity:** O(N) for dequeue when shifting is required.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a fixed-size array.
2. Maintain front, rear, and size.
3. Insert at rear using circular indexing.
4. Remove from front using circular indexing.
5. Update front and rear using modulo.
6. Use size to distinguish full and empty states.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Circular Queue**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How can the rear wrap around to the beginning?

### Hint 2

What does modulo help you achieve?

---

## Common Mistakes

- Incorrect modulo calculation.
- Confusing full and empty conditions.
- Incorrect front/rear updates.
- Losing elements when rear wraps around.

---

## Edge Cases

- Empty queue.
- Full queue.
- Single element.
- Wraparound.
- Dequeue and then enqueue.

---

## Complexity Analysis

### Time Complexity

**O(1) for enqueue and dequeue.**

### Space Complexity

**O(N)**

---

## Interview Explanation

A concise interview explanation for **Circular Queue** is:

> A circular queue reuses empty positions created after dequeue by wrapping the rear and front positions around the array.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- circular queue
- circular array
- queue modulo
- front rear circular queue

---

## Problem Retrieval Identity

Problem Name: Circular Queue

Problem ID: circular_queue

Topic: queue

Pattern: Circular Queue

Difficulty: Medium

Primary Retrieval Entity:

**Circular Queue**

This document should be preferred when a user explicitly asks about:

- circular queue
- circular array
- queue modulo
- front rear circular queue

Related concepts:

- circular queue
- circular array
- queue modulo
- front rear circular queue
