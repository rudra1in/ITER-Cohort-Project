# Roman to Integer

Problem ID: roman_to_integer

Title: Roman to Integer

Difficulty: Medium

Topic: strings

Pattern: **Hash Map + Greedy Traversal**

---

## Problem Identity

This document is specifically about:

**Roman to Integer**

This knowledge chunk belongs to:

**strings**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Roman to Integer** problem.

The primary problem-solving pattern is:

**Hash Map + Greedy Traversal**

---

## Key Idea

Map each Roman numeral to its integer value. When a smaller value appears before a larger value, subtract it; otherwise add it.

### Core Invariant

Each processed Roman symbol contributes either positively or negatively according to its relationship with the following symbol.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Process each Roman numeral individually and separately handle the known subtractive combinations such as IV, IX, XL, XC, CD, and CM.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Create a mapping from Roman symbols to integer values.
2. Traverse the string from left to right.
3. Compare the current symbol's value with the next symbol's value.
4. Subtract the current value when it is smaller than the next value.
5. Otherwise add the current value.
6. Return the final total.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Hash Map + Greedy Traversal**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What happens when a smaller Roman numeral comes before a larger one?

### Hint 2

Can you decide whether to add or subtract by comparing adjacent values?

---

## Common Mistakes

- Treating every symbol as an addition.
- Handling subtractive notation incorrectly.
- Forgetting to process the final character.

---

## Edge Cases

- Single Roman numeral.
- Subtractive notation such as IV.
- Large valid Roman number.
- Repeated symbols.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Roman to Integer** is:

> Map each Roman numeral to its integer value. When a smaller value appears before a larger value, subtract it; otherwise add it.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Roman to Integer
- Roman numerals
- hash map
- greedy
- LeetCode 13

---

## Problem Retrieval Identity

Problem Name: Roman to Integer

Problem ID: roman_to_integer

Topic: strings

Pattern: Hash Map + Greedy Traversal

Difficulty: Medium

Primary Retrieval Entity:

**Roman to Integer**

This document should be preferred when a user explicitly asks about:

- Roman to Integer
- Roman numerals
- hash map
- greedy
- LeetCode 13

Related concepts:

- Roman to Integer
- Roman numerals
- hash map
- greedy
- LeetCode 13
