# Arrays

## Definition

An **Array** is a linear data structure that collects elements of the same data type (homogeneous elements) stored in contiguous memory locations. It is one of the most fundamental and oldest data structures, used to implement numerous other data structures such as lists, stacks, queues, and heaps.

An array uses an index-based system to access its elements, where the index of the first element typically starts at `0` (zero-based indexing).

```
Index:      0     1     2     3     4
         +-----+-----+-----+-----+-----+
Value:   |  10 |  20 |  30 |  40 |  50 |
         +-----+-----+-----+-----+-----+
Address:  2000  2004  2008  2012  2016  (Assuming 4-byte integers)
```

---

## Why it is needed

Before arrays, if you needed to store multiple values (e.g., the test scores of 100 students), you would have to declare 100 individual variables:

```c
int score1, score2, score3, ..., score100;
```

This approach is highly impractical because:
1. **Inefficient Code Management**: Writing operations (like finding the average or maximum) requires massive, repetitive code blocks.
2. **Lack of Dynamic Access**: You cannot easily loop through variables named `score1`, `score2`, etc., using a variable index.
3. **Memory Fragmentation**: Individual variables are allocated arbitrarily across memory, destroying cache locality.

**Arrays solve these issues by:**
* Storing an entire collection under a single name (e.g., `int scores[100]`).
* Allowing mathematical access to any element in $O(1)$ constant time using its index.
* Allowing efficient traversal using loops (`for`, `while`).

---

## Characteristics

1. **Contiguous Memory Allocation**: Elements are stored sequentially in memory, with no gaps between them.
2. **Homogeneous Elements**: Every element in the array must be of the same data type (e.g., all integers, all floats, or all characters), meaning they all occupy the same size in memory.
3. **Fixed Size (Static)**: The size of a static array must be known at compile-time or allocation-time and cannot be changed dynamically during runtime.
4. **Random Access**: Elements can be accessed directly in $O(1)$ time if their index is known.
5. **Index-Based**: Elements are indexed from $0$ to $N - 1$, where $N$ is the total capacity of the array.

---

## Working

An array works by mapping logical indices ($0, 1, 2, \dots$) to physical memory addresses. Because the memory is contiguous and elements are of uniform size, computing the physical memory address of any element requires only basic arithmetic.

When you declare an array, the operating system allocates a continuous block of memory of size:

$$\text{Total Bytes} = \text{Array Capacity} \times \text{Size of Data Type}$$

When you write `arr[i]`, the computer does not scan the array sequentially. Instead, it performs a single multiplication and addition to jump directly to the target memory address.

---

## Memory Representation

The absolute memory location of an element in a 1D array is computed using its **Base Address** (the memory location of the first element, `arr[0]`) and the size of each element.

### 1D Array Address Calculation Formula
$$\text{Address}(A[i]) = \text{Base Address} (BA) + i \times W$$

Where:
* $BA$ = Base Address of the array (address of index $0$).
* $i$ = Target index.
* $W$ = Width / size of each element in bytes (e.g., $4$ bytes for `int`, $8$ bytes for `double`, $1$ byte for `char`).

#### Example:
If an integer array starts at base address $2000$ and each integer takes $4$ bytes, the address of index $3$ is:
$$\text{Address}(A[3]) = 2000 + 3 \times 4 = 2000 + 12 = 2012$$

---

### 2D Array Memory Representation
In a computer's physical RAM, memory is strictly linear (1D). Therefore, multi-dimensional arrays must be flattened into a 1D sequence using one of two layout techniques:

#### 1. Row-Major Order (Used by C, C++, Java)
Elements are stored row-by-row. First, all elements of Row 0 are stored, followed by Row 1, and so on.

$$\text{Address}(A[i][j]) = BA + (i \times C + j) \times W$$

Where:
* $C$ = Total number of columns in the 2D array.
* $i$ = Row index of the target element.
* $j$ = Column index of the target element.

#### 2. Column-Major Order (Used by Fortran, MATLAB)
Elements are stored column-by-column. First, all elements of Column 0 are stored, followed by Column 1, and so on.

$$\text{Address}(A[i][j]) = BA + (j \times R + i) \times W$$

