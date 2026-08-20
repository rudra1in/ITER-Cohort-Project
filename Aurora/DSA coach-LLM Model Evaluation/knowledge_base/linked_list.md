# Linked List

## Definition

A **Linked List** is a linear data structure in which elements are not stored at contiguous memory locations. Instead, elements are stored in nodes, and each node points to the next node in the sequence using a reference (or pointer). 

A linked list consists of:
*   **Node**: The individual unit of a linked list. Each node contains:
    *   **Data**: The actual value or information stored.
    *   **Pointer/Reference (Next)**: A memory address pointing to the next node in the sequence.
*   **Head**: A reference pointer to the first node of the linked list. If the list is empty, the head points to `NULL`.
*   **Tail (optional but common)**: A reference pointer to the last node of the linked list, which points to `NULL` to signify the end of the list.

```
Head
 │
 ▼
┌───────────┬───────────┐      ┌───────────┬───────────┐      ┌───────────┬───────────┐
│  Data (A) │  Next ───┼─────>│  Data (B) │  Next ───┼─────>│  Data (C) │  Next:NULL│
└───────────┴───────────┘      └───────────┴───────────┘      └───────────┴───────────┘
```

---

## Why it is needed

While arrays are excellent for static storage and fast index-based lookups, they present structural inefficiencies that linked lists address:

1.  **Fixed Size Limitation**: Standard arrays have a fixed size defined at compilation. If dynamic arrays (like Python lists or C++ vectors) are used, resizing requires allocating a new, larger memory block and copying all elements over, which takes $O(N)$ time. Linked lists grow and shrink dynamically at runtime without performance penalties.
2.  **Expensive Insertions and Deletions**: Inserting or deleting an element in the middle or start of an array requires shifting all subsequent elements in memory. This is an $O(N)$ operation. Linked lists perform these insertions and deletions in $O(1)$ auxiliary time once the insertion/deletion point is located, requiring only pointer updates.
3.  **Contiguous Memory Allocation**: Arrays require a single continuous block of physical memory. If memory is fragmented, allocating a large array might fail even if total free memory is sufficient. Linked lists utilize non-contiguous memory blocks, allocating memory on-demand per node.

---

## Characteristics

*   **Dynamic Size**: Allocates memory dynamically during runtime.
*   **Sequential Access**: Does not support random access. To access the $i$-th element, you must traverse sequentially from the `head` ($O(N)$ access time).
*   **Extra Memory Overhead**: Requires extra memory for storing pointers/references alongside data in each node.
*   **Non-Contiguous**: Nodes are scattered across the heap memory, meaning there is no guarantee of spatial locality (causing potential cache misses).

---

## Working

A linked list operates by traversing node references. 

1.  **Initialization**: A list starts with a `head` variable initialized to `NULL` or pointing to a single root node.
2.  **Traversal**: Traversal begins at `head`. The program reads the `data` of the current node, then assigns the current pointer to the address stored in the `next` field. This loop repeats until the `next` pointer is `NULL`.
3.  **Pointer Manipulation**: Structural alterations (inserting, deleting, swapping nodes) are performed by modifying the addresses stored in the `next` (and/or `prev`) pointer fields of the affected nodes, leaving the rest of the list unchanged.

---

## Memory Representation

Unlike an array where elements are packed sequentially in memory addresses like `1000`, `1004`, `1008`, a linked list's nodes can reside anywhere in the heap.

### Abstract Comparison

**Array Memory Layout (Sequential):**
```
Index:    [0]     [1]     [2]
Address:  1000    1004    1008
Value:    'A'     'B'     'C'
```

**Linked List Memory Layout (Non-Contiguous):**
```
Heap Address    Node Content (Data, Next Pointer Address)
────────────────────────────────────────────────────────
1024            Node 2 -> ('B', 4096)
...             
3008            Head  -> Points to Address 5012
...             
4096            Node 3 -> ('C', NULL)
...             
5012            Node 1 -> ('A', 1024)
```

**Traversal Sequence based on pointers:**
`Head (3008)` $\rightarrow$ `Addr 5012 ('A')` $\rightarrow$ `Addr 1024 ('B')` $\rightarrow$ `Addr 4096 ('C')` $\rightarrow$ `NULL`.

---

## Types

### 1. Singly Linked List
Each node contains data and a pointer to the *next* node. Traversal is strictly uni-directional (forward).
```
Head ──> [Data|Next] ──> [Data|Next] ──> [Data|NULL]
```

