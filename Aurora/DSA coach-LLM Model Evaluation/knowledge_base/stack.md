# Stack

---

## Definition

A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** or **FILO (First In, Last Out)** principle. This means that the element inserted last is the first one to be removed, and the element inserted first is the last one to be removed. 

All insertions and deletions in a stack are restricted to a single end, known as the **Top** of the stack. The opposite end is called the **Bottom**.

```
           +-----------+
    Top -> | Element 3 |  <- Insert (Push) / Remove (Pop) here
           +-----------+
           | Element 2 |
           +-----------+
           | Element 1 |
           +-----------+
  Bottom ->| Element 0 |
           +-----------+
```

---

## Why it is needed

The Stack is indispensable in computing due to its structured restriction of access. It is needed for:

1. **State Preservation & Backtracking**: To remember previous states or decision points, allowing applications to return to them in reverse chronological order (e.g., "Undo" actions).
2. **Context Switching and Function Calls**: Operating systems and language runtimes must keep track of active subroutines, local variables, and return addresses.
3. **Strict Sequencing**: When data must be processed in the exact reverse order of its arrival.
4. **Parsing and Compilation**: Compilers require stacks to parse mathematical expressions, evaluate postfix/prefix notations, and validate syntax grammar (like matching parentheses).

---

## Characteristics

* **Linear Structure**: Elements are organized sequentially.
* **Single Access Point**: Elements can only be added or removed from the **Top**.
* **LIFO/FILO Order**: The order of retrieval is the inverse of the order of insertion.
* **Dynamic or Static**: Can be implemented with a fixed size (using arrays) or dynamic size (using linked lists).
* **No Random Access**: Elements in the middle or bottom cannot be accessed or modified directly without removing all elements above them.

---

## Working

A stack works like a stack of plates in a cafeteria. You can only place a new plate on top, and you can only take the top plate off.

### Step-by-Step Execution Trace

Let us trace a stack with a maximum capacity of 3:

1. **Initial State**: The stack is empty. The `top` pointer is initialized to `-1` (in array index terms).
   ```
   Empty Stack []
   top = -1
   ```

2. **Push(10)**: Inserts `10` onto the stack. `top` increments to `0`.
   ```
   [ 10 ]  <- top = 0
   ```

3. **Push(20)**: Inserts `20`. `top` increments to `1`.
   ```
   [ 20 ]  <- top = 1
   [ 10 ]
   ```

4. **Push(30)**: Inserts `30`. `top` increments to `2`. The stack is now full.
   ```
   [ 30 ]  <- top = 2
   [ 20 ]
   [ 10 ]
   ```

5. **Pop()**: Removes the topmost element (`30`). `top` decrements to `1`.
   ```
   Value popped: 30
   [ 20 ]  <- top = 1
   [ 10 ]
   ```

6. **Peek()**: Views the topmost element (`20`) without removing it. `top` remains `1`.
   ```
   Value peeked: 20
   [ 20 ]  <- top = 1
   [ 10 ]
   ```

---

## Memory Representation

A stack can be represented in memory in two primary ways:

### 1. Array-Based Representation (Contiguous Allocation)
* Elements are stored in contiguous memory blocks.
* A single variable, `top`, stores the index of the highest occupied element.
* **Pros**: Cache-friendly, fast access, minimal memory overhead (no pointers).
* **Cons**: Fixed size (unless using dynamic arrays like Vector/ArrayList), risk of Stack Overflow.

```
Index:    0     1     2     3      (Max Capacity = 4)
       +-----+-----+-----+-----+
Array: | 10  | 20  | 30  |     |   
       +-----+-----+-----+-----+
                     ^
                    top = 2
```

### 2. Linked List-Based Representation (Non-Contiguous Allocation)
* Elements are stored in nodes scattered across heap memory.
* Each node contains a `data` field and a `next` pointer pointing to the node below it.
* The head pointer of the linked list serves as the `top` of the stack.
* **Pros**: Dynamic sizing; will not overflow unless system memory is exhausted.
* **Cons**: High memory overhead (due to pointer storage), poor cache locality.

