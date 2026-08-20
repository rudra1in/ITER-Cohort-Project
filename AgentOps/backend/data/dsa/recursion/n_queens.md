# N Queens

Problem ID: n_queens

Title: N Queens

Difficulty: Hard

Topic: recursion

Pattern: **Backtracking + Constraint Checking**

---

## Problem Identity

This document is specifically about:

**N Queens**

This knowledge chunk belongs to:

**recursion**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **N Queens** problem.

The primary problem-solving pattern is:

**Backtracking + Constraint Checking**

---

## Key Idea

Place one queen in each row while ensuring that no two queens share the same column or diagonal. Backtrack whenever a placement leads to an invalid state.

### Core Invariant

Before processing a row, all previously placed queens are in different columns and diagonals and therefore do not attack one another.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Try every possible placement of queens on the board and check whether the resulting arrangement is valid.

### Brute Force Complexity

- **Time Complexity:** O(N^(N)) for a straightforward brute-force placement approach.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Start with the first row.
2. Try placing a queen in each column.
3. Check whether the column is already occupied.
4. Check whether the main diagonal is occupied.
5. Check whether the anti-diagonal is occupied.
6. If the position is safe, place the queen.
7. Recursively solve the next row.
8. If the placement fails, remove the queen and try the next column.
9. When all rows are filled, record the solution.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Backtracking + Constraint Checking**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can you place exactly one queen in each row?

### Hint 2

What three conditions determine whether a position is safe?

---

## Common Mistakes

- Checking only columns and not diagonals.
- Forgetting to remove a queen during backtracking.
- Using incorrect diagonal indexing.
- Placing multiple queens in the same row.

---

## Edge Cases

- N = 1.
- N = 2.
- N = 3.
- N = 4.
- Larger N.

---

## Complexity Analysis

### Time Complexity

**O(N!) approximately for the standard backtracking solution.**

### Space Complexity

**O(N) auxiliary space for recursion and constraint tracking excluding the board and output.**

---

## Interview Explanation

A concise interview explanation for **N Queens** is:

> Place one queen in each row while ensuring that no two queens share the same column or diagonal. Backtrack whenever a placement leads to an invalid state.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- n queens
- n-queens
- backtracking
- recursion
- chess board
- diagonal checking

---

## Problem Retrieval Identity

Problem Name: N Queens

Problem ID: n_queens

Topic: recursion

Pattern: Backtracking + Constraint Checking

Difficulty: Hard

Primary Retrieval Entity:

**N Queens**

This document should be preferred when a user explicitly asks about:

- n queens
- n-queens
- backtracking
- recursion
- chess board
- diagonal checking

Related concepts:

- n queens
- n-queens
- backtracking
- recursion
- chess board
- diagonal checking
