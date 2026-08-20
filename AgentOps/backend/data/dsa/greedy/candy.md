# Candy

Problem ID: candy

Title: Candy

Difficulty: Hard

Topic: greedy

Pattern: **Greedy Two Pass**

---

## Problem Identity

This document is specifically about:

**Candy**

This knowledge chunk belongs to:

**greedy**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Candy** problem.

The primary problem-solving pattern is:

**Greedy Two Pass**

---

## Key Idea

Each child must have at least one candy, and a child with a higher rating than a neighbor must have more candies. Process ratings from left to right and right to left to satisfy both directions.

### Core Invariant

After the left-to-right pass, every child satisfies the rating condition relative to the left neighbor. The right-to-left pass adds the constraints from the right without breaking the left-side requirement.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Repeatedly increase candy counts for children violating the neighbor conditions until all constraints are satisfied.

### Brute Force Complexity

- **Time Complexity:** Can require multiple passes and may become O(N^2) in straightforward implementations.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize every child with one candy.
2. Traverse from left to right.
3. If rating[i] is greater than rating[i-1], increase candies[i].
4. Traverse from right to left.
5. If rating[i] is greater than rating[i+1], ensure candies[i] is greater than candies[i+1].
6. Use the maximum of the existing value and the right-side requirement.
7. Return the total candies.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Greedy Two Pass**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Why is one direction not enough?

### Hint 2

Can you satisfy the left neighbor condition first and then the right neighbor condition?

---

## Common Mistakes

- Using only one traversal.
- Replacing instead of taking the maximum during the second pass.
- Forgetting that every child must receive at least one candy.
- Comparing ratings in the wrong direction.

---

## Edge Cases

- One child.
- All ratings equal.
- Strictly increasing ratings.
- Strictly decreasing ratings.
- Peak in the middle.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(N)**

---

## Interview Explanation

A concise interview explanation for **Candy** is:

> Each child must have at least one candy, and a child with a higher rating than a neighbor must have more candies. Process ratings from left to right and right to left to satisfy both directions.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- candy
- candy distribution
- greedy two pass
- ratings
- minimum candies

---

## Problem Retrieval Identity

Problem Name: Candy

Problem ID: candy

Topic: greedy

Pattern: Greedy Two Pass

Difficulty: Hard

Primary Retrieval Entity:

**Candy**

This document should be preferred when a user explicitly asks about:

- candy
- candy distribution
- greedy two pass
- ratings
- minimum candies

Related concepts:

- candy
- candy distribution
- greedy two pass
- ratings
- minimum candies