### 2. Doubly Linked List
Each node contains data, a pointer to the *next* node, and a pointer to the *previous* node. Allows bi-directional traversal.
```
         ┌─── Prev           ┌─── Prev
         ▼                   ▼
Head ──> [Prev|Data|Next] ── [Prev|Data|Next] ──> [Prev|Data|NULL]
              │                   ▲
              └───────────────────┘ Next
```

### 3. Circular Linked List
*   **Singly Circular**: The `next` pointer of the last node points back to the `head` node.
*   **Doubly Circular**: The `next` pointer of the last node points back to the `head`, and the `prev` pointer of the `head` points back to the last node.

```
       ┌──────────────────────────────────────────────┐
       │                                              ▼
Head ──┴──> [Data|Next] ──> [Data|Next] ──> [Data|Next]
```

---

## Operations

### 1. Insertion
Insertion can occur at three major positions:

#### A. Insertion at the Beginning (Prepending)
1.  Create a new node.
2.  Set the new node's `next` pointer to point to the current `head`.
3.  Update `head` to point to the new node.

```
Step 1 & 2:  [New Node] ──> [Head Node] ──> [Node 2] ──> NULL
Step 3:      Head ──> [New Node] ──> [Head Node] ──> [Node 2] ──> NULL
```

#### B. Insertion at the End (Appending)
1.  Create a new node with `next` pointing to `NULL`.
2.  If the list is empty, make this node the `head`.
3.  Otherwise, traverse from `head` to find the last node (whose `next` is `NULL`).
4.  Set the last node's `next` to point to the new node.

```
Traverse to End:  [Head] ──> [Node 1] ──> [Last Node] ──> NULL
Update pointer:                           [Last Node] ──> [New Node] ──> NULL
```

#### C. Insertion After a Given Node
1.  Verify if the given node exists.
2.  Create a new node.
3.  Set the new node's `next` pointer to point to the given node's `next`.
4.  Set the given node's `next` pointer to point to the new node.

```
Given Node (A), Next Node (B)
Before:   [Node A] ──────────────────────────> [Node B]
New Node:             [New Node]
Link 1:               [New Node] ────────────> [Node B]
Link 2:   [Node A] ──> [New Node]
```

---

### 2. Deletion
Deletion removes a node and repairs the broken links.

#### A. Deletion from the Beginning
1.  Check if the list is empty. If so, return.
2.  Hold a temporary reference to the current `head`.
3.  Move the `head` pointer to `head->next`.
4.  Deallocate/free the memory of the temporary node.

```
Before:  Head ──> [Node A] ──> [Node B] ──> [Node C]
After:   Head ───────────────> [Node B] ──> [Node C]   (Node A freed)
```

#### B. Deletion from the End
1.  If the list is empty or has only one node, handle appropriately (set `head` to `NULL`).
2.  Traverse the list keeping track of two pointers: `current` and `previous`.
3.  Stop when `current` reaches the last node (where `next` is `NULL`).
4.  Set `previous->next` to `NULL`.
5.  Deallocate the `current` node.

```
Before:  [Head] ──> [Prev Node] ──> [Current Node] ──> NULL
After:   [Head] ──> [Prev Node] ──> NULL              (Current Node freed)
```

#### C. Deletion of a Node by Value (Key)
1.  Search for the node containing the key, keeping track of the `previous` node.
2.  If found:
    *   Set `previous->next` to `current->next`.
    *   Deallocate `current`.
3.  If not found, take no action.

---

### 3. Traversal / Search
1.  Initialize a tracking pointer `temp` to `head`.
2.  Loop while `temp` is not `NULL`:
    *   Process data (print, check if matches search target).
    *   Advance `temp` via `temp = temp->next`.

---

## Time Complexity Table

| Operation | Singly Linked List (Best) | Singly Linked List (Worst) | Doubly Linked List (Best) | Doubly Linked List (Worst) | Remarks |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Access / Search** | $O(1)$ | $O(N)$ | $O(1)$ | $O(N)$ | Must traverse linearly to find element. |
| **Insert at Head** | $O(1)$ | $O(1)$ | $O(1)$ | $O(1)$ | Only changes pointers. |
| **Insert at Tail** | $O(1)$ | $O(N)$ | $O(1)$ | $O(1)$ | $O(1)$ if tail pointer is maintained, $O(N)$ if traversal is needed. |
| **Insert in Middle** | $O(1)$ | $O(N)$ | $O(1)$ | $O(N)$ | $O(1)$ if the pointer to the insertion node is already known. |
| **Delete at Head** | $O(1)$ | $O(1)$ | $O(1)$ | $O(1)$ | Only changes pointer of head. |
| **Delete at Tail** | $O(1)$ | $O(N)$ | $O(1)$ | $O(1)$ | DLL can delete in $O(1)$ because of the `prev` pointer (with tail pointer). SLL requires $O(N)$ to find the second-to-last node. |
| **Delete in Middle** | $O(1)$ | $O(N)$ | $O(1)$ | $O(N)$ | $O(1)$ if the pointer to the node is known (DLL only). |

