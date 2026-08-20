# Implement Min Stack

Problem ID: implement_min_stack

Title: Implement Min Stack

Difficulty: Hard

Topic: stack

Pattern: **Stack with Auxiliary Minimum Tracking**

---

## Problem Identity

This document is specifically about:

**Implement Min Stack**

This knowledge chunk belongs to:

**stack**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Implement Min Stack** problem.

The primary problem-solving pattern is:

**Stack with Auxiliary Minimum Tracking**

---

## Key Idea

A Min Stack supports normal stack operations while also returning the minimum element in O(1). This can be achieved by maintaining additional minimum information along with the stack.

### Core Invariant

The minimum-tracking structure always represents the minimum value among the elements currently present in the stack.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Use a normal stack and scan all elements whenever getMin is called.

### Brute Force Complexity

- **Time Complexity:** O(1) for push and pop, but O(N) for getMin.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Maintain a stack for the elements.
2. Maintain minimum information for the current stack state.
3. When pushing, update the current minimum if the new value is smaller.
4. When popping, restore the previous minimum.
5. Return the tracked minimum directly for getMin.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Stack with Auxiliary Minimum Tracking**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How can you remember the minimum when pushing a new value?

### Hint 2

What minimum should be restored after removing the current minimum?

---

## Common Mistakes

- Scanning the entire stack during getMin.
- Forgetting to restore the previous minimum after pop.
- Incorrectly handling duplicate minimum values.
- Using an incorrect sentinel for an empty stack.

---

## Edge Cases

- Empty stack.
- Single element.
- Duplicate minimum values.
- Negative values.
- Increasing values.
- Decreasing values.

---

## Complexity Analysis

### Time Complexity

**O(1) for push, pop, top, and getMin.**

### Space Complexity

**O(N)**

---

## Interview Explanation

A concise interview explanation for **Implement Min Stack** is:

> A Min Stack supports normal stack operations while also returning the minimum element in O(1). This can be achieved by maintaining additional minimum information along with the stack.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- min stack
- minimum stack
- getMin O(1)
- stack minimum
- auxiliary stack

---

## Problem Retrieval Identity

Problem Name: Implement Min Stack

Problem ID: implement_min_stack

Topic: stack

Pattern: Stack with Auxiliary Minimum Tracking

Difficulty: Hard

Primary Retrieval Entity:

**Implement Min Stack**

This document should be preferred when a user explicitly asks about:

- min stack
- minimum stack
- getMin O(1)
- stack minimum
- auxiliary stack

Related concepts:

- min stack
- minimum stack
- getMin O(1)
- stack minimum
- auxiliary stack
