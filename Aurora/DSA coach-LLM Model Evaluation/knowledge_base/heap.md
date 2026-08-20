# Heap

---

## Definition

A **Heap** is a specialized, tree-based data structure that satisfies the **Heap Property** and is represented as a **Complete Binary Tree**.

*   **Complete Binary Tree Property**: A binary tree is complete if all its levels are completely filled except possibly the last level, which is filled from left to right. This structural constraint guarantees that the height of a tree with $n$ nodes is always $\Theta(\log n)$, allowing for highly efficient operations.
*   **The Heap Property**:
    *   **Max-Heap Property**: For any given node $i$ (except the root), the key of its parent is greater than or equal to its own key: 
        $$\text{Value}(\text{Parent}(i)) \ge \text{Value}(i)$$
        Consequently, the maximum key is always located at the root of the tree.
    *   **Min-Heap Property**: For any given node $i$ (except the root), the key of its parent is less than or equal to its own key:
        $$\text{Value}(\text{Parent}(i)) \le \text{Value}(i)$$
        Consequently, the minimum key is always located at the root of the tree.

```
       [Min-Heap]                  [Max-Heap]
           10                          90
          /  \                        /  \
        15    30                    80    40
       /  \   /                    /  \   /
      40  50 100                  70  75 15
```

---

## Why It Is Needed

While other data structures like unsorted/sorted arrays, linked lists, or Binary Search Trees (BST) can manage dynamic collections of elements, they fall short of optimal performance when handling **Priority-based retrieval** patterns (i.e., constantly identifying and removing the minimum or maximum element).

### Comparison with Alternative Data Structures

| Data Structure | Get Min/Max | Insert | Delete Min/Max | Search |
| :--- | :--- | :--- | :--- | :--- |
| **Unsorted Array** | $O(n)$ | $O(1)$ | $O(n)$ | $O(n)$ |
| **Sorted Array** | $O(1)$ | $O(n)$ | $O(n)$ (if shifting) | $O(\log n)$ |
| **Balanced BST** | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ |
| **Binary Heap** | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |

### Primary Motivations

1.  **Optimal Priority Queue Performance**: Priority queues require rapid insertions and rapid removals of the highest priority element. Heaps achieve $O(1)$ lookup for the extreme element and $O(\log n)$ for both insertion and deletion.
2.  **No Pointer Overhead**: Unlike balanced BSTs (e.g., AVL trees, Red-Black trees), binary heaps can be stored implicitly within a contiguous array. This eliminates pointer overhead (saving memory) and leverages spatial locality of reference for faster CPU cache access.
3.  **Fast Construction**: A heap can be constructed from an unsorted array of $n$ elements in linear $O(n)$ time using the bottom-up `buildHeap` (heapify) algorithm, whereas building a balanced BST takes $O(n \log n)$ time.

---

## Characteristics

1.  **Structural Completeness**: A heap is always a complete binary tree. Nodes are added level-by-level, from left to right. This ensures the tree remains balanced without requiring complex rotation algorithms.
2.  **Weak Ordering**: A heap enforces a vertical order (ancestor-descendant relationship) but *no* horizontal order among siblings. The left child of a node is not guaranteed to be smaller or larger than its right child.
3.  **Array Representation**: The structural completeness of the tree allows it to be mapped directly into a standard array. This means no left/right child pointers are necessary.
4.  **Non-Uniqueness**: For a given set of keys, there is no unique binary heap representation. Multiple valid heap configurations can represent the exact same set of elements.

---

## Working

The fundamental mechanics of a heap center around maintaining its two primary invariant properties: the **Shape Property** (complete binary tree) and the **Heap Property** (ordering). 

When these properties are violated during mutations (insertion or deletion), we restore them using two primary operations:

### 1. Sift-Up (Up-Heapify / Bubble-Up)
Used when a new element is added to the bottom-most, right-most vacant position in the tree (the end of the array), potentially violating the heap property if it is larger (Max-Heap) or smaller (Min-Heap) than its parent.
*   **Mechanism**: Compare the newly added node with its parent. If the ordering property is violated, swap them. Repeat this process recursively upward until the node reaches the root or its parent satisfies the heap property.

```
Inserting '55' into a Max-Heap:

     [50]                   [50]                  [55]
    /    \                 /    \                /    \
  [30]   [40]     -->    [30]   [55]     -->   [30]   [50]
  /                      /                     /
[10]                   [10]                  [10]
(Add to bottom-left)   (55 > 40: Swap!)      (55 > 50: Swap! Root reached)
```

### 2. Sift-Down (Down-Heapify / Sink-Down)
Used when the root element is removed (extracted) and replaced with the last element of the array. The root's value now likely violates the heap property.
*   **Mechanism**: Compare the root node with its two children. Swap the node with its *largest* child (in a Max-Heap) or *smallest* child (in a Min-Heap). Repeat this process downward until the node reaches a level where it satisfies the heap property relative to its children, or it becomes a leaf node.