---

## Space Complexity

*   **Auxiliary Space Complexity**: 
    *   All basic iterative operations (Insertion, Deletion, Traversal) run in **$O(1)$** auxiliary space because they only use a few tracking pointers.
    *   Recursive implementations of operations (like recursive traversal or reversal) require **$O(N)$** auxiliary space due to call-stack overhead.
*   **Total Space Complexity**: **$O(N)$**, where $N$ is the number of elements in the list. Each node takes $O(1)$ space for the value and $O(P)$ space for pointer references (where $P$ is pointer size, typically 4 bytes on 32-bit systems and 8 bytes on 64-bit systems).

---

## Advantages

1.  **Dynamic Size**: Adjusts its size dynamically without copying overhead.
2.  **Efficient Insert/Delete**: Changing connections requires only altering references, which takes $O(1)$ time once the position is reached.
3.  **No Memory Fragmentation**: Does not need a single large continuous chunk of virtual/physical memory.
4.  **Advanced Structure Integration**: Serves as the foundation for other data structures such as Stacks, Queues, Graphs (Adjacency Lists), and Hash Tables (Chaining).

---

## Disadvantages

1.  **High Memory Overhead**: Each node must store pointer addresses alongside data, significantly increasing the structural memory footprint compared to arrays.
2.  **No Random Access**: Elements cannot be fetched directly using an index; resolving the $i$-th element requires $O(i)$ pointer de-references.
3.  **Cache Inefficiency**: Elements are not stored in contiguous physical locations, which leads to frequent cache misses because the hardware prefetcher cannot predict the next node's address.
4.  **No Reverse Traversal (Singly Linked List)**: You cannot move backward through a singly linked list; if the head is lost, the entire list is unrecoverable.

---

## Real World Applications

1.  **Web Browser History**: Back and Forward buttons use a Doubly Linked List to navigate through visited pages.
2.  **Music Playlists**: Sequential music playback uses a Doubly/Circular Linked List to step forward to the next song, backward to the previous song, or loop back to the start.
3.  **Operating Systems Scheduler**: CPU scheduling algorithms (like Round-Robin) maintain processes in a Circular Linked List.
4.  **Image Slidshows**: Image galleries use doubly/circular linked lists to navigate through a sequence of images.
5.  **Garbage Collection**: Memory managers use a linked list of free blocks (known as the "free list") to track unallocated memory gaps.

---

## Python Implementation

```python
class Node:
    """A class representing a single node in a Singly Linked List."""
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """A class representing a Singly Linked List."""
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        """Inserts a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        """Appends a new node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete_node(self, key) -> bool:
        """Deletes the first occurrence of a node with the given key.
        Returns True if deleted, False if key not found.
        """
        curr = self.head
        
        # Scenario 1: Empty List
        if not curr:
            return False
            
        # Scenario 2: Node to delete is the Head Node
        if curr.data == key:
            self.head = curr.next
            curr = None
            return True
            
        # Scenario 3: Node is in the middle or end
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
            
        # If key was not found
        if not curr:
            return False
            
        # Unlink the node from the list
        prev.next = curr.next
        curr = None
        return True

    def search(self, key) -> bool:
        """Searches for a value in the list. Returns True if found."""
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    def display(self):
        """Prints the linked list representation to stdout."""
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elements) + " -> None" if elements else "Empty List")


# Example Execution
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_tail(10)
    sll.insert_at_tail(20)
    sll.insert_at_head(5)
    sll.display()  # Expected output: 5 -> 10 -> 20 -> None
    
    print("Searching for 10:", sll.search(10))  # True
    sll.delete_node(10)
    sll.display()  # Expected output: 5 -> 20 -> None
```

---

## C++ Implementation

