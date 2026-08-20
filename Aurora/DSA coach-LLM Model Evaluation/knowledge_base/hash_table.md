# Hash Table

## Definition

A **Hash Table** (also known as a Hash Map) is a data structure that implements an associative array abstract data type, which maps unique **keys** to **values**. 

It uses a mathematical function, called a **Hash Function**, to compute an index (also known as a hash value or hash code) into an array of buckets or slots, from which the desired value can be found.

```
┌─────────┐       ┌───────────────┐       ┌───────────┐       ┌─────────────┐
│  Key    │ ────> │ Hash Function │ ────> │   Index   │ ────> │ Value Slot  │
│ ("John")│       │   h(key)      │       │ (e.g., 4) │       │ ("555-0199")│
└─────────┘       └───────────────┘       └───────────┘       └─────────────┘
```

---

## Why it is needed

Before Hash Tables, retrieving data from structures involved trade-offs:
1. **Arrays**: Accessing elements via an index is extremely fast ($O(1)$), but searching for an element by value or using non-integer keys (like strings) requires sequential search ($O(N)$) or binary search ($O(\log N)$ on sorted data). Insertion and deletion inside arrays are also slow ($O(N)$) due to element shifting.
2. **Linked Lists**: Extremely dynamic and easy to insert/delete at known locations ($O(1)$), but searching requires linear scanning ($O(N)$).
3. **Balanced Binary Search Trees (BSTs)**: Maintain sorted order and provide logarithmic time ($O(\log N)$) for search, insertion, and deletion, which degrades for massive datasets.

**The Hash Table Solution**: By converting arbitrary keys into array indices using a hash function, Hash Tables combine the $O(1)$ random-access speed of arrays with the flexibility of using any data type (strings, custom objects) as keys, achieving **$O(1)$ average-case time complexity** for search, insertion, and deletion.

---

## Characteristics

- **Associative Mapping**: Stores data in Key-Value pairs ($[Key, Value]$).
- **Key Uniqueness**: Keys must be unique. Values, however, can be duplicated.
- **Hashability**: Keys must be immutable and hashable so that their hash code remains constant during their lifespan inside the table.
- **Unordered Storage**: By default, elements are not stored in any sorted order of keys or values.
- **Dynamic Resizing**: As the number of elements increases, the table dynamically grows (rehashes) to maintain its efficiency.

---

## Working

The core working of a Hash Table relies on three main components: **Hash Function**, **Collision Resolution**, and **Resizing**.

### 1. The Hash Function
A hash function takes a key of arbitrary size and maps it to a fixed-size integer value (hash code). This integer is then compressed to fit the size of the underlying array using the modulo operator:

$$\text{Index} = \text{Hash}(Key) \pmod{\text{Table Size}}$$

#### Properties of a Good Hash Function:
- **Deterministic**: For a given key, it must always return the exact same index.
- **Uniformly Distributed**: It should distribute keys uniformly across the array to minimize collisions.
- **Fast Computation**: The computation must be $O(1)$ time complexity.

### 2. Collision Resolution
Since the output space (array size) is smaller than the input space (infinite possible keys), two distinct keys can map to the exact same array index. This event is called a **Collision**.

$$Key_1 \neq Key_2 \quad \text{but} \quad \text{Hash}(Key_1) \pmod M = \text{Hash}(Key_2) \pmod M$$

To handle collisions, Hash Tables use specific collision resolution strategies (detailed in the *Types* section below).

### 3. Load Factor ($\alpha$) and Rehashing
The **Load Factor** ($\alpha$) measures how full the hash table is:

$$\alpha = \frac{N}{M}$$

Where:
- $N = \text{Number of elements stored}$
- $M = \text{Size of the bucket array (capacity)}$

When $\alpha$ exceeds a pre-defined threshold (typically $0.75$), the table is prone to high collisions. The hash table performs **Rehashing**:
1. It allocates a new underlying array, typically **double** the size of the original array ($2M$).
2. It re-maps (rehashes) all existing keys to the new array using the new capacity in the modulo math.

---

## Memory Representation

The memory representation depends on the collision resolution strategy. Below is the memory layout of a **Separate Chaining** Hash Table of capacity 8:

