# Combination Sum

Problem ID: combination_sum

Title: Combination Sum

Difficulty: Medium

Topic: recursion

Pattern: **Backtracking + Reuse Elements**

---

## Problem Identity

This document is specifically about:

**Combination Sum**

This knowledge chunk belongs to:

**recursion**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Combination Sum** problem.

The primary problem-solving pattern is:

**Backtracking + Reuse Elements**

---

## Key Idea

Use backtracking to construct combinations whose sum equals the target. The same candidate can be selected multiple times, so the recursive call can continue from the same index.

### Core Invariant

The current combination contains only candidates selected so far and its remaining target represents the exact sum still required.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Generate possible combinations and check whether their sum equals the target.

### Brute Force Complexity

- **Time Complexity:** Exponential in the number of candidates and target-dependent combinations.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Start backtracking from index 0 with target equal to the required sum.
2. If target becomes zero, add the current combination.
3. If the current candidate can be selected, include it.
4. Because an element may be reused, recursively call using the same index.
5. If the candidate is too large, move to the next candidate.
6. Backtrack after every choice.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Backtracking + Reuse Elements**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can a candidate be used more than once?

### Hint 2

If you choose a candidate again, which index should recursion start from?

---

## Common Mistakes

- Moving to the next index after selecting a reusable candidate.
- Allowing combinations with a negative remaining target.
- Forgetting to backtrack.
- Generating duplicate combinations.

---

## Edge Cases

- Target is zero.
- No valid combination.
- Single candidate.
- Candidate larger than target.
- Multiple combinations.

---

## Complexity Analysis

### Time Complexity

**Exponential in the worst case.**

### Space Complexity

**O(T) recursion depth in the worst case, where T depends on the target and smallest candidate.**

---

## Interview Explanation

A concise interview explanation for **Combination Sum** is:

> Use backtracking to construct combinations whose sum equals the target. The same candidate can be selected multiple times, so the recursive call can continue from the same index.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- combination sum
- backtracking
- recursion
- reuse elements
- target sum

---

## Problem Retrieval Identity

Problem Name: Combination Sum

Problem ID: combination_sum

Topic: recursion

Pattern: Backtracking + Reuse Elements

Difficulty: Medium

Primary Retrieval Entity:

**Combination Sum**

This document should be preferred when a user explicitly asks about:

- combination sum
- backtracking
- recursion
- reuse elements
- target sum

Related concepts:

- combination sum
- backtracking
- recursion
- reuse elements
- target sum
