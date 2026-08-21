# Task Scheduler

Problem ID: task_scheduler

Title: Task Scheduler

Difficulty: Medium

Topic: heap

Pattern: **Max Heap + Greedy**

---

## Problem Identity

This document is specifically about:

**Task Scheduler**

This knowledge chunk belongs to:

**heap**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Task Scheduler** problem.

The primary problem-solving pattern is:

**Max Heap + Greedy**

---

## Key Idea

Always execute the task with the highest remaining frequency while respecting the required cooldown interval. A max heap efficiently selects the most frequent available task.

### Core Invariant

At every scheduling cycle, the max heap contains the frequencies of tasks that are available to be scheduled.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Repeatedly scan all task frequencies to find the best task to execute.

### Brute Force Complexity

- **Time Complexity:** Can take O(N²) depending on implementation.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Count the frequency of every task.
2. Insert task frequencies into a max heap.
3. At each scheduling cycle, remove up to n + 1 tasks with the highest frequencies.
4. Decrease each selected frequency.
5. Store tasks that still have remaining occurrences.
6. Put those remaining frequencies back into the heap after the cooldown cycle.
7. Count idle slots when fewer than n + 1 tasks are available.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Max Heap + Greedy**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Which task should be scheduled first?

### Hint 2

Why is the most frequent remaining task important?

---

## Common Mistakes

- Ignoring the cooldown interval.
- Always scheduling the same task.
- Counting idle slots incorrectly.
- Forgetting to reinsert unfinished tasks.

---

## Edge Cases

- No cooldown.
- One unique task.
- All tasks unique.
- One task occurring many times.
- Multiple tasks with equal frequencies.

---

## Complexity Analysis

### Time Complexity

**O(N log K)**

### Space Complexity

**O(K)**

---

## Interview Explanation

A concise interview explanation for **Task Scheduler** is:

> Always execute the task with the highest remaining frequency while respecting the required cooldown interval. A max heap efficiently selects the most frequent available task.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- task scheduler
- cpu task scheduling
- max heap
- greedy scheduling
- cooldown

---

## Problem Retrieval Identity

Problem Name: Task Scheduler

Problem ID: task_scheduler

Topic: heap

Pattern: Max Heap + Greedy

Difficulty: Medium

Primary Retrieval Entity:

**Task Scheduler**

This document should be preferred when a user explicitly asks about:

- task scheduler
- cpu task scheduling
- max heap
- greedy scheduling
- cooldown

Related concepts:

- task scheduler
- cpu task scheduling
- max heap
- greedy scheduling
- cooldown
