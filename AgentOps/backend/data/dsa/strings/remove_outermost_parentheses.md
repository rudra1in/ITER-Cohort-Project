# Remove Outermost Parentheses

Problem ID: remove_outermost_parentheses

Title: Remove Outermost Parentheses

Difficulty: Medium

Topic: strings

Pattern: **Parentheses Depth Tracking**

---

## Problem Identity

This document is specifically about:

**Remove Outermost Parentheses**

This knowledge chunk belongs to:

**strings**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Remove Outermost Parentheses** problem.

The primary problem-solving pattern is:

**Parentheses Depth Tracking**

---

## Key Idea

Track the current parentheses depth. An opening parenthesis should be included only when it is not the outermost opening parenthesis, and a closing parenthesis should be included only when it does not close the outermost layer.

### Core Invariant

The depth represents how deeply nested the current parenthesis is, allowing the outermost pair of every primitive valid parentheses string to be excluded.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use a stack or repeatedly identify primitive valid parentheses groups and remove their first and last parentheses.

### Brute Force Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Initialize depth = 0.
2. Traverse the string character by character.
3. When encountering '(', check the current depth before increasing it.
4. If depth is greater than zero, include the opening parenthesis.
5. Increase depth.
6. When encountering ')', decrease depth first.
7. If depth is greater than zero after decreasing, include the closing parenthesis.
8. Return the resulting string.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Parentheses Depth Tracking**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can you determine whether a parenthesis is outermost by tracking the current nesting depth?

### Hint 2

When should an opening or closing parenthesis be excluded?

---

## Common Mistakes

- Removing every first and last parenthesis from the entire string instead of each primitive group.
- Changing depth at the wrong time for closing parentheses.
- Including parentheses when the depth represents the outermost level.

---

## Edge Cases

- Single primitive parentheses pair.
- Multiple primitive groups.
- Deeply nested parentheses.
- Empty string.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(N) for the output string.**

---

## Interview Explanation

A concise interview explanation for **Remove Outermost Parentheses** is:

> Track the current parentheses depth. An opening parenthesis should be included only when it is not the outermost opening parenthesis, and a closing parenthesis should be included only when it does not close the outermost layer.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- Remove Outermost Parentheses
- parentheses
- depth
- nesting
- LeetCode 1021

---

## Problem Retrieval Identity

Problem Name: Remove Outermost Parentheses

Problem ID: remove_outermost_parentheses

Topic: strings

Pattern: Parentheses Depth Tracking

Difficulty: Medium

Primary Retrieval Entity:

**Remove Outermost Parentheses**

This document should be preferred when a user explicitly asks about:

- Remove Outermost Parentheses
- parentheses
- depth
- nesting
- LeetCode 1021

Related concepts:

- Remove Outermost Parentheses
- parentheses
- depth
- nesting
- LeetCode 1021
