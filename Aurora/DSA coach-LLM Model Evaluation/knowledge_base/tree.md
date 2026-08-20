# Tree

---

## Definition

A **Tree** is a non-linear, hierarchical data structure consisting of a collection of entities called **nodes** connected by directed or undirected **edges**. Unlike linear data structures (such as Arrays, Linked Lists, Stacks, and Queues) which store data sequentially, a tree organizes data in a parent-child relationship.

Formally, in graph theory, a tree is defined as an **acyclic connected graph** $G = (V, E)$, where:
*   $V$ is a set of vertices (nodes).
*   $E$ is a set of edges connecting these vertices.
*   The number of edges is exactly $|V| - 1$.
*   There is exactly one unique path between any two nodes.

```
       [A]          <-- Root Node
      /   \
    [B]   [C]       <-- Parent / Child Nodes
   /   \     \
 [D]   [E]   [F]    <-- Leaf Nodes (No children)
```

---

## Why it is needed

Linear data structures have significant performance trade-offs:
1.  **Arrays**: Offer $O(1)$ access time if the index is known, but search in an unsorted array takes $O(n)$ time. Insertion and deletion require shifting elements, taking $O(n)$ time.
2.  **Linked Lists**: Offer $O(1)$ insertion and deletion once the position is found, but searching for an element requires a linear scan taking $O(n)$ time.

Trees bridge this gap by offering highly efficient operations:
*   **Logarithmic Search and Modification**: Balanced trees (like AVL or Red-Black trees) allow searching, insertion, and deletion in $O(\log n)$ time.
*   **Hierarchical Representation**: Many real-world domains are inherently hierarchical (e.g., file systems, organization charts, XML/HTML documents). Linear structures cannot naturally model these relationships.
*   **Efficient Sorting and Priority**: Structures like Heaps (a type of tree) allow $O(1)$ access to the minimum or maximum element and $O(\log n)$ updates, which is optimal for priority queues.

---

## Characteristics

To understand and manipulate trees, you must master their fundamental terminology and properties:

```
             (Root: A)                -- Depth 0, Height 3
             /       \
         (B)           (C)            -- Depth 1, Height 2
        /   \             \
     (D)     (E)           (F)        -- Depth 2, Height 1
            /   \
          (G)   (H)                   -- Depth 3, Height 0
```

*   **Root**: The topmost node of a tree. It is the unique node that has no parent (Node `A`).
*   **Parent**: A node that has an edge leading to a child node. For example, `B` is the parent of `D` and `E`.
*   **Child**: A node directly connected to another node when moving away from the root. `D` and `E` are children of `B`.
*   **Leaf Node (External Node)**: A node with no children (Nodes `D`, `G`, `H`, and `F`).
*   **Internal Node**: A node with at least one child (Nodes `A`, `B`, `C`, and `E`).
*   **Edge**: The link or connection between two nodes.
*   **Siblings**: Nodes that share the same parent. For example, `B` and `C` are siblings; `D` and `E` are siblings.
*   **Path**: A sequence of nodes and edges connecting a node to another node. The path from `A` to `G` is `A -> B -> E -> G`.
*   **Subtree**: Any node in a tree can be viewed as the root of a smaller tree, called a subtree. For example, the tree rooted at `B` is a subtree of `A`.
*   **Ancestors**: All nodes along the path from the root to a given node (excluding the node itself). Ancestors of `G` are `E`, `B`, and `A`.
*   **Descendants**: All nodes reachable from a node by moving downwards. Descendants of `B` are `D`, `E`, `G`, and `H`.
*   **Degree of a Node**: The total number of children a node has. The degree of `B` is 2; the degree of `F` is 0.
*   **Degree of a Tree**: The maximum degree among all nodes in the tree.
*   **Depth of a Node**: The number of edges along the unique path from the root to that node. The depth of root `A` is 0; the depth of `G` is 3.
*   **Height of a Node**: The number of edges on the longest downward path from that node to a leaf. The height of `E` is 1 (path `E -> G` or `E -> H`); the height of root `A` is 3.
*   **Height of a Tree**: The height of the root node (which is equivalent to the maximum depth of any node in the tree).

---

## Working

Trees work by maintaining structural pointers (or references) from parent nodes to child nodes. 

```
               [ Parent Node ]
               |  Data: Value |
               |  Left  | Right |
                 /          \
                /            \
    [ Left Child ]          [ Right Child ]
    | Data: Value |         | Data: Value |
    | Left | Right|         | Left | Right|
```

