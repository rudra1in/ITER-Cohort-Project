# Binary Search

---

## Definition

**Binary Search** is an efficient, comparison-based search algorithm used to find the position of a target value within a **sorted array** (or any sorted, indexed data structure). 

Operating on the **Divide and Conquer** paradigm, Binary Search works by repeatedly dividing the search space in half. At each step, it compares the target value with the middle element of the current search interval:
* If the target value matches the middle element, its index is returned.
* If the target value is smaller than the middle element, the search continues in the left half (lower sub-array).
* If the target value is larger than the middle element, the search continues in the right half (upper sub-array).

This elimination process reduces the search space by half with each comparison, preventing the need to examine every single element.

```
Initial Search Space:  [ 2, 5, 8, 12, 16, 23, 38, 56, 72, 91 ]   Target = 23
                                  ^
                             Middle Element
                                 (16)
                    Since 23 > 16, discard left half!
                             
New Search Space:                  [ 23, 38, 56, 72, 91 ]
                                         ^
                                    Middle Element
                                        (56)
                    Since 23 < 56, discard right half!
                             
New Search Space:                  [ 23, 38 ]
                                     ^
                                Middle Element
                                    (23) -> Found!
```

---

## Why it is needed

When searching for an element in an unsorted array, we have no choice but to use **Linear Search**, which checks each element sequentially from left to right. This takes $O(n)$ time. While acceptable for small datasets, Linear Search becomes highly inefficient as the size of the dataset ($n$) grows.

For instance, consider a system with **1 billion ($1,000,000,000$) items**:
* **Linear Search ($O(n)$):** In the worst case, it must perform **1 billion comparisons**. On a computer performing 10 million comparisons per second, this would take **100 seconds**.
* **Binary Search ($O(\log n)$):** In the worst case, it must perform at most $\approx \log_2(1,000,000,000) \approx 30$ comparisons. This takes a tiny fraction of a millisecond.

### Comparative Growth Rate
| Array Size ($n$) | Linear Search Operations ($n$) | Binary Search Operations ($\approx \log_2 n$) |
| :--- | :--- | :--- |
| $10$ | $10$ | $4$ |
| $1,000$ | $1,000$ | $10$ |
| $1,000,000$ | $1,000,000$ | $20$ |
| $1,000,000,000$ | $1,000,000,000$ | $30$ |

Hence, Binary Search is essential for building highly scalable systems, database search engines, dictionaries, and APIs handling large quantities of sorted data.

---

## Characteristics

1. **Prerequisite:** The underlying collection **must be sorted** in ascending or descending order. If the collection is not sorted, it must be sorted first ($O(n \log n)$ complexity) before applying Binary Search.
2. **Paradigm:** It follows the **Divide and Conquer** (or more specifically, **Decrease and Conquer**) algorithmic paradigm.
3. **Data Structure Dependency:** Requires **Random Access** to data elements in $O(1)$ time. This makes it highly efficient on arrays or vectors, but highly inefficient on standard Linked Lists, where finding the middle element requires $O(n)$ traversal.
4. **Non-destructive:** It does not modify or re-arrange the array during execution; it only changes pointer locations.
5. **Static Data Suitability:** Works best on data structures that are static or rarely modified, as frequent insertions/deletions require costly array re-sorting or re-arranging.

---

## Working

Binary search works by maintaining three pointers (or indexes) within the array:
* `low`: Points to the start of the current search interval.
* `high`: Points to the end of the current search interval.
* `mid`: Points to the middle element of the current interval.

### Step-by-Step Algorithm
1. Initialize `low = 0` and `high = n - 1` (where $n$ is the array length).
2. While `low <= high`:
   * Calculate the middle index:
     $$\text{mid} = \text{low} + \frac{\text{high} - \text{low}}{2}$$
   * Compare the target value with the element at the middle index (`array[mid]`):
     * **Case 1 (Target found):** If `array[mid] == target`, return `mid`.
     * **Case 2 (Target is smaller):** If `target < array[mid]`, the target can only lie in the left half. Therefore, set `high = mid - 1`.
     * **Case 3 (Target is larger):** If `target > array[mid]`, the target can only lie in the right half. Therefore, set `low = mid + 1`.