```
 top
  |
  v
+-----+-----+     +-----+-----+     +-----+------+
| 30  |  *------> | 20  |  *------> | 10  | NULL |
+-----+-----+     +-----+-----+     +-----+------+
```

---

## Types

While the fundamental behaviors of stacks are identical, stacks are categorized by how they are applied or constrained:

1. **Static Stack**: Fixed memory allocation. Uses arrays. Size is defined at compile-time.
2. **Dynamic Stack**: Grows and shrinks dynamically at runtime. Uses linked lists or dynamic arrays.
3. **Register Stack**: Implemented inside the CPU as hardware. It has a tiny capacity but operates at maximum processor speed.
4. **Monotonic Stack**: An algorithmic stack pattern where elements are kept in a strict order (either strictly increasing or decreasing). If a new element violates the order, elements are popped until the order is preserved.

---

## Operations

### 1. Push
Adds an element to the top of the stack.
* **Pre-condition**: Check if the stack is full (Stack Overflow check).
* **Steps**:
  1. Increment `top` pointer by 1.
  2. Write the new element into the memory slot pointed to by `top`.

```
Before Push(40):              After Push(40):
    [ 30 ] <- top                 [ 40 ] <- top
    [ 20 ]                        [ 30 ]
    [ 10 ]                        [ 20 ]
                                  [ 10 ]
```

### 2. Pop
Removes and returns the element at the top of the stack.
* **Pre-condition**: Check if the stack is empty (Stack Underflow check).
* **Steps**:
  1. Store the value pointed to by `top` to return it.
  2. Decrement `top` pointer by 1.

```
Before Pop():                 After Pop(): (Returns 40)
    [ 40 ] <- top                 [ 30 ] <- top
    [ 30 ]                        [ 20 ]
    [ 20 ]                        [ 10 ]
    [ 10 ]
```

### 3. Peek / Top
Retrieves the value of the topmost element without removing it.
* **Pre-condition**: Check if the stack is empty.
* **Steps**: Return the value at index `top`.

### 4. isEmpty
Checks whether the stack has any elements.
* **Steps**: Return `true` if `top == -1` (or `head == NULL`), else `false`.

### 5. isFull (Only for bounded/array stacks)
Checks whether the stack is at maximum capacity.
* **Steps**: Return `true` if `top == Capacity - 1`, else `false`.

---

## Time Complexity Table

| Operation | Best Case | Worst Case | Amortized (Dynamic Array) |
| :--- | :--- | :--- | :--- |
| **Push** | $O(1)$ | $O(1)$ (or $O(N)$ when resizing) | $O(1)$ |
| **Pop** | $O(1)$ | $O(1)$ | $O(1)$ |
| **Peek** | $O(1)$ | $O(1)$ | $O(1)$ |
| **isEmpty** | $O(1)$ | $O(1)$ | $O(1)$ |
| **isFull** | $O(1)$ | $O(1)$ | $O(1)$ |
| **Search/Access** | $O(N)$ | $O(N)$ | $O(N)$ |

---

## Space Complexity

* **Total Space Complexity**: $O(N)$ where $N$ is the maximum number of elements stored in the stack.
* **Auxiliary Space Complexity**: $O(1)$ auxiliary space for standard operations (`push`, `pop`, `peek`, `isEmpty`), as they modify a constant number of pointers and require no additional runtime allocation.

---

## Advantages

* **Simple and Intuitive**: Very easy to understand and implement in any programming language.
* **Highly Efficient**: Push and Pop operations execute in constant $O(1)$ time.
* **Secure and Controlled**: Since random access is prevented, data integrity is preserved; values cannot be accidentally overwritten or corrupted in the middle.
* **Memory Management**: Keeps track of runtime call allocations clean and predictable.

---

## Disadvantages