```
Bucket Array (Contiguous Memory Pointer Array)
┌───┬──────────────────────────────────────────┐
│ 0 │ Pointer ──> [ Key: "Bob", Val: 12 ] ──> NULL
├───┼──────────────────────────────────────────┐
│ 1 │ NULL
├───┼──────────────────────────────────────────┐
│ 2 │ Pointer ──> [ Key: "Ada", Val: 42 ] ──> [ Key: "Leo", Val: 99 ] ──> NULL  <-- (Collision)
├───┼──────────────────────────────────────────┐
│ 3 │ NULL
├───┼──────────────────────────────────────────┐
│ 4 │ Pointer ──> [ Key: "Zoe", Val: 71 ] ──> NULL
├───┼──────────────────────────────────────────┐
│ 5 │ NULL
├───┼──────────────────────────────────────────┐
│ 6 │ NULL
├───┼──────────────────────────────────────────┐
│ 7 │ Pointer ──> [ Key: "Ted", Val: 55 ] ──> NULL
└───┴──────────────────────────────────────────┘
```

---

## Types of Collision Resolution Techniques

Collision resolution techniques are broadly categorized into two families:

```
                       Collision Resolution
                               │
         ┌─────────────────────┴─────────────────────┐
         ▼                                           ▼
  Open Hashing (Separate Chaining)            Closed Hashing (Open Addressing)
                                                     │
                                   ┌─────────────────┼─────────────────┐
                                   ▼                 ▼                 ▼
                            Linear Probing   Quadratic Probing   Double Hashing
```

### 1. Open Hashing (Separate Chaining)
Each slot of the bucket array points to a dynamic data structure (usually a Singly Linked List, Doubly Linked List, or a Balanced BST like a Red-Black Tree).

- **How it works**: If a collision occurs at index $i$, the new key-value pair is appended to the list at index $i$.
- **Pros**: Simple to implement; never overflows (size can grow beyond capacity $M$); deletions are straightforward.
- **Cons**: High cache performance degradation (pointers jump around memory); memory waste due to pointer overhead.

### 2. Closed Hashing (Open Addressing)
All elements are stored within the bucket array itself. No external structures are used. If a collision occurs, the system searches (probes) for another vacant slot.

#### A. Linear Probing
The algorithm probes subsequent slots sequentially with a constant interval of 1:

