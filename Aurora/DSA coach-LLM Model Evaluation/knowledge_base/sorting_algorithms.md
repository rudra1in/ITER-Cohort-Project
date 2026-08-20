# Sorting Algorithms

---

## Definition

**Sorting** is the process of arranging a collection of data elements in a specific, systematic order (typically ascending or descending) based on a well-defined ordering relation (such as numerical order or lexicographical order). 

Mathematically, given an input sequence:
$$A = \langle a_1, a_2, \dots, a_n \rangle$$

A sorting algorithm produces a permutation of the sequence:
$$A' = \langle a'_1, a'_2, \dots, a'_n \rangle$$

Such that:
$$a'_1 \le a'_2 \le \dots \le a'_n$$

---

## Why it is needed

Sorting is a fundamental building block in computer science for several reasons:

1. **Searching Optimization**: Searching for an element in an unsorted array takes linear time $\mathcal{O}(n)$. If the array is sorted, we can use binary search, reducing the search time complexity to $\mathcal{O}(\log n)$.
2. **Duplicate Detection**: Identifying duplicates in an unsorted collection requires $\mathcal{O}(n^2)$ comparison steps. On a sorted collection, duplicates lie adjacent to each other, allowing detection in a single linear pass $\mathcal{O}(n)$.
3. **Database Indexing**: Databases sort keys to construct index structures (like B-Trees or B+ Trees) that allow high-speed data retrieval.
4. **Simplifying Downstream Algorithms**: Many complex algorithms require sorted data as a preprocessing step. For example:
   * **Kruskal's Minimum Spanning Tree Algorithm** requires edges sorted by weight.
   * **Closest Pair of Points** algorithms sort coordinates to divide and conquer.
   * **Divide-and-conquer geometry algorithms** (e.g., Convex Hull via Graham Scan).
5. **Human Readability**: Users expect lists (e.g., transaction histories, directories, e-commerce products) to be sorted alphabetically, chronologically, or by numerical metrics.

---

## Characteristics

Sorting algorithms are analyzed and classified using the following system-level characteristics:

### 1. Stability
A sorting algorithm is **stable** if it preserves the relative order of records with equal keys.
* If two elements $A[i]$ and $A[j]$ have equal keys ($A[i] = A[j]$) and $i < j$ in the input, then $A[i]$ must appear before $A[j]$ in the sorted output.
* **Stable Algorithms**: Merge Sort, Insertion Sort, Bubble Sort.
* **Unstable Algorithms**: Quick Sort, Heap Sort, Selection Sort.

```
Input:  [ (Card: 5, Suit: ♠), (Card: 3, Suit: ♦), (Card: 5, Suit: ♥) ]
Stable:   [ (Card: 3, Suit: ♦), (Card: 5, Suit: ♠), (Card: 5, Suit: ♥) ]  <- ♠ remains before ♥
Unstable: [ (Card: 3, Suit: ♦), (Card: 5, Suit: ♥), (Card: 5, Suit: ♠) ]  <- Order of equal values flipped
```

### 2. In-place vs. Out-of-place
* **In-place**: An algorithm is in-place if it requires constant auxiliary memory space $\mathcal{O}(1)$ beyond the memory occupied by the input itself. (Usually, $\mathcal{O}(\log n)$ stack space for recursion is still considered in-place in broad definitions, though strictly speaking, it is not $\mathcal{O}(1)$).
  * *Examples*: Quick Sort, Heap Sort, Bubble Sort, Insertion Sort.
* **Out-of-place**: An algorithm requires extra memory proportional to the size of the input data to hold intermediate results.
  * *Examples*: Merge Sort (requires $\mathcal{O}(n)$ helper arrays), Radix Sort.

### 3. Adaptivity
An algorithm is **adaptive** if its execution time changes based on the pre-existing order of the input.
* If the input is already sorted (or nearly sorted), adaptive algorithms run faster (often $\mathcal{O}(n)$).
* *Examples of Adaptive*: Insertion Sort, Bubble Sort (with optimization flag).
* *Examples of Non-adaptive*: Selection Sort, Merge Sort (always performs the same splits and merges).

### 4. Comparison-based vs. Non-comparison-based
* **Comparison-based**: Algorithms determine the relative order of elements solely by comparing pairs of values using a comparison operator ($<, \le, >, \ge$). 
  * The mathematical lower bound for comparison-based sorting is $\Omega(n \log n)$.
* **Non-comparison-based**: Algorithms use mathematical properties of keys (e.g., integer ranges, digit distributions) to sort without direct key-to-key comparisons.
  * They can break the lower bound, achieving linear time complexity $\mathcal{O}(n)$.
  * *Examples*: Counting Sort, Radix Sort, Bucket Sort.

