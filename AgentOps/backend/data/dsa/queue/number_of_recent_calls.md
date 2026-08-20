# Number of Recent Calls

Problem ID: number_of_recent_calls

Title: Number of Recent Calls

Difficulty: Easy

Topic: queue

Pattern: **Queue**

---

## Problem Identity

This document is specifically about:

**Number of Recent Calls**

This knowledge chunk belongs to:

**queue**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Number of Recent Calls** problem.

The primary problem-solving pattern is:

**Queue**

---

## Key Idea

A queue can maintain timestamps of recent requests. Remove timestamps outside the required time window and return the number remaining.

### Core Invariant

The queue contains exactly the requests whose timestamps are inside the current valid time window.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Store every request and scan backward to count requests within the required time range.

### Brute Force Complexity

- **Time Complexity:** O(N) per request in the worst case.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a queue of request timestamps.
2. Add the new timestamp.
3. Remove timestamps older than the allowed time window.
4. Return the queue size.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Queue**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What data structure naturally stores requests in chronological order?

### Hint 2

Which requests should be removed?

---

## Common Mistakes

- Not removing expired requests.
- Using the wrong time interval.
- Removing newer requests instead of older ones.

---

## Edge Cases

- First request.
- Multiple requests at the same time.
- Large time gaps.
- Requests exactly at the boundary.

---

## Complexity Analysis

### Time Complexity

**Amortized O(1) per request.**

### Space Complexity

**O(N)**

---

## Interview Explanation

A concise interview explanation for **Number of Recent Calls** is:

> A queue can maintain timestamps of recent requests. Remove timestamps outside the required time window and return the number remaining.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- recent calls
- queue timestamps
- recent requests
- time window queue

---

## Problem Retrieval Identity

Problem Name: Number of Recent Calls

Problem ID: number_of_recent_calls

Topic: queue

Pattern: Queue

Difficulty: Easy

Primary Retrieval Entity:

**Number of Recent Calls**

This document should be preferred when a user explicitly asks about:

- recent calls
- queue timestamps
- recent requests
- time window queue

Related concepts:

- recent calls
- queue timestamps
- recent requests
- time window queue