The system interacts with a tree by holding a single pointer to the **Root Node**. 
*   To read or manipulate data, algorithms traverse the tree by following these pointers.
*   Unlike linear structures where traversal is straightforward (left-to-right), tree traversal requires making branching choices at each node.
*   Because a tree is a recursive structure (a tree is composed of a root and several subtrees), almost all operations on trees can be elegantly implemented using **recursion**.

---

## Memory Representation

Trees can be represented in memory in two main ways:

### 1. Linked Representation (Dynamic Node Allocation)
This is the most common representation. Each node is dynamically allocated on the heap as an object or structure containing a data field and pointers to its children.

For a Binary Tree:
```
+------------------------+
|      Left Pointer      |  ---> Points to Left Child Node
+------------------------+
|          Data          |  ---> Stores actual value
+------------------------+
|     Right Pointer      |  ---> Points to Right Child Node
+------------------------+
```

### 2. Array Representation (Sequential Representation)
Typically used for **Complete Binary Trees** (such as heaps). Nodes are stored in a contiguous array without explicit pointers. The structural relationship is maintained implicitly using mathematical indices.

If the root is stored at index `0` (0-based indexing):
*   The parent of node at index `i` is at index: $\lfloor \frac{i - 1}{2} \rfloor$
*   The left child of node at index `i` is at index: $2i + 1$
*   The right child of node at index `i` is at index: $2i + 2$

```
Tree:
      (A)
     /   \
   (B)   (C)
   / \
 (D) (E)

Array Representation:
Index:  0    1    2    3    4
Array: [A]  [B]  [C]  [D]  [E]
```

---

## Types

```
                                    Tree
                                     |
       +-----------------------------+-----------------------------+
       |                             |                             |
  General Tree                 Binary Tree                       Trie
                                     |
             +-----------------------+-----------------------+
             |                                               |
    Binary Search Tree (BST)                         Self-Balancing Trees
                                                             |
                                               +-------------+-------------+
                                               |                           |
                                           AVL Tree                 Red-Black Tree
```

### 1. General Tree
A tree where there are absolutely no constraints on the number of children a node can have.

### 2. Binary Tree
A tree in which each node can have at most two children, referred to as the left child and the right child.
*   **Full Binary Tree**: Every node has either 0 or 2 children. No node has only 1 child.
*   **Complete Binary Tree**: All levels are completely filled except possibly the last level, which is filled from left to right.
*   **Perfect Binary Tree**: All internal nodes have exactly two children, and all leaf nodes are at the exact same level.
*   **Degenerate (Skewed) Tree**: A tree where each parent node has only one child. It behaves essentially like a Linked List, degrading operations to $O(n)$.

### 3. Binary Search Tree (BST)
An extension of the Binary Tree with a critical ordering property:
*   The value of all nodes in the left subtree of a node is strictly **less than** the node's value.
*   The value of all nodes in the right subtree of a node is strictly **greater than** (or equal to, depending on implementation) the node's value.

### 4. AVL Tree
A self-balancing Binary Search Tree where the difference between the heights of the left and right subtrees (called the **Balance Factor**) of any node cannot exceed $1$ or $-1$. If at any point they differ by more than 1, rotations are performed to restore balance.

$$\text{Balance Factor} = \text{Height}(\text{Left Subtree}) - \text{Height}(\text{Right Subtree}) \in \{-1, 0, 1\}$$

### 5. Red-Black Tree
A self-balancing Binary Search Tree where each node has a color attribute (Red or Black). It maintains balance using rules involving node colors during insertions and deletions, ensuring the tree's height remains $O(\log n)$. It is widely used in standard library maps and sets (e.g., C++ `std::map`, Java `TreeMap`).

### 6. Trie (Prefix Tree)
An information re**trie**val tree optimized for string searches. Nodes do not store keys; instead, their position in the tree defines the key they are associated with.

---

## Operations

To illustrate operations clearly, we will use a **Binary Search Tree (BST)** as our reference model.

### 1. Insertion
To insert a node with value `X`:
1.  Compare `X` with the current node's value.
2.  If `X` is smaller, recurse down the left subtree.
3.  If `X` is larger, recurse down the right subtree.
4.  Once a null spot is reached, construct the new node and link it there.

#### Example: Insert `15` into the BST below

```
      (20)                 (20)                 (20)
     /    \               /    \               /    \
  (10)    (30)   ===>  (10)    (30)   ===>  (10)    (30)
                       \                    \
                       (15)                 (15)  <-- Inserted
```

