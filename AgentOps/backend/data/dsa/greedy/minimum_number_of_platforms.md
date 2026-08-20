# Minimum Number of Platforms Required for a Railway

Problem ID: minimum_number_of_platforms

Title: Minimum Number of Platforms Required for a Railway

Difficulty: Medium

Topic: greedy

Pattern: **Greedy + Two Pointers**

---

## Problem Identity

This document is specifically about:

**Minimum Number of Platforms Required for a Railway**

This knowledge chunk belongs to:

**greedy**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Minimum Number of Platforms Required for a Railway** problem.

The primary problem-solving pattern is:

**Greedy + Two Pointers**

---

## Key Idea

Sort arrival and departure times separately. Use two pointers to determine when trains arrive before existing trains depart, increasing the required platforms, and when departures occur, freeing a platform.

### Core Invariant

The current platform count represents the number of trains simultaneously occupying platforms among the events processed so far.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

For every train, compare its interval with all other train intervals to determine the maximum number of overlapping trains.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Sort all arrival times.
2. Sort all departure times.
3. Initialize arrival and departure pointers.
4. If the next train arrives before the earliest departure, increase the platform count.
5. Otherwise decrease the current platform count when a train departs.
6. Track the maximum number of platforms required.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Greedy + Two Pointers**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What happens when an arrival occurs before the next departure?

### Hint 2

Can sorting arrivals and departures separately simplify the problem?

---

## Common Mistakes

- Not sorting arrival and departure times.
- Using the wrong comparison for equal arrival and departure times.
- Tracking only total trains instead of simultaneous trains.
- Forgetting to decrease the platform count after departure.

---

## Edge Cases

- One train.
- All trains arrive before any departure.
- No overlapping trains.
- Equal arrival and departure times.
- Multiple trains at the same time.

---

## Complexity Analysis

### Time Complexity

**O(N log N)**

### Space Complexity

**O(N) for the sorted time arrays.**

---

## Interview Explanation

A concise interview explanation for **Minimum Number of Platforms Required for a Railway** is:

> Sort arrival and departure times separately. Use two pointers to determine when trains arrive before existing trains depart, increasing the required platforms, and when departures occur, freeing a platform.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- minimum platforms
- railway platforms
- train scheduling
- greedy intervals
- two pointers

---

## Problem Retrieval Identity

Problem Name: Minimum Number of Platforms Required for a Railway

Problem ID: minimum_number_of_platforms

Topic: greedy

Pattern: Greedy + Two Pointers

Difficulty: Medium

Primary Retrieval Entity:

**Minimum Number of Platforms Required for a Railway**

This document should be preferred when a user explicitly asks about:

- minimum platforms
- railway platforms
- train scheduling
- greedy intervals
- two pointers

Related concepts:

- minimum platforms
- railway platforms
- train scheduling
- greedy intervals
- two pointers
