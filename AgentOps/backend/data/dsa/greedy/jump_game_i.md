# Jump Game I

Problem ID: jump_game_i

Title: Jump Game I

Difficulty: Easy

Topic: greedy

Pattern: **Greedy Reachability**

---

## Problem Identity

This document is specifically about:

**Jump Game I**

This knowledge chunk belongs to:

**greedy**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Jump Game I** problem.

The primary problem-solving pattern is:

**Greedy Reachability**

---

## Key Idea

Maintain the farthest index that can currently be reached. If the current index is beyond that reachable range, the last index cannot be reached.

### Core Invariant

After processing an index, farthest represents the maximum index reachable from all valid positions processed so far.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Try different jump lengths from each index recursively or using dynamic programming.

### Brute Force Complexity

- **Time Complexity:** O(2^N) for the naive recursive exploration.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize the farthest reachable index to zero.
2. Traverse the array from left to right.
3. If the current index is greater than the farthest reachable index, return false.
4. Update the farthest reachable index using current index plus nums[current].
5. If the farthest reachable index reaches the last index, return true.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Greedy Reachability**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Do you need to know the exact path of jumps?

### Hint 2

Can you track only the farthest position reachable so far?

---

## Common Mistakes

- Choosing a jump greedily without considering reachability.
- Ignoring indices that cannot be reached.
- Forgetting to update the farthest position.
- Using unnecessary recursion.

---

## Edge Cases

- Single-element array.
- First element is zero.
- Last index is immediately reachable.
- A zero blocks all possible paths.
- Very large jump values.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Jump Game I** is:

> Maintain the farthest index that can currently be reached. If the current index is beyond that reachable range, the last index cannot be reached.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- jump game
- jump game I
- maximum reach
- greedy reachability
- array jumps

---

## Problem Retrieval Identity

Problem Name: Jump Game I

Problem ID: jump_game_i

Topic: greedy

Pattern: Greedy Reachability

Difficulty: Easy

Primary Retrieval Entity:

**Jump Game I**

This document should be preferred when a user explicitly asks about:

- jump game
- jump game I
- maximum reach
- greedy reachability
- array jumps

Related concepts:

- jump game
- jump game I
- maximum reach
- greedy reachability
- array jumps
