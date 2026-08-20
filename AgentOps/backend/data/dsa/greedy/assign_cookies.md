# Assign Cookies

Problem ID: assign_cookies

Title: Assign Cookies

Difficulty: Easy

Topic: greedy

Pattern: **Greedy + Sorting**

---

## Problem Identity

This document is specifically about:

**Assign Cookies**

This knowledge chunk belongs to:

**greedy**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Assign Cookies** problem.

The primary problem-solving pattern is:

**Greedy + Sorting**

---

## Key Idea

Sort the children by their greed and the cookies by their sizes. Assign the smallest cookie that can satisfy the current child so that larger cookies remain available for children with greater requirements.

### Core Invariant

At every step, all cookies before the current cookie pointer have already been considered, and the current smallest usable cookie is assigned whenever it can satisfy the current child.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

For each child, search for an unused cookie that satisfies the child's greed value. Mark the cookie as used after assignment.

### Brute Force Complexity

- **Time Complexity:** O(N * M) time in the straightforward implementation.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Sort the greed array of the children.
2. Sort the cookie sizes.
3. Use one pointer for children and one pointer for cookies.
4. If the current cookie can satisfy the current child, assign it and move both pointers.
5. Otherwise move the cookie pointer because that cookie is too small.
6. Return the number of satisfied children.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Greedy + Sorting**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Should you give a large cookie to an easy-to-satisfy child?

### Hint 2

What happens if you always use the smallest cookie that can satisfy the current child?

---

## Common Mistakes

- Assigning cookies in arbitrary order.
- Using a large cookie when a smaller cookie would work.
- Forgetting that each cookie can be assigned only once.
- Moving the wrong pointer after an unsuccessful match.

---

## Edge Cases

- No children.
- No cookies.
- All cookies are too small.
- More cookies than children.
- More children than cookies.

---

## Complexity Analysis

### Time Complexity

**O(N log N + M log M)**

### Space Complexity

**O(1) auxiliary space excluding the sorting implementation.**

---

## Interview Explanation

A concise interview explanation for **Assign Cookies** is:

> Sort the children by their greed and the cookies by their sizes. Assign the smallest cookie that can satisfy the current child so that larger cookies remain available for children with greater requirements.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- assign cookies
- cookie distribution
- greedy
- sorting greedy
- maximum satisfied children

---

## Problem Retrieval Identity

Problem Name: Assign Cookies

Problem ID: assign_cookies

Topic: greedy

Pattern: Greedy + Sorting

Difficulty: Easy

Primary Retrieval Entity:

**Assign Cookies**

This document should be preferred when a user explicitly asks about:

- assign cookies
- cookie distribution
- greedy
- sorting greedy
- maximum satisfied children

Related concepts:

- assign cookies
- cookie distribution
- greedy
- sorting greedy
- maximum satisfied children
