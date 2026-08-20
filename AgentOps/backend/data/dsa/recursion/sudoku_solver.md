# Sudoku Solver

Problem ID: sudoku_solver

Title: Sudoku Solver

Difficulty: Hard

Topic: recursion

Pattern: **Backtracking + Constraint Checking**

---

## Problem Identity

This document is specifically about:

**Sudoku Solver**

This knowledge chunk belongs to:

**recursion**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Sudoku Solver** problem.

The primary problem-solving pattern is:

**Backtracking + Constraint Checking**

---

## Key Idea

Fill empty cells one by one. For each empty cell, try digits from 1 to 9 and place a digit only when it does not violate the row, column, or 3x3 subgrid constraints.

### Core Invariant

Before every recursive call, all filled cells satisfy the Sudoku row, column, and subgrid constraints.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Try every possible digit in every empty cell and keep only complete boards that satisfy all Sudoku constraints.

### Brute Force Complexity

- **Time Complexity:** O(9^E), where E is the number of empty cells.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Find an empty cell.
2. Try each digit from 1 to 9.
3. Check whether the digit is valid in the current row.
4. Check whether the digit is valid in the current column.
5. Check whether the digit is valid in the corresponding 3x3 subgrid.
6. Place the digit if it is valid.
7. Recursively solve the remaining board.
8. If the recursive call fails, reset the cell and try another digit.
9. When there are no empty cells left, the Sudoku is solved.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Backtracking + Constraint Checking**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How can you determine whether a digit is safe for a cell?

### Hint 2

What three constraints must every Sudoku placement satisfy?

---

## Common Mistakes

- Checking only the row and column.
- Using the wrong 3x3 subgrid.
- Forgetting to undo an invalid placement.
- Returning success before all cells are filled.
- Modifying the board without backtracking.

---

## Edge Cases

- Already solved board.
- Board with many empty cells.
- Only one possible digit for a cell.
- Backtracking required to find the solution.

---

## Complexity Analysis

### Time Complexity

**O(9^E) in the worst case, with constraint checks reducing invalid branches.**

### Space Complexity

**O(E) recursion depth.**

---

## Interview Explanation

A concise interview explanation for **Sudoku Solver** is:

> Fill empty cells one by one. For each empty cell, try digits from 1 to 9 and place a digit only when it does not violate the row, column, or 3x3 subgrid constraints.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- sudoku solver
- sudoku
- backtracking
- recursion
- constraint satisfaction
- 3x3 grid

---

## Problem Retrieval Identity

Problem Name: Sudoku Solver

Problem ID: sudoku_solver

Topic: recursion

Pattern: Backtracking + Constraint Checking

Difficulty: Hard

Primary Retrieval Entity:

**Sudoku Solver**

This document should be preferred when a user explicitly asks about:

- sudoku solver
- sudoku
- backtracking
- recursion
- constraint satisfaction
- 3x3 grid

Related concepts:

- sudoku solver
- sudoku
- backtracking
- recursion
- constraint satisfaction
- 3x3 grid
