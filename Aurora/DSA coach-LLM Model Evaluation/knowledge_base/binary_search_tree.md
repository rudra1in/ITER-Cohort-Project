# Binary Search Tree

---

## Definition

A **Binary Search Tree (BST)** is a node-based binary tree data structure that possesses the following properties:

1. **Left Subtree Property:** The left subtree of a node contains only nodes with keys **less than** the node's key.
2. **Right Subtree Property:** The right subtree of a node contains only nodes with keys **greater than** the node's key.
3. **Subtree Recursion:** Both the left and right subtrees must also be binary search trees.
4. **No Duplicate Keys:** Typically, a BST does not allow duplicate keys, though some variations allow duplicates by placing them consistently either on the left or the right, or by maintaining a frequency count within the node.

```
          [50]
         /    \
      [30]    [70]
      /  \    /  \
    [20] [40][60] [80]
```

---

## Why it is needed

Before BSTs, linear data structures like Arrays and Linked Lists were standard:

* **Arrays (Sorted):** Finding an element is very fast ($O(\log n)$ using Binary Search), but inserting or deleting an element is slow ($O(n)$) because it requires shifting elements in memory.
* **Linked Lists:** Inserting and deleting elements can be fast ($O(1)$) if the pointer is already at the correct location, but searching for an element is slow ($O(n)$) because it requires sequential access.

The **Binary Search Tree** was designed to bridge this gap. It combines the fast, logarithmic searching capability of a sorted array with the dynamic insertion and deletion capabilities of a linked list. 

| Data Structure | Search Time | Insertion Time | Deletion Time |
| :--- | :--- | :--- | :--- |
| **Sorted Array** | $O(\log n)$ | $O(n)$ | $O(n)$ |
| **Linked List** | $O(n)$ | $O(1)$ (with pointer) | $O(1)$ (with pointer) |
| **Binary Search Tree (Average)** | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ |

---

## Characteristics

* **Inorder Traversal Guarantee:** An *Inorder* traversal (`Left -> Root -> Right`) of a BST always yields the keys in **strictly sorted ascending order**.
* **Structural Dependency:** The shape and height of a BST depend entirely on the order in which the keys are inserted. For instance, inserting keys in strictly sorted order ($1, 2, 3, 4, 5$) results in a degenerate tree (essentially a linked list).
* **Dynamic Size:** Unlike static arrays, a BST grows and shrinks dynamically in memory as elements are added or removed.
* **Relation to Binary Search:** Every node in a BST acts as a decision point. Comparing a target key with a node's key allows you to discard half of the remaining search space.

---

## Working

A BST operates on a divide-and-conquer strategy. At each step of a search, insertion, or deletion:
1. You compare the target value $K$ with the current node's value $C$.
2. If $K == C$, you have found your target.
3. If $K < C$, you branch to the **left child**, ignoring the entire right subtree.
4. If $K > C$, you branch to the **right child**, ignoring the entire left subtree.

This branching halves the remaining search path on average, mimicking the behavior of binary search on a sorted array.

---

## Memory Representation

In memory, a BST is represented dynamically using structures or classes linked together via references (pointers).

### Conceptual Node Layout
Each node contains three distinct fields:
1. **Data:** The actual value/key stored in the node.
2. **Left Pointer:** A memory address pointing to the left child node.
3. **Right Pointer:** A memory address pointing to the right child node.

```
+-----------------------------------+
|  Left Pointer  |  Data  |  Right  |
|   (address)    | (value)| Pointer |
+-----------------------------------+
```

### Memory Schematic Example
If we store nodes in dynamic memory (Heap), they might look like this:

```
Address: 0x100 (Root Node)
+------------------------+
| Left: 0x200 | Data: 50 | Right: 0x300 |
+------------------------+
       /                  \
      /                    \
Address: 0x200          Address: 0x300
+-------------------+   +-------------------+
| Null | 30 | Null  |   | Null | 70 | Null  |
+-------------------+   +-------------------+
```

---

## Types

1. **Unbalanced / Skewed BST:**
   * **Left-Skewed:** Every node has only a left child. It behaves exactly like a singly linked list.
   * **Right-Skewed:** Every node has only a right child.
