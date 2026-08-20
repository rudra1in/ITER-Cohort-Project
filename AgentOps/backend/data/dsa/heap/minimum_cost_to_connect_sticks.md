# Minimum Cost to Connect Sticks

Problem ID: minimum_cost_to_connect_sticks

Title: Minimum Cost to Connect Sticks

Difficulty: Medium

Topic: heap

Pattern: **Min Heap / Greedy**

---

## Problem Identity

This document is specifically about:

**Minimum Cost to Connect Sticks**

This knowledge chunk belongs to:

**heap**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Minimum Cost to Connect Sticks** problem.

The primary problem-solving pattern is:

**Min Heap / Greedy**

---

## Key Idea

Always connect the two smallest sticks first. A min heap efficiently provides the two smallest available sticks.

### Core Invariant

At every step, combining the two smallest available sticks produces the minimum possible additional cost.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Repeatedly scan the complete collection to find the two smallest sticks.

### Brute Force Complexity

- **Time Complexity:** O(N²)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Insert every stick length into a min heap.
2. Remove the two smallest sticks.
3. Add their lengths to obtain the connection cost.
4. Add this cost to the total.
5. Insert the combined stick back into the heap.
6. Repeat until only one stick remains.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Min Heap / Greedy**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Which two sticks should be connected first to minimize cost?

### Hint 2

What happens to the combined stick?

---

## Common Mistakes

- Connecting arbitrary sticks.
- Forgetting to insert the combined stick.
- Stopping too early.
- Calculating the total cost incorrectly.

---

## Edge Cases

- One stick.
- Two sticks.
- Duplicate lengths.
- Very large stick lengths.
- Empty input.

---

## Complexity Analysis

### Time Complexity

**O(N log N)**

### Space Complexity

**O(N)**

---

## Interview Explanation

A concise interview explanation for **Minimum Cost to Connect Sticks** is:

> Always connect the two smallest sticks first. A min heap efficiently provides the two smallest available sticks.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- minimum cost connect sticks
- connect sticks
- min heap
- greedy
- priority queue

---

## Problem Retrieval Identity

Problem Name: Minimum Cost to Connect Sticks

Problem ID: minimum_cost_to_connect_sticks

Topic: heap

Pattern: Min Heap / Greedy

Difficulty: Medium

Primary Retrieval Entity:

**Minimum Cost to Connect Sticks**

This document should be preferred when a user explicitly asks about:

- minimum cost connect sticks
- connect sticks
- min heap
- greedy
- priority queue

Related concepts:

- minimum cost connect sticks
- connect sticks
- min heap
- greedy
- priority queue
