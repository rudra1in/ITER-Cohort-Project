# Queue

## Definition

A **Queue** is a linear data structure that follows the **FIFO (First-In-First-Out)** principle. This means that the element inserted first into the queue will be the first one to be removed. 

It mimics a real-world queue (such as a line of people waiting to buy a ticket): the person who arrives first is served first, and any newcomer joins at the end of the line.

```
       Back/Rear (Insertion End)                 Front/Head (Deletion End)
      +-----------------------------------------------------------------+
In -> |  Element N  |  Element 3  |  Element 2  |  Element 1 (Oldest)   | -> Out
      +-----------------------------------------------------------------+
```

A queue has two main pointers:
*   **Front (or Head):** Points to the first/oldest element in the queue (where deletion occurs).
*   **Rear (or Tail/Back):** Points to the last/newest element in the queue (where insertion occurs).

---

## Why it is needed

Queues are essential in computer science whenever resources need to be shared among multiple entities but must be processed sequentially to maintain order and fairness.

1. **Asynchronous Data Transfer:** When data is sent between processes or devices but not necessarily received at the same rate (e.g., IO buffers, file writing, pipe streams).
2. **Resource Scheduling:** Managing shared system resources like CPU scheduling (Round Robin), Disk scheduling, or handling print jobs in a print spooler.
3. **Breadth-First Search (BFS):** In graph and tree traversal algorithms, a queue is used to keep track of nodes that have been discovered but not yet fully processed.
4. **Decoupling Architectures:** In modern system design, message queues (e.g., RabbitMQ, Apache Kafka) are used to decouple microservices, allowing them to communicate asynchronously.

---

## Characteristics

*   **Ordered Structure:** The chronological order of arrival is strictly preserved.
*   **Sequential Access:** Random access to arbitrary elements in the middle of a queue is not allowed without removing the preceding elements.
*   **Dual Entry Points:** Unlike a Stack (which is single-ended), a Queue operates on both ends: insertions at the `rear` and deletions at the `front`.

---

## Working

To understand how a queue works, let's visualize a sequential array-based queue of size 4.

1. **Initialization:**
   * `front = -1`, `rear = -1` (Queue is empty)

2. **Enqueue(10):**
   * Since the queue is empty, set `front = 0` and `rear = 0`.
   * Store `10` at index `0`.
   * Queue state: `[10, _, _, _]`, `front = 0`, `rear = 0`.

3. **Enqueue(20):**
   * Increment `rear` to `1`.
   * Store `20` at index `1`.
   * Queue state: `[10, 20, _, _]`, `front = 0`, `rear = 1`.

4. **Enqueue(30):**
   * Increment `rear` to `2`.
   * Store `30` at index `2`.
   * Queue state: `[10, 20, 30, _]`, `front = 0`, `rear = 2`.

5. **Dequeue():**
   * Retrieve the element at `front` (`10`).
   * Increment `front` to `1`.
   * Queue state: `[_, 20, 30, _]`, `front = 1`, `rear = 2`.

6. **Dequeue():**
   * Retrieve the element at `front` (`20`).
   * Increment `front` to `2`.
   * Queue state: `[_, _, 30, _]`, `front = 2`, `rear = 2`.

---

## Memory Representation

A queue can be represented in memory in two primary ways:

### 1. Sequential (Array-Based) Representation
Elements are stored in contiguous memory blocks. 
* **Static Queue:** Uses a fixed-size array. If the queue is full and we try to add an item, an *overflow* condition occurs.
* **Circular Queue:** Uses a circular array where the last position wraps around to the first position. This prevents "false overflow" where memory space at the front is wasted after deletions.

```
Index:    [0]   [1]   [2]   [3]
Array:  | 10  | 20  | 30  | 40  |
          ^                 ^
        Front              Rear
```

### 2. Linked List Representation
Elements are stored as dynamic nodes in non-contiguous memory locations.
* Each node contains a data field and a pointer (`next`) pointing to the successive element.
* The `front` pointer tracks the head node, and the `rear` pointer tracks the tail node.
* **No capacity issues:** It can grow dynamically without causing an overflow (until system memory is exhausted).