```cpp
#include <iostream>

class Node {
public:
    int data;
    Node* next;

    Node(int val) {
        data = val;
        next = nullptr;
    }
};

class SinglyLinkedList {
private:
    Node* head;

public:
    SinglyLinkedList() {
        head = nullptr;
    }

    // Destructor to prevent memory leaks by freeing resources
    ~SinglyLinkedList() {
        Node* current = head;
        while (current != nullptr) {
            Node* nextNode = current->next;
            delete current;
            current = nextNode;
        }
        head = nullptr;
    }

    void insertAtHead(int val) {
        Node* newNode = new Node(val);
        newNode->next = head;
        head = newNode;
    }

    void insertAtTail(int val) {
        Node* newNode = new Node(val);
        if (head == nullptr) {
            head = newNode;
            return;
        }
        Node* temp = head;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = newNode;
    }

    bool deleteNode(int key) {
        Node* temp = head;
        Node* prev = nullptr;

        // If head node itself holds the key
        if (temp != nullptr && temp->data == key) {
            head = temp->next;
            delete temp;
            return true;
        }

        // Search for the key to be deleted
        while (temp != nullptr && temp->data != key) {
            prev = temp;
            temp = temp->next;
        }

        // If key was not present in linked list
        if (temp == nullptr) return false;

        // Unlink the node from the linked list
        prev->next = temp->next;
        delete temp;
        return true;
    }

    bool search(int key) {
        Node* temp = head;
        while (temp != nullptr) {
            if (temp->data == key) return true;
            temp = temp->next;
        }
        return false;
    }

    void display() {
        Node* temp = head;
        while (temp != nullptr) {
            std::cout << temp->data << " -> ";
            temp = temp->next;
        }
        std::cout << "NULL" << std::endl;
    }
};

int main() {
    SinglyLinkedList sll;
    sll.insertAtTail(10);
    sll.insertAtTail(20);
    sll.insertAtHead(5);
    sll.display();  // Expected output: 5 -> 10 -> 20 -> NULL

    std::cout << "Searching for 10: " << (sll.search(10) ? "Found" : "Not Found") << std::endl;
    sll.deleteNode(10);
    sll.display();  // Expected output: 5 -> 20 -> NULL

    return 0;
}
```

---

## Java Implementation

```java
public class SinglyLinkedList {
    
    // Inner node class representation
    private static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    private Node head;

    public SinglyLinkedList() {
        this.head = null;
    }

    public void insertAtHead(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }

    public void insertAtTail(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        Node temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = newNode;
    }

    public boolean deleteNode(int key) {
        Node temp = head;
        Node prev = null;

        if (temp != null && temp.data == key) {
            head = temp.next;
            return true;
        }

        while (temp != null && temp.data != key) {
            prev = temp;
            temp = temp.next;
        }

        if (temp == null) {
            return false;
        }

        prev.next = temp.next;
        return true;
    }

    public boolean search(int key) {
        Node temp = head;
        while (temp != null) {
            if (temp.data == key) {
                return true;
            }
            temp = temp.next;
        }
        return false;
    }

    public void display() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        SinglyLinkedList sll = new SinglyLinkedList();
        sll.insertAtTail(10);
        sll.insertAtTail(20);
        sll.insertAtHead(5);
        sll.display(); // Expected output: 5 -> 10 -> 20 -> null

        System.out.println("Searching for 10: " + sll.search(10));
        sll.deleteNode(10);
        sll.display(); // Expected output: 5 -> 20 -> null;
    }
}
```

---

## 3 Solved Examples

### Example 1: Reverse a Singly Linked List
*   **Problem Statement**: Given the head of a singly linked list, reverse the list, and return the pointer of the new head node.
*   **Constraint**: Change the actual directions of pointers, do not swap data contents.
*   **Approach (Iterative)**:
    1.  Initialize three pointers: `prev` as `None`, `curr` as `head`, and `next_node` as `None`.
    2.  Iterate through the list. For each node, store the next node (`next_node = curr.next`).
    3.  Reverse the current node's pointer (`curr.next = prev`).
    4.  Move `prev` and `curr` forward (`prev = curr`, `curr = next_node`).
    5.  Once the loop ends, set the `head` to `prev`.

```
Initial:          [1] ───> [2] ───> [3] ───> NULL
                 curr

Step 1: Save next node.
                  [1] ───> [2] ───> [3] ───> NULL
                 curr     next

Step 2: Reverse the next pointer of curr.
        NULL <─── [1]      [2] ───> [3] ───> NULL
         prev    curr     next

Step 3: Move prev and curr forward.
        NULL <─── [1]      [2] ───> [3] ───> NULL
                 prev     curr
                          next
```

