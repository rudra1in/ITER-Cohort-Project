# Longest Subarray with Sum K

Problem ID: longest_subarray_with_sum_k

Title: Longest Subarray with Sum K

Difficulty: Medium

Topic: arrays

Pattern: **Prefix Sum + Hash Map**

---

## Problem Identity

This document is specifically about:

**Longest Subarray with Sum K**

This knowledge chunk belongs to:

**arrays**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Longest Subarray with Sum K** problem.

The primary problem-solving pattern is:

**Prefix Sum + Hash Map**

---

## Key Idea

Use prefix sums and store the first index where each prefix sum occurs. If the current prefix sum is S, then a previous prefix sum of S-K means the subarray between those indices has sum K.

### Core Invariant

The first stored index for a prefix sum gives the longest possible subarray ending at the current position when that prefix sum is needed.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Consider every possible starting index and extend the subarray while calculating its sum.

### Brute Force Complexity

- **Time Complexity:** O(N²)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize prefixSum to zero.
2. Store the first occurrence of each prefix sum in a hash map.
3. For each element, add it to prefixSum.
4. If prefixSum equals k, the subarray from index zero has sum k.
5. Check whether prefixSum - k exists in the map.
6. If it exists, calculate the corresponding subarray length.
7. Store the first occurrence of the current prefix sum if it has not already been stored.
8. Return the maximum length found.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Prefix Sum + Hash Map**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

If prefixSum is S, what previous prefix sum would give a subarray sum of K?

### Hint 2

Why should you store the first occurrence of each prefix sum rather than overwrite it?

---

## Common Mistakes

- Overwriting an earlier prefix sum index.
- Forgetting the case where the prefix sum itself equals K.
- Using a sliding window when negative numbers may be present.
- Calculating the subarray length incorrectly.

---

## Edge Cases

- No subarray has sum K.
- The entire array has sum K.
- Negative numbers.
- Zeros.
- K equals zero.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(N)**

---

## Interview Explanation

A concise interview explanation for **Longest Subarray with Sum K** is:

> Use prefix sums and store the first index where each prefix sum occurs. If the current prefix sum is S, then a previous prefix sum of S-K means the subarray between those indices has sum K.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Longest Subarray with Sum K
- subarray sum K
- prefix sum
- hash map
- longest subarray
- LeetCode subarray sum

---

## Problem Retrieval Identity

Problem Name: Longest Subarray with Sum K

Problem ID: longest_subarray_with_sum_k

Topic: arrays

Pattern: Prefix Sum + Hash Map

Difficulty: Medium

Primary Retrieval Entity:

**Longest Subarray with Sum K**

This document should be preferred when a user explicitly asks about:

- Longest Subarray with Sum K
- subarray sum K
- prefix sum
- hash map
- longest subarray
- LeetCode subarray sum

Related concepts:

- Longest Subarray with Sum K
- subarray sum K
- prefix sum
- hash map
- longest subarray
- LeetCode subarray sum
