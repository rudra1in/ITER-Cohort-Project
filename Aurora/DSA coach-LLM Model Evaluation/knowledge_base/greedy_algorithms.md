# Greedy Algorithms

## Definition

A **Greedy Algorithm** is an algorithmic paradigm that builds up a solution piece by piece, always making the choice that offers the most obvious and immediate benefit at that specific moment. This strategy is known as a **locally optimal choice**. The underlying hope of this heuristic is that by consistently making locally optimal choices, the algorithm will eventually arrive at a **globally optimal solution**.

Mathematically, a greedy algorithm solves an optimization problem by making a sequence of decisions. For a problem to be solvable optimally using a greedy approach, it must satisfy two key properties:

1. **Greedy Choice Property:** A global optimal solution can be reached by making a locally optimal (greedy) choice at each step, without ever having to reconsider previous choices.
2. **Optimal Substructure:** An optimal solution to the problem contains within it optimal solutions to its subproblems.

---

## Why it is needed

In computer science, solving optimization problems (finding the maximum or minimum value of a function under constraints) can be computationally expensive. Dynamic Programming (DP) or Backtracking can guarantee global optimality, but they often require exponential ($O(2^n)$) or high-degree polynomial time.

Greedy algorithms are needed for the following reasons:

* **Computational Efficiency:** Greedy algorithms generally run in $O(n \log n)$ or $O(n)$ time, making them significantly faster than Dynamic Programming or Branch and Bound solutions.
* **Heuristic for NP-Hard Problems:** For NP-complete or NP-hard optimization problems (e.g., the Travelling Salesperson Problem), finding the exact global optimum is computationally intractable for large inputs. Greedy algorithms serve as excellent heuristics to find a near-optimal solution in polynomial time.
* **Simplicity in Design:** They are straightforward to conceptualize, design, and implement compared to state-transition-based DP algorithms.

---

## Characteristics

To identify whether a problem can be modeled or analyzed using a greedy approach, look for these defining characteristics:

* **Irreversibility:** Once a decision/choice is made, it is locked in. The algorithm never backtracks or changes a past decision.
* **No State Dependencies on Future Choices:** The choice made at the current step does not depend on any future choices or solutions to subsequent subproblems.
* **Sorting or Prioritization:** The input data is almost always sorted or partitioned based on a specific key metric (e.g., ratio of value-to-weight, earliest finish time, shortest distance) before processing begins.
* **Feasibility:** The choice must satisfy the problem's constraints.
* **Optimality:** The choice must be the best candidate among all feasible options at the current step.

---

## Working

The systematic process of a greedy algorithm can be generalized into the following structural loop:

```
                  +-----------------------+
                  |  Initialize Empty     |
                  |  Solution Set (S)     |
                  +-----------+-----------+
                              |
                              v
                  +-----------------------+
                  | Sort / Structure the  | <--- Usually via sorting or Heap
                  | Raw Input Candidates  |
                  +-----------+-----------+
                              |
                              v
+-------------> +-----------------------+
|               | Select next candidate |
|               | 'x' using Greedy rule |
|               +-----------+-----------+
|                           |
|                           v
|               +-----------------------+
|               |   Is 'x' feasible?    |
|               +-----------+-----------+
|                           |
|                 Yes       +----------------+ No (Discard 'x')
|               +-----------+                |
|               v                            v
|         +-----+---------------+      +-----+---------------+
|         | Union 'x' into      |      | Ignore 'x' and move |
|         | Solution Set (S)    |      | to next candidate   |
|         +-----------+---------+      +-----+---------------+
|                     |                      |
+---------------------+                      |
                      |                      |
                      v                      v
            +----------------------------------+
            | Are all elements processed?      |
            | OR Constraints fully saturated?  |
            +----------------+-----------------+
                             | Yes
                             v
                  +-----------------------+
                  | Return Solution Set S |
                  +-----------------------+
```

### Mathematical Formulation
Let $C$ be the candidate set, $S$ be the selected solution set (initially empty), and $f(x)$ be the objective function we want to optimize.
1. **Selection:** Choose $x \in C$ that maximizes or minimizes $f(x)$ at step $i$.
2. **Feasibility Check:** Verify if $S \cup \{x\}$ satisfies the problem constraints. If yes, $S \leftarrow S \cup \{x\}$.
3. **Reduction:** $C \leftarrow C \setminus \{x\}$.
4. **Termination:** Repeat steps 1–3 until $C$ is empty or the capacity limits of $S$ are fully saturated.