```
  Front                                       Rear
  +----+----+    +----+----+    +----+------+
  | 10 | --*---> | 20 | --*---> | 30 | NULL |
  +----+----+    +----+----+    +----+------+
```

---

## Types

### 1. Simple Queue (Linear Queue)
* Insertions take place strictly at the `rear` and deletions strictly at the `front`.
* **Drawback:** Once the `rear` reaches the last index, we cannot insert any more elements, even if there are free slots at the front (caused by previous dequeues).

### 2. Circular Queue
* The last slot of the queue is connected back to the first slot.
* It avoids memory wastage of linear queues by utilizing empty slots at the beginning of the array.
* Insertion is calculated using modulo arithmetic: `rear = (rear + 1) % capacity`.

```
          [0] (Empty)
         /   \
   [3] 40     [1] 20  <-- Front
         \   /
          [2] 30  <-- Rear
```

### 3. Double-Ended Queue (Deque)
* A generalized queue where insertion and deletion can be performed at **both** ends (Front and Rear).
* Types of Deque:
  * **Input-restricted Deque:** Insertion only at one end, deletions at both ends.
  * **Output-restricted Deque:** Deletion only at one end, insertions at both ends.

### 4. Priority Queue
* Each element is assigned a priority.
* Elements are served based on their priority:
  * High-priority elements are dequeued before low-priority ones.
  * If elements have the same priority, they are served based on their FIFO order.
* Typically implemented using a Heap data structure for efficiency.

---

## Operations

### 1. Enqueue
Inserts an element at the rear of the queue.

* **Example (Fixed-Size Queue):**
  If Queue is `[5, 12, _, _]` (size = 4, `front = 0`, `rear = 1`) and we call `enqueue(18)`:
  * Check if full: `rear != size - 1` (1 != 3, not full).
  * Increment `rear` to `2`.
  * Store element: `Queue[2] = 18`.
  * New State: `[5, 12, 18, _]`, `front = 0`, `rear = 2`.

### 2. Dequeue
Removes and returns the element at the front of the queue.

* **Example:**
  If Queue is `[5, 12, 18, _]` (`front = 0`, `rear = 2`) and we call `dequeue()`:
  * Check if empty: `front != -1` (not empty).
  * Get element at `front`: `val = Queue[0] = 5`.
  * Increment `front` to `1`.
  * New State: `[_, 12, 18, _]`, `front = 1`, `rear = 2`. Returns `5`.

### 3. Peek (or Front)
Returns the element at the front of the queue *without* removing it.

* **Example:**
  If Queue is `[_, 12, 18, _]` (`front = 1`, `rear = 2`), calling `peek()` returns `12`. Pointers and array state remain unchanged.

### 4. isEmpty
Checks if the queue contains no elements.

* **Logic:** Returns `true` if `front == -1` or `front > rear`. Otherwise, returns `false`.

### 5. isFull
Checks if the queue has reached its maximum storage capacity (relevant for fixed-size arrays).

* **Logic:** Returns `true` if `rear == capacity - 1` (for a Linear Queue).

---

## Time Complexity Table

| Operation | Array Implementation (Linear) | Circular Queue (Array) | Linked List Implementation |
| :--- | :--- | :--- | :--- |
| **Enqueue** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| **Dequeue** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| **Peek / Front** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| **isEmpty** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| **isFull** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| **Search** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

*Note: In some dynamic array implementations, if `dequeue` is written to shift elements left by one index to keep `front` always at index `0`, the time complexity of `dequeue` becomes $\mathcal{O}(N)$. Using pointers (as shown above) ensures $\mathcal{O}(1)$.*

---

## Space Complexity

* **Auxiliary Space Complexity:** $\mathcal{O}(1)$ for all standard operations (enqueue, dequeue, peek, etc.) because they only require a constant amount of extra memory for pointer manipulation.
* **Total Space Complexity:** $\mathcal{O}(N)$, where $N$ is the number of elements currently stored in the queue.

---

## Advantages