3. If the loop terminates and `low` exceeds `high` without finding the target, the target is not present in the array. Return `-1` (or an appropriate sentinel value).

---

## Memory Representation

In an array, elements are stored in **contiguous memory locations**. This allows us to calculate the exact memory location of any element in $O(1)$ time using its index:
$$\text{Address of } \text{Array}[i] = \text{Base Address} + (i \times \text{Size of element})$$

```
Array indices:     0       1       2       3       4       5       6       7       8       9
Values:        [  2  |  5  |  8  | 12  | 16  | 23  | 38  | 56  | 72  | 91  ]
Addresses:       1000    1004    1008    1012    1016    1020    1024    1028    1032    1036  (Assuming 4-byte integers)

Initially:
low  = 0 (Addr: 1000)
high = 9 (Addr: 1036)
mid  = 0 + (9 - 0) / 2 = 4 (Addr: 1016, Value: 16)
```

Because finding the midpoint is a simple arithmetic index calculation, we can jump directly to any element's memory address in $O(1)$ time. 

If we try to perform Binary Search on a **Linked List**, finding the midpoint requires traversing from the head node to the middle node step-by-step:
$$\text{Head} \rightarrow \text{Node}_1 \rightarrow \text{Node}_2 \rightarrow \dots \rightarrow \text{Node}_{\text{mid}}$$
This traversal takes $O(n)$ time, making the overall time complexity of Binary Search on a Linked List $O(n \log n)$ or $O(n)$—defeating its entire purpose.

---

## Types

There are two primary styles of implementation:

### 1. Iterative Binary Search
Uses a standard loop (`while`) to iteratively modify boundaries. It is highly optimized because it uses a constant amount of memory ($O(1)$ space).

### 2. Recursive Binary Search
Uses a recursive function that passes modified bounds of the sub-array as parameters to new stack frames. While conceptually clean, it uses $O(\log n)$ memory due to call stack overhead.

### 3. Binary Search on Answer (Monotonic Functions)
A powerful variation used when you cannot search directly in an array, but can define a monotonic decision function $f(x) \in \{\text{True}, \text{False}\}$. If the answer space is sorted (e.g., finding the minimum capacity, shortest distance, etc.), Binary Search is run on the range of possible answers.

---

## Operations

### 1. Standard Search (Find exact index)
Locates the exact index of an element in a sorted array. If duplicate elements exist, it can return the index of *any* matching element.

#### Example:
* **Array:** `[10, 20, 30, 40, 50]`, **Target:** `40`
* **Result:** `3`

---

### 2. Finding the Leftmost / First Occurrence
If duplicates exist, standard Binary Search may skip past the first instance. To find the first occurrence, when `array[mid] == target`, we do not stop; instead, we record this index as a temporary result and continue searching the left half by setting `high = mid - 1`.

```
Array: [2, 4, 4, 4, 6, 8, 10]   Target: 4
        L           M         H   -> mid = 3 (Value: 4). Record index 3. Search left half.
        L  M     H                -> mid = 1 (Value: 4). Record index 1. Search left half.
        L  H                      -> mid = 0 (Value: 2). target > 2, so low = 1.
        Loop ends (low > high). First occurrence is at index 1.
```

---

### 3. Finding the Rightmost / Last Occurrence
Conversely, to find the last occurrence, when `array[mid] == target`, we record the index and continue searching the right half by setting `low = mid + 1`.

#### Example:
* **Array:** `[2, 4, 4, 4, 6, 8, 10]`, **Target:** `4`
* **Result:** `3`

---

## Time Complexity Table