Where:
* $R$ = Total number of rows in the 2D array.

---

## Types

### 1. One-Dimensional (1D) Array
A linear list where elements are accessed via a single index.
```c
int arr[5] = {1, 2, 3, 4, 5};
```

### 2. Multi-Dimensional Array
An array of arrays. The most common is the **Two-Dimensional (2D) Array**, represented as a grid/matrix with rows and columns.
```c
int matrix[3][4]; // 3 rows, 4 columns
```
There can also be 3D arrays (an array of matrices, like RGB pixel maps) or higher dimensions.

### 3. Static Array
The size of the array is allocated at compile-time and allocated on the **Stack**. Its size cannot be altered during execution.
```cpp
int arr[50]; // Static array of size 50
```

### 4. Dynamic Array
Allocated on the **Heap** at runtime. Its size can grow or shrink dynamically (e.g., `std::vector` in C++, `ArrayList` in Java, or `list` in Python). When a dynamic array runs out of space, it allocates a new, larger memory block (usually double the current size), copies the old elements over, and frees the old block.

---

## Operations

### 1. Traversal
Iterating through all elements of the array sequentially from index $0$ to $N-1$ to perform an action (e.g., printing, summing).

#### Example:
```
Array: [10, 20, 30]
Output: "10 20 30"
```

### 2. Insertion
Adding an element at a specific index. 
* **At End**: If there is space, we append it directly in $O(1)$ time.
* **At Beginning/Middle**: We must shift all subsequent elements to the right to clear space, which takes $O(N)$ time.

#### Example: Insert `99` at index `2` in `[10, 20, 30, 40]`
1. Shift `40` to index 4: `[10, 20, 30,  , 40]`
2. Shift `30` to index 3: `[10, 20,  , 30, 40]`
3. Insert `99` at index 2: `[10, 20, 99, 30, 40]`

### 3. Deletion
Removing an element at a specific index.
* **At End**: Decrease the logical size tracker by 1 in $O(1)$ time.
* **At Beginning/Middle**: Shift all subsequent elements to the left to fill the gap, taking $O(N)$ time.

#### Example: Delete element at index `1` from `[10, 20, 30, 40]`
1. Remove `20` (leaves a gap): `[10,  , 30, 40]`
2. Shift `30` to index 1: `[10, 30,  , 40]`
3. Shift `40` to index 2: `[10, 30, 40]`

### 4. Search
Finding the index of a target element.
* **Linear Search**: Checks each element from index $0$ to $N-1$. Works on unsorted arrays. Worst-case: $O(N)$.
* **Binary Search**: Divides search space in half. Requires a sorted array. Worst-case: $O(\log N)$.

#### Example (Linear Search): Search for `30` in `[10, 50, 30, 20]`
* Compare `10 == 30` (False)
* Compare `50 == 30` (False)
* Compare `30 == 30` (True) -> Return index `2`.

### 5. Update
Changing the value of an element at a specific index. Since it uses direct indexing, it is highly efficient.

#### Example: Update index `1` to `99` in `[10, 20, 30]`
* Direct assignment: `arr[1] = 99` -> Array becomes `[10, 99, 30]`.

---

## Time Complexity Table

| Operation | Best Case | Average Case | Worst Case | Remarks |
| :--- | :--- | :--- | :--- | :--- |
| **Access** (by index) | $O(1)$ | $O(1)$ | $O(1)$ | Instant lookup via address calculation |
| **Search (Linear)** | $O(1)$ | $O(N)$ | $O(N)$ | Element could be at the first index, middle, or end |
| **Search (Binary)** | $O(1)$ | $O(\log N)$ | $O(\log N)$ | Array must be sorted beforehand |
| **Insertion (At End)** | $O(1)$ | $O(1)$ | $O(1)$ / $O(N)$ | $O(1)$ for static/dynamic with capacity; $O(N)$ if dynamic array must resize |
| **Insertion (Middle/Start)** | $O(1)$ | $O(N)$ | $O(N)$ | Requires shifting elements to the right |
| **Deletion (At End)** | $O(1)$ | $O(1)$ | $O(1)$ | Simply decrement the array size pointer |
| **Deletion (Middle/Start)** | $O(1)$ | $O(N)$ | $O(N)$ | Requires shifting elements to the left |
| **Update** | $O(1)$ | $O(1)$ | $O(1)$ | Instant assignment via direct index |