2. **Balanced BST:**
   * A BST where the height of the left and right subtrees of any node differs by at most a specified limit. 
   * **Self-Balancing Binary Search Trees** automatically adjust their structures during insertions and deletions to guarantee $O(\log n)$ height. Examples include:
     * **AVL Trees:** Strictly balanced by height (difference $\le 1$).
     * **Red-Black Trees:** Moderately balanced using node coloring rules (used in standard library implementations like C++ `std::map` or Java `TreeMap`).
     * **Splay Trees:** Automatically move recently accessed nodes closer to the root.

---

## Operations

### 1. Search
To search for a key in a BST:
1. Start at the root node.
2. If the root is null or the key matches the root's key, return the root.
3. If the key is smaller than the root's key, search the left subtree recursively.
4. If the key is larger than the root's key, search the right subtree recursively.

#### Example: Search for `40`
```
          [50]         --> 40 < 50, go Left
         /    \
      [30]    [70]     --> 40 > 30, go Right
      /  \
    [20] [40]          --> 40 == 40, Found!
```

---

### 2. Insertion
To insert a new key into a BST:
1. Start at the root.
2. Compare the new key with the current node's key.
3. If the new key is smaller, go to the left child. If the left child is null, insert the new node here. Otherwise, repeat the process on the left child.
4. If the new key is larger, go to the right child. If the right child is null, insert the new node here. Otherwise, repeat the process on the right child.

#### Example: Insert `35`
```
          [50]         --> 35 < 50, go Left
         /    \
      [30]    [70]     --> 35 > 30, go Right
      /  \
    [20] [40]          --> 35 < 40, go Left. Left is Null!
         /
       [35]            --> Insert [35] here.
```

---

### 3. Deletion
Deleting a node is more complex because we must preserve the BST properties after removal. There are three distinct cases:

#### Case A: The node to delete is a Leaf Node (no children)
* Simply remove the node from the tree by setting its parent's pointer to null.

```
Delete 20:
          [50]                    [50]
         /    \                  /    \
      [30]    [70]     --->   [30]    [70]
      /  \                      \
    [20] [40]                   [40]
```

#### Case B: The node to delete has exactly One Child
* Bypass the node by linking its parent directly to its single child.

```
Delete 30:
          [50]                    [50]
         /    \                  /    \
      [30]    [70]     --->   [40]    [70]
        \                     
        [40]                  
```

#### Case C: The node to delete has Two Children
1. Find the **Inorder Successor** (the smallest node in its right subtree) OR the **Inorder Predecessor** (the largest node in its left subtree).
2. Copy the successor's/predecessor's value to the target node.
3. Delete the successor/predecessor node (which is guaranteed to have at most one child).

```
Delete 50 (Root):
Inorder Successor of 50 is 60 (minimum value in right subtree).

          [50]                    [60]  <-- Copy 60 to root
         /    \                  /    \
      [30]    [70]     --->   [30]    [70]
              /  \                    /  \
            [60] [80]              [NULL] [80] <-- Delete original 60
```

---

### 4. Traversals

* **Inorder (Left, Root, Right):** Visits nodes in sorted ascending order.
* **Preorder (Root, Left, Right):** Useful for creating a copy of the tree.
* **Postorder (Left, Right, Root):** Useful for deleting/freeing the entire tree from leaf to root.

---

## Time Complexity Table

Let $n$ be the number of nodes in the BST, and $h$ be the height of the tree.

| Operation | Best Case | Average Case | Worst Case (Skewed Tree) |
| :--- | :--- | :--- | :--- |
| **Search** | $O(1)$ | $O(\log n)$ | $O(n)$ |
| **Insertion** | $O(1)$ | $O(\log n)$ | $O(n)$ |
| **Deletion** | $O(1)$ | $O(\log n)$ | $O(n)$ |
| **Space (Traversals)** | $O(h)$ | $O(h)$ | $O(n)$ |

> **Note:** In the best-case scenarios for operations like Search/Insert, the target node might be the root node, resolving in $O(1)$ steps. On average, balanced heights yield $h \approx \log n$.

---

## Space Complexity

* **Auxiliary Space (Iterative Operations):** $O(1)$. No recursion stack is used.
* **Auxiliary Space (Recursive Operations):** $O(h)$ where $h$ is the height of the tree. This space is used by the system call stack.
  * In the **best/average case** (balanced tree), the space complexity is $O(\log n)$.
  * In the **worst case** (skewed tree), the space complexity becomes $O(n)$.
* **Total Structural Space:** $O(n)$ to store $n$ nodes.

---

## Advantages