| Operation / Case | Best Case | Average Case | Worst Case |
| :--- | :--- | :--- | :--- |
| **Standard Search (Iterative)** | $O(1)$ | $O(\log n)$ | $O(\log n)$ |
| **Standard Search (Recursive)** | $O(1)$ | $O(\log n)$ | $O(\log n)$ |
| **First Occurrence Search** | $O(1)$ | $O(\log n)$ | $O(\log n)$ |
| **Last Occurrence Search** | $O(1)$ | $O(\log n)$ | $O(\log n)$ |
| **Lower Bound / Upper Bound** | $O(1)$ | $O(\log n)$ | $O(\log n)$ |

* **Best Case:** The target element is located exactly at the first midpoint index calculated (e.g., searching for `16` in `[2, 5, 8, 12, 16, 23, 38, 56, 72]`).
* **Average / Worst Case:** The target is at the extreme ends of the array, or is not present at all, requiring the maximum number of divisions ($1 + \lfloor \log_2 n \rfloor$).

---

## Space Complexity

### Iterative Implementation
* **Space Complexity:** $O(1)$ (Auxiliary/Extra space)
* **Explanation:** Only a few pointer variables (`low`, `high`, `mid`) are maintained in memory, requiring a constant amount of memory regardless of array size.

### Recursive Implementation
* **Space Complexity:** $O(\log n)$ (Auxiliary stack space)
* **Explanation:** Each recursive division adds a new frame to the function call stack. The maximum depth of the call stack is proportional to the number of splits, which is $\log_2 n$.

---

## Advantages

1. **Exceptional Speed:** An $O(\log n)$ runtime allows searching through trillions of items in under 40 comparisons.
2. **Low Memory Footprint:** The iterative variation operates in-place with a strict space complexity of $O(1)$.
3. **Versatility:** Can be extended to non-array problems like finding square roots, finding peaks in unimodal arrays, or solving complex optimization problems (Binary Search on Answer).
4. **Predictability:** The performance remains highly consistent regardless of the distribution of items in the sorted array.

---

## Disadvantages

1. **Requires Sorted Data:** Sorting an unsorted array takes $O(n \log n)$ time. Running a search on an unsorted array by first sorting it and then applying binary search is slower than a simple $O(n)$ Linear Search if you only need to run the search once.
2. **Contiguous Storage Requirement:** Requires random access, meaning memory must be allocated contiguously (arrays/vectors). This can be difficult to allocate for massive datasets on systems with highly fragmented memory.
3. **Complexity of Maintenance:** Dynamic datasets with frequent insert/delete operations require overhead to maintain sorted order (e.g., using balanced trees or skip lists, which are more complex).
4. **Overkill for Small Data:** For very small arrays (e.g., $n < 10$), the overhead of calculating midpoints and branching may make Linear Search faster in practice.

---

## Real World Applications

1. **Database Indexing:** Database engines use B-Trees and B+ Trees to index records. Traversing these trees internally utilizes binary searches on internal nodes to quickly locate records.
2. **Compiler Symbol Tables:** Compilers utilize binary search to lookup identifiers, keywords, or operators in sorted tables.
3. **Git Bisect:** Developers use the `git bisect` command to perform a binary search on the commit history to pinpoint the exact commit that introduced a bug.
4. **Standard Libraries:** Most standard libraries feature highly optimized implementations (e.g., `std::binary_search` and `std::lower_bound` in C++, `Arrays.binarySearch` in Java, and `bisect` module in Python).
5. **Network Routing:** Looking up IP routing targets in routing tables (longest prefix matching) utilizes binary search variations.

---

## Python Implementation

