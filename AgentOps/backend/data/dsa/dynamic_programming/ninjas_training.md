# Ninja's Training

Problem ID: ninjas_training

Title: Ninja's Training

Difficulty: Medium

Topic: dynamic_programming

Pattern: **DP on States**

---

## Problem Identity

This document is specifically about:

**Ninja's Training**

This knowledge chunk belongs to:

**dynamic_programming**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Ninja's Training** problem.

The primary problem-solving pattern is:

**DP on States**

---

## Key Idea

For each day, the ninja chooses one of several activities but cannot repeat the activity performed on the previous day. The DP state keeps track of the previous activity.

### Core Invariant

Every DP state represents the best score achievable for the processed days while respecting the restriction on repeating the previous activity.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use recursion to try every activity for every day while remembering the activity selected on the previous day.

### Brute Force Complexity

- **Time Complexity:** O(3^N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Define dp[day][last] as the maximum points obtainable up to the current day when last represents the activity performed on the previous day.
2. For each day, try every activity except the previous activity.
3. Add the current activity's points to the best result from the previous day.
4. Store the maximum result.
5. The final answer is the maximum over all activities on the last day.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**DP on States**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What information from the previous day affects today's choices?

### Hint 2

How can you represent the previous activity as part of the state?

---

## Common Mistakes

- Allowing the same activity on consecutive days.
- Not storing the previous activity in the state.
- Using the wrong base case.
- Forgetting to consider every activity on the final day.

---

## Edge Cases

- One day.
- Two days.
- All activities have equal points.
- Different point values every day.

---

## Complexity Analysis

### Time Complexity

**O(N * 4 * 3)**

### Space Complexity

**O(4) using space optimization for the previous day's states.**

---

## Interview Explanation

A concise interview explanation for **Ninja's Training** is:

> For each day, the ninja chooses one of several activities but cannot repeat the activity performed on the previous day. The DP state keeps track of the previous activity.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- ninja training
- DP states
- activity selection
- 2D DP
- dynamic programming

---

## Problem Retrieval Identity

Problem Name: Ninja's Training

Problem ID: ninjas_training

Topic: dynamic_programming

Pattern: DP on States

Difficulty: Medium

Primary Retrieval Entity:

**Ninja's Training**

This document should be preferred when a user explicitly asks about:

- ninja training
- DP states
- activity selection
- 2D DP
- dynamic programming

Related concepts:

- ninja training
- DP states
- activity selection
- 2D DP
- dynamic programming
