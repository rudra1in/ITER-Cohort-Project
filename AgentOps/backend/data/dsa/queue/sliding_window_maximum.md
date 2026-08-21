# Sliding Window Maximum

Problem ID: sliding_window_maximum

Title: Sliding Window Maximum

Difficulty: Hard

Topic: queue

Pattern: **Monotonic Queue**

---

## Problem Identity

This document is specifically about:

**Sliding Window Maximum**

This knowledge chunk belongs to:

**queue**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Sliding Window Maximum** problem.

The primary problem-solving pattern is:

**Monotonic Queue**

---

## Key Idea

A monotonic deque maintains useful candidates for the maximum of the current sliding window while removing elements that can never become maximum.

### Core Invariant

The deque contains indices in decreasing order of their corresponding values, and its front is always the maximum of the current window.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

For every window, scan all K elements and find the maximum.

### Brute Force Complexity

- **Time Complexity:** O(NK)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Maintain a deque of indices.
2. Remove indices that are outside the current window.
3. Remove indices from the back while their values are smaller than the current value.
4. Add the current index.
5. The front of the deque represents the maximum element.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Monotonic Queue**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can you keep only candidates that may become the maximum?

### Hint 2

What should happen to smaller elements behind the current value?

---

## Common Mistakes

- Not removing expired indices.
- Maintaining increasing instead of decreasing values.
- Storing values instead of indices when window boundaries matter.

---

## Edge Cases

- Window size one.
- Window size equals array length.
- Increasing array.
- Decreasing array.
- Duplicate values.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(K)**

---

## Interview Explanation

A concise interview explanation for **Sliding Window Maximum** is:

> A monotonic deque maintains useful candidates for the maximum of the current sliding window while removing elements that can never become maximum.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- sliding window maximum
- monotonic queue
- deque
- sliding window
- maximum in window

---

## Problem Retrieval Identity

Problem Name: Sliding Window Maximum

Problem ID: sliding_window_maximum

Topic: queue

Pattern: Monotonic Queue

Difficulty: Hard

Primary Retrieval Entity:

**Sliding Window Maximum**

This document should be preferred when a user explicitly asks about:

- sliding window maximum
- monotonic queue
- deque
- sliding window
- maximum in window

Related concepts:

- sliding window maximum
- monotonic queue
- deque
- sliding window
- maximum in window
