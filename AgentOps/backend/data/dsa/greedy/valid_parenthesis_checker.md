# Valid Parenthesis Checker

Problem ID: valid_parenthesis_checker

Title: Valid Parenthesis Checker

Difficulty: Hard

Topic: greedy

Pattern: **Greedy + Range of Possible Balance**

---

## Problem Identity

This document is specifically about:

**Valid Parenthesis Checker**

This knowledge chunk belongs to:

**greedy**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Valid Parenthesis Checker** problem.

The primary problem-solving pattern is:

**Greedy + Range of Possible Balance**

---

## Key Idea

Maintain a range of possible open-parenthesis balances while scanning the string. A '(' increases the possible balance, ')' decreases it, and '*' can behave as either '(' or ')' or an empty character.

### Core Invariant

The range [minBalance, maxBalance] represents all possible unmatched opening-parenthesis counts after processing the current prefix.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Try all possible interpretations of every '*' character and check whether any interpretation forms a valid parenthesis sequence.

### Brute Force Complexity

- **Time Complexity:** O(2^N) in the worst case because every '*' can have multiple interpretations.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Maintain the minimum possible balance.
2. Maintain the maximum possible balance.
3. For '(' increase both bounds.
4. For ')' decrease both bounds.
5. For '*' decrease the minimum bound and increase the maximum bound.
6. If the maximum balance becomes negative, the sequence cannot be valid.
7. Clamp the minimum balance to zero.
8. At the end, the sequence is valid if the minimum balance is zero.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Greedy + Range of Possible Balance**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

What if '*' can represent three different possibilities?

### Hint 2

Can you track a range instead of explicitly trying every possibility?

---

## Common Mistakes

- Treating '*' as only one fixed character.
- Allowing the maximum balance to become negative.
- Forgetting to clamp minimum balance to zero.
- Checking only the final balance.

---

## Edge Cases

- Empty string.
- Only opening parentheses.
- Only closing parentheses.
- String containing only '*'.
- Multiple '*' characters.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Valid Parenthesis Checker** is:

> Maintain a range of possible open-parenthesis balances while scanning the string. A '(' increases the possible balance, ')' decreases it, and '*' can behave as either '(' or ')' or an empty character.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- valid parenthesis checker
- parentheses
- wildcard parentheses
- greedy parentheses
- minimum maximum balance

---

## Problem Retrieval Identity

Problem Name: Valid Parenthesis Checker

Problem ID: valid_parenthesis_checker

Topic: greedy

Pattern: Greedy + Range of Possible Balance

Difficulty: Hard

Primary Retrieval Entity:

**Valid Parenthesis Checker**

This document should be preferred when a user explicitly asks about:

- valid parenthesis checker
- parentheses
- wildcard parentheses
- greedy parentheses
- minimum maximum balance

Related concepts:

- valid parenthesis checker
- parentheses
- wildcard parentheses
- greedy parentheses
- minimum maximum balance
