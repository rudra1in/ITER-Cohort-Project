# Non-overlapping Intervals

Problem ID: non_overlapping_intervals

Title: Non-overlapping Intervals

Difficulty: Medium

Topic: greedy

Pattern: **Greedy Interval Scheduling**

---

## Problem Identity

This document is specifically about:

**Non-overlapping Intervals**

This knowledge chunk belongs to:

**greedy**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Non-overlapping Intervals** problem.

The primary problem-solving pattern is:

**Greedy Interval Scheduling**

---

## Key Idea

Sort intervals by their ending time and keep the interval that finishes earliest whenever an overlap occurs. This leaves maximum room for future intervals.

### Core Invariant

Among all possible sets of the same number of non-overlapping intervals considered so far, the selected set has the smallest possible ending time for its last interval.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Try different subsets of intervals and determine the maximum number of non-overlapping intervals that can remain.

### Brute Force Complexity

- **Time Complexity:** O(2^N) for exhaustive subset exploration.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Sort intervals by increasing end time.
2. Keep track of the end time of the last selected interval.
3. Start with the first interval.
4. For every next interval, check whether its start is at least the previous end.
5. If it does not overlap, keep it.
6. If it overlaps, remove the interval with the later end time.
7. Return the number of intervals that must be removed.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Greedy Interval Scheduling**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

When two intervals overlap, which one is better to keep?

### Hint 2

Why is an earlier finishing interval more useful?

---

## Common Mistakes

- Sorting by starting time.
- Always removing the first interval in an overlap.
- Forgetting to count removals.
- Using the wrong overlap condition.

---

## Edge Cases

- No intervals.
- One interval.
- No overlapping intervals.
- All intervals overlap.
- Intervals with equal end times.

---

## Complexity Analysis

### Time Complexity

**O(N log N)**

### Space Complexity

**O(1) auxiliary space excluding sorting.**

---

## Interview Explanation

A concise interview explanation for **Non-overlapping Intervals** is:

> Sort intervals by their ending time and keep the interval that finishes earliest whenever an overlap occurs. This leaves maximum room for future intervals.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- non overlapping intervals
- remove overlapping intervals
- interval scheduling
- greedy intervals
- activity selection

---

## Problem Retrieval Identity

Problem Name: Non-overlapping Intervals

Problem ID: non_overlapping_intervals

Topic: greedy

Pattern: Greedy Interval Scheduling

Difficulty: Medium

Primary Retrieval Entity:

**Non-overlapping Intervals**

This document should be preferred when a user explicitly asks about:

- non overlapping intervals
- remove overlapping intervals
- interval scheduling
- greedy intervals
- activity selection

Related concepts:

- non overlapping intervals
- remove overlapping intervals
- interval scheduling
- greedy intervals
- activity selection