---

## Working

Sorting algorithms work by systematically manipulating the index locations of elements. They rely on two underlying strategies:

1. **Incremental/Iterative Strategies**: Building up a sorted sequence one element at a time (e.g., Insertion Sort shifts elements to insert the current item; Selection Sort scans for the absolute minimum and places it at the start).
2. **Divide-and-Conquer Strategies**: Recursively breaking the array down into smaller subarrays, sorting those subarrays, and then combining them (e.g., Merge Sort splits down the middle; Quick Sort partitions around a calculated pivot element).

---

## Memory Representation

How an algorithm manipulates memory heavily affects its physical execution performance.

### Array Representation (Contiguous Memory)
```
Index:    [0]   [1]   [2]   [3]   [4]
Memory:  0x100 0x104 0x108 0x10C 0x110
Value:   [ 45,  12,  89,  34,  22 ]
```
* **Cache Locality**: Contiguous arrays exhibit high spatial cache locality. When elements are compared and swapped sequentially, CPU caches load the adjacent elements, yielding extremely low latency.
* **Swapping overhead**: Exchanging large objects can be slow because the program must copy entire chunks of memory.

### Linked List Representation (Non-contiguous Memory)
```
[ Node 1: 45 ] -> [ Node 2: 12 ] -> [ Node 3: 89 ] -> [ Node 4: 34 ] -> null
```
* **No Swapping Required**: Elements are sorted by modifying next-pointers rather than copying physical memory data.
* **Poor Cache Locality**: Nodes are scattered across the heap, causing frequent CPU cache misses.
* *Algorithm preference*: Merge Sort is highly optimized for Linked Lists because it does not require auxiliary memory when working with pointers and avoids the random access limitations of lists.

---

## Types

```
                       Sorting Algorithms
                               |
        +----------------------+----------------------+
        |                                             |
Comparison-Based                               Non-Comparison-Based
  ├─ Iterative (O(n²))                           ├─ Counting Sort (O(n + k))
  │   ├─ Bubble Sort                             ├─ Radix Sort (O(d * (n + k)))
  │   ├─ Insertion Sort                          └─ Bucket Sort (O(n + k))
  │   └─ Selection Sort
  │
  └─ Divide & Conquer / Tree-Based (O(n log n))
      ├─ Merge Sort
      ├─ Quick Sort
      └─ Heap Sort
```

---

## Operations

Sorting is powered by several lower-level utility operations.

### 1. Compare
Evaluating the relationship between two values.
```
Given array: A = [15, 8]
Compare(A[0], A[1]) -> Is 15 > 8? -> True.
```

### 2. Swap
Exchanging the locations of two elements in-place.
```
Before Swap: A[i] = 15, A[j] = 8
Temp = A[i]
A[i] = A[j]
A[j] = Temp
After Swap:  A[i] = 8, A[j] = 15
```

### 3. Shift
Moving a block of elements one position to the right to clear an insertion slot. This is the core mechanic of Insertion Sort.
```
Goal: Insert key = 5 into sorted array [2, 4, 7, 9]

Step 1: Check 9 > 5 -> Shift 9 right -> [2, 4, 7, _, 9]
Step 2: Check 7 > 5 -> Shift 7 right -> [2, 4, _, 7, 9]
Step 3: Check 4 > 5 -> False -> Insert 5 at index 2 -> [2, 4, 5, 7, 9]
```

### 4. Partition
Choosing a pivot element and rearranging the array such that all elements smaller than the pivot are placed before it, and all larger elements are placed after it. This is the core mechanic of Quick Sort.
```
Array: [5, 2, 9, 1, 7, 6], Pivot = 6
After Partitioning:
[5, 2, 1]  <-- [6] <-- [9, 7]
(Left of 6 < 6)        (Right of 6 > 6)
```

### 5. Merge
Combining two pre-sorted arrays into a single, cohesive sorted array. This is the core mechanic of Merge Sort.
```
Left Array:  [3, 8]      Right Array: [2, 10]
Pointers:    L^                       R^
Target Array: [_, _, _, _]

Compare L[0] and R[0] (3 vs 2) -> Take 2.  Target: [2, _, _, _] (Advance R)
Compare L[0] and R[1] (3 vs 10) -> Take 3. Target: [2, 3, _, _] (Advance L)
Compare L[1] and R[1] (8 vs 10) -> Take 8. Target: [2, 3, 8, _] (Advance L)
Exhausted L -> Copy remaining R.          Target: [2, 3, 8, 10]
```