* **Efficient Dynamic Operations:** Provides faster insertion and deletion times than sorted arrays.
* **Sorted Output for Free:** An inorder traversal extracts all stored elements in sorted order in linear time ($O(n)$).
* **Flexible Memory Allocation:** Nodes do not need to be stored in contiguous memory locations.
* **Custom Range Queries:** Easy to find all elements within a specified range $[Min, Max]$ by pruning unneeded subtrees.

---

## Disadvantages

* **Worst-case Performance degradation:** Without self-balancing mechanisms, sequential insertions collapse the BST into a linked list with $O(n)$ search time.
* **High Memory Overhead:** Each node must store two pointers (left and right) alongside the actual data.
* **No Random Access:** Unlike arrays, you cannot jump directly to the $i$-th element in $O(1)$ time. You must traverse from the root.

---

## Real World Applications

* **Database Indexes:** Most databases use B-Trees and B+ Trees (variants of BSTs) to index disk storage for quick record retrieval.
* **Virtual Memory Management:** Virtual memory areas (VMAs) in Unix-like operating systems are often kept in red-black trees to track memory allocations.
* **Symbol Tables:** Used in compilers to look up identifiers, variables, and function names quickly.
* **Spelling Checkers:** Used for fast word search and matching operations.
* **Network Routing Algorithms:** Used in routing tables to match destination IP prefixes.

---

## Python Implementation

```python
class Node:
    """Represents a single node in the BST."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """Represents the Binary Search Tree."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Public method to insert a key."""
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
        return root

    def search(self, key):
        """Public method to search for a key. Returns True if found."""
        return self._search_recursive(self.root, key) is not None

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    def delete(self, key):
        """Public method to delete a key."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        # Navigate the tree
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            # Node found: Handle deletion cases
            
            # Case 1 & 2: Leaf or single child (right only or left only)
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Node with two children
            # Get the inorder successor (smallest in the right subtree)
            root.key = self._min_value(root.right)
            # Delete the inorder successor
            root.right = self._delete_recursive(root.right, root.key)

        return root

    def _min_value(self, root):
        min_val = root.key
        while root.left is not None:
            min_val = root.left.key
            root = root.left
        return min_val

    def inorder(self):
        """Prints the inorder traversal of the BST."""
        result = []
        self._inorder_recursive(self.root, result)
        print(" -> ".join(map(str, result)))

    def _inorder_recursive(self, root, result):
        if root:
            self._inorder_recursive(root.left, result)
            result.append(root.key)
            self._inorder_recursive(root.right, result)


# Verification Execution
if __name__ == "__main__":
    bst = BinarySearchTree()
    elements = [50, 30, 70, 20, 40, 60, 80]
    for el in elements:
        bst.insert(el)

    print("Inorder traversal of the BST:")
    bst.inorder()  # Expected: 20 -> 30 -> 40 -> 50 -> 60 -> 70 -> 80

    print("\nSearch for 40:", bst.search(40))  # Expected: True
    print("Search for 90:", bst.search(90))  # Expected: False

    print("\nDelete 20 (Leaf node):")
    bst.delete(20)
    bst.inorder()

    print("\nDelete 30 (Node with one child):")
    bst.delete(30)
    bst.inorder()

    print("\nDelete 50 (Node with two children):")
    bst.delete(50)
    bst.inorder()
```

---

## C++ Implementation

