# Maximum Consecutive Ones

Problem ID: maximum_consecutive_ones

Title: Maximum Consecutive Ones

Difficulty: Easy

Topic: arrays

Pattern: **Linear Scan / Counting**

---

## Problem Identity

This document is specifically about:

**Maximum Consecutive Ones**

This knowledge chunk belongs to:

**arrays**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Maximum Consecutive Ones** problem.

The primary problem-solving pattern is:

**Linear Scan / Counting**

---

## Key Idea

Maintain a running count of consecutive ones. Reset the count when a zero is encountered and keep track of the maximum count reached.

### Core Invariant

currentCount represents the number of consecutive ones ending at the current position, while maximumCount stores the largest run seen so far.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Start from every position containing 1 and count consecutive ones until a zero is encountered.

### Brute Force Complexity

- **Time Complexity:** O(N²)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize currentCount and maximumCount to zero.
2. Scan the array.
3. If the current value is 1, increment currentCount.
4. If the current value is zero, reset currentCount to zero.
5. Update maximumCount whenever currentCount becomes larger.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Linear Scan / Counting**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What should happen to the current streak when you encounter a zero?

### Hint 2

Can you track the current streak and the best streak separately?

---

## Common Mistakes

- Not resetting the current count after zero.
- Returning the final streak instead of the maximum streak.
- Updating the maximum only at the end.

---

## Edge Cases

- All zeros.
- All ones.
- Empty array.
- Single element.
- Alternating zeros and ones.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Maximum Consecutive Ones** is:

> Maintain a running count of consecutive ones. Reset the count when a zero is encountered and keep track of the maximum count reached.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Maximum Consecutive Ones
- consecutive ones
- maximum streak
- array counting
- LeetCode 485

---

## Problem Retrieval Identity

Problem Name: Maximum Consecutive Ones

Problem ID: maximum_consecutive_ones

Topic: arrays

Pattern: Linear Scan / Counting

Difficulty: Easy

Primary Retrieval Entity:

**Maximum Consecutive Ones**

This document should be preferred when a user explicitly asks about:

- Maximum Consecutive Ones
- consecutive ones
- maximum streak
- array counting
- LeetCode 485

Related concepts:

- Maximum Consecutive Ones
- consecutive ones
- maximum streak
- array counting
- LeetCode 485