### 6. Heapify
Converting a binary tree into a Max-Heap or Min-Heap representation stored within an array. This is the core mechanic of Heap Sort.
```
Array representing binary tree: [4, 10, 3, 5, 1]
     4
    / \
  10   3
  / \
 5   1

Apply Heapify on Node at index 0 (value 4):
Compare 4 with its children (10, 3) -> Largest is 10. Swap 4 and 10.
     10
    /  \
   4    3
  / \
 5   1

Recursively heapify on the swapped index: Compare 4 with children (5, 1) -> Swap 4 and 5.
     10
    /  \
   5    3
  / \
 4   1
Array becomes: [10, 5, 3, 4, 1] (Valid Max-Heap)
```

---

## Time Complexity Table

The asymptotic runtime complexities of key sorting algorithms:

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity (Auxiliary) | Stable | In-Place |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Bubble Sort** | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | Yes | Yes |
| **Selection Sort** | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | No | Yes |
| **Insertion Sort** | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | Yes | Yes |
| **Merge Sort** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n)$ | Yes | No |
| **Quick Sort** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(\log n)$ (stack) | No | Yes |
| **Heap Sort** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(1)$ | No | Yes |
| **Counting Sort** | $\mathcal{O}(n + k)$ | $\mathcal{O}(n + k)$ | $\mathcal{O}(n + k)$ | $\mathcal{O}(n + k)$ | Yes | No |
| **Radix Sort** | $\mathcal{O}(d \cdot (n + k))$ | $\mathcal{O}(d \cdot (n + k))$ | $\mathcal{O}(d \cdot (n + k))$ | $\mathcal{O}(n + k)$ | Yes | No |
| **Bucket Sort** | $\mathcal{O}(n + k)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n + k)$ | Yes | No |

*Note: $k$ represents the range of the key space (max value - min value), $d$ represents the number of digits/characters in the keys, and $b$ represents the bucket count.*

---

## Space Complexity

Sorting algorithms scale in space usage based on how they process intermediate states:

* **In-place algorithms ($\mathcal{O}(1)$)**: Bubble Sort, Selection Sort, and Insertion Sort only allocate a few scalar variables for temporary storage during swapping or indexing.
* **Recursive Call Stack Space ($\mathcal{O}(\log n)$)**: Quick Sort partitions in-place, but the recursive execution path generates stack frames. With optimal pivot selection (e.g., median-of-three), the maximum height of the call stack is bounded by $\mathcal{O}(\log n)$. In the worst-case pivot strategy (skewed partitions), this stack depth can grow to $\mathcal{O}(n)$.
* **Auxiliary Space ($\mathcal{O}(n)$)**: Merge Sort breaks the array into two separate lists. Merging requires copying elements to an auxiliary array of size $n$ before writing them back to the original container.
* **Key-space Dynamic Allocation ($\mathcal{O}(n + k)$)**: Counting Sort and Radix Sort allocate memory pools proportional to the size of the alphabet/counting array ($k$) and a copy of the input size ($n$) to reassemble the output array stably.

---

## Advantages

* **Efficiency Boosts**: Transforming unsorted collections to sorted representations scales down the lookup complexity from linear to logarithmic.
* **Deterministic Behavior**: Several algorithms (like Heap Sort and Merge Sort) guarantee a worst-case performance of $\mathcal{O}(n \log n)$, ensuring safe real-time system performance.
* **Stability Support**: Preservation of secondary attributes allows sorting objects by multiple sequential conditions (e.g., sorting by "Last Name", then by "First Name").

---

## Disadvantages

* **Memory Overhead**: Merge Sort and Radix Sort demand a secondary footprint equal to or greater than the input data size, which can cause out-of-memory errors on highly constrained embedded targets.
* **Worst-Case Sinking (Quick Sort)**: Quick Sort can degrade to quadratic complexity ($\mathcal{O}(n^2)$) if pivots are chosen poorly, exposing code to Denial-of-Service attacks (Hash-flooding/Unbalanced trees).
* **High Swap Overhead**: Algorithms like Selection Sort make few swaps, but Insertion Sort and Bubble Sort perform continuous read-writes, which can degrade solid-state drive lifetimes if applied frequently on large disk-stored files.

---

## Real World Applications

1. **System Libraries**:
   * **Timsort**: A hybrid algorithm (combining Insertion Sort and Merge Sort) used in Python's `list.sort()`, Java's `Arrays.sort()` for objects, and Rust's stable sort.
   * **Introsort**: A hybrid algorithm (starts with Quick Sort, transitions to Heap Sort if recursion depth exceeds a threshold, and uses Insertion Sort for small arrays) used in C++ STL's `std::sort()`.
