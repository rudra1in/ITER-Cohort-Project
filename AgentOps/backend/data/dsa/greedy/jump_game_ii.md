# Jump Game II

Problem ID: jump_game_ii

Title: Jump Game II

Difficulty: Medium

Topic: greedy

Pattern: **Greedy Range Expansion**

---

## Problem Identity

This document is specifically about:

**Jump Game II**

This knowledge chunk belongs to:

**greedy**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Jump Game II** problem.

The primary problem-solving pattern is:

**Greedy Range Expansion**

---

## Key Idea

Treat each jump as covering a range of reachable positions. While scanning the current range, find the farthest position that can be reached with the next jump.

### Core Invariant

All indices inside the current range can be reached using the current number of jumps.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Explore different jump choices recursively or use dynamic programming to calculate the minimum number of jumps.

### Brute Force Complexity

- **Time Complexity:** O(N^2) for the typical dynamic programming solution.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Maintain the current jump range using the current end.
2. Track the farthest position reachable from this range.
3. Scan positions inside the current range.
4. When the current index reaches the end of the range, take another jump.
5. Set the new range end to the farthest reachable position.
6. Continue until the last index is reachable.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Greedy Range Expansion**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Instead of choosing one exact jump, can you consider the entire range reachable after a jump?

### Hint 2

What is the farthest position reachable from the current range?

---

## Common Mistakes

- Incrementing jumps at every index.
- Choosing the largest immediate jump without considering the next range.
- Confusing this with Jump Game I.
- Using nested loops unnecessarily.

---

## Edge Cases

- Single-element array.
- Only one jump required.
- Every value is one.
- Large jump at the beginning.
- Multiple possible optimal paths.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Jump Game II** is:

> Treat each jump as covering a range of reachable positions. While scanning the current range, find the farthest position that can be reached with the next jump.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- jump game II
- minimum jumps
- greedy jump
- range expansion
- minimum number of jumps

---

## Problem Retrieval Identity

Problem Name: Jump Game II

Problem ID: jump_game_ii

Topic: greedy

Pattern: Greedy Range Expansion

Difficulty: Medium

Primary Retrieval Entity:

**Jump Game II**

This document should be preferred when a user explicitly asks about:

- jump game II
- minimum jumps
- greedy jump
- range expansion
- minimum number of jumps

Related concepts:

- jump game II
- minimum jumps
- greedy jump
- range expansion
- minimum number of jumps