1.  Compare $15$ with root $20$. Since $15 < 20$, go left to Node $10$.
2.  Compare $15$ with Node $10$. Since $15 > 10$, go right.
3.  The right child of $10$ is `null`. Create Node $15$ and link it as the right child of $10$.

---

### 2. Deletion
Deleting a node `X` from a BST involves handling three possible structural scenarios:

#### Case A: The node to be deleted is a leaf (has 0 children)
Simply remove the node and update its parent's child reference to `null`.

**Example: Delete `5`**
```
      (10)                 (10)
     /    \    ===>       /    \
   (5)    (15)               (15)
```

#### Case B: The node to be deleted has exactly one child
Bypass the node by linking its parent directly to its child.

**Example: Delete `15` (which has child `18`)**
```
      (10)                 (10)
     /    \    ===>       /    \
   (5)    (15)          (5)    (18)
            \
            (18)
```

#### Case C: The node to be deleted has two children
This is the most complex case. You cannot simply pull up a child because it would break the binary tree structure.
1.  Find either the **Inorder Successor** (smallest node in the right subtree) or the **Inorder Predecessor** (largest node in the left subtree).
2.  Copy the successor's value into the target node.
3.  Recursively delete the successor node (which is guaranteed to have at most 1 child, falling into Case A or Case B).

**Example: Delete `10`**
```
         (10) <-- Node to delete                (12) <-- Value copied
        /    \                                 /    \
      (5)    (15)              ===>          (5)    (15)
            /    \                                    \
          (12)   (18)                                 (18)
           \                                           
           (13)  <-- Succ is (12). Right child (13) is linked to parent (15)
```

---

### 3. Search
To locate value `X` in a BST:
1.  Start at the root.
2.  If the root is null, the value does not exist (return `null`/`false`).
3.  If the root's value equals `X`, return the node (found!).
4.  If `X < root.val`, search recursively in the left subtree.
5.  If `X > root.val`, search recursively in the right subtree.

---

### 4. Traversals
Traversing means visiting every node in the tree exactly once. There are two primary categories:

#### A. Depth-First Search (DFS) Traversals

##### I. Inorder Traversal (Left, Root, Right)
Visits the left subtree, then the root node, and finally the right subtree.
*   **Key Property**: An Inorder traversal of a BST always yields the values in **strictly ascending order**.
*   **Recursive Formula**: $T(node) = \text{Inorder}(node.left) \to \text{Visit}(node) \to \text{Inorder}(node.right)$

##### II. Preorder Traversal (Root, Left, Right)
Visits the root node first, then the left subtree, and finally the right subtree.
*   **Key Property**: Highly useful for making a clone/copy of a tree, or generating prefix expressions.
*   **Recursive Formula**: $T(node) = \text{Visit}(node) \to \text{Preorder}(node.left) \to \text{Preorder}(node.right)$

##### III. Postorder Traversal (Left, Right, Root)
Visits the left subtree, then the right subtree, and finally the root node.
*   **Key Property**: Useful for deleting trees, evaluating postfix expressions, or calculating the size/height of subtrees bottom-up.
*   **Recursive Formula**: $T(node) = \text{Postorder}(node.left) \to \text{Postorder}(node.right) \to \text{Visit}(node)$

---

#### B. Breadth-First Search (BFS) Traversal

##### Level-Order Traversal
Visits nodes level-by-level, from top to bottom, and left to right within each level. It is implemented iteratively using a **Queue**.

---

### Dry Run of Traversals on a Sample Tree

```
      (1)
     /   \
   (2)   (3)
   / \
 (4) (5)
```

*   **Inorder (L-N-R)**:
    1.  Go left from `1` to `2`, go left from `2` to `4`.
    2.  `4` has no left child. Print `4`. `4` has no right child.
    3.  Backtrack to `2`. Print `2`.
    4.  Go right from `2` to `5`. `5` has no left child. Print `5`.
    5.  Backtrack to `1`. Print `1`.
    6.  Go right from `1` to `3`. `3` has no left child. Print `3`.
    *   **Output**: `4, 2, 5, 1, 3`

*   **Preorder (N-L-R)**:
    1.  Print root `1`.
    2.  Go left to `2`. Print `2`.
    3.  Go left to `4`. Print `4`.
    4.  Go right from `2` to `5`. Print `5`.
    5.  Go right from `1` to `3`. Print `3`.
    *   **Output**: `1, 2, 4, 5, 3`

