# Find Median from Data Stream

Problem ID: find_median_from_data_stream

Title: Find Median from Data Stream

Difficulty: Hard

Topic: heap

Pattern: **Two Heaps**

---

## Problem Identity

This document is specifically about:

**Find Median from Data Stream**

This knowledge chunk belongs to:

**heap**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Find Median from Data Stream** problem.

The primary problem-solving pattern is:

**Two Heaps**

---

## Key Idea

Maintain two heaps: a max heap for the smaller half of numbers and a min heap for the larger half. Keep their sizes balanced so the median can be obtained efficiently.

### Core Invariant

Every element in the max heap is less than or equal to every element in the min heap, and the heap sizes differ by at most one.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Store all numbers, sort them whenever the median is requested, and calculate the middle value.

### Brute Force Complexity

- **Time Complexity:** O(N log N) for each median query if sorting is performed each time.
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Maintain a max heap containing the smaller half.
2. Maintain a min heap containing the larger half.
3. Insert each new number into the appropriate heap.
4. Rebalance the heaps if their size difference exceeds one.
5. If both heaps have equal size, average their roots.
6. Otherwise the root of the larger heap is the median.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**Two Heaps**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

Can you divide the numbers into a smaller half and a larger half?

### Hint 2

Which heap should represent each half?

---

## Common Mistakes

- Using only one heap.
- Not maintaining the size difference.
- Using the wrong root when calculating the median.
- Forgetting to rebalance after insertion.

---

## Edge Cases

- First element.
- Two elements.
- Odd number of elements.
- Even number of elements.
- Duplicate values.
- Negative values.

---

## Complexity Analysis

### Time Complexity

**O(log N) per insertion and O(1) per median query.**

### Space Complexity

**O(N)**

---

## Interview Explanation

A concise interview explanation for **Find Median from Data Stream** is:

> Maintain two heaps: a max heap for the smaller half of numbers and a min heap for the larger half. Keep their sizes balanced so the median can be obtained efficiently.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- median from data stream
- find median
- two heaps
- max heap
- min heap

---

## Problem Retrieval Identity

Problem Name: Find Median from Data Stream

Problem ID: find_median_from_data_stream

Topic: heap

Pattern: Two Heaps

Difficulty: Hard

Primary Retrieval Entity:

**Find Median from Data Stream**

This document should be preferred when a user explicitly asks about:

- median from data stream
- find median
- two heaps
- max heap
- min heap

Related concepts:

- median from data stream
- find median
- two heaps
- max heap
- min heap