* **Maintains Order:** Inherently guarantees chronological sequence processing (FIFO).
* **Speed:** Insertion and deletion operations are highly optimized, running in constant time $\mathcal{O}(1)$.
* **Safety & Decoupling:** Ideal for pipeline workflows where components operate at different speeds without risking data race conditions or blocking.
* **Flexibility in Memory:** Linked-list queues can dynamically expand and shrink based on runtime needs.

---

## Disadvantages

* **No Random Access:** Retrieving a value in the middle of a queue requires popping all elements before it, causing high time complexity ($\mathcal{O}(N)$) and loss of data unless cached.
* **Memory Wastage (Linear Array Queue):** When elements are dequeued, their vacated slots cannot be reused unless the entire queue is reset or shifted, or a circular design is adopted.
* **Fixed Size Limits:** Static array implementations require defining the maximum capacity upfront.

---

## Real World Applications

* **Operating System Task Scheduler:** Processing tasks in First-Come, First-Served (FCFS) or Round-Robin order.
* **Call Center Phone Systems:** Placing incoming customer phone calls on hold in a queue until an operator is free.
* **Web Servers:** Managing incoming HTTP requests via a request queue during high traffic spikes.
* **Media Players:** Maintaining a playlist queue where songs are played in the order they were queued.
* **Graph Traversal (BFS):** Navigating networks, social graph connections, or shortest path routing.

---

## Python Implementation

Using standard list objects in Python for a queue is inefficient because `list.pop(0)` takes $\mathcal{O}(N)$ time. The standard library provides `collections.deque` which implements highly optimized double-ended queues with $\mathcal{O}(1)$ modifications on both sides.

Below is an implementation of a **Circular Queue** using a fixed-size array to demonstrate underlying algorithmic mechanics:

```python
class CircularQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_full(self) -> bool:
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self) -> bool:
        return self.front == -1

    def enqueue(self, value: int) -> bool:
        if self.is_full():
            print("Queue Overflow! Cannot enqueue:", value)
            return False
        
        if self.is_empty():
            self.front = 0
            
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        print(f"Enqueued: {value}")
        return True

    def dequeue(self) -> int:
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue.")
            return -1
        
        removed_value = self.queue[self.front]
        self.queue[self.front] = None # Help garbage collection
        
        # If queue has only one element left, reset pointers
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
            
        return removed_value

    def peek(self) -> int:
        if self.is_empty():
            print("Queue is empty.")
            return -1
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        
        print("Queue structure:", end=" ")
        curr = self.front
        while True:
            print(self.queue[curr], end=" -> ")
            if curr == self.rear:
                break
            curr = (curr + 1) % self.capacity
        print("None")


# Driver code to test the Queue implementation
if __name__ == "__main__":
    q = CircularQueue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.display()
    
    print(f"Dequeued element: {q.dequeue()}")
    print(f"Front element: {q.peek()}")
    q.display()
    
    q.enqueue(50)
    q.enqueue(60) # Fits because of circular properties
    q.display()
```

---

## C++ Implementation

Here is a template-based **Circular Queue** implementation in C++:

```cpp
#include <iostream>
#include <stdexcept>

template <typename T>
class CircularQueue {
private:
    T* arr;
    int front;
    int rear;
    int capacity;

public:
    CircularQueue(int size) {
        capacity = size;
        arr = new T[capacity];
        front = -1;
        rear = -1;
    }

    ~CircularQueue() {
        delete[] arr;
    }

    bool isFull() const {
        return (rear + 1) % capacity == front;
    }

    bool isEmpty() const {
        return front == -1;
    }

    void enqueue(T value) {
        if (isFull()) {
            throw std::overflow_error("Queue Overflow: Capacity reached.");
        }
        if (isEmpty()) {
            front = 0;
        }
        rear = (rear + 1) % capacity;
        arr[rear] = value;
    }

    T dequeue() {
        if (isEmpty()) {
            throw std::underflow_error("Queue Underflow: Queue is empty.");
        }
        T element = arr[front];
        if (front == rear) {
            // Only one element was in queue, reset pointers
            front = -1;
            rear = -1;
        } else {
            front = (front + 1) % capacity;
        }
        return element;
    }

    T peek() const {
        if (isEmpty()) {
            throw std::underflow_error("Queue is empty.");
        }
        return arr[front];
    }

    void display() const {
        if (isEmpty()) {
            std::cout << "Queue is empty.\n";
            return;
        }
        int i = front;
        std::cout << "Queue elements: ";
        while (true) {
            std::cout << arr[i] << " ";
            if (i == rear) break;
            i = (i + 1) % capacity;
        }
        std::cout << "\n";
    }
};

int main() {
    try {
        CircularQueue<int> q(5);
        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        q.display();

        std::cout << "Removed: " << q.dequeue() << "\n";
        q.display();

        q.enqueue(4);
        q.enqueue(5);
        q.enqueue(6); // Wrap-around insertion
        q.display();
    } catch (const std::exception& e) {
        std::cerr << "Exception: " << e.what() << "\n";
    }
    return 0;
}
```

