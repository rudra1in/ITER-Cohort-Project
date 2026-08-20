# Count All Subsequences with Sum K

Problem ID: count_subsequences_with_sum_k

Title: Count All Subsequences with Sum K

Difficulty: Easy

Topic: recursion

Pattern: **Recursion + Subsequences**

---

## Problem Identity

This document is specifically about:

**Count All Subsequences with Sum K**

This knowledge chunk belongs to:

**recursion**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Count All Subsequences with Sum K** problem.

The primary problem-solving pattern is:

**Recursion + Subsequences**

---

## Key Idea

For each element, recursively choose whether to include or exclude it and count the subsequences whose sum equals K.

### Core Invariant

The running sum represents exactly the sum of elements selected in the current recursive path.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Generate all subsequences and check the sum of each subsequence.

### Brute Force Complexity

- **Time Complexity:** O(2^N * N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Start recursion from index 0 with sum equal to zero.
2. At each index, choose to include the current element.
3. Recursively continue with the updated sum.
4. Backtrack and choose to exclude the current element.
5. When all elements are processed, return 1 if the sum equals K, otherwise return 0.
6. Add the counts returned by the include and exclude branches.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Recursion + Subsequences**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What are the two choices for every element?

### Hint 2

Can each recursive branch return a count instead of storing every subsequence?

---

## Common Mistakes

- Forgetting the exclude branch.
- Incorrectly updating the running sum.
- Returning the wrong base-case value.
- Counting the same subsequence multiple times.

---

## Edge Cases

- Empty array.
- K = 0.
- No subsequence has sum K.
- Multiple valid subsequences.

---

## Complexity Analysis

### Time Complexity

**O(2^N)**

### Space Complexity

**O(N) recursion depth.**

---

## Interview Explanation

A concise interview explanation for **Count All Subsequences with Sum K** is:

> For each element, recursively choose whether to include or exclude it and count the subsequences whose sum equals K.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- count subsequences
- sum K
- subsequence
- recursion
- include exclude

---

## Problem Retrieval Identity

Problem Name: Count All Subsequences with Sum K

Problem ID: count_subsequences_with_sum_k

Topic: recursion

Pattern: Recursion + Subsequences

Difficulty: Easy

Primary Retrieval Entity:

**Count All Subsequences with Sum K**

This document should be preferred when a user explicitly asks about:

- count subsequences
- sum K
- subsequence
- recursion
- include exclude

Related concepts:

- count subsequences
- sum K
- subsequence
- recursion
- include exclude