```python
def binary_search_iterative(arr, target):
    """
    Performs standard iterative binary search on a sorted list.
    Returns the index of target if found, otherwise returns -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Prevents integer overflow in languages, good habit in Python too
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1


def binary_search_recursive(arr, low, high, target):
    """
    Performs standard recursive binary search on a sorted list.
    Returns the index of target if found, otherwise returns -1.
    """
    if low > high:
        return -1
        
    mid = low + (high - low) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, high, target)
    else:
        return binary_search_recursive(arr, low, mid - 1, target)


# Runner Code
if __name__ == "__main__":
    sorted_array = [3, 9, 15, 20, 24, 31, 45, 56, 77, 90]
    target_value = 31
    
    print("--- Python Implementation Demo ---")
    print(f"Array: {sorted_array}")
    print(f"Target: {target_value}")
    
    # Iterative Search
    iter_result = binary_search_iterative(sorted_array, target_value)
    print(f"Iterative Result Index: {iter_result}")
    
    # Recursive Search
    recur_result = binary_search_recursive(sorted_array, 0, len(sorted_array) - 1, target_value)
    print(f"Recursive Result Index: {recur_result}")
```

---

## C++ Implementation

```cpp
#include <iostream>
#include <vector>

// Iterative Binary Search
int binarySearchIterative(const std::vector<int>& arr, int target) {
    int low = 0;
    int high = arr.size() - 1;

    while (low <= high) {
        // Safe calculation of mid to avoid potential integer overflow
        int mid = low + (high - low) / 2;

        if (arr[mid] == target) {
            return mid; 
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1; // Target not found
}

// Recursive Binary Search Helper
int binarySearchRecursiveHelper(const std::vector<int>& arr, int low, int high, int target) {
    if (low > high) {
        return -1;
    }

    int mid = low + (high - low) / 2;

    if (arr[mid] == target) {
        return mid;
    } else if (arr[mid] < target) {
        return binarySearchRecursiveHelper(arr, mid + 1, high, target);
    } else {
        return binarySearchRecursiveHelper(arr, low, mid - 1, target);
    }
}

// Recursive entry function
int binarySearchRecursive(const std::vector<int>& arr, int target) {
    return binarySearchRecursiveHelper(arr, 0, arr.size() - 1, target);
}

int main() {
    std::vector<int> sorted_array = {3, 9, 15, 20, 24, 31, 45, 56, 77, 90};
    int target_value = 31;

    std::cout << "--- C++ Implementation Demo ---" << std::endl;
    
    int iter_idx = binarySearchIterative(sorted_array, target_value);
    std::cout << "Iterative Result Index: " << iter_idx << std::endl;

    int recur_idx = binarySearchRecursive(sorted_array, target_value);
    std::cout << "Recursive Result Index: " << recur_idx << std::endl;

    return 0;
}
```

---

## Java Implementation

```java
public class BinarySearch {

    // Iterative Binary Search implementation
    public static int binarySearchIterative(int[] arr, int target) {
        int low = 0;
        int high = arr.length - 1;

        while (low <= high) {
            // Prevents integer overflow: (low + high) / 2 could exceed Integer.MAX_VALUE
            int mid = low + (high - low) / 2;

            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1; // Target not found
    }

    // Recursive Binary Search helper
    private static int binarySearchRecursiveHelper(int[] arr, int low, int high, int target) {
        if (low > high) {
            return -1;
        }

        int mid = low + (high - low) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            return binarySearchRecursiveHelper(arr, mid + 1, high, target);
        } else {
            return binarySearchRecursiveHelper(arr, low, mid - 1, target);
        }
    }

    // Recursive Binary Search entry point
    public static int binarySearchRecursive(int[] arr, int target) {
        return binarySearchRecursiveHelper(arr, 0, arr.length - 1, target);
    }

    // Main runner method
    public static void main(String[] args) {
        int[] sortedArray = {3, 9, 15, 20, 24, 31, 45, 56, 77, 90};
        int targetValue = 31;

        System.out.println("--- Java Implementation Demo ---");
        
        int iterResult = binarySearchIterative(sortedArray, targetValue);
        System.out.println("Iterative Result Index: " + iterResult);

        int recurResult = binarySearchRecursive(sortedArray, targetValue);
        System.out.println("Recursive Result Index: " + recurResult);
    }
}
```

---

## 3 Solved Examples