---

## Memory Representation

Greedy algorithms themselves do not require unique complex memory layouts; instead, they leverage existing foundational data structures to implement their choice mechanics efficiently.

```
+-----------------------------------------------------------------+
|                         Memory Layout                           |
+-----------------------------------------------------------------+
|  1. INPUT ARRAY / COLLECTION                                    |
|     [ Item 1 ] [ Item 2 ] [ Item 3 ] ... [ Item N ]             |
|                                                                 |
|  2. SORTED VIEW (Often managed via pointers or new allocations) |
|     [ Optimal ] ---> [ Suboptimal ] ---> [ Least Optimal ]      |
|                                                                 |
|  3. AUXILIARY PRIORITY QUEUE (Min/Max Heap)                     |
|            ( Root: Greedy Choice )                              |
|                    /     \                                      |
|                (Child)  (Child)                                 |
|                                                                 |
|  4. SELECTED SOLUTION STATE SET                                 |
|     [ Solution Step 1 ] [ Solution Step 2 ] ...                 |
+-----------------------------------------------------------------+
```

### Data Structures Employed:
* **Arrays / Vectors:** Used when the candidate set is static and sorted once at the beginning of the execution.
* **Priority Queues (Heaps):** Used when the candidate set is dynamic (elements are added or priority updates occur during execution, e.g., Dijkstra's or Prim's algorithms).
* **Disjoint Set Union (DSU):** Used specifically in graph-based greedy algorithms like Kruskal's to track connectivity and detect cycles in $O(\alpha(V))$ amortized time.

---

## Types of Greedy Problems

Greedy approaches are commonly categorized based on their application domain and constraint types:

### 1. Pure Greedy Algorithms
The local choices are guaranteed to lead to the exact global optimal solution.
* *Examples:* Kruskal’s Minimum Spanning Tree, Prim's Minimum Spanning Tree, Huffman Coding, Dijkstra’s Single-Source Shortest Path.

### 2. Orthogonal / Approximation Greedy Algorithms
Used for NP-Hard optimization problems. The greedy choice does not yield the exact global optimum but guarantees a solution within a bounded factor of the optimal choice.
* *Examples:* Greedy Vertex Cover, Greedy Set Cover, Knapsack (0/1 approximation).

### 3. Matroid-based Greedy Algorithms
Problems that can be structurally modeled as a *Matroid* (a combinatorial structure that generalizes the notion of linear independence in vector spaces). If a problem exhibits Matroid properties, a greedy algorithm is mathematically proven to always find the optimal solution.

---

## Operations

To write any greedy algorithm, you must perform these structural operations:

### 1. Preprocessing / Sorting
The candidates must be sorted based on a calculated weight, ratio, or cost factor.
* **Example:** In the Fractional Knapsack problem, you calculate the density value-to-weight ratio: $r_i = \frac{v_i}{w_i}$. The array of items is sorted in descending order of $r_i$.

### 2. Selection (Extract Minimum / Maximum)
Retrieving the best-ranking candidate from the structured memory.
* **Example:** Using `std::priority_queue` in C++ or `heapq` in Python to fetch the shortest edge in Dijkstra's algorithm.

### 3. Feasibility Verification
Validating that adding the selected item does not violate constraints.
* **Example:** In the Activity Selection problem, verifying if the starting time of the next activity $s_i$ is greater than or equal to the finish time $f_{\text{last}}$ of the last selected activity ($s_i \ge f_{\text{last}}$).

### 4. Solution Set Union
Adding the validated candidate to our collection and updating state variables (e.g., remaining capacity, total cost).

---

## Time Complexity Table