```
Extracting Root '90' (replaced by last leaf '15'):

     [15]                   [80]                  [80]
    /    \                 /    \                /    \
  [80]   [40]     -->    [15]   [40]     -->   [70]   [40]
  /                      /                     /
[70]                   [70]                  [15]
(Root replaced by 15)  (15 swaps with 80)    (15 swaps with 70)
```

---

## Memory Representation

Because a binary heap is a complete binary tree, it is stored in contiguous memory (such as a dynamic array or vector) instead of using linked nodes with heap-allocated pointers.

### The Indexing Formulae

Using a **0-based indexing** system (where the root is at index `0`):

| Node | Index Formula |
| :--- | :--- |
| **Parent of node at index $i$** | $\text{parent}(i) = \lfloor \frac{i - 1}{2} \rfloor$ (for $i > 0$) |
| **Left Child of node at index $i$** | $\text{left}(i) = 2i + 1$ |
| **Right Child of node at index $i$** | $\text{right}(i) = 2i + 2$ |

Using a **1-based indexing** system (where the root is at index `1`):

| Node | Index Formula |
| :--- | :--- |
| **Parent of node at index $i$** | $\text{parent}(i) = \lfloor \frac{i}{2} \rfloor$ (for $i > 1$) |
| **Left Child of node at index $i$** | $\text{left}(i) = 2i$ |
| **Right Child of node at index $i$** | $\text{right}(i) = 2i + 1$ |

### Visual Layout (0-based Indexing)

```
Tree representation:
             [10] (Index 0)
            /    \
  (Index 1) [15]  [30] (Index 2)
           /   \
 (Index 3)[40] [50] (Index 4)

Array Representation:
+----+----+----+----+----+
| 10 | 15 | 30 | 40 | 50 |
+----+----+----+----+----+
  0    1    2    3    4    <-- Indices
```

---

## Types of Heaps

While the **Binary Heap** is the most common implementation, several other types of heaps offer distinct performance profiles:

### 1. Binary Heap
The standard implementation described above, using a complete binary tree.
*   **Use-case**: Standard priority queues, Heap Sort.

### 2. $d$-ary Heap
A generalization of the binary heap where each non-leaf node has $d$ children instead of 2.
*   **Pros**: Speeds up the `decreaseKey` operation because the height of the tree shrinks to $\log_d n$. Good for memory hierarchies (cache performance).
*   **Cons**: Increases the cost of deletion operations (`extractMin`/`extractMax`), which scale as $O(d \log_d n)$ because we must find the minimum/maximum child among $d$ children at each level.

### 3. Binomial Heap
A collection of binomial trees of various sizes. Binomial trees are defined recursively: a binomial tree of order $k$ has a root whose children are roots of binomial trees of orders $k-1, k-2, \dots, 0$.
*   **Pros**: Supports the union/merge of two heaps in $O(\log n)$ time, whereas a standard binary heap takes $O(n)$ time to merge.