```cpp
#include <iostream>

class BinarySearchTree {
private:
    struct Node {
        int key;
        Node* left;
        Node* right;
        Node(int val) : key(val), left(nullptr), right(nullptr) {}
    };

    Node* root;

    Node* insertRecursive(Node* node, int key) {
        if (node == nullptr) {
            return new Node(key);
        }
        if (key < node->key) {
            node->left = insertRecursive(node->left, key);
        } else if (key > node->key) {
            node->right = insertRecursive(node->right, key);
        }
        return node;
    }

    Node* searchRecursive(Node* node, int key) const {
        if (node == nullptr || node->key == key) {
            return node;
        }
        if (key < node->key) {
            return searchRecursive(node->left, key);
        }
        return searchRecursive(node->right, key);
    }

    Node* findMin(Node* node) const {
        while (node && node->left != nullptr) {
            node = node->left;
        }
        return node;
    }

    Node* deleteRecursive(Node* node, int key) {
        if (node == nullptr) return nullptr;

        if (key < node->key) {
            node->left = deleteRecursive(node->left, key);
        } else if (key > node->key) {
            node->right = deleteRecursive(node->right, key);
        } else {
            // Node found

            // Case 1 & 2: Leaf or Single Child
            if (node->left == nullptr) {
                Node* temp = node->right;
                delete node;
                return temp;
            } else if (node->right == nullptr) {
                Node* temp = node->left;
                delete node;
                return temp;
            }

            // Case 3: Two Children
            Node* temp = findMin(node->right);
            node->key = temp->key;
            node->right = deleteRecursive(node->right, temp->key);
        }
        return node;
    }

    void inorderRecursive(Node* node) const {
        if (node != nullptr) {
            inorderRecursive(node->left);
            std::cout << node->key << " ";
            inorderRecursive(node->right);
        }
    }

    void destroyTree(Node* node) {
        if (node != nullptr) {
            destroyTree(node->left);
            destroyTree(node->right);
            delete node;
        }
    }

public:
    BinarySearchTree() : root(nullptr) {}
    
    ~BinarySearchTree() {
        destroyTree(root);
    }

    void insert(int key) {
        root = insertRecursive(root, key);
    }

    bool search(int key) const {
        return searchRecursive(root, key) != nullptr;
    }

    void remove(int key) {
        root = deleteRecursive(root, key);
    }

    void printInorder() const {
        inorderRecursive(root);
        std::cout << std::endl;
    }
};

int main() {
    BinarySearchTree bst;
    bst.insert(50);
    bst.insert(30);
    bst.insert(70);
    bst.insert(20);
    bst.insert(40);
    bst.insert(60);
    bst.insert(80);

    std::cout << "Inorder Traversal: ";
    bst.printInorder(); // Expected: 20 30 40 50 60 70 80

    std::cout << "Search for 40: " << (bst.search(40) ? "Found" : "Not Found") << std::endl;
    std::cout << "Search for 95: " << (bst.search(95) ? "Found" : "Not Found") << std::endl;

    std::cout << "Removing 20 (Leaf): ";
    bst.remove(20);
    bst.printInorder();

    std::cout << "Removing 30 (One child): ";
    bst.remove(30);
    bst.printInorder();

    std::cout << "Removing 50 (Root/Two children): ";
    bst.remove(50);
    bst.printInorder();

    return 0;
}
```

---

## Java Implementation

```java
public class BinarySearchTree {

    // Node blueprint
    private static class Node {
        int key;
        Node left, right;

        public Node(int item) {
            key = item;
            left = right = null;
        }
    }

    private Node root;

    public BinarySearchTree() {
        root = null;
    }

    public void insert(int key) {
        root = insertRec(root, key);
    }

    private Node insertRec(Node root, int key) {
        if (root == null) {
            root = new Node(key);
            return root;
        }
        if (key < root.key) {
            root.left = insertRec(root.left, key);
        } else if (key > root.key) {
            root.right = insertRec(root.right, key);
        }
        return root;
    }

    public boolean search(int key) {
        return searchRec(root, key) != null;
    }

    private Node searchRec(Node root, int key) {
        if (root == null || root.key == key) {
            return root;
        }
        if (key < root.key) {
            return searchRec(root.left, key);
        }
        return searchRec(root.right, key);
    }

    public void delete(int key) {
        root = deleteRec(root, key);
    }

    private Node deleteRec(Node root, int key) {
        if (root == null) {
            return root;
        }

        if (key < root.key) {
            root.left = deleteRec(root.left, key);
        } else if (key > root.key) {
            root.right = deleteRec(root.right, key);
        } else {
            // Node matches key

            // Case 1 & 2: Single or zero children
            if (root.left == null) {
                return root.right;
            } else if (root.right == null) {
                return root.left;
            }

            // Case 3: Two children
            root.key = minValue(root.right);
            root.right = deleteRec(root.right, root.key);
        }
        return root;
    }

    private int minValue(Node root) {
        int minv = root.key;
        while (root.left != null) {
            minv = root.left.key;
            root = root.left;
        }
        return minv;
    }

    public void inorder() {
        inorderRec(root);
        System.out.println();
    }

    private void inorderRec(Node root) {
        if (root != null) {
            inorderRec(root.left);
            System.out.print(root.key + " ");
            inorderRec(root.right);
        }
    }

    public static void main(String[] args) {
        BinarySearchTree bst = new BinarySearchTree();

        bst.insert(50);
        bst.insert(30);
        bst.insert(70);
        bst.insert(20);
        bst.insert(40);
        bst.insert(60);
        bst.insert(80);

        System.out.print("Inorder Traversal: ");
        bst.inorder(); // Expected: 20 30 40 50 60 70 80

        System.out.println("Search 40: " + bst.search(40)); // True
        System.out.println("Search 100: " + bst.search(100)); // False

        System.out.print("Delete 20 (Leaf): ");
        bst.delete(20);
        bst.inorder();

        System.out.print("Delete 30 (One child): ");
        bst.delete(30);
        bst.inorder();

        System.out.print("Delete 50 (Two children): ");
        bst.delete(50);
        bst.inorder();
    }
}
```