| Algorithm / Problem | Preprocessing Complexity | Selection (per step) | Total Time Complexity |
| :--- | :--- | :--- | :--- |
| **Fractional Knapsack** | $O(n \log n)$ (Sorting) | $O(1)$ | $O(n \log n)$ |
| **Activity Selection** | $O(n \log n)$ (Sorting) | $O(1)$ | $O(n \log n)$ (if pre-sorted, $O(n)$) |
| **Huffman Coding** | $O(n)$ (Frequency map) | $O(\log n)$ (Heap extract/insert) | $O(n \log n)$ |
| **Kruskal's MST** | $O(E \log E)$ (Edge sorting) | $O(\alpha(V))$ (Union-Find) | $O(E \log E)$ or $O(E \log V)$ |
| **Prim's MST** | None | $O(\log V)$ (Min-Heap extract) | $O((V + E) \log V)$ |
| **Dijkstra's Algorithm** | None | $O(\log V)$ (Fibonacci / Binary Heap) | $O((V + E) \log V)$ |

---

## Space Complexity

The space complexity of greedy algorithms depends on whether preprocessing or auxiliary data structures are needed:

* **In-place Sorting:** If the inputs can be sorted in place, the auxiliary space is $O(1)$ or $O(\log n)$ (stack space for QuickSort).
* **Heaps & Priority Queues:** Algorithms like Dijkstra's, Prim's, or Huffman Coding require storing vertices or tree nodes in heaps, yielding an auxiliary space complexity of $O(V)$ or $O(N)$.
* **Graph Algorithms:** Storing adjacency lists takes $O(V + E)$ auxiliary space. Disjoint Set Union structures in Kruskal's algorithm require $O(V)$ auxiliary space to maintain parent and rank arrays.

---

## Advantages

* **Speed:** They exhibit exceptionally low time complexities, typically running in $O(n)$ or $O(n \log n)$ time.
* **Ease of Implementation:** They do not require maintaining complex recursive call stacks (like Backtracking) or tracking large multidimensional state-transition tables (like Dynamic Programming).
* **Low Memory Footprint:** Most greedy algorithms do not store overlapping state solutions, making them far more space-efficient than Dynamic Programming.
* **Step-by-step Execution:** Highly suitable for streaming data or online environments where decisions must be made in real-time as data arrives.

---

## Disadvantages

* **Lack of Global Guarantee:** They easily fall into "local optima traps." For example, in the 0/1 Knapsack problem, choosing the item with the highest density first can prevent you from selecting a combination of slightly less dense items that collectively yield a higher value.
* **Irreversibility:** If a choice made early on turns out to be suboptimal down the line, a greedy algorithm cannot go back to change it.
* **Difficult Proof of Correctness:** While writing a greedy algorithm is simple, proving mathematically that it always yields the optimal solution is notoriously difficult and usually requires induction, exchange arguments, or Matroid theory.

---

## Real World Applications

* **Data Compression:** Huffman Coding is used in file compression systems (such as ZIP, GZIP) and image formats (like JPEG) to assign variable-length binary codes based on frequency.
* **Network Routing:** Dijkstra's single-source shortest path algorithm is utilized in network routing protocols such as OSPF (Open Shortest Path First) to route data packets through paths with minimum latency or cost.
* **Minimum Spanning Trees:** Kruskal's and Prim's algorithms are used to design physical networks (e.g., electrical grids, telecommunication lines, water pipe layouts) to connect all nodes with minimal cabling cost.
* **Resource Scheduling:** Project management tools and OS task schedulers utilize greedy strategies to schedule CPU/GPU tasks to maximize throughput or minimize completion delay.

---

## Python Implementation

Below is a complete, production-grade Python implementation of the **Fractional Knapsack** problem.