### 4. Fibonacci Heap
A collection of heap-ordered trees, which do not constrain the structural shape of the trees as strictly as binomial heaps.
*   **Pros**: Achieves remarkable amortized performance bounds: $O(1)$ amortized for `insert`, `decreaseKey`, and `union`.
*   **Cons**: Extremely complex to implement, has high constant factors in practice, and is rarely used outside of theoretical network flow and shortest-path algorithms (e.g., Dijkstra's on sparse graphs).

---

## Operations

Here is how key heap operations are implemented for a **Min-Heap** using a 0-based indexed array.

### 1. Insertion (`insert`)
Add an element to the end of the array, then perform a Sift-Up operation to restore the heap property.

#### Step-by-Step Example (Min-Heap):
Insert element `12` into heap array `[10, 20, 30, 40]`.

1.  Append `12` at the end: `[10, 20, 30, 40, 12]`.
2.  `12` is at index $4$. Parent is at index $\lfloor(4-1)/2\rfloor = 1$, which contains `20`.
3.  Compare `12` and `20`. Since $12 < 20$, the Min-Heap property is violated. Swap them.
4.  Array becomes: `[10, 12, 30, 40, 20]`.
5.  New index of our element is $1$. Parent is at index $\lfloor(1-1)/2\rfloor = 0$, which contains `10`.
6.  Compare `12` and `10`. Since $12 \ge 10$, the heap property holds. Stop.

### 2. Extract Minimum (`extractMin`)
Retrieve the root element (index 0), swap it with the last element in the array, truncate the array, and perform Sift-Down on the new root.

#### Step-by-Step Example (Min-Heap):
Extract minimum from array `[10, 15, 30, 40, 50]`.

1.  The minimum is the root value `10`.
2.  Replace root `10` with the last element `50`.
3.  Truncate array size by 1. Array is now `[50, 15, 30, 40]`.
4.  Perform Sift-Down starting at index $0$ (value `50`):
    *   Left child: index $1$ (value `15`).
    *   Right child: index $2$ (value `30`).
    *   Identify the smaller of the children: $\min(15, 30) = 15$ at index $1$.
    *   Compare parent `50` with smaller child `15`. Since $50 > 15$, swap them.
5.  Array becomes `[15, 50, 30, 40]`.
6.  Current index of our element is $1$.
    *   Left child: index $2(1) + 1 = 3$ (value `40`).
    *   Right child: index $2(1) + 2 = 5$ (out of bounds).
    *   Smaller child is `40` at index $3$.
    *   Compare parent `50` with child `40`. Since $50 > 40$, swap them.
7.  Array becomes `[15, 40, 30, 50]`.
8.  Current index is $3$. It has no children. Stop.

### 3. Peek (`getMin` / `getMax`)
Read the root element of the heap array directly.
*   **Mechanism**: Return index $0$ of the array.
*   **Time Complexity**: $O(1)$.

### 4. Heapify (`heapify` or `buildHeap`)
Convert an arbitrary, unsorted array of size $n$ into a valid heap.

#### Why bottom-up is $O(n)$ instead of $O(n \log n)$:
If we insert $n$ elements one by one, the complexity is $O(n \log n)$. However, we can construct the heap in-place in $O(n)$ time by processing the elements in reverse index order, starting from the last non-leaf node down to the root, and calling `siftDown` on each node.

$$\text{Last Non-Leaf Node Index} = \lfloor \frac{n}{2} \rfloor - 1$$

Since leaf nodes (the bottom half of the array) already satisfy the heap property because they have no children, we do not need to sift them down. As we move up the tree, the height $h$ increases, but the number of nodes at that height decreases exponentially. The mathematical derivation of the total work is:

$$\text{Total Work} = \sum_{h=0}^{\log n} \left( \frac{n}{2^{h+1}} \right) \cdot O(h) = O\left( n \sum_{h=0}^{\log n} \frac{h}{2^h} \right) = O(n)$$

```
Unsorted Array: [20, 10, 15, 30, 5] (n = 5)
Last non-leaf index = floor(5/2) - 1 = 1 (value 10)

1. Sift-down index 1 (value 10):
   Children: index 3 (30), index 4 (5). Min child is 5.
   Swap 10 and 5. Array: [20, 5, 15, 30, 10]

2. Sift-down index 0 (value 20):
   Children: index 1 (5), index 2 (15). Min child is 5.
   Swap 20 and 5. Array: [5, 20, 15, 30, 10]
   Now, index of 20 is 1. Children: index 3 (30), index 4 (10). Min child is 10.
   Swap 20 and 10. Array: [5, 10, 15, 30, 20]

Resulting Array is a valid Min-Heap!
```

### 5. Decrease Key (`decreaseKey`)
Modify the value of a node at index $i$ to a smaller value (in a Min-Heap) and restore the heap property.
*   **Mechanism**: Update array element at index $i$ to the new value. Since the value is decreased, it may violate the heap property relative to its parent. Perform `siftUp` starting from index $i$.

### 6. Deletion (`delete`)
Remove an element at an arbitrary index $i$.
*   **Mechanism**:
    1.  Call `decreaseKey(i, -INF)` to bubble the node up to the root.
    2.  Call `extractMin()` to remove it.
    *   *Alternative*: Swap index $i$ with the last element of the array, shrink the array size by 1, and perform either `siftUp` or `siftDown` on the swapped node depending on how its value compares to its parent and children.

---

## Time Complexity Table

| Heap Operation | Binary Heap (Array) | $d$-ary Heap | Binomial Heap | Fibonacci Heap |
| :--- | :--- | :--- | :--- | :--- |
| **Get Min/Max (Peek)** | $O(1)$ | $O(1)$ | $O(\log n)$ (or $O(1)$) | $O(1)$ |
| **Insert** | $O(\log n)$ | $O(\log_d n)$ | $O(\log n)$ | $O(1)$ |
| **Extract Min/Max** | $O(\log n)$ | $O(d \log_d n)$ | $O(\log n)$ | $O(\log n)$ amortized |
| **Decrease Key** | $O(\log n)$ | $O(\log_d n)$ | $O(\log n)$ | $O(1)$ amortized |
| **Union (Merge)** | $O(n)$ | $O(n)$ | $O(\log n)$ | $O(1)$ |
| **Build Heap** | $O(n)$ | $O(n)$ | $O(n)$ | $O(n)$ |
| **Delete Element** | $O(\log n)$ | $O(d \log_d n)$ | $O(\log n)$ | $O(\log n)$ amortized |

---

## Space Complexity

*   **Total Auxiliary Space**: $O(n)$ to store $n$ elements in the array representation.
*   **In-place Heap Sort Space**: $O(1)$ auxiliary space. The input array is converted into a heap in-place, and then the sorted output is written directly back to the same array by repeatedly swapping the root element with the last unsorted element.
*   **Call Stack Space (Recursive Heapify)**: $O(\log n)$ due to the call stack of recursive heapify calls. This can be reduced to $O(1)$ by using iterative implementation of `siftUp` and `siftDown`.

---

## Advantages

1.  **Strict Performance Guarantees**: Guaranteed worst-case performance of $O(1)$ for finding the extreme element and $O(\log n)$ for insertions and deletions.
2.  **No Pointer Overheads**: Because they are mapped directly to arrays, they avoid allocating separate node blocks on the heap memory and traversing pointers, which makes them highly cache-friendly.
3.  **In-place Sorting Capability**: Heap sort runs in $O(n \log n)$ time and requires $O(1)$ extra space, unlike Merge Sort which requires $O(n)$ auxiliary space.
4.  **No Dynamic Rebalancing Code**: Unlike AVL or Red-Black trees, which require complex rotation mechanisms (single, double, left-right, right-left rotations) to maintain height-balance, a binary heap maintains balance by default because of its complete binary tree structure.

---

## Disadvantages

1.  **Inefficient Search**: Finding an arbitrary element in a heap takes $O(n)$ time. This is because heaps do not maintain any horizontal ordering constraint among sibling subtrees.
2.  **Slow Traversal**: Printing the elements of a heap in sorted order is slow. It requires copying the heap and extracting elements one-by-one, taking $O(n \log n)$ time, whereas a BST can be traversed in-order in $O(n)$ time.
3.  **Unstable Sorting**: When used for sorting (Heap Sort), the algorithm is **unstable**; it does not preserve the relative order of duplicate elements.
4.  **No Range Queries**: Operations like "find all elements between $x$ and $y$" cannot be done efficiently in a heap, unlike in a balanced BST where it takes $O(\log n + k)$ time (where $k$ is the number of keys in the range).

---

## Real World Applications

1.  **Priority Queues**: Used in operating systems for scheduling high-priority processes over background worker threads.
2.  **Graph Algorithms**:
    *   **Dijkstra's Shortest Path Algorithm**: Min-Heaps are used to extract the unvisited vertex with the minimum tentative distance.
    *   **Prim's Minimum Spanning Tree Algorithm**: Uses Min-Heaps to select the cheapest edge connecting to the growing spanning tree.
3.  **Heap Sort**: An in-place, highly robust $O(n \log n)$ sorting algorithm often used in safety-critical systems where memory usage limits are strict and worst-case time guarantees are required.
4.  **Selection Algorithms (Kth Largest/Smallest Element)**: Finding the $k$-th smallest element in a dynamic stream of data can be completed in $O(n \log k)$ time with a heap of size $k$.
5.  **Data Compression (Huffman Coding)**: Building a prefix-free binary tree requires repeatedly extracting the two lowest-frequency trees. A Min-Heap optimizes this step.
6.  **Load Balancing**: Distributing incoming network traffic across multiple servers by tracking the current load of each server in a Min-Heap.

---

## Python Implementation

Below is a complete, bug-free, iterative implementation of a generic **Min-Heap** class from scratch.

```python
class MinHeap:
    def __init__(self):
        """Initialize an empty list to represent the dynamic heap array."""
        self.heap = []

    def get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def get_left_child_index(self, index: int) -> int:
        return 2 * index + 1

    def get_right_child_index(self, index: int) -> int:
        return 2 * index + 2

    def has_parent(self, index: int) -> bool:
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index: int) -> bool:
        return self.get_left_child_index(index) < len(self.heap)

    def has_right_child(self, index: int) -> bool:
        return self.get_right_child_index(index) < len(self.heap)

    def parent(self, index: int):
        return self.heap[self.get_parent_index(index)]

    def left_child(self, index: int):
        return self.heap[self.get_left_child_index(index)]

    def right_child(self, index: int):
        return self.heap[self.get_right_child_index(index)]

    def swap(self, index_one: int, index_two: int):
        self.heap[index_one], self.heap[index_two] = self.heap[index_two], self.heap[index_one]

    def peek(self):
        """Return the minimum element without removing it."""
        if not self.heap:
            raise IndexError("Heap is empty.")
        return self.heap[0]

    def insert(self, value):
        """Insert a new element into the heap and restore heap property."""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract_min(self):
        """Remove and return the minimum element from the heap."""
        if not self.heap:
            raise IndexError("Heap is empty.")
        
        min_val = self.heap[0]
        last_val = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last_val
            self._sift_down(0)
            
        return min_val

    def _sift_up(self, index: int):
        """Iteratively sift up node at index to restore min-heap property."""
        while self.has_parent(index) and self.parent(index) > self.heap[index]:
            parent_idx = self.get_parent_index(index)
            self.swap(parent_idx, index)
            index = parent_idx

    def _sift_down(self, index: int):
        """Iteratively sift down node at index to restore min-heap property."""
        while self.has_left_child(index):
            smaller_child_idx = self.get_left_child_index(index)
            
            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smaller_child_idx = self.get_right_child_index(index)
                
            if self.heap[index] <= self.heap[smaller_child_idx]:
                break
            else:
                self.swap(index, smaller_child_idx)
                index = smaller_child_idx

    def size(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0


# Driver demonstration
if __name__ == "__main__":
    heap = MinHeap()
    elements = [15, 30, 10, 40, 50, 100, 40]
    print(f"Inserting elements sequentially: {elements}")
    for el in elements:
        heap.insert(el)
        
    print(f"Min element (peek): {heap.peek()}")
    
    print("Extracting elements in sorted order:")
    while not heap.is_empty():
        print(heap.extract_min(), end=" ")
    print()
```

---

## C++ Implementation

Here is a template-driven, object-oriented **Min-Heap** implementation in C++ using `std::vector`.

```cpp
#include <iostream>
#include <vector>
#include <stdexcept>
#include <algorithm>

template <typename T>
class MinHeap {
private:
    std::vector<T> heap;

    int getParentIndex(int i) { return (i - 1) / 2; }
    int getLeftChildIndex(int i) { return 2 * i + 1; }
    int getRightChildIndex(int i) { return 2 * i + 2; }

    bool hasParent(int i) { return getParentIndex(i) >= 0; }
    bool hasLeftChild(int i) { return getLeftChildIndex(i) < heap.size(); }
    bool hasRightChild(int i) { return getRightChildIndex(i) < heap.size(); }

    void siftUp(int index) {
        while (hasParent(index) && heap[getParentIndex(index)] > heap[index]) {
            int parentIdx = getParentIndex(index);
            std::swap(heap[parentIdx], heap[index]);
            index = parentIdx;
        }
    }

    void siftDown(int index) {
        while (hasLeftChild(index)) {
            int smallerChildIdx = getLeftChildIndex(index);
            if (hasRightChild(index) && heap[getRightChildIndex(index)] < heap[getLeftChildIndex(index)]) {
                smallerChildIdx = getRightChildIndex(index);
            }

            if (heap[index] <= heap[smallerChildIdx]) {
                break;
            } else {
                std::swap(heap[index], heap[smallerChildIdx]);
                index = smallerChildIdx;
            }
        }
    }

public:
    MinHeap() = default;

    bool isEmpty() const {
        return heap.empty();
    }

    size_t size() const {
        return heap.size();
    }

    T peek() const {
        if (heap.empty()) {
            throw std::out_of_range("Heap is empty.");
        }
        return heap[0];
    }

    void insert(T value) {
        heap.push_back(value);
        siftUp(heap.size() - 1);
    }

    T extractMin() {
        if (heap.empty()) {
            throw std::out_of_range("Heap is empty.");
        }
        T minVal = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        if (!heap.empty()) {
            siftDown(0);
        }
        return minVal;
    }
};

int main() {
    MinHeap<int> heap;
    std::vector<int> vals = {45, 10, 20, 5, 50, 15, 30};

    std::cout << "Inserting: ";
    for (int v : vals) {
        std::cout << v << " ";
        heap.insert(v);
    }
    std::cout << "\n";

    std::cout << "Extracted sequentially: ";
    while (!heap.isEmpty()) {
        std::cout << heap.extractMin() << " ";
    }
    std::cout << "\n";

    return 0;
}
```

---

## Java Implementation

Below is a robust Java generic class implementation of a standard binary **Min-Heap**.

```java
import java.util.ArrayList;
import java.util.NoSuchElementException;

public class MinHeap<T extends Comparable<T>> {
    private final ArrayList<T> heap;

    public MinHeap() {
        this.heap = new ArrayList<>();
    }

    private int getParentIndex(int index) { return (index - 1) / 2; }
    private int getLeftChildIndex(int index) { return 2 * index + 1; }
    private int getRightChildIndex(int index) { return 2 * index + 2; }

    private boolean hasParent(int index) { return getParentIndex(index) >= 0; }
    private boolean hasLeftChild(int index) { return getLeftChildIndex(index) < heap.size(); }
    private boolean hasRightChild(int index) { return getRightChildIndex(index) < heap.size(); }

    private void swap(int indexOne, int indexTwo) {
        T temp = heap.get(indexOne);
        heap.set(indexOne, heap.get(indexTwo));
        heap.set(indexTwo, temp);
    }

    public boolean isEmpty() {
        return heap.isEmpty();
    }

    public int size() {
        return heap.size();
    }

    public T peek() {
        if (heap.isEmpty()) {
            throw new NoSuchElementException("Heap is empty.");
        }
        return heap.get(0);
    }

    public void insert(T value) {
        heap.add(value);
        siftUp(heap.size() - 1);
    }

    public T extractMin() {
        if (heap.isEmpty()) {
            throw new NoSuchElementException("Heap is empty.");
        }
        T minVal = heap.get(0);
        T lastVal = heap.remove(heap.size() - 1);
        
        if (!heap.isEmpty()) {
            heap.set(0, lastVal);
            siftDown(0);
        }
        return minVal;
    }

    private void siftUp(int index) {
        while (hasParent(index) && heap.get(getParentIndex(index)).compareTo(heap.get(index)) > 0) {
            int parentIdx = getParentIndex(index);
            swap(parentIdx, index);
            index = parentIdx;
        }
    }

    private void siftDown(int index) {
        while (hasLeftChild(index)) {
            int smallerChildIdx = getLeftChildIndex(index);
            if (hasRightChild(index) && heap.get(getRightChildIndex(index)).compareTo(heap.get(getLeftChildIndex(index))) < 0) {
                smallerChildIdx = getRightChildIndex(index);
            }

            if (heap.get(index).compareTo(heap.get(smallerChildIdx)) <= 0) {
                break;
            } else {
                swap(index, smallerChildIdx);
                index = smallerChildIdx;
            }
        }
    }

    public static void main(String[] args) {
        MinHeap<Integer> heap = new MinHeap<>();
        int[] vals = {100, 19, 36, 17, 3, 25, 1, 2, 7};

        for (int v : vals) {
            heap.insert(v);
        }

        System.out.println("Extracted sequentially (Sorted Output):");
        while (!heap.isEmpty()) {
            System.out.print(heap.extractMin() + " ");
        }
        System.out.println();
    }
}
```

---

## 3 Solved Examples

### Example 1: Kth Largest Element in an Array (LeetCode 215)
Find the $k$-th largest element in an unsorted array.

#### Algorithm
1.  **Selection Strategy**: Instead of sorting the array in $O(n \log n)$ time, we can maintain a **Min-Heap** of size $k$.
2.  Iterate through the array:
    *   Add each element to our Min-Heap.
    *   If the size of the heap exceeds $k$, pop the smallest element off the heap (`extractMin`).
3.  By doing this, the Min-Heap will always hold the $k$ largest elements seen so far.
4.  At the end of the iteration, the root of the Min-Heap will be the $k$-th largest element in the overall array.

```
Array: [3, 2, 1, 5, 6, 4], k = 2

Iterate:
- Add 3: Heap = [3]
- Add 2: Heap = [2, 3]
- Add 1: Heap = [1, 3, 2] -> size = 3 > 2 -> pop! Heap = [2, 3]
- Add 5: Heap = [2, 3, 5] -> size = 3 > 2 -> pop! Heap = [3, 5]
- Add 6: Heap = [3, 5, 6] -> size = 3 > 2 -> pop! Heap = [5, 6]
- Add 4: Heap = [4, 6, 5] -> size = 3 > 2 -> pop! Heap = [5, 6]

Root of heap is 5, which is the 2nd largest element!
```

#### Code Implementation (Python)
```python
import heapq

def findKthLargest(nums: list[int], k: int) -> int:
    # Build a min-heap from first k elements
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    
    # Process remaining elements
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappushpop(min_heap, num)
            
    return min_heap[0]
```
*   **Time Complexity**: $O(n \log k)$ where $n$ is the number of elements.
*   **Space Complexity**: $O(k)$ for the min-heap.

---

### Example 2: Merge $k$ Sorted Lists (LeetCode 23)
Merge $k$ sorted linked lists into one single, sorted linked list.

#### Algorithm
1.  **Priority Strategy**: We can compare the head elements of all $k$ lists. The smallest head element should be the next node in our merged list.
2.  We maintain a **Min-Heap** containing nodes from our lists. The heap compares nodes by their scalar values.
3.  Initialize the heap by inserting the head node of each of the $k$ lists.
4.  While the heap is not empty:
    *   Pop the smallest node from the heap (`extractMin`). Append it to our merged result list.
    *   If this popped node has a next node in its original list, insert that next node into the heap.

```
Lists:
L1: 1 -> 4 -> 5
L2: 1 -> 3 -> 4
L3: 2 -> 6

1. Insert head nodes of L1, L2, L3: Min-Heap = [1(L1), 1(L2), 2(L3)]
2. Pop 1(L1). Result: 1. Push next node 4(L1): Heap = [1(L2), 4(L1), 2(L3)]
3. Pop 1(L2). Result: 1 -> 1. Push next node 3(L2): Heap = [2(L3), 4(L1), 3(L2)]
4. Pop 2(L3). Result: 1 -> 1 -> 2. Push next node 6(L3): Heap = [3(L2), 4(L1), 6(L3)]
...and so on.
```

#### Code Implementation (Python)
```python
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # We need a custom comparator to avoid conflicts in heapq
    def __lt__(self, other):
        return self.val < other.val

def mergeKLists(lists: list[ListNode]) -> ListNode:
    min_heap = []
    
    # Insert the head of each list into the heap
    for i, head in enumerate(lists):
        if head:
            # We use index 'i' as a tie-breaker for unique elements
            heapq.heappush(min_heap, (head.val, i, head))
            
    dummy = ListNode(0)
    current = dummy
    
    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))
            
    return dummy.next
```
*   **Time Complexity**: $O(n \log k)$ where $n$ is the total number of nodes across all lists, and $k$ is the number of lists.
*   **Space Complexity**: $O(k)$ for the min-heap.

---

### Example 3: Find Median from Data Stream (LeetCode 295)
Design a data structure that supports adding numbers from a data stream and finding the median of the numbers added so far.

#### Algorithm
We can divide our stream of data into two halves:
1.  **Lower Half**: We store the smaller half of the numbers in a **Max-Heap** (called `max_heap` or `left_heap`).
2.  **Upper Half**: We store the larger half of the numbers in a **Min-Heap** (called `min_heap` or `right_heap`).

This setup allows us to easily access the largest element of the lower half and the smallest element of the upper half.

```
Lower Half (Max-Heap)             Upper Half (Min-Heap)
   [Max of Lows]                     [Min of Highs]
```

##### Balancing Rules:
*   We ensure that `max_heap` has either the same number of elements as `min_heap`, or exactly one more element.
*   Thus, the difference in size is:
    $$0 \le |\text{size}(\text{max\_heap}) - \text{size}(\text{min\_heap})| \le 1$$

##### Mechanics of Insertion:
1.  Add number to `max_heap` first.
2.  Pop the maximum from `max_heap` and push it to `min_heap` to ensure the lower-half elements are smaller than the upper-half.
3.  If `min_heap` grows larger in size than `max_heap`, pop the minimum element from `min_heap` and push it back to `max_heap`.

##### Finding the Median:
*   If `len(max_heap) > len(min_heap)`: The median is simply the root of `max_heap`.
*   If `len(max_heap) == len(min_heap)`: The median is the average of the roots of both heaps:
    $$\text{Median} = \frac{\text{root}(\text{max\_heap}) + \text{root}(\text{min\_heap})}{2.0}$$

#### Code Implementation (Python)
```python
import heapq

class MedianFinder:
    def __init__(self):
        # Python does not have a native max-heap, so we store negative values in a min-heap
        self.lows = []   # Max-Heap (stores lower half)
        self.highs = []  # Min-Heap (stores upper half)

    def addNum(self, num: int) -> None:
        # Push to Max-Heap (stored as negative values)
        heapq.heappush(self.lows, -num)
        
        # Ensure every element in lows is <= every element in highs
        # Balance by shifting the max of lows to highs
        val = -heapq.heappop(self.lows)
        heapq.heappush(self.highs, val)
        
        # Balance sizes (lows can have at most 1 more element than highs)
        if len(self.highs) > len(self.lows):
            val = heapq.heappop(self.highs)
            heapq.heappush(self.lows, -val)

    def findMedian(self) -> float:
        if len(self.lows) > len(self.highs):
            return float(-self.lows[0])
        else:
            return (-self.lows[0] + self.highs[0]) / 2.0
```
*   **Time Complexity**:
    *   `addNum`: $O(\log n)$
    *   `findMedian`: $O(1)$
*   **Space Complexity**: $O(n)$ to store all numbers.

---

## 5 Interview Questions with Answers

### Q1: Why is a Binary Heap represented as an array rather than a pointer-based binary tree?
**Answer**: 
*   **Space Efficiency**: A pointer-based tree node requires left child, right child, and parent pointers. In a 64-bit architecture, each pointer takes 8 bytes (totaling 24 bytes of pointer overhead per node). An array-based heap eliminates this pointer overhead completely, saving substantial memory.
*   **Cache Locality**: Array elements are stored in contiguous memory blocks. This layout allows CPUs to load heap elements into the high-speed L1/L2 cache pre-emptively, which minimizes CPU cache misses and speeds up array traversals.
*   **Perfect Structural Balance**: Because heaps are complete binary trees, their indices form a contiguous range from $0$ to $n-1$, leaving no unused index gaps in our array representation.

---

### Q2: Prove why building a heap from an unsorted array takes $O(n)$ time instead of $O(n \log n)$ time.
**Answer**:
A binary heap of size $n$ has height $h = \lfloor \log n \rfloor$. At a given height $i$ (where $i=0$ is the leaf level and $i=h$ is the root), there are at most $\lceil n/2^{i+1} \rceil$ nodes. 

The work required to sift down a node at height $i$ is proportional to its height, $O(i)$. Therefore, the total work $S$ done by the bottom-up heap construction is:

$$S = \sum_{i=0}^{\log n} \frac{n}{2^{i+1}} \cdot O(i) = \frac{n}{2} \sum_{i=0}^{\log n} \frac{i}{2^i}$$

This summation is a classic arithmetic-geometric series:
$$\sum_{i=0}^{\infty} \frac{i}{2^i} = 2$$

Substituting this back into our formula:
$$S \approx \frac{n}{2} \cdot 2 = O(n)$$

Thus, the total work is bounded by $O(n)$, making bottom-up heap construction a linear-time operation.

---

### Q3: How can you implement a Max-Heap using a Min-Heap library (e.g., Python's standard `heapq`)?
**Answer**:
You can implement a Max-Heap using a Min-Heap library by **negating the values** before inserting them.
*   If you want to store a list of numbers $[3, 10, 5]$ in a Max-Heap, you multiply each value by $-1$ and insert them into the Min-Heap as $[-3, -10, -5]$.
*   The Min-Heap will order these negated values as:
    $$-10 < -5 < -3$$
    This places $-10$ at the root (the minimum value).
*   When retrieving or popping an element, you negate it once more to restore its original positive value:
    $$-(-10) = 10$$
    This correctly returns the maximum value first.
*   For complex objects, you can override the less-than operator (`__lt__` in Python or `compareTo` in Java) to reverse the comparison logic.

---

### Q4: What is the main difference between a Binary Heap and a Binary Search Tree (BST)?
**Answer**:

| Feature | Binary Heap | Binary Search Tree (BST) |
| :--- | :--- | :--- |
| **Ordering Property** | Vertical: Parent is always $\ge$ (max-heap) or $\le$ (min-heap) its children. No horizontal order among siblings. | Horizontal: Left child $<$ Parent $<$ Right child. Strict ordering across the entire tree. |
| **Structure** | Must be a complete binary tree. No gaps are allowed. | Can have any shape. Can become unbalanced (skewed) unless self-balancing (AVL, Red-Black). |
| **Search Cost** | $O(n)$ (requires scanning all elements). | $O(\log n)$ average/worst-case (if balanced). |
| **Use Case** | Extracting the minimum/maximum element. | Fast searching, range queries, and sorted traversals. |

---

### Q5: Can we design a heap where both `extractMin` and `extractMax` can be performed in $O(\log n)$ time?
**Answer**:
Yes, this is possible using a **Min-Max Heap** (or a **Double-Ended Priority Queue**). 

A Min-Max Heap is a complete binary tree that alternates between **Min levels** and **Max levels**:
*   The root is on a **Min level** (Level 0).
*   Its children are on a **Max level** (Level 1).
*   Its grandchildren are on a **Min level** (Level 2), and so on.

```
Level 0 (Min):         [ 6 ]                   <-- Overall Min
                      /     \
Level 1 (Max):     [ 80 ]  [ 50 ]              <-- Candidate Maxes
                   /   \    /
Level 2 (Min):   [30] [40] [10]
```

*   **Min Element**: Located at the root (index 0). Finding it takes $O(1)$ time; extracting it takes $O(\log n)$ time.
*   **Max Element**: Located among the children of the root (index 1 or index 2). Finding it takes $O(1)$ time; extracting it takes $O(\log n)$ time.

Alternatively, you can implement this by maintaining a Min-Heap and a Max-Heap side-by-side, with cross-pointers connecting matching elements. When an element is deleted from one heap, it is removed from the other heap using its corresponding pointer. This dual-heap approach also achieves $O(\log n)$ time for both operations.

---

## Common Mistakes

1.  **Confusing Heap Order with BST Order**:
    *   *Mistake*: Assuming that the left child of a node is smaller than the right child in a heap.
    *   *Correction*: Sibling nodes in a heap are completely unordered. The only guaranteed relationship is vertical: parents are larger (or smaller) than their children.
2.  **Using Sequential Insertions for Build-Heap**:
    *   *Mistake*: Creating a heap by calling `insert` $n$ times on an empty heap, which takes $O(n \log n)$ time.
    *   *Correction*: Use the bottom-up `heapify` algorithm, which converts an array to a heap in $O(n)$ time.
3.  **Off-by-One Indexing Errors**:
    *   *Mistake*: Using 1-based indexing formulas ($2i$ and $2i+1$) on a 0-based array.
    *   *Correction*: If the array is 0-indexed, the left child is at $2i+1$ and the right child is at $2i+2$.
4.  **Inefficient Search Operations**:
    *   *Mistake*: Attempting to search for an arbitrary item in a heap using a binary search algorithm.
    *   *Correction*: A heap does not maintain search tree properties. You must perform a linear scan over the array, taking $O(n)$ time.

---

## Summary

*   A **Heap** is a complete binary tree that maintains a vertical ordering constraint (the parent node is always extreme relative to its children).
*   Its complete structure allows it to be stored compactly within a **standard array**, avoiding the memory and performance overhead of pointers.
*   **Key Complexities**:
    *   **Retrieval (Min/Max)**: $O(1)$
    *   **Insertion / Deletion**: $O(\log n)$
    *   **Heap Construction (Heapify)**: $O(n)$
*   A heap is the standard underlying data structure for **Priority Queues** and is widely used in core computer science algorithms like **Dijkstra's** shortest-path, **Prim's** MST, and **Heap Sort**.