---

## 3 Solved Examples

### Example 1: Construct a BST from an Unsorted Array
**Input Array:** `[50, 30, 20, 40, 70, 60, 80]`

#### Step-by-Step Construction:
1. **Insert 50:** Tree is empty. Make `50` the root.
   ```
   [50]
   ```
2. **Insert 30:** Compare $30 < 50$. Place as the left child of `50`.
   ```
     [50]
     /
   [30]
   ```
3. **Insert 20:** Compare $20 < 50$ (go left), compare $20 < 30$. Place as the left child of `30`.
   ```
       [50]
       /
     [30]
     /
   [20]
   ```
4. **Insert 40:** Compare $40 < 50$ (go left), compare $40 > 30$. Place as the right child of `30`.
   ```
       [50]
       /
     [30]
     /  \
   [20] [40]
   ```
5. **Insert 70:** Compare $70 > 50$. Place as the right child of `50`.
   ```
          [50]
         /    \
      [30]    [70]
      /  \
    [20] [40]
   ```
6. **Insert 60:** Compare $60 > 50$ (go right), compare $60 < 70$. Place as the left child of `70`.
   ```
          [50]
         /    \
      [30]    [70]
      /  \    /
    [20] [40][60]
   ```
7. **Insert 80:** Compare $80 > 50$ (go right), compare $80 > 70$. Place as the right child of `70`.
   ```
          [50]
         /    \
      [30]    [70]
      /  \    /  \
    [20] [40][60] [80]
   ```

---

### Example 2: Delete Node `50` (Root) from the Tree constructed in Example 1
**Target Tree:**
```
          [50]
         /    \
      [30]    [70]
      /  \    /  \
    [20] [40][60] [80]
```

#### Step-by-Step Deletion Process:
1. **Identify Target Node:** The target value to delete is `50` which is located at the root.
2. **Evaluate Case:** Node `50` has two children (`30` and `70`).
3. **Find Inorder Successor:** Look at the right subtree of `50` (rooted at `70`) and find its smallest element.
   * Start at `70`, move to the left child: `60`.
   * Node `60` has no left children. Hence, `60` is the **inorder successor**.
4. **Copy Successor Key:** Overwrite the target node's key with the successor's key.
   ```
          [60]  <-- Changed from 50
         /    \
      [30]    [70]
      /  \    /  \
    [20] [40][60] [80]
   ```
5. **Delete Successor Node:** Delete the original successor node `60` from the right subtree. Because `60` is a leaf node, this is solved by Case A (simple link truncation).
   ```
          [60]
         /    \
      [30]    [70]
      /  \       \
    [20] [40]    [80]
   ```

---

### Example 3: Find the Lowest Common Ancestor (LCA) of `20` and `40`
Using the resulting tree from Example 1:
```
          [50]
         /    \
      [30]    [70]
      /  \    /  \
    [20] [40][60] [80]
```

The LCA is the lowest node in a tree that has both targets as descendants.

#### Step-by-Step Walkthrough:
1. **Start at Root (50):** 
   * Compare both targets (`20`, `40`) with root `50`.
   * Both $20 < 50$ and $40 < 50$. This means the LCA must reside in the **left subtree**. Move search to node `30`.
2. **Move to Node `30`:**
   * Compare both targets (`20`, `40`) with node `30`.
   * $20 < 30$ (left) and $40 > 30$ (right).
   * Since the targets split (one is smaller, one is larger), this current node `30` is the **split point**.
3. **Result:** Node `30` is the Lowest Common Ancestor.

---

## 5 Interview Questions with Answers

### Q1. How do you validate whether a given Binary Tree is a valid Binary Search Tree?
**Answer:**  
Checking only whether each node's left child is smaller and right child is larger is a common pitfall. Instead, you must pass down a range `[min_allowed, max_allowed]` recursively.
* **Algorithm:**
  1. The root has a range of `[-infinity, +infinity]`.
  2. When traversing left, update the upper bound: `max_allowed = parent.key`.
  3. When traversing right, update the lower bound: `min_allowed = parent.key`.
  4. If any node's key falls outside its valid range, return `False`.