---

## Space Complexity

* **Total Space Complexity**: $O(N)$ to store $N$ elements in the array.
* **Auxiliary Space Complexity**: $O(1)$ for in-place operations (like traversal, update, in-place reversal).

---

## Advantages

1. **Random Access**: Fast access to any element in $O(1)$ time.
2. **Cache Friendliness**: Spatial locality of reference. Because array elements are stored contiguously in memory, modern CPU cache controllers pre-fetch adjacent array elements into high-speed CPU caches, minimizing slow system RAM accesses.
3. **Memory Efficient**: Minimal memory overhead. Unlike linked lists, arrays do not store additional structural metadata like pointers (`next` or `prev`).
4. **Implementation Foundation**: Highly versatile; acts as the building block for other data structures like stacks, queues, and hash tables.

---

## Disadvantages

1. **Fixed Size**: In static arrays, size is allocated at compile-time. If the array is too small, it overflows; if too large, memory is wasted.
2. **Expensive Insertions/Deletions**: Inserting or deleting elements in the middle requires shifting elements, leading to slow $O(N)$ operations.
3. **Contiguous Memory Requirement**: Finding a large, continuous chunk of unallocated memory can fail on highly fragmented systems, even if total free memory is sufficient.

---

## Real World Applications

1. **Images and Graphics**: 2D/3D arrays are used in computer graphics where each element represents a pixel color (e.g., RGB values at coordinate `[x][y]`).
2. **Database Indices**: Storing database rows sequentially for fast index-based retrieval.
3. **Matrix Algebra**: Solving scientific and engineering equations using matrix operations represented as 2D arrays.
4. **Lookup Tables**: Fast static tables stored in arrays for immediate data extraction (e.g., ASCII value conversions, mathematical sine/cosine pre-computed tables).
5. **Operating System Scheduling**: Storing raw task buffers, page tables, or process control lists.

---

## Python Implementation

Python does not have native low-level static arrays. Python’s `list` is a dynamic array under the hood. To demonstrate clean static array behavior, the custom class below uses a fixed-capacity list with explicit operations, boundaries, and pointer management.

```python
class StaticArray:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self._capacity = capacity
        # Pre-allocate array with None values
        self._array = [None] * capacity
        self._size = 0  # Tracks the current number of active elements

    def get_size(self) -> int:
        return self._size

    def get_capacity(self) -> int:
        return self._capacity

    def get_at(self, index: int):
        """Accesses element at index in O(1) time."""
        self._validate_index(index)
        return self._array[index]

    def update_at(self, index: int, value) -> None:
        """Updates element at index in O(1) time."""
        self._validate_index(index)
        self._array[index] = value

    def insert_at(self, index: int, value) -> None:
        """Inserts an element at a given index, shifting elements to the right."""
        if self._size >= self._capacity:
            raise OverflowError("Array is full. Cannot insert.")
        
        # We allow inserting at index == self._size (appending)
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds.")

        # Shift elements to the right to make space
        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]

        self._array[index] = value
        self._size += 1

    def append(self, value) -> None:
        """Appends an element to the end in O(1) time."""
        self.insert_at(self._size, value)

    def delete_at(self, index: int) -> None:
        """Deletes an element at a given index, shifting elements to the left."""
        self._validate_index(index)

        # Shift elements to the left to close the gap
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]

        self._array[self._size - 1] = None  # Clear the last element reference
        self._size -= 1

    def search(self, target) -> int:
        """Performs a linear search. Returns index if found, else -1."""
        for i in range(self._size):
            if self._array[i] == target:
                return i
        return -1

    def traverse(self) -> None:
        """Traverses and prints active array elements."""
        elements = [str(self._array[i]) for i in range(self._size)]
        print("[" + ", ".join(elements) + "]")

    def _validate_index(self, index: int) -> None:
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of bounds for size {self._size}.")


# Driver Demonstration
if __name__ == "__main__":
    arr = StaticArray(5)
    print("--- Inserting Elements ---")
    arr.append(10)
    arr.append(20)
    arr.append(30)
    arr.traverse()  # Expected: [10, 20, 30]

    print("\n--- Inserting 99 at index 1 ---")
    arr.insert_at(1, 99)
    arr.traverse()  # Expected: [10, 99, 20, 30]

    print("\n--- Updating index 2 to 50 ---")
    arr.update_at(2, 50)
    arr.traverse()  # Expected: [10, 99, 50, 30]

    print(f"\nElement at index 1: {arr.get_at(1)}")  # Expected: 99

    print("\n--- Deleting index 1 ---")
    arr.delete_at(1)
    arr.traverse()  # Expected: [10, 50, 30]

    print(f"\nSearching for 50: Index {arr.search(50)}")  # Expected: 1
    print(f"Searching for 100: Index {arr.search(100)}")  # Expected: -1
```