---

## Java Implementation

Below is a robust Java implementation of a **Linked-List-Based Queue** which can expand dynamically:

```java
public class LinkedListQueue<T> {
    private static class Node<T> {
        private final T data;
        private Node<T> next;

        public Node(T data) {
            this.data = data;
            this.next = null;
        }
    }

    private Node<T> front;
    private Node<T> rear;
    private int size;

    public LinkedListQueue() {
        this.front = null;
        this.rear = null;
        this.size = 0;
    }

    public boolean isEmpty() {
        return front == null;
    }

    public int size() {
        return size;
    }

    public void enqueue(T data) {
        Node<T> newNode = new Node<>(data);
        if (isEmpty()) {
            front = newNode;
            rear = newNode;
        } else {
            rear.next = newNode;
            rear = newNode;
        }
        size++;
        System.out.println("Enqueued: " + data);
    }

    public T dequeue() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue Underflow: Empty Queue!");
        }
        T data = front.data;
        front = front.next;
        if (front == null) {
            rear = null;
        }
        size--;
        return data;
    }

    public T peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty.");
        }
        return front.data;
    }

    public void display() {
        if (isEmpty()) {
            System.out.println("Queue is empty.");
            return;
        }
        Node<T> current = front;
        System.out.print("Queue (Front -> Rear): ");
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        LinkedListQueue<String> stringQueue = new LinkedListQueue<>();
        stringQueue.enqueue("Alice");
        stringQueue.enqueue("Bob");
        stringQueue.enqueue("Charlie");
        stringQueue.display();

        System.out.println("Peek: " + stringQueue.peek());
        System.out.println("Dequeued: " + stringQueue.dequeue());
        stringQueue.display();
    }
}
```

---

## 3 Solved Examples

### Example 1: Reverse First K Elements of a Queue
**Problem Statement:** Given an integer $K$ and a queue of integers, reverse the order of the first $K$ elements of the queue, leaving the other elements in their original relative positions.

#### Step-by-Step Explanation:
1. **Use an Auxiliary Stack:** A Stack naturally reverses data (LIFO).
2. **Phase 1 (Dequeue & Push):** Dequeue the first $K$ elements from the queue one by one and push them onto the stack.
3. **Phase 2 (Pop & Enqueue):** Pop all elements from the stack and enqueue them back into the queue. Now, the reversed $K$ elements are at the back of the queue.
4. **Phase 3 (Rotate Remaining Elements):** Dequeue the remaining $(N - K)$ elements from the front of the queue and enqueue them back to the rear of the queue to restore original order for the rest.

#### Python Code:
```python
from collections import deque

def reverse_first_k(queue: deque, k: int):
    if not queue or k > len(queue) or k <= 0:
        return
    
    stack = []
    
    # Step 1: Push first k elements onto stack
    for _ in range(k):
        stack.append(queue.popleft())
        
    # Step 2: Enqueue stack elements back into queue
    while stack:
        queue.append(stack.pop())
        
    # Step 3: Dequeue remaining N-k elements & append back to rear
    for _ in range(len(queue) - k):
        queue.append(queue.popleft())

# Dry Run Example:
# Input Queue: [10, 20, 30, 40, 50], K = 3
# Step 1: Pop 10, 20, 30 -> Stack: [10, 20, 30]. Queue: [40, 50]
# Step 2: Pop from Stack -> Queue: [40, 50, 30, 20, 10]
# Step 3: Shift remaining (5-3) = 2 items: 40 and 50 to the end.
# Final Queue: [30, 20, 10, 40, 50]
```