### Example 1: Classic Search
Find the index of `target = 23` in the array `arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]`.

#### Step-by-Step Walkthrough:
* **Initial Setup:**
  * `arr` length ($n$) = 10. Indices are 0 to 9.
  * `low` = 0, `high` = 9.

* **Iteration 1:**
  * Calculate mid: $\text{mid} = 0 + (9-0)/2 = 4$.
  * Compare value: `arr[4]` is `16`.
  * Since `target (23) > arr[4] (16)`, discard the left half.
  * Set `low = mid + 1` $\rightarrow$ `low = 5`.

* **Iteration 2:**
  * Check condition: `low (5) <= high (9)` is True.
  * Calculate mid: $\text{mid} = 5 + (9-5)/2 = 7$.
  * Compare value: `arr[7]` is `56`.
  * Since `target (23) < arr[7] (56)`, discard the right half.
  * Set `high = mid - 1` $\rightarrow$ `high = 6`.

* **Iteration 3:**
  * Check condition: `low (5) <= high (6)` is True.
  * Calculate mid: $\text{mid} = 5 + (6-5)/2 = 5$.
  * Compare value: `arr[5]` is `23`.
  * Since `arr[5] == target (23)`, the target is found!
  * **Return index 5.**

---

### Example 2: First and Last Position of Element
Find the starting and ending index of a given target value in a sorted array (e.g., `arr = [5, 7, 7, 8, 8, 10]`, `target = 8`).

#### Step-by-Step Walkthrough:
We will perform two independent Binary Searches: one for the leftmost (first) index and one for the rightmost (last) index.

##### Part A: Finding the First Occurrence
1. Initialize `low = 0`, `high = 5`, `first_occurrence = -1`.
2. **Iteration 1:**
   * $\text{mid} = 0 + (5-0)/2 = 2$.
   * `arr[2] = 7`. Since `target (8) > 7`, set `low = mid + 1` $\rightarrow$ `low = 3`.
3. **Iteration 2:**
   * $\text{mid} = 3 + (5-3)/2 = 4$.
   * `arr[4] = 8`. Target matches! 
   * **Action:** Save index `4` as a candidate (`first_occurrence = 4`), then narrow search space to the left side to see if there is an earlier occurrence: set `high = mid - 1` $\rightarrow$ `high = 3`.
4. **Iteration 3:**
   * $\text{mid} = 3 + (3-3)/2 = 3$.
   * `arr[3] = 8`. Target matches!
   * **Action:** Update candidate (`first_occurrence = 3`), then search left side: set `high = mid - 1` $\rightarrow$ `high = 2`.
5. Loop terminates (`low (3) > high (2)`). First occurrence is at **index 3**.

##### Part B: Finding the Last Occurrence
1. Initialize `low = 0`, `high = 5`, `last_occurrence = -1`.
2. **Iteration 1:**
   * $\text{mid} = 2$. `arr[2] = 7`. Set `low = 3`.
3. **Iteration 2:**
   * $\text{mid} = 4$. `arr[4] = 8`. Target matches!
   * **Action:** Save index `4` as a candidate (`last_occurrence = 4`), then narrow search space to the right side to find a later occurrence: set `low = mid + 1` $\rightarrow$ `low = 5`.
4. **Iteration 3:**
   * $\text{mid} = 5$. `arr[5] = 10`. Since `target (8) < 10`, set `high = mid - 1` $\rightarrow$ `high = 4`.
5. Loop terminates (`low (5) > high (4)`). Last occurrence is at **index 4**.

* **Final Output:** `[3, 4]`

---

### Example 3: Search in Rotated Sorted Array
An array sorted in ascending order is rotated at some pivot unknown to you beforehand (e.g., `[0,1,2,4,5,6,7]` becomes `[4,5,6,7,0,1,2]`). You are given a target value `0` to find. If found in the array, return its index; otherwise, return `-1`.