* **Python Implementation:**
  ```python
  def isValidBST(root, min_val=float('-inf'), max_val=float('inf')):
      if not root:
          return True
      if not (min_val < root.key < max_val):
          return False
      return (isValidBST(root.left, min_val, root.key) and 
              isValidBST(root.right, root.key, max_val))
  ```

---

### Q2. How can you find the $k$-th smallest element in a BST?
**Answer:**  
An **inorder traversal** of a BST yields elements in sorted ascending order. We can perform an in-order traversal and decrement $k$ at each node visit. When $k$ reaches $0$, we have found our element.
* **Optimization:** If we are allowed to modify the node structure, we can store the size of the left subtree in each node (order-statistic tree). This reduces the search complexity to $O(h)$ instead of $O(n)$.

---

### Q3. How do you convert a Sorted Array to a Balanced Binary Search Tree?
**Answer:**  
To keep the tree balanced, the middle element of the sorted array must become the root of the tree. The left half of the array forms the left subtree, and the right half forms the right subtree.

* **Algorithm:**
  1. Find the middle element index: `mid = (left + right) // 2`.
  2. Create a node with array value at `mid`.
  3. Recursively run the process for array slice `[left, mid - 1]` to build the left child.
  4. Recursively run the process for array slice `[mid + 1, right]` to build the right child.

* **Python Implementation:**
  ```python
  def sortedArrayToBST(arr):
      if not arr:
          return None
      mid = len(arr) // 2
      root = Node(arr[mid])
      root.left = sortedArrayToBST(arr[:mid])
      root.right = sortedArrayToBST(arr[mid+1:])
      return root
  ```

---

### Q4. What is the Inorder Successor of a node in a BST, and how do you find it?
**Answer:**  
The inorder successor of a node $N$ is the node with the smallest key value greater than the key of $N$.
* **Case 1: If the right subtree of $N$ is not null:**
  * The successor is the minimum node in $N$'s right subtree.
* **Case 2: If the right subtree of $N$ is null:**
  * Start searching from the root. Keep track of the last node where you took a left turn. That ancestor is your inorder successor.

---

### Q5. What is the difference between a BST and a Binary Heap?
**Answer:**
1. **Ordering Property:**
   * **BST:** Left descendants are smaller than parent; right descendants are larger. This creates a horizontal ordering.
   * **Binary Heap:** Parents are strictly larger (Max-Heap) or smaller (Min-Heap) than their children. There is no ordering relationship between sibling nodes.
2. **Search Time Complexity:**
   * **BST:** Average search takes $O(\log n)$ time.
   * **Heap:** Searching for an arbitrary key takes $O(n)$ time because it is not ordered horizontally. Heaps are designed to find only the min/max element in $O(1)$ time.
3. **Structure Property:**
   * **BST:** Can have arbitrary tree shapes (unless self-balanced).
   * **Heap:** Must always be a **complete binary tree** (filled level-by-level from left to right).

---

## Common Mistakes

1. **Local Variable Check Only:** Checking only if `node.left.key < node.key < node.right.key` recursively is incorrect. A node's left child could be smaller than the node but larger than one of its ancestors, which violates the BST property. Range conditions must span the entire recursive path.
2. **Ignoring Skewed Tree Cases:** Assuming operations always run in $O(\log n)$. In interview situations, always mention that unless a BST is explicitly balanced (e.g., AVL or Red-Black Tree), the worst-case performance is $O(n)$.
3. **Memory Leaks in C++:** When deleting a node with children, failing to call `delete` on the target nodes or losing pointers to subtrees can cause memory leaks.
4. **Modifying Keys In-Place:** Changing the key of an existing node in-place will break the BST invariant. To update a key, the old node must first be deleted, and a new node with the updated key must be inserted.

---

## Summary

* A **Binary Search Tree** is an ordered tree structure that ensures fast searches, insertions, and deletions ($O(\log n)$ average case).
* The central property of a BST is that **$\text{Left child} < \text{Root} < \text{Right child}$**.
* **Inorder traversal** on a BST visits nodes in strictly sorted order.
* Without structural balancing, a BST can degenerate into a linked list with $O(n)$ operations, highlighting the practical necessity of **Self-Balancing BSTs** like AVL and Red-Black Trees in production-grade software.