```python
from typing import List

class Item:
    def __init__(self, value: float, weight: float):
        self.value = value
        self.weight = weight
        # Calculate value per unit of weight (Greedy Metric)
        self.cost = value / weight

def get_max_fractional_value(capacity: float, items: List[Item]) -> float:
    """
    Computes the maximum value that can be fit in a knapsack of given capacity.
    Time Complexity: O(N log N) where N is the number of items.
    Space Complexity: O(1) auxiliary (ignoring Python's Timsort allocation).
    """
    # Sort items based on cost (value/weight ratio) in descending order
    items.sort(key=lambda item: item.cost, reverse=True)
    
    total_value: float = 0.0
    current_capacity: float = capacity
    
    for item in items:
        if current_capacity <= 0:
            break
            
        if item.weight <= current_capacity:
            # If the item can be fully added, take it all
            total_value += item.value
            current_capacity -= item.weight
        else:
            # If the item cannot be fully added, take the fractional part
            fraction = current_capacity / item.weight
            total_value += item.value * fraction
            current_capacity = 0 # Knapsack is full
            
    return total_value

if __name__ == "__main__":
    # Test Data
    knapsack_capacity = 50
    raw_items = [
        Item(60, 10),  # Ratio: 6.0
        Item(100, 20), # Ratio: 5.0
        Item(120, 30)  # Ratio: 4.0
    ]
    
    max_val = get_max_fractional_value(knapsack_capacity, raw_items)
    print(f"--- Fractional Knapsack Execution (Python) ---")
    print(f"Knapsack Capacity: {knapsack_capacity}")
    print(f"Maximum value obtained in Knapsack: {max_val:.2f}")
```

---

## C++ Implementation

Below is a complete, compilable C++ implementation of the **Fractional Knapsack** problem.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

struct Item {
    double value;
    double weight;
    double ratio;

    Item(double v, double w) : value(v), weight(w) {
        ratio = v / w;
    }
};

// Comparator function to sort items based on value-to-weight ratio in descending order
bool compareItems(const Item& a, const Item& b) {
    return a.ratio > b.ratio;
}

double getMaxFractionalValue(double capacity, std::vector<Item>& items) {
    // Sort items using the comparator
    std::sort(items.begin(), items.end(), compareItems);

    double totalValue = 0.0;
    double currentCapacity = capacity;

    for (const auto& item : items) {
        if (currentCapacity <= 0) {
            break;
        }

        if (item.weight <= currentCapacity) {
            // Take the whole item
            totalValue += item.value;
            currentCapacity -= item.weight;
        } else {
            // Take the fractional part
            totalValue += item.value * (currentCapacity / item.weight);
            currentCapacity = 0; // Knapsack is full
        }
    }
    return totalValue;
}

int main() {
    double capacity = 50.0;
    std::vector<Item> items = {
        Item(60.0, 10.0),
        Item(100.0, 20.0),
        Item(120.0, 30.0)
    };

    double maxVal = getMaxFractionalValue(capacity, items);

    std::cout << "--- Fractional Knapsack Execution (C++) ---" << std::endl;
    std::cout << "Knapsack Capacity: " << capacity << std::endl;
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Maximum value obtained in Knapsack: " << maxVal << std::endl;

    return 0;
}
```

---

## Java Implementation

Below is a complete, compilable Java implementation of the **Fractional Knapsack** problem.

```java
import java.util.Arrays;
import java.util.Comparator;

class Item {
    double value;
    double weight;
    double ratio;

    public Item(double value, double weight) {
        this.value = value;
        this.weight = weight;
        this.ratio = value / weight;
    }
}

public class FractionalKnapsack {
    /**
     * Computes the maximum value that can be fit in a knapsack of given capacity.
     */
    public static double getMaxFractionalValue(double capacity, Item[] items) {
        // Sort items in descending order of value-to-weight ratio
        Arrays.sort(items, new Comparator<Item>() {
            @Override
            public int compare(Item a, Item b) {
                // Return -1 if a should come before b (descending order)
                return Double.compare(b.ratio, a.ratio);
            }
        });

        double totalValue = 0.0;
        double currentCapacity = capacity;

        for (Item item : items) {
            if (currentCapacity <= 0) {
                break;
            }

            if (item.weight <= currentCapacity) {
                // Take the complete item
                totalValue += item.value;
                currentCapacity -= item.weight;
            } else {
                // Take fractional part of the item
                totalValue += item.value * (currentCapacity / item.weight);
                currentCapacity = 0; // Knapsack is now full
            }
        }
        return totalValue;
    }