---

### Example 2: Generate Binary Numbers from 1 to N
**Problem Statement:** Write a function to generate and print all binary numbers with decimal values from $1$ to $N$.

#### Step-by-Step Explanation:
1. **Initialize a Queue:** Store strings. Enqueue `"1"`.
2. **Loop $N$ times:**
   * Dequeue a string $S$. This is the next binary number.
   * Print/Store $S$.
   * Generate the next two numbers by appending `"0"` and `"1"` to $S$:
     * $S_1 = S + "0"$
     * $S_2 = S + "1"$
   * Enqueue $S_1$ and $S_2$.
3. This creates a level-order traversal pattern generating binary numbers sequentially.

```
          "1"
        /     \
    "10"       "11"
    /  \       /   \
"100" "101" "110" "111"
```

#### Python Code:
```python
from collections import deque

def generate_binary_numbers(n: int):
    q = deque()
    q.append("1")
    result = []
    
    for _ in range(n):
        curr = q.popleft()
        result.append(curr)
        
        # Enqueue child binary transitions
        q.append(curr + "0")
        q.append(curr + "1")
        
    return result

# Dry Run for N = 4:
# Initialize: q = ["1"]
# Loop 1: Dequeue "1" -> result = ["1"]. Enqueue "10", "11". q = ["10", "11"]
# Loop 2: Dequeue "10" -> result = ["1", "10"]. Enqueue "100", "101". q = ["11", "100", "101"]
# Loop 3: Dequeue "11" -> result = ["1", "10", "11"]. Enqueue "110", "111". q = ["100", "101", "110", "111"]
# Loop 4: Dequeue "100" -> result = ["1", "10", "11", "100"].
```

---

### Example 3: Implement Queue using Stacks
**Problem Statement:** Implement a FIFO queue using only two LIFO stacks. The implemented queue should support `push`, `pop`, `peek`, and `empty`.

#### Step-by-Step Explanation:
We use two stacks: `input_stack` and `output_stack`.
* **Push (Enqueue):** Push elements directly onto `input_stack`. This is an $\mathcal{O}(1)$ operation.
* **Pop (Dequeue) / Peek:**
  * If `output_stack` is not empty, pop/peek from it.
  * If `output_stack` is empty, move **all** elements from `input_stack` to `output_stack` (which reverses their order, making the oldest elements end up on top of `output_stack`).
  * Pop/peek from `output_stack`.
  * This is amortized $\mathcal{O}(1)$ time complexity because each element is moved at most once between the stacks.

#### Java Code:
```java
import java.util.Stack;

class MyQueue {
    private final Stack<Integer> inputStack = new Stack<>();
    private final Stack<Integer> outputStack = new Stack<>();

    public void push(int x) {
        inputStack.push(x);
    }

    public int pop() {
        peek(); // Ensures outputStack is filled
        return outputStack.pop();
    }

    public int peek() {
        if (outputStack.isEmpty()) {
            while (!inputStack.isEmpty()) {
                outputStack.push(inputStack.pop());
            }
        }
        return outputStack.peek();
    }

    public boolean empty() {
        return inputStack.isEmpty() && outputStack.isEmpty();
    }
}
```

---

## 5 Interview Questions with Answers

### Q1: What is the difference between a Deque and a Circular Queue?
**Answer:**
* **Circular Queue:** It is a linear queue with circular arithmetic wrap-around. It maintains a strict single-in, single-out standard structure (insertions exclusively at the `rear`, deletions exclusively at the `front`).
* **Deque (Double-Ended Queue):** It is a generalized queue that permits insertions and deletions at **both** ends (`front` and `rear`). A Deque can be configured to behave either like a Stack or a Queue.

