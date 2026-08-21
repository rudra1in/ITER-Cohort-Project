# Top K Frequent Elements

Problem ID: top_k_frequent_elements

Title: Top K Frequent Elements

Difficulty: Medium

Topic: heap

Pattern: **HashMap + Min Heap**

---

## Problem Identity

This document is specifically about:

**Top K Frequent Elements**

This knowledge chunk belongs to:

**heap**

Do not confuse this problem with another problem that uses a similar pattern.

---

## Problem

Solve the standard **Top K Frequent Elements** problem.

The primary problem-solving pattern is:

**HashMap + Min Heap**

---

## Key Idea

Count the frequency of every value and maintain a min heap containing only the k most frequent values.

### Core Invariant

The heap contains at most k elements and represents the k highest frequencies processed so far.

The invariant explains why binary search can eliminate part of the search space without losing the correct answer.

---

## Brute Force Approach

Count frequencies, sort all distinct elements by frequency, and return the first k.

### Brute Force Complexity

- **Time Complexity:** O(N log N)
- **Space Complexity:** O(1) auxiliary space unless otherwise required by the implementation.

---

## Optimized Approach

### Algorithm Steps

1. Use a hash map to count the frequency of every element.
2. Create a min heap ordered by frequency.
3. Insert each distinct element into the heap.
4. If the heap size exceeds k, remove the least frequent element.
5. After processing all frequencies, the heap contains the k most frequent elements.
6. Extract the elements from the heap.

### Why This Works

The optimized solution works because it exploits the structure provided by:

**HashMap + Min Heap**

The search space is reduced systematically while preserving the correct answer inside the remaining range.

---

## Hints

### Hint 1

How can you count the frequency of each element?

### Hint 2

Do you need to keep every distinct element in the heap?

---

## Common Mistakes

- Using a max heap and keeping every element.
- Forgetting to count frequencies first.
- Allowing the heap size to exceed k.
- Returning frequencies instead of the actual elements.

---

## Edge Cases

- k = 1.
- k equals the number of distinct elements.
- All elements have equal frequency.
- One element dominates the frequency.
- Duplicate values.

---

## Complexity Analysis

### Time Complexity

**O(N log K)**

### Space Complexity

**O(N)**

---

## Interview Explanation

A concise interview explanation for **Top K Frequent Elements** is:

> Count the frequency of every value and maintain a min heap containing only the k most frequent values.

When explaining this problem in an interview, focus on:

1. Why binary search is applicable.
2. What invariant is maintained.
3. How the search boundaries change.
4. Why half of the search space can be eliminated.
5. The final time and space complexity.

---

## Retrieval Keywords

- top k frequent elements
- frequency
- hashmap
- min heap
- priority queue

---

## Problem Retrieval Identity

Problem Name: Top K Frequent Elements

Problem ID: top_k_frequent_elements

Topic: heap

Pattern: HashMap + Min Heap

Difficulty: Medium

Primary Retrieval Entity:

**Top K Frequent Elements**

This document should be preferred when a user explicitly asks about:

- top k frequent elements
- frequency
- hashmap
- min heap
- priority queue

Related concepts:

- top k frequent elements
- frequency
- hashmap
- min heap
- priority queue