#### Core Insight:
No matter where the division pivot is, if you divide a rotated sorted array in half, at least one of the halves will always remain normally sorted.

#### Step-by-Step Walkthrough:
* **Array:** `[4, 5, 6, 7, 0, 1, 2]`, `target = 0`
* **Initial Setup:** `low = 0`, `high = 6`

1. **Iteration 1:**
   * Calculate mid: $\text{mid} = 0 + (6-0)/2 = 3$.
   * Element values: `low_val = arr[0] (4)`, `mid_val = arr[3] (7)`, `high_val = arr[6] (2)`.
   * Is `mid_val == target`? No (`7 != 0`).
   * **Determine which half is sorted:**
     * Is the left half sorted? Compare `arr[low] (4) <= arr[mid] (7)`. **Yes, it is sorted**.
     * Now, check if the target lies within this sorted left half: `(target >= 4 && target < 7)`. Since `0` does not, the target must lie in the other half.
     * Set `low = mid + 1` $\rightarrow$ `low = 4`.

2. **Iteration 2:**
   * `low = 4`, `high = 6`.
   * Calculate mid: $\text{mid} = 4 + (6-4)/2 = 5$.
   * Element values: `low_val = arr[4] (0)`, `mid_val = arr[5] (1)`, `high_val = arr[6] (2)`.
   * Is `mid_val == target`? No (`1 != 0`).
   * **Determine which half is sorted:**
     * Is the left half sorted? Compare `arr[low] (0) <= arr[mid] (1)`. **Yes, it is sorted**.
     * Now, check if target lies within this sorted left half: `(target >= 0 && target < 1)`. Yes, target `0` is in this range.
     * Set `high = mid - 1` $\rightarrow$ `high = 4`.

3. **Iteration 3:**
   * `low = 4`, `high = 4`.
   * Calculate mid: $\text{mid} = 4 + (4-4)/2 = 4$.
   * `arr[4] == 0`. Target is found!
   * **Return index 4.**

---

## 5 Interview Questions with Answers

### Q1: Find the Peak Element in a Mountain Array
**Question:** An array is a mountain array if it strictly increases to a peak element and then strictly decreases. Find the index of the peak element in $O(\log n)$ time. (e.g., `arr = [1, 3, 8, 12, 4, 2]`).

**Answer:**
We can use Binary Search by comparing the middle element with its next element:
* If `arr[mid] < arr[mid + 1]`, we are in the rising part of the mountain. The peak must be to the right. Set `low = mid + 1`.
* If `arr[mid] > arr[mid + 1]`, we are in the falling part of the mountain. The peak could be `mid` or to its left. Set `high = mid`.
* When `low == high`, the pointer points directly to the peak.

```python
def findPeakElement(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low # or high
```

---

### Q2: Search in an Infinite Sorted Array
**Question:** How would you perform Binary Search on a sorted array of infinite size (where you do not know the length of the array beforehand, and reading out-of-bounds throws an error)?

**Answer:**
We cannot set `high = len(arr) - 1`. Instead, we must dynamically find the search boundaries first using **Exponential Backoff**:
1. Start with an interval of size 1: `low = 0`, `high = 1`.
2. As long as `target` is greater than the element at `high` index, double the search range size:
   * Set `low = high`
   * Set `high = high * 2`
3. Once `target <= arr[high]` (or an index is out of bounds, handled by catching the exception), perform standard Binary Search within the range `[low, high]`.
This pre-search step runs in $O(\log p)$ where $p$ is the actual index of the target, maintaining an overall $O(\log p)$ time complexity.

---

### Q3: Calculate the Square Root of an Integer
**Question:** Implement `sqrt(x)` without using standard library functions. Compute it in $O(\log x)$ time.

**Answer:**
The square root of $x$ is guaranteed to lie in the range $[0, x]$. Since this search space is sorted and monotonic, we can perform a binary search on the answers:
* If `mid * mid == x`, then `mid` is the square root.
* If `mid * mid < x`, then `mid` could be the answer, so we record it and search the right half to find a larger integer: `low = mid + 1`.
* If `mid * mid > x`, search the left half: `high = mid - 1`.