---

### Q2: How can we implement a Stack using only Queues?
**Answer:**
A Stack can be implemented using two queues ($q_1$ and $q_2$) using either a push-costly or pop-costly approach:

* **Push-Costly Approach:**
  1. Enqueue the new element to $q_2$.
  2. Dequeue all elements of $q_1$ and enqueue them to $q_2$.
  3. Swap the names of $q_1$ and $q_2$.
  * This maintains the newest element always at the front of $q_1$, making standard pop an $\mathcal{O}(1)$ step.

```python
# Push-costly Implementation
from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()
```

---

### Q3: What is the "false overflow" problem in simple array-based queues, and how is it resolved?
**Answer:**
In a standard linear array queue, when elements are repeatedly enqueued and dequeued, the `rear` index eventually reaches the end of the array (`capacity - 1`), while the `front` index advances forward. 

Even if the slots at the beginning of the array are vacant, any subsequent `enqueue` operation will report a **Queue Full (Overflow)** condition. 

```
[ Vacant ] [ Vacant ] [ 30 ] [ 40 ] -> rear (Cannot add more elements!)
```

This is solved by using a **Circular Queue** where modulo arithmetic `(index + 1) % capacity` maps the next position back to the beginning of the array, reusing empty slots.

---

### Q4: Explain Priority Queue. How does its complexity compare to a standard Queue?
**Answer:**
A **Priority Queue** is a specialized queue where each element has a priority. High-priority elements are dequeued before low-priority elements. 

* **Standard Queue:** Enqueue and Dequeue are always $\mathcal{O}(1)$.
* **Priority Queue (via Binary Heap):**
  * Insertion: $\mathcal{O}(\log N)$
  * Extraction of Max/Min (Dequeue): $\mathcal{O}(\log N)$
  * Peek: $\mathcal{O}(1)$

---

### Q5: What is the significance of the "Breadth-First Search" (BFS) queue usage? Why can't we use a Stack?
**Answer:**
BFS explores a graph level by level. It must process all adjacent neighbors of a node before moving to nodes at the next deeper level. 

* **Why Queue works:** Because queues use FIFO ordering. Inserting neighbors at the rear guarantees they will be explored chronologically *after* all currently active nodes at the current level have been dequeued and evaluated.
* **Why Stack fails:** A stack uses LIFO ordering. If a stack is used, it recursively dives deep down a single path before backtracking, which represents **Depth-First Search (DFS)** rather than BFS.

---

## Common Mistakes

### 1. Using Python `list` for $O(1)$ Queue Operations
A common mistake in Python is implementing a queue using basic lists:
```python
queue = []
queue.append(1)  # O(1)
queue.pop(0)     # O(N) amortized error!
```
Calling `list.pop(0)` shifts all remaining items in memory one index to the left, degrading dequeue performance to $\mathcal{O}(N)$. Use `collections.deque` instead.

### 2. Off-by-One Pointer Resets
In custom circular queues, forgetting to reset the pointers (`front = -1`, `rear = -1`) when the last element is dequeued is a common error. This causes the queue to report empty status incorrectly or read garbage memory.

### 3. Missing Check for Underflow
Attempting to retrieve or delete elements from an empty queue without validating `isEmpty()` returns `null` pointer exceptions or array out-of-bound errors. Always validate state before reading.

### 4. Overcomplicating Array Size check in Circular Queue
Using `rear == front` to indicate a full queue is an error because `rear == front` also occurs when the queue contains exactly one element. Use `(rear + 1) % capacity == front` to check if a circular queue is full.

---

## Summary

* **FIFO Rule:** The cornerstone of the Queue is the First-In-First-Out rule.
* **Key Pointers:** Double-ended control using `front` (deletion) and `rear` (insertion).
* **Circular Improvement:** Circular queues solve memory waste by looping array boundaries.
* **Performance:** Basic operations (Enqueue/Dequeue) execute in super-fast $\mathcal{O}(1)$ constant time.
* **Core Systems Use Cases:** Underlying engine behind asynchronous processing, OS schedulers, network packet queuing, and BFS pathfinding.