*   **Postorder (L-R-N)**:
    1.  Go left-most to `4`. Print `4`.
    2.  Go to sibling of `4` which is `5`. Print `5`.
    3.  Print parent of `4` and `5` which is `2`.
    4.  Go to right child of `1` which is `3`. Print `3`.
    5.  Print root `1`.
    *   **Output**: `4, 5, 2, 3, 1`

*   **Level-Order**:
    1.  Level 0: `1`
    2.  Level 1: `2, 3`
    3.  Level 2: `4, 5`
    *   **Output**: `1, 2, 3, 4, 5`

---

## Time Complexity Table

Let $n$ be the total number of nodes in the tree.

| Operation | Unbalanced Binary Tree | Binary Search Tree (Average) | Binary Search Tree (Worst Case - Skewed) | Balanced Trees (AVL, Red-Black) |
| :--- | :--- | :--- | :--- | :--- |
| **Search** | $O(n)$ | $O(\log n)$ | $O(n)$ | $O(\log n)$ |
| **Insertion** | $O(1)$ (if pointer known) | $O(\log n)$ | $O(n)$ | $O(\log n)$ |
| **Deletion** | $O(n)$ | $O(\log n)$ | $O(n)$ | $O(\log n)$ |
| **Preorder** | $O(n)$ | $O(n)$ | $O(n)$ | $O(n)$ |
| **Inorder** | $O(n)$ | $O(n)$ | $O(n)$ | $O(n)$ |
| **Postorder** | $O(n)$ | $O(n)$ | $O(n)$ | $O(n)$ |
| **Level-Order**| $O(n)$ | $O(n)$ | $O(n)$ | $O(n)$ |

---

## Space Complexity

*   **Traversals (Inorder/Preorder/Postorder - Recursive)**:
    *   **Average Case (Balanced Tree)**: $O(\log n)$ stack space (proportional to tree height).
    *   **Worst Case (Skewed Tree)**: $O(n)$ stack space.
*   **Level-Order Traversal (Iterative)**:
    *   **Space**: $O(w)$ where $w$ is the maximum width of the tree. In a perfect binary tree, the maximum width is at the leaf level, which contains $\lceil n/2 \rceil$ nodes, leading to $O(n)$ space complexity.
*   **Structural Storage**:
    *   $O(n)$ to store $n$ nodes in memory.

---

## Advantages

1.  **Reflects Real-world Hierarchies**: Naturally maps data like folder directories, organizational structures, and biological classifications.
2.  **Highly Adaptable size**: Dynamic node allocation means no fixed array boundaries. The tree grows and shrinks as needed.
3.  **Extremely Fast Search/Modify**: Balanced binary trees achieve $O(\log n)$ operations. For $1,000,000$ items, an array search takes up to $1,000,000$ operations, whereas a balanced BST takes only $\approx 20$ operations.
4.  **Order Maintenance**: BSTs keep elements organized dynamically, which is much faster than repeatedly sorting an array.

---

## Disadvantages

1.  **Memory Overhead**: Each node must store data *plus* multiple pointers (`left`, `right`, and sometimes `parent`).
2.  **No Constant Time Access**: Unlike arrays where you can directly access index `[99]` in $O(1)$ time, a tree must be traversed from the root, requiring up to $O(\log n)$ steps.
3.  **Worst-Case Degradation**: Without complex self-balancing algorithms (AVL, Red-Black), insertions can cause a tree to become highly skewed, turning its performance into $O(n)$ (equivalent to a slow linked list).
4.  **Implementation Complexity**: Writing and debugging balanced tree modifications (such as AVL rotations or Red-Black recolorings) is highly complex.

---

## Real World Applications

1.  **File Systems**: Operating systems structure directories and files as trees (e.g., Windows NTFS, Linux ext4).
2.  **Domain Name System (DNS)**: Resolves domain names hierarchically (e.g., `. -> .com -> google.com`).
3.  **Databases**: Indexing systems in major databases (like MySQL, PostgreSQL, Oracle) utilize **B-Trees** and **B+ Trees** to perform lightning-fast queries on disk storage.
4.  **Compilers**: Programming language compilers parse raw source code into an **Abstract Syntax Tree (AST)** to validate semantics and generate machine code.
5.  **Network Routing**: Trees like Spanning Trees are used by routers to construct loop-free paths across network bridges.
6.  **HTML/XML DOM**: Modern web browsers represent pages internally using the **Document Object Model (DOM)** tree to quickly render and manipulate layouts.

---

## Python Implementation

Below is a complete, fully functional Python implementation of a Binary Search Tree (BST) featuring insertion, searching, deletion (covering all three cases), and all major traversals.