```python
def mySqrt(x):
    if x < 2: return x
    low, high = 1, x // 2
    ans = 0
    while low <= high:
        mid = low + (high - low) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans
```

---

### Q4: Explain "Binary Search on Answer" with an Example
**Question:** What does "Binary Search on Answer" mean, and when should you use it?

**Answer:**
"Binary Search on Answer" is a technique used when the search space consists of a **range of possible solutions** rather than an array of values, and those solutions have a monotonic relation. 

If we have a decision function `canFeasiblySolve(K)` which returns `True` for any value $\ge \text{target}$ and `False` for any value $< \text{target}$ (or vice-versa), we can binary search across the range of possible values of $K$.

**Example Problems:**
* **Capacity to Ship Packages within $D$ Days:** Find the minimum ship capacity to complete delivery. The range of possible capacities is from `max_weight` to `sum_weights`. If we can ship with capacity $C$, we can also ship with any capacity $> C$.
* **Koko Eating Bananas:** Find the minimum speed $K$ to eat all bananas within $H$ hours.

---

### Q5: Why is `mid = low + (high - low) / 2` preferred over `mid = (low + high) / 2`?
**Question:** Explain why the mathematical formulation of mid calculation matters in standard programming languages.

**Answer:**
In languages with fixed-size integers (like Java, C, and C++ where standard signed `int` is 32-bit with a maximum value of $2,147,483,647$):
* If we use `(low + high) / 2` and both `low` and `high` are very large (e.g., greater than $10^9$), their sum `low + high` can exceed $2^{31}-1$.
* This causes an **integer overflow**, resulting in a negative number.
* Dividing this negative number by 2 yields a negative index, which causes an `ArrayIndexOutOfBoundsException` or memory access violation.

Using `low + (high - low) / 2` prevents overflow because it subtracts two non-negative numbers first, ensuring the intermediate values never exceed the maximum integer limit.

---

## Common Mistakes

### 1. Incorrect Loop Termination Condition
* **Mistake:** Writing `while (low < high)` instead of `while (low <= high)` for standard searches.
* **Consequence:** The loop terminates early and fails to check the final remaining element when `low == high`. If the target is located at that final index, the algorithm returns `-1` (false negative).

### 2. Pointer Updates Leading to Infinite Loops
* **Mistake:** Setting `low = mid` or `high = mid` instead of `low = mid + 1` or `high = mid - 1` in standard search.
* **Consequence:** If `low` and `high` differ by 1 (e.g., `low = 3`, `high = 4`), then `mid = 3 + (4-3)/2 = 3`. If we set `low = mid`, `low` remains `3` indefinitely, creating an **infinite loop**.

### 3. Running Binary Search on Unsorted Data
* **Mistake:** Forgetting to sort the collection prior to running binary search.
* **Consequence:** The algorithm will discard valid search spaces, leading to incorrect "not found" results.

### 4. Integer Overflow
* **Mistake:** Calculating mid as `mid = (low + high) / 2` in typed languages.
* **Consequence:** Out of bounds crashes on large array sizes.

### 5. Overusing Binary Search on Linked Lists
* **Mistake:** Attempting to binary search a linked list by traversing to find the mid element in each step.
* **Consequence:** The time complexity degrades to $O(n \log n)$, which is slower than a simple $O(n)$ linear search.

---

## Summary

* **Binary Search** is a powerful search algorithm operating on **sorted** and **directly indexed** structures.
* It operates in $O(\log n)$ time complexity by continually splitting the search interval in half.
* Iterative implementations run in $O(1)$ space, making them highly efficient, while recursive implementations require $O(\log n)$ call stack space.
* To prevent math overflow, always use the formula: `mid = low + (high - low) / 2`.
* It is widely implemented in database indices, lookup tables, and Git debug tools.