* **Restricted Access**: Cannot retrieve or modify any element other than the one at the top without destroying the stack layout.
* **Size Limitations**: Array-based implementations have fixed capacities. Once filled, trying to push triggers a **Stack Overflow** error.
* **Potential Memory Leaks / Fragmentation**: Dynamic implementation (linked list) requires allocation and deallocation overhead, potentially causing memory fragmentation and extra pointer storage overhead.

---

## Real World Applications

* **Browser History Management**: Tracking previously visited pages. Pressing the "Back" button pops the current page off the stack to reveal the previous one.
* **Text Editor Undo/Redo**: Every keystroke/edit is pushed onto the undo stack. Invoking undo pops the latest operation and pushes it onto a redo stack.
* **Execution Stack (Call Stack)**: Used by OS runtimes to keep track of nested function calls, their parameters, and return points.
* **Backtracking Algorithms**: Used in maze solving, chess game engines, and pathfinding algorithms to return to parent nodes when hitting a dead end.
* **Delimiter Matching**: Used in compilers to verify that brackets and parenthesis match correctly: `{[()]}`.

---

## Python Implementation

This implementation includes error-handling exceptions and demonstrates an array-based dynamic stack.

```python
class StackUnderflowError(Exception):
    """Exception raised when popping from an empty stack."""
    pass


class Stack:
    def __init__(self, capacity: int = None):
        self._stack = []
        self._capacity = capacity

    def push(self, element) -> None:
        """Pushes an element onto the stack."""
        if self._capacity is not None and len(self._stack) >= self._capacity:
            raise OverflowError("Stack Overflow: Cannot push to a full stack.")
        self._stack.append(element)

    def pop(self):
        """Removes and returns the top element of the stack."""
        if self.is_empty():
            raise StackUnderflowError("Stack Underflow: Cannot pop from an empty stack.")
        return self._stack.pop()

    def peek(self):
        """Returns the top element without removing it."""
        if self.is_empty():
            raise StackUnderflowError("Stack is empty. Cannot peek.")
        return self._stack[-1]

    def is_empty(self) -> bool:
        """Checks if the stack is empty."""
        return len(self._stack) == 0

    def is_full(self) -> bool:
        """Checks if the stack is full (only if capacity is bounded)."""
        if self._capacity is None:
            return False
        return len(self._stack) >= self._capacity

    def size(self) -> int:
        """Returns the current size of the stack."""
        return len(self._stack)

    def __str__(self) -> str:
        return "Bottom -> " + " -> ".join(map(str, self._stack)) + " -> Top"


# Example Usage
if __name__ == "__main__":
    my_stack = Stack(capacity=5)
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    
    print(f"Stack: {my_stack}")
    print(f"Top element (peek): {my_stack.peek()}")
    print(f"Popped: {my_stack.pop()}")
    print(f"Stack after pop: {my_stack}")
    print(f"Stack Size: {my_stack.size()}")
```

---

## C++ Implementation

This is a generic template-based Stack implementation utilizing dynamically allocated memory with standard Rule of Three compliance.