```python
class Node:
    """Represents a single node in the Binary Search Tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """Represents the BST and handles operations."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Inserts a new key into the BST."""
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
        """Searches for a key in the BST. Returns True if found, False otherwise."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    def delete(self, key):
        """Deletes a key from the BST."""
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
            # Found the node to delete!
            
            # Case 1 & 2: Node has 0 or 1 child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Node has two children
            # Find the inorder successor (smallest in the right subtree)
            successor = self._min_value_node(root.right)
            # Copy the successor's content to this node
            root.key = successor.key
            # Delete the inorder successor
            root.right = self._delete_recursive(root.right, successor.key)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Depth-First Search Traversals
    def inorder(self):
        res = []
        self._inorder_recursive(self.root, res)
        return res

    def _inorder_recursive(self, root, res):
        if root:
            self._inorder_recursive(root.left, res)
            res.append(root.key)
            self._inorder_recursive(root.right, res)

    def preorder(self):
        res = []
        self._preorder_recursive(self.root, res)
        return res

    def _preorder_recursive(self, root, res):
        if root:
            res.append(root.key)
            self._preorder_recursive(root.left, res)
            self._preorder_recursive(root.right, res)

    def postorder(self):
        res = []
        self._postorder_recursive(self.root, res)
        return res

    def _postorder_recursive(self, root, res):
        if root:
            self._postorder_recursive(root.left, res)
            self._postorder_recursive(root.right, res)
            res.append(root.key)

    # Breadth-First Search Traversal
    def level_order(self):
        res = []
        if self.root is None:
            return res
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            res.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

# --- Demonstration ---
if __name__ == "__main__":
    bst = BinarySearchTree()
    # Constructing a sample BST
    #         50
    #       /    \
    #     30      70
    #    /  \    /  \
    #   20  40  60  80
    
    insert_keys = [50, 30, 70, 20, 40, 60, 80]
    for k in insert_keys:
        bst.insert(k)

    print("Inorder Traversal:   ", bst.inorder())      # Expected: [20, 30, 40, 50, 60, 70, 80]
    print("Preorder Traversal:  ", bst.preorder())     # Expected: [50, 30, 20, 40, 70, 60, 80]
    print("Postorder Traversal: ", bst.postorder())    # Expected: [20, 40, 30, 60, 80, 70, 50]
    print("Level-order Traver.: ", bst.level_order())   # Expected: [50, 30, 70, 20, 40, 60, 80]

    print("\nSearch 40:", bst.search(40))              # Expected: True
    print("Search 99:", bst.search(99))                # Expected: False

    print("\n--- Deleting Node 20 (Leaf Node Case) ---")
    bst.delete(20)
    print("Inorder Traversal after deletion: ", bst.inorder())

    print("\n--- Deleting Node 30 (Two Children Case) ---")
    bst.delete(30)
    print("Inorder Traversal after deletion: ", bst.inorder())
```

---

## C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <queue>

struct Node {
    int key;
    Node* left;
    Node* right;

    Node(int val) {
        key = val;
        left = nullptr;
        right = nullptr;
    }
};

class BinarySearchTree {
private:
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

    bool searchRecursive(Node* node, int key) {
        if (node == nullptr) return false;
        if (node->key == key) return true;
        if (key < node->key) return searchRecursive(node->left, key);
        return searchRecursive(node->right, key);
    }

    Node* minValueNode(Node* node) {
        Node* current = node;
        while (current && current->left != nullptr) {
            current = current->left;
        }
        return current;
    }

    Node* deleteRecursive(Node* node, int key) {
        if (node == nullptr) return node;

        if (key < node->key) {
            node->left = deleteRecursive(node->left, key);
        } else if (key > node->key) {
            node->right = deleteRecursive(node->right, key);
        } else {
            // Target Node Found

            // Case 1 & 2: 0 or 1 child
            if (node->left == nullptr) {
                Node* temp = node->right;
                delete node;
                return temp;
            } else if (node->right == nullptr) {
                Node* temp = node->left;
                delete node;
                return temp;
            }

            // Case 3: 2 children
            Node* temp = minValueNode(node->right);
            node->key = temp->key;
            node->right = deleteRecursive(node->right, temp->key);
        }
        return node;
    }

    void inorderRecursive(Node* node, std::vector<int>& result) {
        if (node) {
            inorderRecursive(node->left, result);
            result.push_back(node->key);
            inorderRecursive(node->right, result);
        }
    }