    public static void main(String[] args) {
        double capacity = 50.0;
        Item[] items = {
            new Item(60, 10),
            new Item(100, 20),
            new Item(120, 30)
        };

        double maxVal = getMaxFractionalValue(capacity, items);

        System.out.println("--- Fractional Knapsack Execution (Java) ---");
        System.out.println("Knapsack Capacity: " + capacity);
        System.out.printf("Maximum value obtained in Knapsack: %.2f\n", maxVal);
    }
}
```

---

## 3 Solved Examples

### Example 1: Activity Selection Problem
Given $N$ activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming they can only work on one activity at a time.

#### Inputs:
* Activities: $A = \{a_1, a_2, a_3, a_4, a_5, a_6\}$
* Start times: $S = [1, 3, 0, 5, 8, 5]$
* Finish times: $F = [2, 4, 6, 7, 9, 9]$

#### Step-by-Step Resolution:
1. **Greedy Strategy Choice:** To maximize activities, we must select activities that finish as early as possible. This frees up maximum room for subsequent activities.
2. **Sort:** Sort activities based on finish times ($F$):
   * $a_1: [1, 2]$
   * $a_2: [3, 4]$
   * $a_4: [5, 7]$
   * $a_5: [8, 9]$
   * $a_6: [5, 9]$
   * $a_3: [0, 6]$

   *Sorted List:* $[(1,2), (3,4), (5,7), (0,6), (8,9), (5,9)]$
3. **Initialize Solution Set:**
   * Select first activity: $a_1 = (1, 2)$. Last finish time $f_{\text{last}} = 2$.
   * Selected Set: $\{a_1\}$
4. **Iterate and Select:**
   * Check $a_2 = (3, 4)$: Start time $3 \ge f_{\text{last}} (2)$. Select $a_2$. Update $f_{\text{last}} = 4$. Selected Set: $\{a_1, a_2\}$
   * Check $a_4 = (5, 7)$: Start time $5 \ge f_{\text{last}} (4)$. Select $a_4$. Update $f_{\text{last}} = 7$. Selected Set: $\{a_1, a_2, a_4\}$
   * Check $a_3 = (0, 6)$: Start time $0 < f_{\text{last}} (7)$. Reject.
   * Check $a_5 = (8, 9)$: Start time $8 \ge f_{\text{last}} (7)$. Select $a_5$. Update $f_{\text{last}} = 9$. Selected Set: $\{a_1, a_2, a_4, a_5\}$
   * Check $a_6 = (5, 9)$: Start time $5 < f_{\text{last}} (9)$. Reject.
5. **Final Output:** The maximum subset of mutually compatible activities is $\{a_1, a_2, a_4, a_5\}$ (Count = 4).

---

### Example 2: Huffman Coding (Data Compression)
Build a Huffman tree and find the unique prefix codes for the given characters with their frequency distribution.

#### Inputs:
* Characters: $\{A, B, C, D, E\}$
* Frequencies: $\{A: 3, B: 12, C: 5, D: 2, E: 8\}$

#### Step-by-Step Resolution:
1. **Initialize Min-Heap:** Insert all character nodes as leaf nodes with frequencies:
   `[(2, 'D'), (3, 'A'), (5, 'C'), (8, 'E'), (12, 'B')]`
2. **Combine Nodes (Iteration 1):**
   * Extract two nodes with lowest frequency: `D` (2) and `A` (3).
   * Create a new parent node $N_1$ with frequency $2 + 3 = 5$.
   * Reinsert $N_1$ into heap.
   * Heap: `[(5, 'C'), (5, 'N1'), (8, 'E'), (12, 'B')]` (where $N_1$ has children $D$ and $A$).
3. **Combine Nodes (Iteration 2):**
   * Extract two lowest: `C` (5) and $N_1$ (5).
   * Create parent $N_2$ with frequency $5 + 5 = 10$.
   * Reinsert $N_2$ into heap.
   * Heap: `[(8, 'E'), (10, 'N2'), (12, 'B')]`.
4. **Combine Nodes (Iteration 3):**
   * Extract two lowest: `E` (8) and $N_2$ (10).
   * Create parent $N_3$ with frequency $8 + 10 = 18$.
   * Reinsert $N_3$ into heap.
   * Heap: `[(12, 'B'), (18, 'N3')]`.
5. **Combine Nodes (Iteration 4 - Final):**
   * Extract lowest: `B` (12) and $N_3$ (18).
   * Create root node with frequency $12 + 18 = 30$.
6. **Assigning Binary Paths (Left = 0, Right = 1):**

```
                 [Root: 30]
               /            \
           (0)                (1)
         [B: 12]            [N3: 18]
                           /        \
                        (0)          (1)
                      [E: 8]        [N2: 10]
                                   /        \
                                (0)          (1)
                              [C: 5]        [N1: 5]
                                           /       \
                                        (0)         (1)
                                      [D: 2]       [A: 3]