---

## C++ Implementation

This C++ implementation creates a template-based static boundary-checked array on the heap, wrapping operations cleanly in a class.

```cpp
#include <iostream>
#include <stdexcept>

template <typename T>
class CustomArray {
private:
    T* arr;
    int capacity;
    int size;

    void validateIndex(int index) const {
        if (index < 0 || index >= size) {
            throw std::out_of_range("Index out of bounds");
        }
    }

public:
    // Constructor
    CustomArray(int cap) {
        if (cap <= 0) {
            throw std::invalid_argument("Capacity must be greater than zero");
        }
        capacity = cap;
        size = 0;
        arr = new T[capacity];
    }

    // Destructor to prevent memory leak
    ~CustomArray() {
        delete[] arr;
    }

    int getSize() const { return size; }
    int getCapacity() const { return capacity; }

    T getAt(int index) const {
        validateIndex(index);
        return arr[index];
    }

    void updateAt(int index, T value) {
        validateIndex(index);
        arr[index] = value;
    }

    void insertAt(int index, T value) {
        if (size >= capacity) {
            throw std::overflow_error("Array is full");
        }
        if (index < 0 || index > size) {
            throw std::out_of_range("Index out of bounds");
        }

        // Shift elements to the right
        for (int i = size; i > index; --i) {
            arr[i] = arr[i - 1];
        }

        arr[index] = value;
        size++;
    }

    void append(T value) {
        insertAt(size, value);
    }

    void deleteAt(int index) {
        validateIndex(index);

        // Shift elements to the left
        for (int i = index; i < size - 1; ++i) {
            arr[i] = arr[i + 1];
        }

        size--;
    }

    int search(T target) const {
        for (int i = 0; i < size; ++i) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }

    void traverse() const {
        std::cout << "[";
        for (int i = 0; i < size; ++i) {
            std::cout << arr[i];
            if (i < size - 1) std::cout << ", ";
        }
        std::cout << "]" << std::endl;
    }
};

int main() {
    try {
        CustomArray<int> arr(5);
        std::cout << "--- Inserting Elements ---" << std::endl;
        arr.append(10);
        arr.append(20);
        arr.append(30);
        arr.traverse(); // [10, 20, 30]

        std::cout << "\n--- Inserting 99 at index 1 ---" << std::endl;
        arr.insertAt(1, 99);
        arr.traverse(); // [10, 99, 20, 30]

        std::cout << "\n--- Deleting index 2 ---" << std::endl;
        arr.deleteAt(2);
        arr.traverse(); // [10, 99, 30]

        std::cout << "\nSearching for 99: Index " << arr.search(99) << std::endl; // Index 1
        std::cout << "Searching for 100: Index " << arr.search(100) << std::endl; // Index -1

    } catch (const std::exception& e) {
        std::cerr << "Exception: " << e.what() << std::endl;
    }
    return 0;
}
```

---

## Java Implementation

This Java implementation uses generics to build a type-safe custom sequential static-like array.

