# N Meetings in One Room

Problem ID: n_meetings_in_one_room

Title: N Meetings in One Room

Difficulty: Medium

Topic: greedy

Pattern: **Activity Selection**

---

## Problem Identity

This document is specifically about:

**N Meetings in One Room**

This knowledge chunk belongs to:

**greedy**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **N Meetings in One Room** problem.

The primary problem-solving pattern is:

**Activity Selection**

---

## Key Idea

Sort meetings by their finishing time and always select the meeting that finishes earliest while being compatible with the previously selected meeting.

### Core Invariant

Among the selected meetings, the last selected meeting has the earliest possible finishing time for the number of meetings selected so far.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Generate different subsets of meetings and check which subsets are mutually compatible.

### Brute Force Complexity

- **Time Complexity:** O(2^N) for exhaustive subset generation.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Represent every meeting using its start and end time.
2. Sort meetings by increasing end time.
3. Select the first compatible meeting.
4. For every next meeting, check whether its start time is greater than the last selected end time.
5. If compatible, select it.
6. Return the total number of selected meetings.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Activity Selection**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

If you want to fit as many meetings as possible, which meeting should finish first?

### Hint 2

Why is choosing the earliest finishing compatible meeting useful?

---

## Common Mistakes

- Sorting by start time.
- Sorting by meeting duration instead of finish time.
- Allowing overlapping meetings.
- Using start >= previous end incorrectly when the problem requires strict separation.

---

## Edge Cases

- Only one meeting.
- All meetings overlap.
- No overlapping meetings.
- Meetings with equal end times.
- Meetings with equal start times.

---

## Complexity Analysis

### Time Complexity

**O(N log N)**

### Space Complexity

**O(N) depending on how meetings are represented.**

---

## Interview Explanation

A concise interview explanation for **N Meetings in One Room** is:

> Sort meetings by their finishing time and always select the meeting that finishes earliest while being compatible with the previously selected meeting.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- n meetings in one room
- activity selection
- meeting scheduling
- interval scheduling
- greedy intervals

---

## Problem Retrieval Identity

Problem Name: N Meetings in One Room

Problem ID: n_meetings_in_one_room

Topic: greedy

Pattern: Activity Selection

Difficulty: Medium

Primary Retrieval Entity:

**N Meetings in One Room**

This document should be preferred when a user explicitly asks about:

- n meetings in one room
- activity selection
- meeting scheduling
- interval scheduling
- greedy intervals

Related concepts:

- n meetings in one room
- activity selection
- meeting scheduling
- interval scheduling
- greedy intervals