$$h(k, i) = (h'(k) + i) \pmod M$$

Where $i = 0, 1, 2, \dots$ is the probe sequence index, and $h'(k)$ is the original hash index.
- **Problem**: **Primary Clustering** — long consecutive blocks of occupied slots build up, drastically slowing down searches.

#### B. Quadratic Probing
The algorithm probes slots using a quadratic function:

$$h(k, i) = (h'(k) + c_1 \cdot i + c_2 \cdot i^2) \pmod M$$

Where $c_1$ and $c_2$ are constants.
- **Problem**: **Secondary Clustering** — keys hashing to the exact same initial index probe the exact same sequence of alternative slots.

#### C. Double Hashing
The algorithm uses a second hash function $h_2(k)$ to calculate the step size of the probe:

$$h(k, i) = (h_1(k) + i \cdot h_2(k)) \pmod M$$

- **Constraint**: $h_2(k)$ must never evaluate to $0$, and $h_2(k)$ must be coprime to $M$.
- **Pros**: Virtually eliminates clustering. Excellent distribution.

---

## Operations

### 1. Insertion (`insert(key, value)`)
1. Compute the hash index using the Hash Function: $idx = \text{hash}(key) \pmod M$.
2. Go to the bucket at $idx$.
3. Check if the key already exists in the bucket.
   - **If yes**: Update its value (overwriting).
   - **If no**: Insert the new key-value pair.
4. Increment the item count. If the load factor exceeds the threshold, trigger **Rehash**.

*Example*: Insert `("John", 25)` into a table of size 5, where `hash("John") = 12`.
- $idx = 12 \pmod 5 = 2$.
- Bucket 2 is empty. Create a node `[ "John", 25 ]` and place it at index 2.

### 2. Search (`search(key)`)
1. Compute the hash index: $idx = \text{hash}(key) \pmod M$.
2. Access the bucket at $idx$.
3. Scan the chain/probe sequence until the target key is found or an empty slot/end-of-chain is reached.
4. Return the associated value if found, or a "not found" status (e.g., `None`, `-1`, or throw an exception).

*Example*: Search for `"John"` in the table above.
- $idx = 12 \pmod 5 = 2$.
- Scan bucket 2. The first node matches key `"John"`. Return `25`.

### 3. Deletion (`delete(key)`)
1. Compute the hash index: $idx = \text{hash}(key) \pmod M$.
2. Search for the key in the bucket at $idx$.
3. **If Separate Chaining**: Adjust pointers of the linked list to unlink the node. Free its memory.
4. **If Open Addressing**: Instead of leaving the slot physically empty, mark it with a special placeholder flag called a **Tombstone** (or "Deleted" state). 
   *(Note: This is vital! Leaving it empty would break the probe chain for other keys that collided and mapped past this slot during insertion.)*

*Example*: Delete `"John"`.
- Find `"John"` at index 2.
- Remove node from chain at index 2. Index 2 becomes empty (`NULL`).

---

## Time Complexity Table

| Operation | Average Case | Worst Case (Extreme Collisions / Poor Hash) |
| :--- | :--- | :--- |
| **Search** | $O(1)$ | $O(N)$ (if all elements hash to the same bucket) / $O(\log N)$ (if BST chaining) |
| **Insertion** | $O(1)$ | $O(N)$ (due to rehashing or traversal of long collision chains) |
| **Deletion** | $O(1)$ | $O(N)$ (due to locating element in a highly-congested bucket) |

---

## Space Complexity

- **Auxiliary Space Complexity**: $O(N + M)$
  Where $N$ is the number of elements inserted, and $M$ is the capacity of the bucket array.
- In practice, since $M \propto N$ (due to a bounded load factor $0.75$), the space complexity is simplified to **$O(N)$**.

---

## Advantages

- **Ultra-fast Retrieval**: Provides $O(1)$ average-case performance for dictionary operations.
- **Flexible Keys**: Allows any immutable type to act as an indexing key, avoiding the integer-only restrictions of array indices.
- **Memory Efficiency**: Only consumes memory proportional to the number of stored keys (if chaining uses dynamic allocations).

---

## Disadvantages

- **Worst-case Degradation**: Poor hash function design or malicious adversarial attacks can cause all keys to collision-collapse into a single bucket, degrading operations to $O(N)$.
- **High Memory Overhead**: Open addressing requires a low load factor (e.g., $< 0.7$), leaving a portion of memory intentionally unused. Chaining requires memory for extra pointer overhead.
- **Unordered Data**: Does not support ordered operations. Finding the minimum, maximum, or items in a sorted range takes $O(N \log N)$ or $O(N)$ scanning.
- **Inefficient Range Queries**: Unlike trees (e.g., B-Trees or Red-Black Trees), searching for values within a range (e.g., $10 < x < 50$) requires checking every single slot in the table.

---

## Real-World Applications

- **Database Indexes**: Hash indexes are used in databases (such as PostgreSQL or MySQL) for ultra-fast equality searches (`WHERE column = value`).
- **Caching Systems**: Redis, Memcached, and local application caches (like LRU Cache) rely on underlying hash maps for instantaneous key-lookup.
- **Compilers and Interpreters**: **Symbol Tables** map variables and function names to their memory addresses or metadata.
- **Cryptography & File Integrity**: MD5, SHA-256 checks use hash systems to match keys with unique file hashes.
- **Domain Name Servers (DNS)**: Resolves human-readable domain names (e.g., `example.com`) to IP addresses.

---

## Python Implementation

This implementation models an explicit **Separate Chaining Hash Map** from scratch, avoiding Python's built-in `dict`.

```python
class Node:
    """A Node representing a single Key-Value pair in a Singly Linked List chain."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapFromScratch:
    """Custom Hash Map implementation using Separate Chaining."""
    def __init__(self, capacity: int = 8):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity
        self.load_factor_threshold = 0.75

    def _hash(self, key) -> int:
        """Internal helper to compute bucket index for a key."""
        # hash() returns an integer; modulo maps it to bucket range
        return abs(hash(key)) % self.capacity

    def put(self, key, value) -> None:
        """Insert or update a key-value pair."""
        # Check load factor threshold before inserting
        if (self.size / self.capacity) >= self.load_factor_threshold:
            self._resize()

        idx = self._hash(key)
        
        # If bucket is empty, insert first node
        if self.buckets[idx] is None:
            self.buckets[idx] = Node(key, value)
            self.size += 1
            return

        # Handle collision via Separate Chaining list traversal
        current = self.buckets[idx]
        while True:
            if current.key == key:
                current.value = value  # Update existing key
                return
            if current.next is None:
                break
            current = current.next

        # Append new node to end of chain
        current.next = Node(key, value)
        self.size += 1

    def get(self, key):
        """Retrieve value associated with the key. Returns None if not found."""
        idx = self._hash(key)
        current = self.buckets[idx]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key) -> bool:
        """Remove a key-value pair. Returns True if removed, else False."""
        idx = self._hash(key)
        current = self.buckets[idx]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.buckets[idx] = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
        return False

    def _resize(self) -> None:
        """Double the capacity and rehash all elements."""
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        self.size = 0  # Reset size; put() will re-increment it

        for head in old_buckets:
            current = head
            while current:
                self.put(current.key, current.value)
                current = current.next

    def __str__(self):
        """String representation of the Hash Map."""
        result = []
        for i in range(self.capacity):
            chain = []
            curr = self.buckets[i]
            while curr:
                chain.append(f"[{curr.key}: {curr.value}]")
                curr = curr.next
            result.append(f"Bucket {i}: {' -> '.join(chain) if chain else 'Empty'}")
        return "\n".join(result)


# --- Driver Code ---
if __name__ == "__main__":
    h_map = HashMapFromScratch(4)  # Small capacity to trigger rehashing quickly
    h_map.put("Apple", 100)
    h_map.put("Banana", 200)
    h_map.put("Cherry", 300)
    h_map.put("Date", 400)  # Should trigger resize (size 4 / capacity 4 >= 0.75)

    print("--- Hash Map State ---")
    print(h_map)
    
    print("\nGet 'Banana':", h_map.get("Banana"))
    print("Get 'Grape' (Not Existing):", h_map.get("Grape"))
    
    print("\nRemoving 'Banana'...")
    h_map.remove("Banana")
    print("Get 'Banana' after deletion:", h_map.get("Banana"))
```

---

## C++ Implementation

This implementation uses dynamic allocation and builds a custom Separate Chaining HashTable template.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <cmath>

template <typename K, typename V>
class HashNode {
public:
    K key;
    V value;
    HashNode* next;

    HashNode(K key, V value) : key(key), value(value), next(nullptr) {}
};

template <typename K, typename V>
class HashTable {
private:
    std::vector<HashNode<K, V>*> buckets;
    int capacity;
    int size;
    double loadFactorThreshold;

    int getBucketIndex(const K& key) {
        // Built-in STL hashing function wrapper
        std::hash<K> hashFn;
        return hashFn(key) % capacity;
    }

    void rehash() {
        int oldCapacity = capacity;
        std::vector<HashNode<K, V>*> oldBuckets = buckets;

        capacity *= 2;
        buckets = std::vector<HashNode<K, V>*>(capacity, nullptr);
        size = 0;

        for (int i = 0; i < oldCapacity; ++i) {
            HashNode<K, V>* curr = oldBuckets[i];
            while (curr != nullptr) {
                insert(curr->key, curr->value);
                HashNode<K, V>* temp = curr;
                curr = curr->next;
                delete temp; // Clean up old nodes to prevent memory leaks
            }
        }
    }

public:
    HashTable(int capacity = 8) : capacity(capacity), size(0), loadFactorThreshold(0.75) {
        buckets.resize(capacity, nullptr);
    }

    ~HashTable() {
        // Clean up all dynamically allocated memory
        for (int i = 0; i < capacity; ++i) {
            HashNode<K, V>* curr = buckets[i];
            while (curr != nullptr) {
                HashNode<K, V>* temp = curr;
                curr = curr->next;
                delete temp;
            }
        }
    }

    void insert(const K& key, const V& value) {
        if ((double)size / capacity >= loadFactorThreshold) {
            rehash();
        }

        int idx = getBucketIndex(key);
        HashNode<K, V>* curr = buckets[idx];

        // Traverse to see if key exists
        while (curr != nullptr) {
            if (curr->key == key) {
                curr->value = value; // Update value
                return;
            }
            curr = curr->next;
        }

        // Key doesn't exist, insert at head of list (O(1) insertion)
        HashNode<K, V>* newNode = new HashNode<K, V>(key, value);
        newNode->next = buckets[idx];
        buckets[idx] = newNode;
        size++;
    }

    bool search(const K& key, V& valueOut) {
        int idx = getBucketIndex(key);
        HashNode<K, V>* curr = buckets[idx];

        while (curr != nullptr) {
            if (curr->key == key) {
                valueOut = curr->value;
                return true;
            }
            curr = curr->next;
        }
        return false;
    }

    bool remove(const K& key) {
        int idx = getBucketIndex(key);
        HashNode<K, V>* curr = buckets[idx];
        HashNode<K, V>* prev = nullptr;

        while (curr != nullptr) {
            if (curr->key == key) {
                if (prev == nullptr) {
                    buckets[idx] = curr->next;
                } else {
                    prev->next = curr->next;
                }
                delete curr;
                size--;
                return true;
            }
            prev = curr;
            curr = curr->next;
        }
        return false;
    }

    void display() {
        for (int i = 0; i < capacity; ++i) {
            std::cout << "Bucket " << i << ": ";
            HashNode<K, V>* curr = buckets[i];
            while (curr != nullptr) {
                std::cout << "[" << curr->key << ": " << curr->value << "] -> ";
                curr = curr->next;
            }
            std::cout << "NULL\n";
        }
    }
};

int main() {
    HashTable<std::string, int> phonebook;
    phonebook.insert("Alice", 12345);
    phonebook.insert("Bob", 67890);
    phonebook.insert("Charlie", 11223);
    phonebook.insert("Bob", 99999); // Update test

    std::cout << "--- Initial Table ---\n";
    phonebook.display();

    int val;
    if (phonebook.search("Bob", val)) {
        std::cout << "\nFound Bob. Value: " << val << "\n";
    }

    std::cout << "\nDeleting Alice...\n";
    phonebook.remove("Alice");
    phonebook.display();

    return 0;
}
```

---

## Java Implementation

This is a clean implementation of a Hash Map in Java, matching the generic specification of `java.util.Map` interfaces.

```java
import java.util.ArrayList;

public class MyHashMap<K, V> {
    private static class HashNode<K, V> {
        K key;
        V value;
        HashNode<K, V> next;

        public HashNode(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }

    private ArrayList<HashNode<K, V>> buckets;
    private int capacity;
    private int size;
    private final double loadFactorThreshold = 0.75;

    public MyHashMap() {
        this.capacity = 8;
        this.size = 0;
        this.buckets = new ArrayList<>(capacity);
        for (int i = 0; i < capacity; i++) {
            buckets.add(null);
        }
    }

    private int getBucketIndex(K key) {
        int hashCode = (key == null) ? 0 : Math.abs(key.hashCode());
        return hashCode % capacity;
    }

    public void put(K key, V value) {
        if ((double) size / capacity >= loadFactorThreshold) {
            rehash();
        }

        int idx = getBucketIndex(key);
        HashNode<K, V> head = buckets.get(idx);
        HashNode<K, V> curr = head;

        // Check if key already exists
        while (curr != null) {
            if ((curr.key == null && key == null) || (curr.key != null && curr.key.equals(key))) {
                curr.value = value; // Update
                return;
            }
            curr = curr.next;
        }

        // Insert at head of the bucket list
        HashNode<K, V> newNode = new HashNode<>(key, value);
        newNode.next = head;
        buckets.set(idx, newNode);
        size++;
    }

    public V get(K key) {
        int idx = getBucketIndex(key);
        HashNode<K, V> curr = buckets.get(idx);

        while (curr != null) {
            if ((curr.key == null && key == null) || (curr.key != null && curr.key.equals(key))) {
                return curr.value;
            }
            curr = curr.next;
        }
        return null;
    }

    public V remove(K key) {
        int idx = getBucketIndex(key);
        HashNode<K, V> curr = buckets.get(idx);
        HashNode<K, V> prev = null;

        while (curr != null) {
            if ((curr.key == null && key == null) || (curr.key != null && curr.key.equals(key))) {
                if (prev == null) {
                    buckets.set(idx, curr.next);
                } else {
                    prev.next = curr.next;
                }
                size--;
                return curr.value;
            }
            prev = curr;
            curr = curr.next;
        }
        return null; // Key was not found
    }

    private void rehash() {
        ArrayList<HashNode<K, V>> oldBuckets = buckets;
        capacity *= 2;
        buckets = new ArrayList<>(capacity);
        size = 0;

        for (int i = 0; i < capacity; i++) {
            buckets.add(null);
        }

        for (HashNode<K, V> head : oldBuckets) {
            HashNode<K, V> curr = head;
            while (curr != null) {
                put(curr.key, curr.value);
                curr = curr.next;
            }
        }
    }

    public void display() {
        for (int i = 0; i < capacity; i++) {
            System.out.print("Bucket " + i + ": ");
            HashNode<K, V> curr = buckets.get(i);
            while (curr != null) {
                System.out.print("[" + curr.key + ": " + curr.value + "] -> ");
                curr = curr.next;
            }
            System.out.println("null");
        }
    }

    public static void main(String[] args) {
        MyHashMap<Integer, String> map = new MyHashMap<>();
        map.put(1, "Value One");
        map.put(2, "Value Two");
        map.put(9, "Value Nine"); // Collides with 1 if capacity is 8 (9 % 8 = 1)
        
        System.out.println("--- Map Output ---");
        map.display();

        System.out.println("\nGet 9: " + map.get(9));
        System.out.println("Remove 1: " + map.remove(1));
        map.display();
    }
}
```

---

## 3 Solved Examples

### Example 1: Two Sum
**Problem Statement**: Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.

- **Input**: `nums = [2, 7, 11, 15]`, `target = 9`
- **Output**: `[0, 1]` (Since `nums[0] + nums[1] == 9`)

#### Step-by-Step Solution:
We can solve this in $O(1)$ lookup time using a Hash Map to store elements we've seen so far and their indices.
1. Initialize an empty hash map `seen = {}`.
2. Loop through the array with elements $nums[i]$ and their index $i$.
3. Compute the complement needed to reach the target: `complement = target - nums[i]`.
4. Check if `complement` exists in the `seen` hash map:
   - **If yes**: We have found our pair! Return `[seen[complement], i]`.
   - **If no**: Store the current value and index in the hash map: `seen[nums[i]] = i`.

*Execution tracing with `nums = [2, 7, 11, 15]`, `target = 9`:*
- **i = 0**: $nums[0] = 2$. $\text{complement} = 9 - 2 = 7$. $7$ is not in `seen`. Add `2` to `seen`: `{2: 0}`.
- **i = 1**: $nums[1] = 7$. $\text{complement} = 9 - 7 = 2$. $2$ *is* in `seen`! 
- Return `[seen[2], 1]` which evaluates to `[0, 1]`.

#### Complexity:
- **Time Complexity**: $O(N)$ because we traverse the list of size $N$ only once, and hash map lookups take $O(1)$ time.
- **Space Complexity**: $O(N)$ for storing up to $N$ elements in the hash map.

---

### Example 2: Group Anagrams
**Problem Statement**: Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

- **Input**: `strs = ["eat","tea","tan","ate","nat","bat"]`
- **Output**: `[["bat"],["nat","tan"],["ate","eat","tea"]]`

#### Step-by-Step Solution:
Anagrams contain identical counts of each letter. If we sort any word that is an anagram of another, they will yield the exact same sorted string. We can use this sorted string as a unique Key in a Hash Map.
1. Initialize a hash map `anagram_map` where the key is a string and the value is a list of strings.
2. Iterate through each string `s` in `strs`:
   - Sort the characters of `s` to create a standard key: `key = "".join(sorted(s))`.
   - Append `s` to the array located at `anagram_map[key]`.
3. Return the compiled values of `anagram_map`.

*Execution tracing with `["eat", "tea", "tan"]`:*
- `s = "eat"`: sorted key is `"aet"`. Add to map: `{"aet": ["eat"]}`
- `s = "tea"`: sorted key is `"aet"`. Add to map: `{"aet": ["eat", "tea"]}`
- `s = "tan"`: sorted key is `"ant"`. Add to map: `{"aet": ["eat", "tea"], "ant": ["tan"]}`
- Collect lists to return: `[["eat", "tea"], ["tan"]]`.

#### Complexity:
- **Time Complexity**: $O(N \cdot K \log K)$ where $N$ is the number of strings and $K$ is the maximum length of a string in `strs` (sorting each string takes $O(K \log K)$ time).
- **Space Complexity**: $O(N \cdot K)$ to store all input strings in the hash map.

---

### Example 3: Longest Consecutive Sequence
**Problem Statement**: Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. The algorithm must run in $O(N)$ time.

- **Input**: `nums = [100, 4, 200, 1, 3, 2]`
- **Output**: `4` (The consecutive sequence is `[1, 2, 3, 4]`)

#### Step-by-Step Solution:
We must avoid sorting, as sorting takes $O(N \log N)$. Instead, we use a **Hash Set** (implemented via a hash table) for $O(1)$ lookups.
1. Convert the array into a hash set `num_set` to eliminate duplicates and enable $O(1)$ lookups.
2. Initialize `longest_streak = 0`.
3. Iterate through every number `num` in the set:
   - Identify if `num` is the **start** of a sequence. It is the start only if `num - 1` is *not* present in the set.
   - If it is the start, increment and count the sequence:
     - Check for `num + 1`, `num + 2`, etc., in the set using a loop.
     - Update `longest_streak = max(longest_streak, current_streak)`.
4. Return `longest_streak`.

*Execution tracing with `[100, 4, 200, 1, 3, 2]`:*
- `num_set = {1, 2, 3, 4, 100, 200}`
- `num = 100`: Is `99` in `num_set`? No. This is a sequence starter. Count consecutive: `100` exists. `101` does not. Streak length = 1.
- `num = 4`: Is `3` in `num_set`? Yes. Skip (it's part of another sequence already).
- `num = 200`: Is `199` in `num_set`? No. Sequence starter. Count consecutive: `200` exists. Streak length = 1.
- `num = 1`: Is `0` in `num_set`? No. Sequence starter. Count consecutive: `1`, `2`, `3`, `4` exist. Streak length = 4.
- Maximum streak recorded is `4`.

#### Complexity:
- **Time Complexity**: $O(N)$ because the inner while loop only executes for the start of a sequence. Each element is visited at most twice (once in the outer loop, and once in the inner sequence verification loop).
- **Space Complexity**: $O(N)$ to store the array elements in a hash set.

---

## 5 Interview Questions with Answers

### Q1: Explain the difference between Separate Chaining and Open Addressing.
| Criteria | Separate Chaining (Open Hashing) | Open Addressing (Closed Hashing) |
| :--- | :--- | :--- |
| **Storage** | Elements are stored in dynamic chains outside the bucket array. | All elements are stored inside the bucket array itself. |
| **Pointer Overhead** | High pointer overhead due to Linked List nodes. | Low. No pointers are required. |
| **Sizing** | Table can store more items than its array capacity. | Table capacity must always be larger than the number of items. |
| **Cache Performance** | Poor, as elements are dynamically scattered in memory. | Excellent, as sequential buckets utilize system cache lines. |
| **Deletion** | Simple unlinking of a node. | Complicated; requires writing "Tombstone" values. |

### Q2: What is the significance of the Load Factor, and how does rehashing work?
The **Load Factor** ($\alpha$) is the ratio of elements stored to total capacity ($\alpha = N/M$). It serves as a threshold indicating when the hash table is getting too congested. 

When the load factor exceeds a limit (commonly $0.75$), collisions spike, degrading operations from $O(1)$ toward $O(N)$. To prevent this, **Rehashing** is triggered:
1. A new array of double the previous size ($2M$) is created.
2. Every existing key in the table is processed again. Its new index is calculated using the updated size: `new_index = hash(key) % (2M)`.
3. The elements are inserted into the new array, and the old memory is freed.

### Q3: What happens if two different keys have the same hash code? How is retrieval handled?
When two keys have identical hash codes, a **Collision** occurs. How retrieval is handled depends on the implementation:
- **In Separate Chaining**: The table finds the bucket index and traverses the linked list at that index. It checks each node key using equality operations (e.g., `.equals()` in Java) until it finds a match.
- **In Open Addressing**: The table checks the calculated bucket index. If the key does not match, it executes its **Probing Sequence** (Linear, Quadratic, or Double Hash) to search the contiguous slots until it finds the matching key, or hits an empty slot (indicating the key is not in the table).

### Q4: Why are prime numbers preferred for hash table sizes?
Using a prime number for the capacity $M$ of a hash table minimizes collisions when the hash function is not perfectly uniform. 

Many key patterns in real-world data have a common factor (e.g., step-wise numbers like $10, 20, 30$). If the table size $M$ is a composite number (like $10$, which shares factors with the keys), keys will map to the same subsets of indices, causing **clustering**. 

A prime number has no factors other than $1$ and itself. This ensures that the modulo arithmetic distributes keys uniformly across all available indices, even when the key data contains patterns.

### Q5: How would you design a Hash Map that supports `getRandomElement()` in $O(1)$ time?
A standard Hash Map cannot retrieve a random element in $O(1)$ because elements are stored sparsely and non-contiguously in memory, making it impossible to choose a random index from $0$ to $N-1$ and retrieve it directly.

To achieve $O(1)$ for `getRandomElement()`, we must combine two data structures:
1. **Dynamic Array (ArrayList/Vector)**: To store the actual values (or key-value pairs) sequentially.
2. **Hash Map**: To map each Key to its current index in the dynamic array.

#### Implementation Logic:
- **Insert**: Append the value to the end of the array, and add the key and its index to the hash map.
- **Delete**: 
  1. To avoid $O(N)$ array shifting, locate the target element's index in the hash map.
  2. Swap the target element in the array with the **very last** element in the array.
  3. Update the hash map with the new index of the swapped element.
  4. Pop the last element from the array in $O(1)$ time and delete the key from the map.
- **getRandomElement()**: Generate a random integer from $0$ to $N-1$ and return the element at that index in the array in $O(1)$ time.

---

## Common Mistakes

1. **Modifying Keys After Insertion**
   If a key object is mutable (e.g., a list or a custom object) and its properties change after insertion, its **hash code changes**. If you try to lookup or delete that key, the table calculates a different index, failing to locate it. The element becomes a "memory leak" trapped inside the table.
2. **Ignoring the Return of Deletion in Open Addressing**
   Using direct array deletions in open-addressed maps (leaving an array slot physically empty/null) breaks the probing chain. Consecutive search processes will stop prematurely when encountering this empty space, hiding elements that were placed further down the probing queue. **Always use Tombstones** to preserve the chain path.
3. **Choosing a Bad Hash Function**
   Creating a hash function that returns a constant (e.g., `return 1;`) is syntactically valid but collapses the table performance to a $O(N)$ linked list. Ensure keys are hashed with high-entropy distributors.
4. **Confusing TreeMap / std::map with HashMap / std::unordered_map**
   Standard Maps in C++ (`std::map`) and Java (`TreeMap`) are implemented using Self-Balancing Binary Search Trees (Red-Black Trees). They provide logarithmic $O(\log N)$ behavior and maintain keys in sorted order. Hash Maps provide average $O(1)$ behavior but do not maintain any order.

---

## Summary

- A **Hash Table** maps unique keys to values using a mathematical hash function, resolving key-lookups in **$O(1)$ average time complexity**.
- **Collisions** are unavoidable and are resolved using either **Separate Chaining** (linked lists at each bucket) or **Open Addressing** (finding other open slots via linear/quadratic probing or double hashing).
- To preserve $O(1)$ speeds, a table must maintain a low **Load Factor** ($\alpha \le 0.75$) by dynamically allocating a larger array and **Rehashing** all keys once the threshold is crossed.
- While incredibly fast, Hash Tables lack **order** and **range queries**, making them ideal for exact-match associative lookups but unsuitable for ordered data processing.