```java
public class CustomArray<T> {
    private Object[] arr;
    private int capacity;
    private int size;

    public CustomArray(int capacity) {
        if (capacity <= 0) {
            throw new IllegalArgumentException("Capacity must be greater than zero");
        }
        this.capacity = capacity;
        this.size = 0;
        this.arr = new Object[capacity];
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }

    @SuppressWarnings("unchecked")
    public T getAt(int index) {
        validateIndex(index);
        return (T) arr[index];
    }

    public void updateAt(int index, T value) {
        validateIndex(index);
        arr[index] = value;
    }

    public void insertAt(int index, T value) {
        if (size >= capacity) {
            throw new RuntimeException("Array is full");
        }
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }

        // Shift elements to the right
        for (int i = size; i > index; i--) {
            arr[i] = arr[i - 1];
        }

        arr[index] = value;
        size++;
    }

    public void append(T value) {
        insertAt(size, value);
    }

    public void deleteAt(int index) {
        validateIndex(index);

        // Shift elements to the left
        for (int i = index; i < size - 1; i++) {
            arr[i] = arr[i + 1];
        }

        arr[size - 1] = null; // Prevent memory leak
        size--;
    }

    public int search(T target) {
        for (int i = 0; i < size; i++) {
            if (arr[i].equals(target)) {
                return i;
            }
        }
        return -1;
    }

    public void traverse() {
        System.print.print("[");
        for (int i = 0; i < size; i++) {
            System.print.print(arr[i]);
            if (i < size - 1) {
                System.print.print(", ");
            }
        }
        System.print.println("]");
    }

    private void validateIndex(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index " + index + " is out of bounds for size " + size);
        }
    }

    public static void main(String[] args) {
        try {
            CustomArray<String> arr = new CustomArray<>(5);
            System.print.println("--- Inserting Strings ---");
            arr.append("Apple");
            arr.append("Banana");
            arr.append("Cherry");
            arr.traverse(); // [Apple, Banana, Cherry]

            System.print.println("\n--- Inserting 'Dragonfruit' at index 1 ---");
            arr.insertAt(1, "Dragonfruit");
            arr.traverse(); // [Apple, Dragonfruit, Banana, Cherry]

            System.print.println("\n--- Deleting index 2 ---");
            arr.deleteAt(2);
            arr.traverse(); // [Apple, Dragonfruit, Cherry]

            System.print.println("\nSearching for 'Cherry': Index " + arr.search("Cherry")); // Index 2
        } catch (Exception e) {
            e.printStacktrace();
        }
    }
}
```

---

## 3 Solved Examples

### Example 1: Reverse an Array In-Place
**Problem Statement**: Write a function that takes an array and reverses its elements in-place (without allocating a completely new array).

#### Step-by-Step Algorithm (Two-Pointer Technique):
1. Place a pointer `left` at the start of the array ($0$).
2. Place a pointer `right` at the end of the array ($N - 1$).
3. Swap the elements at `left` and `right`.
4. Increment `left` by $1$ and decrement `right` by $1$.
5. Repeat steps 3 and 4 while `left < right`.

#### Trace with `[1, 2, 3, 4, 5]`:
* Initial: `left = 0` (val `1`), `right = 4` (val `5`). Swap -> `[5, 2, 3, 4, 1]`
* Step 1: `left = 1` (val `2`), `right = 3` (val `4`). Swap -> `[5, 4, 3, 2, 1]`
* Step 2: `left = 2` (val `3`), `right = 2` (val `3`). Loop terminates because `left < right` is False.

#### Code (Python):
```python
def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        # Swap elements
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

print(reverse_array([10, 20, 30, 40]))  # Output: [40, 30, 20, 10]
```
* **Time Complexity**: $O(N)$ because we scan half the array ($N/2$ swaps).
* **Space Complexity**: $O(1)$ auxiliary space as the change is in-place.

---

### Example 2: Find Maximum and Minimum in an Array
**Problem Statement**: Find the largest and smallest elements in an unsorted array.

#### Step-by-Step Algorithm:
1. Initialize two variables `max_val` and `min_val` with the value of the first element `arr[0]`.
2. Iterate through the array from index $1$ to $N - 1$:
   * If `arr[i] > max_val`, update `max_val = arr[i]`.
   * If `arr[i] < min_val`, update `min_val = arr[i]`.