```cpp
#include <iostream>
#include <stdexcept>

template <typename T>
class Stack {
private:
    T* arr;
    int capacity;
    int topIndex;

    void resize(int newCapacity) {
        T* temp = new T[newCapacity];
        for (int i = 0; i <= topIndex; ++i) {
            temp[i] = arr[i];
        }
        delete[] arr;
        arr = temp;
        capacity = newCapacity;
    }

public:
    // Constructor
    Stack(int initCapacity = 4) {
        capacity = initCapacity;
        arr = new T[capacity];
        topIndex = -1;
    }

    // Destructor
    ~Stack() {
        delete[] arr;
    }

    // Copy Constructor
    Stack(const Stack& other) {
        capacity = other.capacity;
        topIndex = other.topIndex;
        arr = new T[capacity];
        for (int i = 0; i <= topIndex; ++i) {
            arr[i] = other.arr[i];
        }
    }

    // Assignment Operator
    Stack& operator=(const Stack& other) {
        if (this != &other) {
            delete[] arr;
            capacity = other.capacity;
            topIndex = other.topIndex;
            arr = new T[capacity];
            for (int i = 0; i <= topIndex; ++i) {
                arr[i] = other.arr[i];
            }
        }
        return *this;
    }

    void push(const T& element) {
        if (topIndex == capacity - 1) {
            resize(capacity * 2); // Dynamic resizing
        }
        arr[++topIndex] = element;
    }

    T pop() {
        if (isEmpty()) {
            throw std::underflow_error("Stack Underflow: Stack is empty.");
        }
        return arr[topIndex--];
    }

    T peek() const {
        if (isEmpty()) {
            throw std::underflow_error("Stack is empty. Cannot peek.");
        }
        return arr[topIndex];
    }

    bool isEmpty() const {
        return topIndex == -1;
    }

    int size() const {
        return topIndex + 1;
    }
};

int main() {
    try {
        Stack<std::string> stack;
        stack.push("Apple");
        stack.push("Banana");
        stack.push("Cherry");

        std::cout << "Stack Size: " << stack.size() << std::endl;
        std::cout << "Top Element: " << stack.peek() << std::endl;
        std::cout << "Popped: " << stack.pop() << std::endl;
        std::cout << "New Top Element: " << stack.peek() << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Exception: " << e.what() << std::endl;
    }
    return 0;
}
```

---

## Java Implementation

This implementation represents a Linked-List based dynamic stack using generics to showcase the pointer representation alternative in Java.

```java
public class Stack<T> {
    
    // Nested helper Node class
    private static class Node<T> {
        private T data;
        private Node<T> next;

        public Node(T data) {
            this.data = data;
            this.next = null;
        }
    }

    private Node<T> top;
    private int size;

    public Stack() {
        this.top = null;
        this.size = 0;
    }

    // O(1) Push
    public void push(T element) {
        Node<T> newNode = new Node<>(element);
        newNode.next = top;
        top = newNode;
        size++;
    }

    // O(1) Pop
    public T pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack Underflow: Cannot pop from empty stack.");
        }
        T data = top.data;
        top = top.next;
        size--;
        return data;
    }

    // O(1) Peek
    public T peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty: Cannot peek.");
        }
        return top.data;
    }

    public boolean isEmpty() {
        return top == null;
    }

    public int size() {
        return size;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        Node<T> current = top;
        sb.append("Top -> ");
        while (current != null) {
            sb.append("[").append(current.data).append("] -> ");
            current = current.next;
        }
        sb.append("Null");
        return sb.toString();
    }

    public static void main(String[] args) {
        Stack<Integer> numStack = new Stack<>();
        numStack.push(100);
        numStack.push(200);
        numStack.push(300);

        System.out.println(numStack);
        System.out.println("Popped: " + numStack.pop());
        System.out.println("Current Peek: " + numStack.peek());
        System.out.println(numStack);
    }
}
```

---

## 3 Solved Examples

