# First Unique Character in a String

Problem ID: first_unique_character_in_string

Title: First Unique Character in a String

Difficulty: Easy

Topic: queue

Pattern: **Queue + Frequency**

---

## Problem Identity

This document is specifically about:

**First Unique Character in a String**

This knowledge chunk belongs to:

**queue**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **First Unique Character in a String** problem.

The primary problem-solving pattern is:

**Queue + Frequency**

---

## Key Idea

Maintain character frequencies and preserve the order in which characters appear. A queue can help identify the earliest character whose frequency remains one.

### Core Invariant

Characters at the front of the queue are candidates for being the first unique character.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Count the frequency of every character and then scan the string from left to right.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Count the frequency of every character.
2. Store characters in their original order.
3. Process them from the front.
4. Remove or skip characters whose frequency is greater than one.
5. The first character with frequency one is the answer.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Queue + Frequency**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How can you preserve the order of characters?

### Hint 2

Why do you need frequency information?

---

## Common Mistakes

- Checking uniqueness before calculating complete frequencies.
- Losing the original order.
- Returning a repeated character.

---

## Edge Cases

- Empty string.
- All characters repeated.
- First character unique.
- Unique character appears near the end.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(N)**

---

## Interview Explanation

A concise interview explanation for **First Unique Character in a String** is:

> Maintain character frequencies and preserve the order in which characters appear. A queue can help identify the earliest character whose frequency remains one.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- first unique character
- first non repeating character
- queue frequency
- character frequency

---

## Problem Retrieval Identity

Problem Name: First Unique Character in a String

Problem ID: first_unique_character_in_string

Topic: queue

Pattern: Queue + Frequency

Difficulty: Easy

Primary Retrieval Entity:

**First Unique Character in a String**

This document should be preferred when a user explicitly asks about:

- first unique character
- first non repeating character
- queue frequency
- character frequency

Related concepts:

- first unique character
- first non repeating character
- queue frequency
- character frequency