```

* **Generated Huffman Codes:**
  * **B:** `0`
  * **E:** `10`
  * **C:** `110`
  * **D:** `1110`
  * **A:** `1111`

---

### Example 3: Kruskal's Minimum Spanning Tree
Find the MST of the undirected weighted graph using Kruskal's greedy strategy.

```
       1       5
   (A)---(B)---(C)
    |   / |   / |
   3|  /2 |6 /4 |3
    | /   | /   |
   (D)---(E)---(F)
       4       2
```

#### Inputs:
* Vertices: $\{A, B, C, D, E, F\}$
* Edges:
  * $(A, B) \rightarrow 1$, $(B, D) \rightarrow 2$, $(A, D) \rightarrow 3$, $(C, F) \rightarrow 3$, $(D, E) \rightarrow 4$, $(E, F) \rightarrow 2$, $(C, E) \rightarrow 4$, $(B, C) \rightarrow 5$, $(B, E) \rightarrow 6$

#### Step-by-Step Resolution:
1. **Initialize Disjoint Set Union (DSU):** Every vertex is its own parent.
2. **Sort all edges by weight:**
   1. $(A, B) \rightarrow 1$
   2. $(B, D) \rightarrow 2$
   3. $(E, F) \rightarrow 2$
   4. $(A, D) \rightarrow 3$
   5. $(C, F) \rightarrow 3$
   6. $(D, E) \rightarrow 4$
   7. $(C, E) \rightarrow 4$
   8. $(B, C) \rightarrow 5$
   9. $(B, E) \rightarrow 6$
3. **Evaluate and Union:**
   * Select **$(A, B) \rightarrow 1$**: Find(A) $\neq$ Find(B). Union(A, B). **(Add to MST)**.
   * Select **$(B, D) \rightarrow 2$**: Find(B) $\neq$ Find(D). Union(B, D). **(Add to MST)**.
   * Select **$(E, F) \rightarrow 2$**: Find(E) $\neq$ Find(F). Union(E, F). **(Add to MST)**.
   * Select **$(A, D) \rightarrow 3$**: Find(A) = Find(D) (both connected to same set). **Discard (Creates Cycle)**.
   * Select **$(C, F) \rightarrow 3$**: Find(C) $\neq$ Find(F). Union(C, F). **(Add to MST)**.
   * Select **$(D, E) \rightarrow 4$**: Find(D) $\neq$ Find(E). Union(D, E). **(Add to MST)**.
4. **MST Termination Check:** We have selected $V - 1 = 5$ edges. Stop.
5. **Output Minimum Cost:** $1 + 2 + 2 + 3 + 4 = 12$.

---

## 5 Interview Questions with Answers

### Q1. What is the fundamental difference between Greedy and Dynamic Programming?
**Answer:**
* **Greedy:** Makes the best choice at the current step (locally) and commits to it irreversibly. It works top-down, selecting candidates without looking at future consequences or subproblems.
* **Dynamic Programming:** Explores all possible decision paths, solves overlapping subproblems, and remembers solutions to these subproblems (memoization/tabulation) to build the global optimal solution. It is a bottom-up or top-down approach that *does* backtrack through states, guaranteeing optimality when greedy choice fails.

---

### Q2. Why does the greedy approach work for the Fractional Knapsack problem but fail for the 0/1 Knapsack problem?
**Answer:**
In **Fractional Knapsack**, we can split items. By sorting by value-to-weight ratio, we ensure that every unit of weight added to the knapsack has the highest possible value. If capacity remains, we simply take a fraction of the next best item, completely saturating the capacity at maximum density.

In **0/1 Knapsack**, items cannot be divided. If we choose an item with the highest density, its size might prevent us from packing multiple slightly lower-density items that together yield a higher total value. 

*For example:* Knapsack capacity = 10.
* Item A: Weight = 6, Value = 60 (Ratio = 10)
* Item B: Weight = 5, Value = 45 (Ratio = 9)
* Item C: Weight = 5, Value = 45 (Ratio = 9)

A greedy algorithm selects **Item A** (value 60, remaining capacity 4). It cannot fit B or C. Total value = 60.
The optimal solution is to select **Item B and C** (total value = 90, total weight = 10).

---

### Q3. How do you mathematically prove that a greedy algorithm is correct?
**Answer:**
There are two standard proof methods:
1. **Greedy Stays Ahead:** Show that at every index/step of the decision-making process, the greedy solution's progress (e.g., shortest path, earliest finish time) is at least as optimal as any other arbitrary feasible solution.
2. **Exchange Argument:** Assume there is an optimal solution $O$ that differs from our greedy solution $G$. Find the first point of difference, and show that exchanging the choice in $O$ with the greedy choice either improves the solution or keeps it equal. By inductively replacing all elements of $O$ with those in $G$, we prove that the greedy solution is also optimal.

---

### Q4. Does the Coin Change problem always yield an optimal solution using a greedy approach?
**Answer:**
No. The greedy approach for coin change (always choosing the largest denomination that fits) only works for **canonical coin systems** (such as US coins: $[1, 5, 10, 25]$). 

If the denominations are arbitrary, say $\{1, 3, 4\}$, and we want to make change for $6$:
* **Greedy Choice:** Selects $4$, then remaining is $2$. Selects $1$, then another $1$. Total coins = 3 ($4 + 1 + 1$).
* **Optimal Solution:** Selects $3$ and $3$. Total coins = 2 ($3 + 3$).

For non-canonical systems, we must use Dynamic Programming.

---

### Q5. Why does Dijkstra's algorithm fail when graph weight edges are negative?
**Answer:**
Dijkstra's algorithm is based on the greedy choice that once a node's distance is marked as finalized (extracted from the priority queue), its shortest path from the source is determined and will never change.

```
       2
   (S)--->(A)
    |     /
   5|    /-4
    v   v
   (B)-/