### Example 1: Balanced Parentheses Matching
**Problem Statement**: Given a string containing brackets `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid. An input string is valid if open brackets are closed by the same type of brackets and in the correct order.

* **Input**: `"{[()]}"`
* **Output**: `True`

#### Step-by-Step Trace Table:

| Step | Character | Action | Stack State (Bottom -> Top) | Explanation |
| :---: | :---: | :--- | :--- | :--- |
| **0** | - | Initial | `[]` | Stack starts empty. |
| **1** | `{` | Push `{` | `['{']` | Opening bracket. |
| **2** | `[` | Push `[` | `['{', '[']` | Opening bracket. |
| **3** | `(` | Push `(` | `['{', '[', '(']` | Opening bracket. |
| **4** | `)` | Pop & Compare | `['{', '[']` | Pop matches current character `)`. Valid. |
| **5** | `]` | Pop & Compare | `['{']` | Pop matches current character `]`. Valid. |
| **6** | `}` | Pop & Compare | `[]` | Pop matches current character `}`. Valid. |

**Final Check**: The stack is empty. Result is **True**.

---

### Example 2: Infix to Postfix Conversion
**Problem Statement**: Convert the infix algebraic expression `A + B * C` to postfix format.

* **Input**: `A + B * C`
* **Output**: `A B C * +`

#### Precedence Table:
* `+`, `-` has precedence 1
* `*`, `/` has precedence 2

#### Trace Table:

| Step | Character | Type | Action / Output | Stack State | Postfix Expression (Output String) |
| :---: | :---: | :---: | :--- | :--- | :--- |
| **1** | `A` | Operand | Append to output | `[]` | `A` |
| **2** | `+` | Operator | Push to stack | `['+']` | `A` |
| **3** | `B` | Operand | Append to output | `['+']` | `A B` |
| **4** | `*` | Operator | Compare precedence with top (`+`). Since `*` (prec 2) > `+` (prec 1), push to stack. | `['+', '*']` | `A B` |
| **5** | `C` | Operand | Append to output | `['+', '*']` | `A B C` |
| **6** | End | EOF | Pop all remaining operators. | `[]` | `A B C * +` |

---

### Example 3: Evaluate Postfix Expression
**Problem Statement**: Evaluate the value of the arithmetic expression written in postfix notation: `"5 3 2 * +"` (representing $5 + (3 \times 2)$).

* **Input**: `"5 3 2 * +"`
* **Output**: `11`

#### Step-by-Step Evaluation Trace:

```
Expression tokens: ["5", "3", "2", "*", "+"]
```

1. **Token "5"**: Operand. Push to stack.
   * Stack: `[5]`
2. **Token "3"**: Operand. Push to stack.
   * Stack: `[5, 3]`
3. **Token "2"**: Operand. Push to stack.
   * Stack: `[5, 3, 2]`
4. **Token "*"**: Operator.
   * Pop Operand 2: `2`
   * Pop Operand 1: `3`
   * Evaluate: $3 \times 2 = 6$
   * Push result `6` back to stack.
   * Stack: `[5, 6]`
5. **Token "+"**: Operator.
   * Pop Operand 2: `6`
   * Pop Operand 1: `5`
   * Evaluate: $5 + 6 = 11$
   * Push result `11` back to stack.
   * Stack: `[11]`
6. **Finish**: Pop the final value `11` as the final result.

---

## 5 Interview Questions with Answers

### 1. How do you implement a Queue using two Stacks?
**Answer**: 
A stack is LIFO, while a queue is FIFO. By using two stacks, we can reverse the order of elements twice to achieve FIFO behavior.

* **Structure**: Maintain two stacks: `inputStack` and `outputStack`.
* **Push (Enqueue)**: Always push onto `inputStack` ($O(1)$).
* **Pop (Dequeue)**:
  * If `outputStack` is empty, pop all elements from `inputStack` one-by-one and push them into `outputStack`. This reverses the sequence.
  * Pop the top element of `outputStack`.
  * If `outputStack` is not empty, simply pop from it.
* **Complexity**: Amortized $O(1)$ time per operation, and $O(N)$ space.

```
Enqueue(1), Enqueue(2):
inputStack  [1, 2]     outputStack []

Dequeue():
  (Since outputStack is empty, transfer inputStack contents to outputStack)