*   **Python Code**:
```python
def reverse_list(head: Node) -> Node:
    prev = None
    curr = head
    while curr:
        next_node = curr.next  # Save next node
        curr.next = prev       # Reverse the link
        prev = curr            # Move prev forward
        curr = next_node       # Move curr forward
    return prev                # New head of the list
```
*   **Complexity**:
    *   **Time Complexity**: $O(N)$ (One pass through the list).
    *   **Space Complexity**: $O(1)$ (In-place pointer manipulations).

---

### Example 2: Detect Cycle in a Linked List (Floyd's Cycle Detection Algorithm)
*   **Problem Statement**: Determine if a linked list has a cycle in it. A cycle occurs if some node can be reached again by continuously following the `next` pointer.
*   **Approach (Tortoise & Hare)**:
    1.  Initialize two pointers, `slow` and `fast`, to the head.
    2.  `slow` moves 1 node at a time (`slow = slow.next`).
    3.  `fast` moves 2 nodes at a time (`fast = fast.next.next`).
    4.  If there is no cycle, `fast` will reach `NULL` quickly.
    5.  If there is a cycle, `fast` will enter the loop and eventually catch up to `slow` (i.e., `slow == fast`).

```
          ┌───────────────────┐
          ▼                   │
[1] ───> [2] ───> [3] ───> [4]┘
  ▲
slow
fast
```

*   **Python Code**:
```python
def has_cycle(head: Node) -> bool:
    if not head or not head.next:
        return False
        
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next          # Moves 1 step
        fast = fast.next.next     # Moves 2 steps
        
        if slow == fast:          # Meet point indicates cycle presence
            return True
            
    return False                  # fast reached end, no cycle
```
*   **Complexity**:
    *   **Time Complexity**: $O(N)$ (If a cycle exists, the fast pointer catches the slow pointer in less than $N$ cycles once both are inside the loop).
    *   **Space Complexity**: $O(1)$ (Uses only two reference pointers).

---

### Example 3: Find the Middle of a Linked List
*   **Problem Statement**: Given a singly linked list, return the middle node. If there are two middle nodes (even length), return the second middle node.
*   **Approach (Two Pointer / Runner)**:
    1.  Set two pointers `slow` and `fast` to the head of the list.
    2.  Advance `slow` by 1 step, and `fast` by 2 steps.
    3.  When `fast` reaches the end of the list (`NULL` for odd length, or last node for even length), `slow` will be pointing exactly to the middle node.

```
Odd list:   [1] ───> [2] ───> [3] ───> [4] ───> [5] ───> NULL
                     slow              fast      (fast.next.next is NULL)

Even list:  [1] ───> [2] ───> [3] ───> [4] ───> [5] ───> [6] ───> NULL
                               slow                               fast
```

*   **Python Code**:
```python
def find_middle(head: Node) -> Node:
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow  # slow represents the middle node
```
*   **Complexity**:
    *   **Time Complexity**: $O(N)$ (One-pass scan, visits each node at most once).
    *   **Space Complexity**: $O(1)$ (No memory allocated dynamically).

---

## 5 Interview Questions with Answers

### 1. How do you find the $N$-th node from the end of a Linked List?
**Answer**:
Using the **two-pointer approach** (often called fast/slow or primary/ahead):
1.  Initialize two pointers, `p1` and `p2`, at the `head`.
2.  Move `p1` forward by $N$ nodes.
3.  If `p1` becomes `NULL` during this step, the list contains fewer than $N$ nodes (throw an exception or return a sentinel value).
4.  If it is not null, move both `p1` and `p2` one step at a time simultaneously.
5.  When `p1` reaches the end (i.e. `p1` is `NULL` or points to the last node), `p2` will point to the $N$-th node from the end.

**Time Complexity**: $O(N)$ (Single traversal).
**Space Complexity**: $O(1)$.

---

### 2. What is the difference between a Singly Linked List and a Doubly Linked List?
**Answer**:

| Metric | Singly Linked List (SLL) | Doubly Linked List (DLL) |
| :--- | :--- | :--- |
| **Pointers per node** | 1 pointer (`next`) | 2 pointers (`next`, `prev`) |
| **Memory usage** | Less overhead (1 address per node) | Greater overhead (2 addresses per node) |
| **Traversal Direction** | Forward only | Forward and Backward |
| **Deletion efficiency** | Requires $O(N)$ to find the previous node of a target to change its link. | $O(1)$ deletion if the pointer of the node to be deleted is provided. |
| **Implementation complexity**| Simpler to implement | Harder to implement due to complex pointer updates. |

