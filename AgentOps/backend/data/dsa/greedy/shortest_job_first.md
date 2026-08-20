# Shortest Job First

Problem ID: shortest_job_first

Title: Shortest Job First

Difficulty: Medium

Topic: greedy

Pattern: **Greedy Scheduling**

---

## Problem Identity

This document is specifically about:

**Shortest Job First**

This knowledge chunk belongs to:

**greedy**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Shortest Job First** problem.

The primary problem-solving pattern is:

**Greedy Scheduling**

---

## Key Idea

To minimize the average waiting time, process jobs in increasing order of their burst time. Short jobs completed earlier reduce the waiting time accumulated by later jobs.

### Core Invariant

At each step, the scheduled jobs are the shortest available jobs, minimizing the waiting time contributed to the remaining jobs.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Try different execution orders and calculate the total waiting time for each ordering.

### Brute Force Complexity

- **Time Complexity:** O(N!) for exhaustive permutation-based scheduling.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Sort jobs by increasing burst time.
2. Initialize elapsed time to zero.
3. For each job, add the current elapsed time to total waiting time.
4. Increase elapsed time by the current job's burst time.
5. Calculate the average waiting time.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Greedy Scheduling**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Which job should finish first if the goal is minimum waiting time?

### Hint 2

How does delaying a long job affect the waiting time of other jobs?

---

## Common Mistakes

- Sorting in descending order.
- Confusing waiting time with turnaround time.
- Adding the current job's duration before calculating its waiting time.
- Ignoring the scheduling objective.

---

## Edge Cases

- One job.
- All jobs have equal duration.
- One extremely long job.
- Already sorted jobs.
- Reverse sorted jobs.

---

## Complexity Analysis

### Time Complexity

**O(N log N)**

### Space Complexity

**O(1) auxiliary space excluding sorting.**

---

## Interview Explanation

A concise interview explanation for **Shortest Job First** is:

> To minimize the average waiting time, process jobs in increasing order of their burst time. Short jobs completed earlier reduce the waiting time accumulated by later jobs.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- shortest job first
- SJF
- CPU scheduling
- minimum waiting time
- greedy scheduling

---

## Problem Retrieval Identity

Problem Name: Shortest Job First

Problem ID: shortest_job_first

Topic: greedy

Pattern: Greedy Scheduling

Difficulty: Medium

Primary Retrieval Entity:

**Shortest Job First**

This document should be preferred when a user explicitly asks about:

- shortest job first
- SJF
- CPU scheduling
- minimum waiting time
- greedy scheduling

Related concepts:

- shortest job first
- SJF
- CPU scheduling
- minimum waiting time
- greedy scheduling