```
If we start at $S$:
1. $S$ is initialized to $0$. Neighbors: $A$ is at distance $2$, $B$ is at distance $5$.
2. The greedy choice selects $A$ as finalized with distance $2$ (since $2 < 5$).
3. Later, when evaluating $B$, we find the edge $B \rightarrow A$ with weight $-4$. The path $S \rightarrow B \rightarrow A$ has a total cost of $5 + (-4) = 1$.
4. Because $A$ was already finalized, Dijkstra's algorithm cannot update $A$'s distance to $1$, leading to an incorrect result.

---

## Common Mistakes

* **Assuming Greedy always yields the Absolute Optimal Solution:** Many developers default to a greedy strategy because of its simplicity, forgetting that it often leads to suboptimal results for complex constraint structures (such as 0/1 Knapsack, Coin Change with arbitrary systems, or Traveling Salesperson).
* **Failing to Sort the Inputs:** A greedy algorithm's correctness almost always depends on processing elements in a specific order. Forgetting to implement custom sorting criteria based on the correct greedy choice metric will cause the algorithm to fail.
* **Incorrect Priority Queue Comparator Logic:** When implementing graph algorithms like Dijkstra's or Prim's, setting a Max-Heap instead of a Min-Heap (or vice versa) is a common implementation bug.
* **Overlooking Time Spent in Preprocessing:** While the selection loop of a greedy algorithm may run in $O(n)$ time, if the sorting step takes $O(n \log n)$, the global time complexity is $O(n \log n)$. This must be factored into performance analysis.

---

## Summary

* **Core Premise:** Greedy algorithms make locally optimal choices at each step, hoping they will lead to a globally optimal solution.
* **Prerequisites:** A problem must exhibit both the **Greedy Choice Property** and **Optimal Substructure** to be solved optimally via a greedy strategy.
* **Algorithmic Flow:** Typically involves: (1) Sorting/Prioritizing candidates, (2) Iterating through them, (3) Confirming feasibility, and (4) Accumulating valid candidates.
* **Performance:** They generally run in $O(n \log n)$ time with $O(1)$ auxiliary space if sorting is done in-place, making them faster than Dynamic Programming.
* **Classic Examples:** Fractional Knapsack, Activity Selection, Huffman Coding, Dijkstra's, Prim's, and Kruskal's algorithms.