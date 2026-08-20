# Container With Most Water

Problem ID: container_with_most_water

Title: Container With Most Water

Difficulty: Medium

Topic: two_pointers

Pattern: **Opposite Pointers**

---

## Problem Identity

This document is specifically about:

**Container With Most Water**

This knowledge chunk belongs to:

**two_pointers**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Container With Most Water** problem.

The primary problem-solving pattern is:

**Opposite Pointers**

---

## Key Idea

The area formed by two lines is limited by the shorter line. Start with the widest container and move the pointer pointing to the shorter line.

### Core Invariant

When the shorter boundary is discarded, any container using that boundary with a smaller width cannot produce a larger area unless a taller boundary is found.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Check every pair of lines and calculate the area between them.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize left = 0 and right = n - 1.
2. Calculate width = right - left.
3. Calculate height = min(height[left], height[right]).
4. Update the maximum area.
5. If height[left] is smaller, move left forward.
6. Otherwise move right backward.
7. Continue until left reaches right.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Opposite Pointers**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What determines the height of the container?

### Hint 2

Why should the shorter side be moved?

---

## Common Mistakes

- Moving the taller pointer instead of the shorter pointer.
- Using the sum of heights instead of the minimum height.
- Calculating width incorrectly.
- Using nested loops unnecessarily.

---

## Edge Cases

- Only two elements.
- All heights are equal.
- One very tall line.
- Increasing heights.
- Decreasing heights.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Container With Most Water** is:

> The area formed by two lines is limited by the shorter line. Start with the widest container and move the pointer pointing to the shorter line.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- container with most water
- maximum area
- opposite pointers
- two pointers
- greedy pointer movement

---

## Problem Retrieval Identity

Problem Name: Container With Most Water

Problem ID: container_with_most_water

Topic: two_pointers

Pattern: Opposite Pointers

Difficulty: Medium

Primary Retrieval Entity:

**Container With Most Water**

This document should be preferred when a user explicitly asks about:

- container with most water
- maximum area
- opposite pointers
- two pointers
- greedy pointer movement

Related concepts:

- container with most water
- maximum area
- opposite pointers
- two pointers
- greedy pointer movement