3. Return `(max_val, min_val)`.

#### Trace with `[7, 2, 9, 1, 5]`:
* Start: `max_val = 7`, `min_val = 7`.
* $i = 1$ (`2`): `2 < 7` -> `min_val = 2`.
* $i = 2$ (`9`): `9 > 7` -> `max_val = 9`.
* $i = 3$ (`1`): `1 < 2` -> `min_val = 1`.
* $i = 4$ (`5`): No updates.
* Return `(9, 1)`.

#### Code (Python):
```python
def find_min_max(arr):
    if not arr:
        return None, None
    
    min_val = arr[0]
    max_val = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
        elif arr[i] < min_val:
            min_val = arr[i]
            
    return max_val, min_val

print(find_min_max([12, 1200, 1, -5, 85]))  # Output: (1200, -5)
```
* **Time Complexity**: $O(N)$ (requires a single pass of $N-1$ comparisons).
* **Space Complexity**: $O(1)$ auxiliary space.

---

### Example 3: Two Sum (On Sorted Array)
**Problem Statement**: Given a **sorted** array of integers, find if there exist two elements that add up to a target sum. Return their indices (1-based).

#### Step-by-Step Algorithm (Two-Pointer Technique):
Since the array is sorted, we can optimize the lookup without using nested loops ($O(N^2)$) or a Hash Map ($O(N)$ space):
1. Place a `low` pointer at index $0$ and a `high` pointer at index $N - 1$.
2. Calculate current sum: `current_sum = arr[low] + arr[high]`.
3. If `current_sum == target`, return `[low + 1, high + 1]`.
4. If `current_sum < target`, we need a larger value. Increment `low` by $1$.
5. If `current_sum > target`, we need a smaller value. Decrement `high` by $1$.
6. Repeat while `low < high`.

#### Trace with `[1, 3, 4, 6, 8, 10]` and target = `14`:
* Step 1: `low = 0` (val `1`), `high = 5` (val `10`). `sum = 11 < 14` -> Increment `low`.
* Step 2: `low = 1` (val `3`), `high = 5` (val `10`). `sum = 13 < 14` -> Increment `low`.
* Step 3: `low = 2` (val `4`), `high = 5` (val `10`). `sum = 14 == 14` -> Return `[3, 6]`.

#### Code (Python):
```python
def two_sum_sorted(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low < high:
        current_sum = arr[low] + arr[high]
        if current_sum == target:
            return [low + 1, high + 1]
        elif current_sum < target:
            low += 1
        else:
            high -= 1
            
    return []

print(two_sum_sorted([1, 3, 4, 6, 8, 10], 14))  # Output: [3, 6]
```
* **Time Complexity**: $O(N)$ as each element is scanned at most once.
* **Space Complexity**: $O(1)$ auxiliary space.

---

## 5 Interview Questions with Answers

### Q1. How do you find the duplicate number in an array of $n+1$ integers where each integer is between $1$ and $n$?
**Answer:**
Since numbers are from $1$ to $n$, this can be framed as a cycle detection problem in a directed graph. We can use **Floyd's Cycle Detection Algorithm (Tortoise and Hare)** to find the duplicate in $O(N)$ time and $O(1)$ auxiliary space without modifying the array.

* **Algorithm**:
  1. Initialize `tortoise = arr[0]` and `hare = arr[0]`.
  2. Move `tortoise` by 1 step (`tortoise = arr[tortoise]`) and `hare` by 2 steps (`hare = arr[arr[hare]]`) until they meet.
  3. Reset `tortoise` to `arr[0]`. Keep `hare` at the meeting point.
  4. Move both `tortoise` and `hare` by 1 step at a time. The point where they meet again is the duplicate element.

---

### Q2. How do you rotate an array of size $N$ to the right by $k$ steps?
**Answer:**
A highly efficient in-place method uses the **Reversal Algorithm**, which runs in $O(N)$ time and $O(1)$ space.

* **Algorithm** (Assuming $k = k \pmod N$):
  1. Reverse the entire array.
  2. Reverse the first $k$ elements.
  3. Reverse the remaining $N - k$ elements.