    void destroyTree(Node* node) {
        if (node) {
            destroyTree(node->left);
            destroyTree(node->right);
            delete node;
        }
    }

public:
    BinarySearchTree() {
        root = nullptr;
    }

    ~BinarySearchTree() {
        destroyTree(root);
    }

    void insert(int key) {
        root = insertRecursive(root, key);
    }

    bool search(int key) {
        return searchRecursive(root, key);
    }

    void remove(int key) {
        root = deleteRecursive(root, key);
    }

    std::vector<int> inorder() {
        std::vector<int> result;
        inorderRecursive(root, result);
        return result;
    }

    void levelOrder() {
        if (!root) return;
        std::queue<Node*> q;
        q.push(root);

        while (!q.empty()) {
            Node* curr = q.front();
            q.pop();
            std::cout << curr->key << " ";
            if (curr->left) q.push(curr->left);
            if (curr->right) q.push(curr->right);
        }
        std::cout << "\n";
    }
};

int main() {
    BinarySearchTree bst;
    bst.insert(50);
    bst.insert(30);
    bst.insert(70);
    bst.insert(20);
    bst.insert(40);

    std::cout << "Inorder Traversal: ";
    std::vector<int> sortedKeys = bst.inorder();
    for (int key : sortedKeys) {
        std::cout << key << " ";
    }
    std::cout << "\n";

    std::cout << "Level Order Traversal: ";
    bst.levelOrder();

    std::cout << "Search 30: " << (bst.search(30) ? "Found" : "Not Found") << "\n";
    bst.remove(30);
    std::cout << "Inorder Traversal after deleting 30: ";
    sortedKeys = bst.inorder();
    for (int key : sortedKeys) {
        std::cout << key << " ";
    }
    std::cout << "\n";

    return 0;
}
```

---

## Java Implementation

```java
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class BinarySearchTree {
    
    // Node Class
    static class Node {
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

    // Insert
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

    // Search
    public boolean search(int key) {
        return searchRec(root, key);
    }

    private boolean searchRec(Node root, int key) {
        if (root == null) return false;
        if (root.key == key) return true;
        if (key < root.key) return searchRec(root.left, key);
        return searchRec(root.right, key);
    }

    // Delete
    public void delete(int key) {
        root = deleteRec(root, key);
    }

    private Node deleteRec(Node root, int key) {
        if (root == null) return root;

        if (key < root.key) {
            root.left = deleteRec(root.left, key);
        } else if (key > root.key) {
            root.right = deleteRec(root.right, key);
        } else {
            // Case 1 & 2: 0 or 1 child
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

    // Traversal
    public List<Integer> inorder() {
        List<Integer> res = new ArrayList<>();
        inorderRec(root, res);
        return res;
    }

    private void inorderRec(Node root, List<Integer> res) {
        if (root != null) {
            inorderRec(root.left, res);
            res.add(root.key);
            inorderRec(root.right, res);
        }
    }

    public void printLevelOrder() {
        if (root == null) return;
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            Node tempNode = queue.poll();
            System.out.print(tempNode.key + " ");
            if (tempNode.left != null) queue.add(tempNode.left);
            if (tempNode.right != null) queue.add(tempNode.right);
        }
        System.out.println();
    }

    // Main driver
    public static void main(String[] args) {
        BinarySearchTree bst = new BinarySearchTree();
        bst.insert(50);
        bst.insert(30);
        bst.insert(70);
        bst.insert(20);
        bst.insert(40);

        System.out.print("Inorder Traversal: ");
        System.out.println(bst.inorder());

        System.out.print("Level Order Traversal: ");
        bst.printLevelOrder();

        System.out.println("Search 40: " + bst.search(40));
        bst.delete(30);
        System.out.print("Inorder Traversal after deleting 30: ");
        System.out.println(bst.inorder());
    }
}
```

---

## 3 Solved Examples

### Example 1: Find the Maximum Depth (Height) of a Binary Tree
Given a binary tree, find its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#### Tree Diagram
```
      (3)
     /   \
   (9)   (20)
        /    \
      (15)   (7)
```

#### Step-by-Step Logic
The height of any node is $1$ plus the maximum height of its left and right subtrees:

$$\text{height}(node) = 1 + \max(\text{height}(node.left), \text{height}(node.right))$$

We can use recursion to solve this bottom-up:
1.  **Base Case**: If node is `null`, return height `0`.
2.  **Recursive Step**:
    *   Call `maxDepth(node.left)`.
    *   Call `maxDepth(node.right)`.
    *   Return $1 + \max(\text{left\_depth}, \text{right\_depth})$.

#### Dry Run
*   `maxDepth(3)` calls `maxDepth(9)` and `maxDepth(20)`.
*   `maxDepth(9)` left and right are null $\to$ returns $1 + \max(0, 0) = 1$.
*   `maxDepth(20)` calls `maxDepth(15)` and `maxDepth(7)`.
    *   `maxDepth(15)` returns $1 + \max(0, 0) = 1$.
    *   `maxDepth(7)` returns $1 + \max(0, 0) = 1$.
    *   `maxDepth(20)` returns $1 + \max(1, 1) = 2$.
*   `maxDepth(3)` returns $1 + \max(1, 2) = 3$.

#### Solution Code (Python)
```python
def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```

---

### Example 2: Validate a Binary Search Tree (BST)
Given the root of a binary tree, determine if it is a valid binary search tree.

#### Step-by-Step Logic
A common mistake is verifying only that `left.key < root.key < right.key` at each node locally. This is incorrect. Consider this tree:
```
      (10)
     /    \
   (5)    (15)
         /    \
       (6)    (20)
```
Even though $6 < 15$ and $20 > 15$, $6$ is in the right subtree of $10$, which violates the BST property because $6 < 10$.

To solve this, we must pass the allowable **minimum** and **maximum** ranges downwards dynamically:
*   For root, range is $(-\infty, \infty)$.
*   When moving left, the upper limit changes: range becomes $(\text{min}, \text{node.val})$.
*   When moving right, the lower limit changes: range becomes $(\text{node.val}, \text{max})$.

#### Dry Run on the invalid tree above
1.  `validate(10, -inf, inf)`: Valid.
2.  Go left: `validate(5, -inf, 10)`: Valid.
3.  Go right: `validate(15, 10, inf)`: Valid.
4.  From `15`, go left: `validate(6, 10, 15)`:
    *   Is $10 < 6 < 15$? No. $6$ is not greater than $10$.
    *   Return `False`.

#### Solution Code (Python)
```python
def isValidBST(root):
    def validate(node, low=-float('inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.key < high):
            return False
        return (validate(node.left, low, node.key) and 
                validate(node.right, node.key, high))
    
    return validate(root)
```

---

### Example 3: Lowest Common Ancestor (LCA) in a BST
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes `p` and `q`.

#### Tree Diagram
```
        (6)
       /   \
     (2)   (8)
    /   \
  (0)   (4)
```

Find LCA of `2` and `4`:
*   `2` and `4` are both in the left subtree of `6`.
*   The lowest common node containing both as descendants is `2`.

#### Step-by-Step Logic
Since it is a BST, we can leverage the node ordering to search efficiently:
1.  If both `p` and `q` are smaller than root, the LCA must be in the left subtree. Move to `root.left`.
2.  If both `p` and `q` are larger than root, the LCA must be in the right subtree. Move to `root.right`.
3.  If they split (one is smaller, one is larger, or one equals the root), then the current root is their **LCA**.

#### Dry Run (LCA of `0` and `4` starting at root `6`)
1.  Compare `0` and `4` to `6`: Both are $< 6$. Go left to `2`.
2.  Compare `0` and `4` to `2`: `0 < 2` but `4 > 2`. They split!
3.  Return node `2` as LCA.

#### Solution Code (Python)
```python
def lowestCommonAncestor(root, p, q):
    while root:
        if p.key < root.key and q.key < root.key:
            root = root.left
        elif p.key > root.key and q.key > root.key:
            root = root.right
        else:
            return root
```

---

## 5 Interview Questions with Answers

### Q1. What is the difference between a Binary Tree and a Binary Search Tree?
**Answer:**
*   A **Binary Tree** is a general tree structure where each node can have at most 2 children. There is absolutely no relationship constraint between the values of parent nodes and child nodes.
*   A **Binary Search Tree (BST)** is a specific type of binary tree that enforces strict ordering: for every node, all values in its left subtree must be less than the node's value, and all values in its right subtree must be greater than the node's value. This structural constraint allows search, insertion, and deletion to be performed in $O(\log n)$ average time instead of $O(n)$ linear time.

---

### Q2. How do you find the Inorder Successor of a node in a BST?
**Answer:**
The Inorder Successor of a node is the node that comes immediately after it during an inorder traversal.
*   **Case 1 (Right subtree exists)**: The successor is the minimum node in the right subtree. Go to the right child, and then go left as far as possible.
*   **Case 2 (No right subtree)**: Start from the root and trace downwards. Keep track of the last node where you took a left turn. That node is the inorder successor.

---

### Q3. Prove that the maximum number of nodes in a binary tree of height $h$ is $2^{h+1} - 1$. (Assuming root is at height 0)
**Answer:**
At height (level) $i$, the maximum number of nodes is $2^i$.
A tree of height $h$ has levels from $0$ to $h$. Summing up the nodes at each level:

$$\text{Total Nodes } N = 2^0 + 2^1 + 2^2 + \dots + 2^h$$

This is a geometric progression with first term $a = 1$, common ratio $r = 2$, and number of terms $n = h + 1$. Using the geometric progression sum formula $S = \frac{a(r^n - 1)}{r - 1}$:

$$N = \frac{1(2^{h+1} - 1)}{2 - 1} = 2^{h+1} - 1$$

Thus, the maximum number of nodes is $2^{h+1} - 1$.

---

### Q4. Compare AVL Trees vs Red-Black Trees. When would you prefer one over the other?
**Answer:**
*   **Strictness of Balance**: AVL trees are much more strictly balanced than Red-Black trees. The height difference in AVL is strictly bounded by $\le 1$, whereas Red-Black trees only guarantee that the height is at most $2 \log (n + 1)$.
*   **Search Operations**: Because AVL trees are strictly balanced, they offer faster lookups/searches because their search path is shorter on average.
*   **Insertion and Deletion**: Red-Black trees require fewer rotations/rebalancing modifications during insertions and deletions.
*   **Decision**:
    *   Prefer **AVL Trees** in read-heavy applications (e.g., dictionary lookups, static database indexes).
    *   Prefer **Red-Black Trees** in write-heavy or dynamic applications where insertion and deletion operations are frequent (e.g., implementation of C++ STL containers like `std::map`, Linux kernel process scheduling).

---

### Q5. What is Morris Traversal? How does it achieve $O(1)$ auxiliary space complexity?
**Answer:**
Standard tree traversals (Inorder, Preorder, Postorder) require recursion or an iterative stack, which takes $O(h)$ auxiliary space to keep track of parent nodes.
**Morris Traversal** achieves $O(1)$ auxiliary space by modifying the tree dynamically during traversal using **threaded binary tree concepts**:
1.  At the current node, if a left child exists, locate its **Inorder Predecessor** (the rightmost node in the left subtree).
2.  Set the right pointer of that predecessor to point to the current node (creating a temporary "thread" or link back to the parent).
3.  This temporary thread allows the algorithm to backtrack up the tree without using a recursive stack.
4.  Once the left subtree is fully traversed, remove the temporary thread to restore the original tree structure.

---

## Common Mistakes

1.  **Confusing Height and Depth**: 
    *   *Depth* starts from $0$ at the root and increases downwards.
    *   *Height* starts from $0$ at the leaves and increases upwards.
    *   Many off-by-one errors stem from forgetting whether your implementation uses $0$-based or $1$-based heights. Always clarify this early on.

2.  **Verifying BST Status Locally Only**:
    *   As shown in Example 2, checking `node.left.val < node.val < node.right.val` only at the parent node is not sufficient. 
    *   A valid BST must satisfy this property globally for all descendants. You must propagate range restrictions $(min, max)$ downward.

3.  **Failing to Update Parent References on Deletion**:
    *   When deleting a node, many developers modify the node itself but forget to update its parent's pointer to refer to the new child. This creates orphaned nodes and memory leaks in languages without garbage collection.

4.  **Infinite Recursion Stack Overflow**:
    *   Running recursion on unbalanced, highly skewed trees (where $h = n$) can cause stack overflow exceptions. For very large or unbalanced datasets, always consider implementing dynamic balancing or using iterative traversals with an explicit stack.

---

## Summary

*   A **Tree** is a hierarchical, non-linear data structure with a root and subtrees, representing data through parent-child relationships.
*   **Binary Search Trees (BSTs)** provide extremely efficient searches ($O(\log n)$ average time) by ensuring left descendants are smaller and right descendants are larger than their ancestor nodes.
*   To prevent performance degradation into a linear $O(n)$ search, trees must be kept balanced. **AVL** and **Red-Black Trees** dynamically balance themselves during operations.
*   Trees are highly recursive, and standard operations like **Inorder**, **Preorder**, and **Postorder** traversals are naturally implemented using recursive routines.
*   Selecting the right type of tree (such as Heaps for priority queues, Tries for prefix lookups, or B-Trees for database indexing) is key to writing high-performance, industry-ready software.