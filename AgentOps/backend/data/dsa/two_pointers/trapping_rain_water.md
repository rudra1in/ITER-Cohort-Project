# Trapping Rain Water

Problem ID: trapping_rain_water

Title: Trapping Rain Water

Difficulty: Hard

Topic: two_pointers

Pattern: **Two Pointers / Left-Right**

---

## Problem Identity

This document is specifically about:

**Trapping Rain Water**

This knowledge chunk belongs to:

**two_pointers**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Trapping Rain Water** problem.

The primary problem-solving pattern is:

**Two Pointers / Left-Right**

---

## Key Idea

Water above a position depends on the smaller of the maximum heights on its left and right. Two pointers can calculate this without storing prefix arrays.

### Core Invariant

At each step, the side with the smaller boundary determines the maximum possible water level for the current position.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

For every position, scan to the left and right to find the maximum boundaries and calculate the trapped water.

### Brute Force Complexity

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize left = 0 and right = n - 1.
2. Maintain leftMax and rightMax.
3. If height[left] is smaller than height[right], process the left side.
4. If height[left] is at least leftMax, update leftMax.
5. Otherwise add leftMax - height[left] to the answer.
6. Move left forward.
7. Otherwise process the right side similarly.
8. Update rightMax or add rightMax - height[right].
9. Move right backward.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Two Pointers / Left-Right**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What determines how much water can sit above an index?

### Hint 2

Can you maintain the maximum height seen from both sides?

---

## Common Mistakes

- Using the larger boundary instead of the smaller boundary.
- Updating max height after calculating water incorrectly.
- Moving the wrong pointer.
- Forgetting that negative trapped water should never be added.

---

## Edge Cases

- Less than three bars.
- All heights are equal.
- Strictly increasing heights.
- Strictly decreasing heights.
- Large valleys between tall boundaries.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Trapping Rain Water** is:

> Water above a position depends on the smaller of the maximum heights on its left and right. Two pointers can calculate this without storing prefix arrays.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- trapping rain water
- two pointers
- left max
- right max
- water trapping

---

## Problem Retrieval Identity

Problem Name: Trapping Rain Water

Problem ID: trapping_rain_water

Topic: two_pointers

Pattern: Two Pointers / Left-Right

Difficulty: Hard

Primary Retrieval Entity:

**Trapping Rain Water**

This document should be preferred when a user explicitly asks about:

- trapping rain water
- two pointers
- left max
- right max
- water trapping

Related concepts:

- trapping rain water
- two pointers
- left max
- right max
- water trapping