---

### 3. How do you merge two sorted linked lists into one sorted linked list?
**Answer**:
You can merge two sorted lists using an **iterative comparison strategy** with a dummy node:
1.  Create a temporary `dummy` node to act as the head of the new list.
2.  Keep a tracker pointer `tail` pointing to `dummy`.
3.  Compare the current nodes of both lists (say `L1` and `L2`).
4.  Attach the smaller node to `tail->next`, and advance that list's pointer.
5.  Move the `tail` pointer forward.
6.  Repeat steps 3-5 until one list becomes `NULL`.
7.  Append the remaining elements of the non-empty list directly to `tail->next`.
8.  Return `dummy->next`.

```python
def merge_two_lists(l1: Node, l2: Node) -> Node:
    dummy = Node(-1)
    tail = dummy
    
    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
        
    tail.next = l1 if l1 else l2
    return dummy.next
```

---

### 4. How do you remove duplicates from an unsorted linked list?
**Answer**:
There are two main strategies:
*   **Strategy A (Hashing)**: Use a Hash Set to store visited values. Traverse the list, checking if the current node's data is already in the set.
    *   If yes, change the pointer of the previous node to skip the current node.
    *   If no, add the current value to the set and advance the previous pointer.
    *   **Complexity**: $O(N)$ Time, $O(N)$ Space.
*   **Strategy B (Brute-Force)**: For each node, run an inner loop to check the remaining nodes and delete duplicates.
    *   **Complexity**: $O(N^2)$ Time, $O(1)$ Space. This is a viable option if extra memory is prohibited.

---

### 5. Why is Binary Search not efficient on a linked list?
**Answer**:
Binary search relies on **random access** to quickly locate middle elements (calculating index `mid = low + (high - low) / 2` in $O(1)$ time). 
In a linked list, there is no physical index-to-address calculation. To locate the "middle" element, you must perform linear traversals by following pointers from node to node, which takes $O(N)$ time. 

Even if you divide the list recursively:
*   Finding the middle node takes $O(N)$ time.
*   The recurrence relation becomes $T(N) = T(N/2) + O(N)$, which yields a time complexity of **$O(N \log N)$** (equivalent to Merge Sort) instead of the $O(\log N)$ search time achieved in arrays.

---

## Common Mistakes

1.  **Dereferencing NULL Pointers**: 
    Attempting to access `temp->next` or `temp->data` when `temp` is already `nullptr/None`. This causes segmentation faults (C++) or Null Pointer Exceptions (Java/Python). Always validate `if (temp != nullptr)` before accessing its properties.
2.  **Memory Leaks (Explicit Memory Management)**:
    In languages like C and C++, deleting a node from a list without manually freeing its heap memory via `free()` or `delete` leaves orphaned nodes in the heap, causing memory leaks.
3.  **Losing the List's Reference (Broken Links)**:
    Changing links in the middle of insertion or deletion without temporarily storing next addresses. 
    *   *Incorrect sequence*: `nodeA->next = nodeB;` (If we didn't save `nodeA->next`'s previous reference first, the rest of the list starting from `nodeA->next` is lost in memory).
4.  **Incorrect Boundary Updates**:
    Forgetting to update the `head` pointer when inserting at index `0` or deleting the first node. If the `head` is not updated, the list remains structurally unchanged or becomes invalid.
5.  **Off-by-one errors during search/traversal**:
    Using `while(temp->next != nullptr)` instead of `while(temp != nullptr)` when you want to visit every node. The first version stops prematurely at the last node, skipping its processing.

---

## Summary

*   A **Linked List** is a dynamic linear data structure composed of non-contiguously allocated nodes connected via pointer references.
*   **Primary Advantage**: Performs dynamic memory resizing and provides highly efficient $O(1)$ insertions and deletions compared to $O(N)$ in arrays.
*   **Primary Disadvantage**: It lacks random access capabilities, leading to slow $O(N)$ access speeds, high memory overhead due to pointer storage, and cache-unfriendly behavior.
*   **Variants**:
    *   *Singly Linked List* (Uni-directional).
    *   *Doubly Linked List* (Bi-directional).
    *   *Circular Linked List* (Last node references the head node).
*   **Crucial Interview Algorithms**: Iterative list reversal, Floyd's Cycle Detection (Tortoise and Hare), Runner technique (finding middle nodes), and pointer-based merging.