2. **Database Engine Merges**: Relational database management systems (RDBMS) leverage **External Merge Sort** to join datasets that are too massive to fit inside system RAM.
3. **Computer Graphics**: Sorting geometric objects back-to-front (using the Painter's Algorithm) resolves visibility and overlapping issues when rendering 3D scenes.
4. **Networking**: Packet routing schedulers sort incoming packets by priority and timestamp queues to prevent packet drops and maintain Quality of Service (QoS).

---

## Python Implementation

This implementation contains both **Merge Sort** and **Quick Sort (with randomized partitioning to guarantee $\mathcal{O}(n \log n)$ average runtime)**.

```python
import random
from typing import List

class SortingSuite:
    """
    Thread-safe, documented implementation of fundamental sorting algorithms.
    """

    @staticmethod
    def merge_sort(arr: List[int]) -> List[int]:
        """
        Sorts an array using the recursive Divide-and-Conquer Merge Sort.
        Time Complexity: O(n log n) stable
        Space Complexity: O(n) auxiliary
        """
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = SortingSuite.merge_sort(arr[:mid])
        right_half = SortingSuite.merge_sort(arr[mid:])

        return SortingSuite._merge(left_half, right_half)

    @staticmethod
    def _merge(left: List[int], right: List[int]) -> List[int]:
        merged = []
        i = j = 0

        # Scan both arrays and merge them in ascending order
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:  # <= preserves stability
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # Append remaining elements
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    @staticmethod
    def quick_sort_in_place(arr: List[int]) -> None:
        """
        Sorts an array in-place using Randomized Quick Sort.
        Time Complexity: O(n log n) average, O(n^2) worst case
        Space Complexity: O(log n) recursive call stack
        """
        SortingSuite._quick_sort_helper(arr, 0, len(arr) - 1)

    @staticmethod
    def _quick_sort_helper(arr: List[int], low: int, high: int) -> None:
        if low < high:
            pivot_idx = SortingSuite._random_partition(arr, low, high)
            SortingSuite._quick_sort_helper(arr, low, pivot_idx - 1)
            SortingSuite._quick_sort_helper(arr, pivot_idx + 1, high)

    @staticmethod
    def _random_partition(arr: List[int], low: int, high: int) -> int:
        rand_idx = random.randint(low, high)
        arr[low], arr[rand_idx] = arr[rand_idx], arr[low]  # Swap pivot to start
        return SortingSuite._partition(arr, low, high)

    @staticmethod
    def _partition(arr: List[int], low: int, high: int) -> int:
        pivot = arr[low]
        left = low + 1
        right = high

        while True:
            # Move the left pointer rightward as long as values are smaller than or equal to pivot
            while left <= right and arr[left] <= pivot:
                left += 1
            # Move the right pointer leftward as long as values are larger than pivot
            while left <= right and arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
            else:
                break

        # Swap the pivot into its correct, sorted index position
        arr[low], arr[right] = arr[right], arr[low]
        return right


# Driver Program to Validate Implementations
if __name__ == "__main__":
    # Test dataset
    test_array = [38, 27, 43, 3, 9, 82, 10]
    
    print("--- Testing Python Sorting Implementations ---")
    print(f"Original Array: {test_array}")

    # Merge Sort Execution
    sorted_merge = SortingSuite.merge_sort(test_array)
    print(f"Merge Sort Result: {sorted_merge}")

    # Quick Sort Execution
    quick_sort_target = test_array.copy()
    SortingSuite.quick_sort_in_place(quick_sort_target)
    print(f"Quick Sort Result: {quick_sort_target}")
```

---

## C++ Implementation

This implementation uses standard vectors (`std::vector`) and templates, showcasing native memory manipulation paradigms.

```cpp
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

class SortingSuite {
private:
    // Helper function to merge two sorted portions of an array
    static void merge(std::vector<int>& arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        std::vector<int> L(n1);
        std::vector<int> R(n2);

        for (int i = 0; i < n1; ++i) L[i] = arr[left + i];
        for (int j = 0; j < n2; ++j) R[j] = arr[mid + 1 + j];

        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k++] = L[i++];
            } else {
                arr[k++] = R[j++];
            }
        }

        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = R[j++];
    }

    // Standard Quick Sort Partition (Lomuto Scheme with Random Pivot)
    static int partition(std::vector<int>& arr, int low, int high) {
        // Randomize the pivot selection to prevent O(n^2) worst case on pre-sorted arrays
        int randPivotIdx = low + rand() % (high - low + 1);
        std::swap(arr[randPivotIdx], arr[high]);

        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; ++j) {
            if (arr[j] <= pivot) {
                i++;
                std::swap(arr[i], arr[j]);
            }
        }
        std::swap(arr[i + 1], arr[high]);
        return i + 1;
    }

    static void quickSortHelper(std::vector<int>& arr, int low, int high) {
        if (low < high) {
            int pivotIdx = partition(arr, low, high);
            quickSortHelper(arr, low, pivotIdx - 1);
            quickSortHelper(arr, pivotIdx + 1, high);
        }
    }

public:
    // Public Merge Sort interface
    static void mergeSort(std::vector<int>& arr, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    // Public Quick Sort interface
    static void quickSort(std::vector<int>& arr) {
        if (arr.empty()) return;
        quickSortHelper(arr, 0, arr.size() - 1);
    }
};

// Helper to print standard vectors
void printVector(const std::vector<int>& arr) {
    for (int val : arr) {
        std::cout << val << " ";
    }
    std::cout << "\n";
}

int main() {
    // Seed random number generator
    srand(static_cast<unsigned>(time(nullptr)));

    std::vector<int> data1 = {64, 34, 25, 12, 22, 11, 90};
    std::vector<int> data2 = data1;

    std::cout << "--- Testing C++ Sorting Implementations ---\n";
    std::cout << "Original Vector: ";
    printVector(data1);

    // Merge Sort
    SortingSuite::mergeSort(data1, 0, data1.size() - 1);
    std::cout << "Merge Sort Result: ";
    printVector(data1);

    // Quick Sort
    SortingSuite::quickSort(data2);
    std::cout << "Quick Sort Result: ";
    printVector(data2);

    return 0;
}
```

---

## Java Implementation

An object-oriented Java implementation of the Merge Sort and Quick Sort algorithms.

```java
import java.util.Arrays;
import java.util.Random;

public class SortingSuite {

    /**
     * Merge Sort implementation
     */
    public static void mergeSort(int[] arr) {
        if (arr == null || arr.length <= 1) return;
        mergeSortHelper(arr, 0, arr.length - 1);
    }

    private static void mergeSortHelper(int[] arr, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            mergeSortHelper(arr, left, mid);
            mergeSortHelper(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    private static void merge(int[] arr, int left, int mid, int right) {
        int[] helper = Arrays.copyOf(arr, arr.length);

        int i = left;      // Left subarray pointer
        int j = mid + 1;   // Right subarray pointer
        int k = left;      // Target original array pointer

        while (i <= mid && j <= right) {
            if (helper[i] <= helper[j]) {
                arr[k++] = helper[i++];
            } else {
                arr[k++] = helper[j++];
            }
        }

        // Copy any remaining elements from the left side
        while (i <= mid) {
            arr[k++] = helper[i++];
        }
        // Right side leftovers are already in position within the original array
    }

    /**
     * Quick Sort implementation (using randomized pivot selection)
     */
    public static void quickSort(int[] arr) {
        if (arr == null || arr.length <= 1) return;
        quickSortHelper(arr, 0, arr.length - 1);
    }

    private static void quickSortHelper(int[] arr, int low, int high) {
        if (low < high) {
            int pivotIdx = partition(arr, low, high);
            quickSortHelper(arr, low, pivotIdx - 1);
            quickSortHelper(arr, pivotIdx + 1, high);
        }
    }

    private static int partition(int[] arr, int low, int high) {
        // Random pivot to guarantee O(n log n) average case
        Random rand = new Random();
        int pivotIdx = low + rand.nextInt(high - low + 1);
        swap(arr, pivotIdx, high);

        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return i + 1;
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // Driver execution block
    public static void main(String[] args) {
        int[] data1 = {19, 9, 4, 12, 5, 20, 1, 8};
        int[] data2 = Arrays.copyOf(data1, data1.length);

        System.out.println("--- Testing Java Sorting Implementations ---");
        System.out.println("Original Array: " + Arrays.toString(data1));

        mergeSort(data1);
        System.out.println("Merge Sort Result: " + Arrays.toString(data1));

        quickSort(data2);
        System.out.println("Quick Sort Result: " + Arrays.toString(data2));
    }
}
```

---

## 3 Solved Examples

### Example 1: Dry run of Quick Sort Lomuto Partitioning
* **Input Subarray**: `[5, 2, 9, 1, 7, 6]` (where `low = 0`, `high = 5`).
* **Pivot**: Choose the last element as the pivot: `pivot = A[high] = 6`.
* **Objective**: Partition elements so that values $\le 6$ are on the left and values $> 6$ are on the right.

```
Initial Setup:
Index:    [0]  [1]  [2]  [3]  [4]  [5]
Array:     5    2    9    1    7    6  (Pivot = 6)
Pointers:  i = -1
           j = 0 -> checks 5
```

```
Step-by-Step Processing Loop:

j = 0: Is A[0] (5) <= 6? -> Yes.
       Increment i (i = 0). Swap A[i] with A[j] (5 swaps with 5 - no change).
       Array: [5, 2, 9, 1, 7, 6]

j = 1: Is A[1] (2) <= 6? -> Yes.
       Increment i (i = 1). Swap A[i] with A[j] (2 swaps with 2 - no change).
       Array: [5, 2, 9, 1, 7, 6]

j = 2: Is A[2] (9) <= 6? -> No.
       Do nothing.
       Array: [5, 2, 9, 1, 7, 6]

j = 3: Is A[3] (1) <= 6? -> Yes.
       Increment i (i = 2). Swap A[i] (9) with A[j] (1).
       Array: [5, 2, 1, 9, 7, 6]

j = 4: Is A[4] (7) <= 6? -> No.
       Do nothing.
       Array: [5, 2, 1, 9, 7, 6]

Loop Ends.

Final Step: Swap Pivot (at index high = 5) with A[i + 1] (at index 3, which is 9).
       Swap A[3] (9) with A[5] (6).
       Array: [5, 2, 1, 6, 7, 9]
```
* **Result**: Pivot `6` is now at index `3`. Elements to its left `[5, 2, 1]` are $< 6$. Elements to its right `[7, 9]` are $> 6$. The partition is successful.

---

### Example 2: Dry run of Merge Sort Recursion Tree
* **Input Array**: `[12, 11, 13, 5]`
* **Trace Diagram**:

```
                       [12, 11, 13, 5]
                        /           \
                 Split /             \ Split
                      v               v
                  [12, 11]         [13, 5]
                   /    \           /    \
            Split /      \ Split   /      \
                 v        v       v        v
               [12]      [11]   [13]      [5]
                 \        /       \        /
            Merge \      / Merge   \      / Merge
                   v    v           v    v
                  [11, 12]         [5, 13]
                      \               /
                 Merge \             / Merge
                        v           v
                       [5, 11, 12, 13]
```

**Step-by-step description**:
1. The root array `[12, 11, 13, 5]` is split into a left subarray `[12, 11]` and a right subarray `[13, 5]`.
2. Subarray `[12, 11]` is split into individual base-case units `[12]` and `[11]`.
3. `[12]` and `[11]` are merged by comparing their values ($11 < 12$), returning the sorted subarray `[11, 12]`.
4. Subarray `[13, 5]` is split into individual base-case units `[13]` and `[5]`.
5. `[13]` and `[5]` are merged ($5 < 13$), returning the sorted subarray `[5, 13]`.
6. The two sorted halves `[11, 12]` and `[5, 13]` are merged:
   * Compare 11 and 5 $\rightarrow$ take 5.
   * Compare 11 and 13 $\rightarrow$ take 11.
   * Compare 12 and 13 $\rightarrow$ take 12.
   * Copy remaining 13 $\rightarrow$ returning the final sorted array `[5, 11, 12, 13]`.

---

### Example 3: Heap Sort Heapify & Build Max-Heap
* **Input Array**: `[4, 10, 3, 5, 1]`
* **Objective**: Build a valid Max-Heap in-place, then extract elements to sort.

```
Initial Binary Tree Mapping:
       4 (Index 0)
      / \
    10   3  (Indices 1, 2)
   /  \
  5    1    (Indices 3, 4)
```

**Step 1: Build the Max-Heap.**
We run `heapify` starting from the last non-leaf node, which is at index:
$$\lfloor n/2 \rfloor - 1 = \lfloor 5/2 \rfloor - 1 = 1$$
This node corresponds to value `10`.

* **Heapify at index 1 (value 10)**:
  * Left child: index 3 (value `5`).
  * Right child: index 4 (value `1`).
  * Since `10 > 5` and `10 > 1`, the sub-heap is already a valid max-heap. No change.

* **Heapify at index 0 (value 4)**:
  * Left child: index 1 (value `10`).
  * Right child: index 2 (value `3`).
  * Since `10 > 4`, the largest value is `10` (at index 1).
  * Swap value `4` (at index 0) with `10` (at index 1).

```
Tree State (Intermediate):
       10
      /  \
     4    3
    / \
   5   1
```
* Now, recursively call `heapify` on the swapped index 1 (value `4`):
  * Left child: index 3 (value `5`).
  * Right child: index 4 (value `1`).
  * Since `5 > 4`, swap `4` with `5`.

```
Tree State (Max-Heap Complete):
       10
      /  \
     5    3
    / \
   4   1
Array State: [10, 5, 3, 4, 1]
```

**Step 2: Sorting (Extract Max).**
We repeatedly swap the root (index 0) with the last element of the active array, reduce the active heap size by 1, and run `heapify` on the root.

* **Swap root (10) with last element (1)** $\rightarrow$ array becomes `[1, 5, 3, 4, | 10]`. (10 is sorted).
* Heapify root `1` in active array `[1, 5, 3, 4]`:
  * Swap `1` with its largest child `5` $\rightarrow$ `[5, 1, 3, 4]`.
  * Swap `1` with its largest child `4` $\rightarrow$ `[5, 4, 3, 1]`.
* **Swap root (5) with last active element (1)** $\rightarrow$ array becomes `[1, 4, 3, | 5, 10]`.
* Heapify root `1` in active array `[1, 4, 3]`:
  * Swap `1` with `4` $\rightarrow$ `[4, 1, 3]`.
* **Swap root (4) with last active element (3)** $\rightarrow$ array becomes `[3, 1, | 4, 5, 10]`.
* Heapify root `3` in active array `[3, 1]`: Already valid.
* **Swap root (3) with last active element (1)** $\rightarrow$ array becomes `[1, | 3, 4, 5, 10]`.
* Final remaining element `1` is in place.
* **Sorted Array**: `[1, 3, 4, 5, 10]`.

---

## 5 Interview Questions with Answers

### Q1: Why is Quick Sort preferred over Merge Sort for sorting arrays, and vice versa for Linked Lists?
**Answer**:
1. **Cache Locality**: Quick Sort partitions elements in-place using array indexing, which exhibits excellent spatial cache locality. Merge Sort requires allocating an auxiliary array and copying elements back and forth, which incurs overhead.
2. **Auxiliary Space**: Quick Sort is in-place and requires only $\mathcal{O}(\log n)$ auxiliary space for recursive stack frames. Merge Sort requires $\mathcal{O}(n)$ auxiliary memory, which can lead to high memory consumption on large arrays.
3. **Linked Lists**: Linked lists are stored in non-contiguous heap memory, meaning we cannot perform $\mathcal{O}(1)$ random access (making Quick Sort's partitioning scheme inefficient). Merge Sort is ideal for linked lists because:
   * It does not require any dynamic $\mathcal{O}(n)$ auxiliary memory when working with linked lists; we can merge them in-place simply by rearranging the node pointers.
   * It accesses elements sequentially via list pointers, avoiding the need for random indexing.

---

### Q2: What is "Stability" in sorting, and why does it matter? Give a real-world scenario.
**Answer**:
A sorting algorithm is **stable** if it preserves the relative order of elements with equal keys. 

**Why it matters / Real-world scenario**:
Suppose you have an e-commerce order system with a list of transaction objects. Each transaction has a `Time` field and a `Location` field. 

```
Initial List (Sorted by Time):
1. [09:00 AM, Chicago]
2. [09:15 AM, New York]
3. [10:30 AM, New York]
4. [11:00 AM, Chicago]
```

If we sort this list by `Location` using a **stable** sorting algorithm, transactions from the same city will remain sorted by their original order (Time):

```
Sorted by Location (Stable):
1. [09:00 AM, Chicago]
2. [11:00 AM, Chicago]   <- Time order preserved
3. [09:15 AM, New York]
4. [10:30 AM, New York]  <- Time order preserved
```

If we use an **unstable** sorting algorithm (like Quick Sort), the chronological order of transactions within Chicago or New York might be scrambled, making it harder to perform multi-key sorting.

---

### Q3: How do you find the $k$-th smallest element in an unsorted array in $\mathcal{O}(n)$ average time?
**Answer**:
This can be solved in $\mathcal{O}(n)$ average time using the **QuickSelect** algorithm, which is based on the Quick Sort partitioning mechanism.

Unlike Quick Sort, which recursively processes both halves of the partitioned array, QuickSelect only recurses into the half that contains the target index $k$.

**Algorithm steps**:
1. Choose a random pivot and partition the array around it. This places the pivot at its correct sorted index, say `p`.
2. If `p == k - 1`, we have found the $k$-th smallest element and return it.
3. If `p > k - 1`, recursively search only the left subarray.
4. If `p < k - 1`, recursively search only the right subarray.

**Complexity**:
* **Average Case**: Since we only recurse into one half of the partition at each step, the recurrence relation is:
  $$T(n) = T(n/2) + \mathcal{O}(n) = \mathcal{O}(n)$$
* **Worst Case**: If the partitions are highly unbalanced (e.g., if we select the minimum or maximum element as the pivot every time), the runtime degrades to $\mathcal{O}(n^2)$. This worst case can be avoided by choosing a random pivot.

---

### Q4: What is the theoretical lower bound for comparison-based sorting algorithms, and how is it proven?
**Answer**:
The theoretical lower bound for any comparison-based sorting algorithm is $\Omega(n \log n)$ in the worst case.

**Proof via Decision Tree Model**:
1. Any comparison-based sorting algorithm can be represented as a binary decision tree where:
   * Each internal node represents a comparison between two elements ($a_i \le a_j$).
   * Each leaf node represents a unique sorted permutation of the input elements.
2. An array of $n$ elements has $n!$ possible permutations. To sort the array correctly, the decision tree must have at least $n!$ leaves (since each possible input order must map to a unique leaf node to be sorted correctly).
3. A binary tree of height $h$ can have at most $2^h$ leaves. Therefore:
   $$2^h \ge n!$$
4. Taking the base-2 logarithm of both sides:
   $$h \ge \log_2(n!)$$
5. Using **Stirling's Approximation** for factorials ($\log_2(n!) \approx n \log_2 n - n \log_2 e$), we get:
   $$h \ge \Omega(n \log n)$$

Since the height $h$ of the decision tree represents the maximum number of comparisons needed in the worst case, any comparison-based sort must make at least $\Omega(n \log n)$ comparisons.

---

### Q5: When would you prefer counting sort or radix sort over quicksort or mergesort? What are their limitations?
**Answer**:
**When to prefer**:
Non-comparison sorting algorithms like **Counting Sort** or **Radix Sort** are preferred when the keys are integers (or objects with integer keys) and the range of those keys ($k$) is relatively small compared to the number of elements ($n$). Under these conditions, they can sort data in linear time $\mathcal{O}(n)$, which is faster than the $\mathcal{O}(n \log n)$ limit of comparison-based algorithms.

**Limitations**:
1. **Type restriction**: They require keys to be integers, characters, or values that can be mapped to a finite integer range. They cannot easily handle floating-point numbers or arbitrary string structures without complex conversions.
2. **Memory overhead**: Counting Sort requires allocating an auxiliary array of size $k$ (the range of the data). If the input array is `[1, 2, 1000000000]`, $n = 3$ but $k = 1,000,000,000$. This would require gigabytes of memory to sort just three numbers, making it highly inefficient.
3. **No cache locality benefit**: Because they place elements into buckets or count arrays based on key values, they often access memory in a non-contiguous pattern, which can lead to frequent cache misses.

---

## Common Mistakes

### 1. Stack Overflow with Quick Sort
Using Quick Sort on a pre-sorted or nearly-sorted array without choosing a random pivot (such as always picking the first or last element). This causes the partition sizes to be completely unbalanced ($0$ and $n-1$), which degrades the time complexity to $\mathcal{O}(n^2)$ and can lead to a stack overflow due to $n$ recursive calls.
* **Fix**: Always use a randomized pivot strategy or a "median-of-three" pivot selection to keep the partitions balanced.

### 2. Off-by-One Errors in Merging
An off-by-one error when calculating the midpoint or partitioning boundaries:
```cpp
// Incorrect mid calculation (can cause infinite recursion)
int mid = (left + right) / 2; // Can overflow for large indices
// Correct mid calculation
int mid = left + (right - left) / 2;
```

### 3. Modifying Stable Algorithms to be Unstable
When writing the merge step in Merge Sort, using a strict inequality instead of a non-strict inequality:
```python
# Unstable Merge Sort Comparison (strict inequality)
if left[i] < right[j]:
    merged.append(left[i])

# Stable Merge Sort Comparison (preserves original order of equal elements)
if left[i] <= right[j]:
    merged.append(left[i])
```

### 4. Overlooking the Space Overhead of Merge Sort
Assuming Merge Sort is memory-efficient because its time complexity is $\mathcal{O}(n \log n)$. This is a common mistake on memory-constrained systems (like embedded systems or microcontrollers), where allocating the $\mathcal{O}(n)$ auxiliary array required for the merge step can easily exhaust the available heap memory.

---

## Summary

To choose the best sorting algorithm for your use case, consider the following trade-offs:

* Use **Insertion Sort** for small datasets ($n < 15$) or nearly-sorted arrays. It has very low overhead and runs in linear time $\mathcal{O}(n)$ in the best case.
* Use **Quick Sort** for general-purpose in-memory sorting of arrays. It is highly optimized for cache performance and runs in $\mathcal{O}(n \log n)$ on average.
* Use **Merge Sort** when you need a stable sort or when sorting linked lists where pointer manipulation makes merging cheap.
* Use **Heap Sort** when you need guaranteed $\mathcal{O}(n \log n)$ performance and cannot afford the $\mathcal{O}(n)$ memory overhead of Merge Sort or the rare $\mathcal{O}(n^2)$ worst case of Quick Sort.
* Use **Counting Sort** or **Radix Sort** when sorting integers within a well-defined, relatively small range, allowing you to bypass the comparison limit and sort in $\mathcal{O}(n)$ time.