inputStack  []         outputStack [2, 1] -> Pop yields 1
```

---

### 2. What is a Monotonic Stack, and how is it used to find the "Next Greater Element"?
**Answer**:
A **Monotonic Stack** is a stack that maintains its elements in a sorted order (strictly increasing or decreasing). 

To find the **Next Greater Element (NGE)** for each position in an array:
1. Traverse the array from right to left.
2. While the stack is not empty and the top element is less than or equal to the current element, pop from the stack.
3. If the stack is empty, the NGE is `-1`. Else, the NGE is the top element of the stack.
4. Push the current element onto the stack.
5. This guarantees each element is pushed and popped at most once, yielding $O(N)$ time complexity instead of $O(N^2)$.

---

### 3. Design a stack that supports `push()`, `pop()`, `top()`, and retrieving the minimum element `getMin()` in $O(1)$ time.
**Answer**:
We can achieve this by maintaining an auxiliary "Min Stack" alongside our main stack.

* **Main Stack**: Stores all elements as standard.
* **Min Stack**: Stores the minimum element encountered so far.
* **Algorithm**:
  * **Push(x)**: Push `x` to Main Stack. If Min Stack is empty or `x <= Min Stack.peek()`, push `x` to Min Stack.
  * **Pop()**: Pop from Main Stack. If the popped value is equal to the top of Min Stack, pop from Min Stack as well.
  * **getMin()**: Return the top value of Min Stack in $O(1)$ time.

```
Push(5) -> Main: [5],     Min: [5]
Push(3) -> Main: [5, 3],  Min: [5, 3]
Push(7) -> Main: [5, 3, 7], Min: [5, 3]
getMin() -> Returns Min.peek() which is 3
```

---

### 4. Explain how the Call Stack handles recursion and what causes a "StackOverflowError".
**Answer**:
Each time a program calls a function, the OS/Compiler allocates a block of memory called an **Activation Record (Stack Frame)** on the **System Call Stack**. This frame stores:
1. Local variables of the function.
2. Function arguments.
3. The return address (where to resume execution after completion).

When a function executes recursively without a base case (or too deeply), call frames are continuously pushed onto the Call Stack without ever being popped. Because stack memory allocation is finite, this causes the stack space to exhaust completely, crashing the application with a **StackOverflowError**.

---

### 5. How do you reverse a stack using recursion without using loops or auxiliary data structures?
**Answer**:
We can use the implicit system call stack to hold the elements. The solution uses two recursive functions: `reverse()` and `insertAtBottom()`.

* **Algorithm**:
  1. `reverse(stack)`:
     * If the stack is empty, return.
     * Else, pop top element `temp`.
     * Recursively call `reverse(stack)`.
     * Call helper `insertAtBottom(stack, temp)`.
  2. `insertAtBottom(stack, element)`:
     * If the stack is empty, push `element`.
     * Else, pop `temp`, call `insertAtBottom(stack, element)`, and then push `temp` back.

* **Time Complexity**: $O(N^2)$ because we process $N$ elements and each call to `insertAtBottom` can take $O(N)$ time.

---

## Common Mistakes

1. **Forgetting Underflow/Overflow Checks**: Accessing `peek()` or `pop()` on an empty stack without checking `isEmpty()` will crash your program at runtime.
2. **Infinite Recursion / Call Stack Abuse**: Using recursive functions to emulate stacks over massive data paths. This can easily trigger a hardware `StackOverflowError`. Always default to an explicit, heap-allocated Stack object for large loop cycles.
3. **Array Bounds Off-by-One**: In manual array implementations, initializing `top = 0` instead of `top = -1`. If initialized to `0`, the first element is placed at index `1` instead of `0` if you increment before write, leading to corrupted layouts.
4. **Incorrect Operator Precedence in Parsers**: During infix conversions, popping operators of lower precedence instead of higher or equal precedence.
5. **Memory Leak in Pointer Implementations**: Forgetting to free/delete popped nodes in manual C/C++ structures, leading to runaway heap usage.

---

## Summary

The **Stack** is a highly efficient, linear data structure operating strictly on the **LIFO (Last In, First Out)** principle. With access restricted exclusively to the **Top**, it provides $O(1)$ constant time complexity for insertions (`push`) and deletions (`pop`). Stacks form the basis of execution control in CPUs, language compiling structures, backtracking procedures, and general undo utility architectures. When designing a stack, developers choose between highly efficient but statically bounded **Arrays** and slightly slower but dynamic **Linked Lists**.