* **Example**: Rotate `[1, 2, 3, 4, 5]` by $k = 2$.
  1. Reverse all: `[5, 4, 3, 2, 1]`
  2. Reverse first $2$: `[4, 5, 3, 2, 1]`
  3. Reverse rest: `[4, 5, 1, 2, 3]` (Done!)

---

### Q3. Explain Kadane's Algorithm for Maximum Subarray Sum.
**Answer:**
Kadane's algorithm finds the contiguous subarray within a 1D numerical array which has the largest sum in $O(N)$ time.

* **Concept**:
  Keep track of the local maximum subarray ending at the current position, and the global maximum found so far.
  For each element, decide whether to add it to the existing subarray, or start a new subarray from that element.
* **Formula**:
  $$\text{current\_sum} = \max(\text{arr}[i], \text{current\_sum} + \text{arr}[i])$$
  $$\text{global\_max} = \max(\text{global\_max}, \text{current\_sum})$$

---

### Q4. What is the difference between Array Size and Array Capacity?
**Answer:**
* **Capacity**: The total amount of physical memory allocated for the array (the maximum number of elements it *can* hold without resizing).
* **Size**: The actual number of active elements stored in the array at any given moment.
For example, in C++ `std::vector` or Java `ArrayList`, capacity is the size of the underlying buffer, while size is the current length of the dynamic array returned by `.size()`.

---

### Q5. What is the "Amortized Cost" of appending an element to a Dynamic Array?
**Answer:**
The amortized cost of an append operation in a dynamic array is $O(1)$.

* **Explanation**:
  * Most of the time, inserting an element at the end of a dynamic array takes $O(1)$ because there is pre-allocated empty space available.
  * When the array becomes completely full, a resize operation is triggered. The system allocates a new array of double the size, copies all $N$ elements to the new array, and deletes the old array. This single operation takes $O(N)$ time.
  * However, this $O(N)$ resize happens very infrequently (specifically, after $N$ append operations).
  * If you distribute (amortize) the cost of the $O(N)$ copy across the $N$ sequential $O(1)$ insertion operations, each insertion ends up with an average time complexity of $O(1)$.

$$\text{Amortized Cost} = \frac{\text{Sum of individual operations}}{\text{Total number of operations}} = \frac{O(N) + N \cdot O(1)}{N} = O(1)$$

---

## Common Mistakes

1. **Off-by-One Errors**: Accessing `arr[N]` instead of `arr[N-1]` in a loop, resulting in index out of bounds exceptions. Always remember that array indices span from $0$ to $N-1$.
2. **Memory Leak on Dynamic Deallocation**: In languages like C++, allocating arrays on the heap with `new` requires releasing them with `delete[] arr` instead of `delete arr`.
3. **Invalid Parameter Passing**: In C/C++, when you pass an array to a function, it decays into a raw pointer to its first element. The size of the array is lost. You must explicitly pass the size as an additional argument:
   ```cpp
   // INCORRECT: sizeof(arr) will return pointer size (8 bytes on 64-bit systems)
   void printArray(int arr[]) { 
       int size = sizeof(arr)/sizeof(arr[0]); 
   }
   ```
4. **Uninitialized Element Reading**: Accessing static stack arrays before writing values can read arbitrary garbage memory data, causing erratic software behavior.
5. **Inefficient Middle Operations**: Using arrays for scenarios requiring constant middle-insertion/deletions. If your application's logic demands frequent mid-point structural alterations, a **Linked List** is usually the superior design choice.

---

## Summary

* **Arrays** are contiguous, homogeneous linear data structures offering unmatched speed for direct random access ($O(1)$) due to mathematical index address projection formulas.
* They provide optimized hardware integration via **spatial locality of reference**, ensuring fast data delivery to high-speed CPU caches.
* While extremely powerful for reading and updating records, **static arrays** suffer from structural rigidness (fixed allocation) and costly elements movement processes ($O(N)$ shifting) on middle-point modifications.
* For dynamic structures, modern engines utilize **Dynamic Arrays** (like Python's Lists or C++ Vectors) which handle allocation growth dynamically behind the scenes with an amortized cost of $O(1)$ on appending.