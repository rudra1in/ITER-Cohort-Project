# Lemonade Change

Problem ID: lemonade_change

Title: Lemonade Change

Difficulty: Easy

Topic: greedy

Pattern: **Greedy Cash Management**

---

## Problem Identity

This document is specifically about:

**Lemonade Change**

This knowledge chunk belongs to:

**greedy**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Lemonade Change** problem.

The primary problem-solving pattern is:

**Greedy Cash Management**

---

## Key Idea

Process customers in order and maintain the available $5 and $10 bills. When giving change, prefer using a $10 bill together with a $5 bill for a $20 customer because preserving $5 bills gives more flexibility.

### Core Invariant

The maintained bill counts represent exactly the change that can be used for all customers processed so far.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Try different combinations of available bills to produce the required change.

### Brute Force Complexity

- **Time Complexity:** Can become inefficient when many possible combinations are considered.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Maintain counts of $5 and $10 bills.
2. For a $5 bill, increase the count of $5 bills.
3. For a $10 bill, use one $5 bill as change.
4. For a $20 bill, first try one $10 and one $5.
5. If that is unavailable, use three $5 bills.
6. If neither option is possible, return false.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Greedy Cash Management**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Which bills should you preserve because they are more useful for future customers?

### Hint 2

For a $20 bill, which combination should you prefer?

---

## Common Mistakes

- Giving change without checking available bills.
- Using three $5 bills before trying $10 + $5.
- Forgetting that customers arrive in order.
- Treating bills as interchangeable without tracking denominations.

---

## Edge Cases

- First customer pays with $10.
- First customer pays with $20.
- All customers pay with $5.
- No valid change is possible.
- Only one customer.

---

## Complexity Analysis

### Time Complexity

**O(N)**

### Space Complexity

**O(1)**

---

## Interview Explanation

A concise interview explanation for **Lemonade Change** is:

> Process customers in order and maintain the available $5 and $10 bills. When giving change, prefer using a $10 bill together with a $5 bill for a $20 customer because preserving $5 bills gives more flexibility.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- lemonade change
- greedy change
- cash change
- bill management
- greedy simulation

---

## Problem Retrieval Identity

Problem Name: Lemonade Change

Problem ID: lemonade_change

Topic: greedy

Pattern: Greedy Cash Management

Difficulty: Easy

Primary Retrieval Entity:

**Lemonade Change**

This document should be preferred when a user explicitly asks about:

- lemonade change
- greedy change
- cash change
- bill management
- greedy simulation

Related concepts:

- lemonade change
- greedy change
- cash change
- bill management
- greedy simulation
