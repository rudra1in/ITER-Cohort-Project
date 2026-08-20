# Dynamic Programming

## Definition

**Dynamic Programming (DP)** is an algorithmic paradigm that solves complex, optimization problems by breaking them down into simpler, overlapping subproblems. It computes the solution to each subproblem exactly once and stores the results in a data structure (such as an array, map, or table). 

When the same subproblem arises again, the algorithm simply looks up the precomputed solution instead of re-evaluating it. This design pattern is governed by **Bellman's Principle of Optimality**, which states that *an optimal policy has the property that whatever the initial state and initial decision are, the remaining decisions must constitute an optimal policy with regard to the state resulting from the first decision.*

---

## Why it is needed

In computer science, naive recursion solves problems by repeatedly branching into smaller subproblems. However, many problems exhibit **redundant computations**—meaning the exact same recursive calls are made multiple times along different branches of the recursion tree.

### The Fibonacci Example
Consider computing the $n$-th Fibonacci number using naive recursion:

$$F(n) = F(n-1) + F(n-2) \quad \text{for } n \ge 2, \text{ with base cases } F(0) = 0, F(1) = 1$$

The recursion tree for $F(5)$ is:

```text
                  F(5)
                /      \
             F(4)      F(3)
            /   \      /   \
         F(3)  F(2)  F(2)  F(1)
         /  \  /  \  /  \
       F(2) F(1)F(1)F(0)F(1)F(0)
       / \
     F(1)F(0)
```

**Inefficiency Analysis:**
*   $F(3)$ is evaluated **2 times**.
*   $F(2)$ is evaluated **3 times**.
*   The overall time complexity is exponential: $O(2^n)$ (specifically, $O(\phi^n)$ where $\phi \approx 1.618$).

Dynamic Programming solves this issue. By caching the results of $F(2), F(3), F(4),$ etc., we resolve each subproblem in $O(1)$ time after its first computation. This reduces the time complexity from **$O(2^n)$ to $O(n)$**, making previously unsolvable inputs computable in milliseconds.

---

## Characteristics

A problem can be solved using Dynamic Programming if and only if it possesses two primary mathematical characteristics:

### 1. Overlapping Subproblems
The space of subproblems must be small; that is, a recursive algorithm visits the same subproblems repeatedly rather than generating new, unique subproblems at every step.
*   **Example:** In the Fibonacci sequence, computing $F(n)$ requires $F(n-1)$ and $F(n-2)$, both of which require $F(n-3)$.
*   **Contrast:** Merge Sort does *not* have overlapping subproblems. Sorting the left half of an array is completely independent of sorting the right half. Thus, Merge Sort is classified as **Divide and Conquer**, not Dynamic Programming.

### 2. Optimal Substructure
An optimal solution to a problem of size $n$ can be constructed efficiently from the optimal solutions of its subproblems.
*   **Example:** In the Shortest Path problem, if the shortest path from node $A$ to node $C$ passes through node $B$, then the sub-path $A \to B$ must be the shortest path from $A$ to $B$, and $B \to C$ must be the shortest path from $B$ to $C$.
*   **Counter-Example:** The Longest Path problem (without cycles) does not have optimal substructure. If the longest path from $A$ to $C$ is $A \to B \to C$, the sub-path $A \to B$ might not be the longest path from $A$ to $B$ because choosing it might exhaust vertices needed to complete the overall path.

---

## Working

The systematic process of designing a Dynamic Programming algorithm follows a structured 4-step workflow:

```text
+------------------------------------+
|  1. Define the State Variables     |
+------------------------------------+
                  |
                  v
+------------------------------------+
|  2. Formulate Recurrence Relation  |
+------------------------------------+
                  |
                  v
+------------------------------------+
|  3. Identify Base Cases & Boundary |
+------------------------------------+
                  |
                  v
+------------------------------------+
|  4. Choose Strategy (Top/Bottom)   |
+------------------------------------+
```

1.  **Define the State:** Identify what a state (or subproblem representation) is. For example, $DP[i]$ could represent the minimum cost to reach step $i$.
2.  **Formulate the Recurrence Relation:** Express the solution to the current state in terms of smaller states. For example:
    $$DP[i] = \min(DP[i-1] + \text{cost}[i-1], DP[i-2] + \text{cost}[i-2])$$
3.  **Identify Base Cases:** Set up the boundaries of the problem where the answer is known without further subproblems (e.g., $DP[0] = 0$).
4.  **Compute the Solution:** Choose either the Top-Down (Memoization) or Bottom-Up (Tabulation) approach to fill the cache.

---

## Memory Representation

Dynamic Programming requires a structured memory space to store subproblem answers. This is known as the **DP Cache/Table**.

### 1D DP Array Representation (e.g., Fibonacci)
For a 1D DP array of size $N+1$, memory is allocated sequentially.

```text
Index:    [0]   [1]   [2]   [3]   [4]   [5]   ...   [N]
Value:  |  0  |  1  |  1  |  2  |  3  |  5  |     | F(N) |
```
*   **State transition:** To compute index `5`, the CPU only queries indices `4` and `3`.

### 2D DP Table Representation (e.g., 0/1 Knapsack)
For problems with two variables (e.g., $i$ items and $w$ capacity), a 2D table of size $(N+1) \times (W+1)$ is constructed.

```text
               Capacity (w) --->
          [0]   [1]   [2]   [3]   [4]   ...   [W]
  Items  +-----+-----+-----+-----+-----+-----+-----+
   [0]   |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  <-- Base Case
   [1]   |  0  |  2  |  2  |  2  |  2  |  2  |  2  |
   [2]   |  0  |  2  |  5  |  7  |  7  |  7  |  7  |
   [3]   |  0  |  2  |  5  |  7  |  9  |  11 |  11 |  <-- Current State DP[i][w]
   ...   |     |     |     |     |     |     |     |
   [N]   |  0  | ... |     |     |     |     | Ans |  <-- Final Answer
         +-----+-----+-----+-----+-----+-----+-----+
```

---

## Types

There are two primary paradigms for implementing Dynamic Programming:

| Attribute | Top-Down (Memoization) | Bottom-Up (Tabulation) |
| :--- | :--- | :--- |
| **Approach** | Starts with the main problem and recursively breaks it down. | Starts from the base cases and iteratively builds up. |
| **Mechanism** | Recursion + Lookup Cache | Iteration + DP Table |
| **Overhead** | High call-stack overhead due to deep recursion. | No call-stack overhead; extremely fast cache-friendly loops. |
| **Subproblem Space** | Solves only the subproblems that are *actually* required. | Solves *all* subproblems within the table boundaries. |
| **Implementation** | Easier to write if the recursive relationship is known. | Can be harder to formulate as it requires structural ordering. |

### Top-Down (Memoization) Abstract Pattern (Python-like)
```python
memo = {}
def solve(state):
    if state is base_case:
        return base_value
    if state not in memo:
        memo[state] = combine(solve(state - 1), solve(state - 2))
    return memo[state]
```

### Bottom-Up (Tabulation) Abstract Pattern (Python-like)
```python
dp = [0] * (N + 1)
dp[0] = base_value_0
dp[1] = base_value_1
for i in range(2, N + 1):
    dp[i] = combine(dp[i - 1], dp[i - 2])
return dp[N]
```

---

## Operations

Since Dynamic Programming is a structural methodology rather than a self-contained data structure, its "operations" refer to state manipulation steps within memory.

### 1. State Initialization
Setting up the storage buffer (e.g., Array, Matrix) with sentinel values (such as `-1` or `null`) to indicate uncomputed states, and initializing base cases.

*   **Example (2D Memoization Init in C++):**
    ```cpp
    vector<vector<int>> memo(N, vector<int>(M, -1));
    ```

### 2. State Transition Query
Evaluating a state's value by polling previously calculated states from memory.
*   **Example (Iterative Transition in Knapsack):**
    ```text
    DP[i][w] = max(DP[i-1][w], val[i-1] + DP[i-1][w - wt[i-1]])
    ```
    This operation performs exactly 1 array write and up to 2 array reads, executing in $O(1)$ time.

### 3. Space Optimization (State Reduction)
Since many transitions only depend on the immediate previous row or column, we can discard historical states to save memory.
*   **Example (1D rolling array for Knapsack):**
    Instead of maintaining a 2D grid of size $N \times W$, we maintain a 1D array of size $W+1$ and update it in reverse order.
    ```python
    # Space reduced from O(N*W) to O(W)
    for i in range(N):
        for w in range(W, wt[i] - 1, -1):
            dp[w] = max(dp[w], val[i] + dp[w - wt[i]])
    ```

---

## Time Complexity Table

Let $N$ be the primary size parameter (e.g., number of items, sequence length) and $W$ or $M$ be secondary constraint parameters (e.g., capacity, second sequence length).

| Algorithm / Scenario | Time Complexity (Naive Recursive) | Time Complexity (Dynamic Programming) | Space Complexity (Memoization / Tabulation) | Space Complexity (Optimized DP) |
| :--- | :--- | :--- | :--- | :--- |
| **Fibonacci Sequence** | $O(2^N)$ | $O(N)$ | $O(N)$ | $O(1)$ |
| **0/1 Knapsack Problem** | $O(2^N)$ | $O(N \times W)$ | $O(N \times W)$ | $O(W)$ |
| **Longest Common Subsequence** | $O(2^{N+M})$ | $O(N \times M)$ | $O(N \times M)$ | $O(\min(N, M))$ |
| **Matrix Chain Multiplication** | $O(2^N)$ | $O(N^3)$ | $O(N^2)$ | $O(N^2)$ |
| **Climbing Stairs** | $O(2^N)$ | $O(N)$ | $O(N)$ | $O(1)$ |
| **Edit Distance** | $O(3^{N+M})$ | $O(N \times M)$ | $O(N \times M)$ | $O(\min(N, M))$ |

---

## Space Complexity

The space complexity of a Dynamic Programming algorithm is determined by the size of the memory allocated to store the state solutions, alongside any recursive call-stack overhead.

### 1. Tabulation Space Complexity
*   **1D State Table:** $O(N)$
*   **2D State Table:** $O(N \times M)$
*   *Stack Overhead:* $O(1)$ (since it uses iterative loops).

### 2. Memoization Space Complexity
*   **Cache Allocation:** $O(N \times M)$
*   **Recursive Stack Depth:** $O(N + M)$
*   *Total Space:* $O(N \times M) + O(N + M) = O(N \times M)$

### 3. Space Optimization (State Compression)
If the recurrence relation for state $DP[i][j]$ only relies on the current and previous rows (i.e., $DP[i-1][j]$), we can store only two rows (or a single row updated in place), bringing the space complexity down to:
$$\text{Optimized Space} = O(\text{Width of Table}) \quad \text{or} \quad O(1)$$

---

## Advantages

*   **Drastic Performance Gains:** Reduces time complexities from exponential levels ($O(2^N)$) to polynomial levels ($O(N^2)$ or $O(N)$).
*   **Guaranteed Global Optimality:** Unlike greedy algorithms, DP explores all candidate states systematically, ensuring an absolute mathematically optimal solution.
*   **Code Reusability:** Simplifies complex recursive code into clean, iterative loops (when utilizing Tabulation).
*   **Standardization:** Offers a repeatable framework (State definition $\to$ Transition relation) for a wide array of optimization problems.

---

## Disadvantages

*   **High Memory Consumption:** Storing intermediate tables can consume a substantial amount of RAM (e.g., $O(N^2)$ or $O(N^3)$ space), which can lead to Out-Of-Memory exceptions on large inputs.
*   **Design Difficulty:** Determining the exact state representation and recurrence relation requires strong analytical skills; there is no single, simple formula that works for all problems.
*   **Stack Overflow Risks:** Deep recursion in Top-Down Memoization can easily exceed stack limit boundaries in languages like C++ or Python if the recursion limit is reached.

---

## Real World Applications

*   **Network Routing Algorithms:** 
    *   **Bellman-Ford Algorithm:** Finds the shortest paths in a graph containing negative edge weights (utilizes DP state formulation).
    *   **Floyd-Warshall Algorithm:** Computes all-pairs shortest paths on dense graphs.
*   **Bioinformatics (Sequence Alignment):**
    *   **Needleman-Wunsch & Smith-Waterman Algorithms:** Used to align DNA, RNA, or protein sequences to detect similarities and evolutionary mutations.
*   **Search Engine Autocomplete & Spell Checking:**
    *   **Levenshtein Distance (Edit Distance):** Measures the minimum operations needed to transform one string into another, enabling typo suggestions.
*   **Financial Portfolio Optimization:**
    *   **Resource Allocation:** Allocating cash assets among projects/stocks with varying risk/reward profiles to maximize return under budget constraints (Knapsack variant).
*   **Text Processing & Typography:**
    *   **Word Wrap / Line Breaking:** Algorithms (such as the one used in $\LaTeX$) that calculate optimal line breaks to minimize uneven gaps (raggedness) across paragraphs.

---

## Python Implementation

Here is a complete, production-ready Python program solving the classic **0/1 Knapsack Problem** using both **Top-Down Memoization** and **Bottom-Up Tabulation**.

```python
class Knapsack:
    """
    Class to solve the 0/1 Knapsack Problem.
    Given weights and values of N items, put these items in a knapsack of capacity W 
    to get the maximum total value in the knapsack.
    """
    
    # --- 1. TOP-DOWN APPROACH (MEMOIZATION) ---
    def solve_memoization(self, weights: list[int], values: list[int], capacity: int) -> int:
        n = len(weights)
        # Create a memoization table initialized with -1
        memo = [[-1 for _ in range(capacity + 1)] for _ in range(n)]
        
        def _helper(idx: int, rem_capacity: int) -> int:
            # Base Case: No items left or capacity is 0
            if idx < 0 or rem_capacity <= 0:
                return 0
            
            # Check cache
            if memo[idx][rem_capacity] != -1:
                return memo[idx][rem_capacity]
            
            # Scenario A: Exclude the current item
            exclude = _helper(idx - 1, rem_capacity)
            
            # Scenario B: Include the current item (if capacity allows)
            include = 0
            if weights[idx] <= rem_capacity:
                include = values[idx] + _helper(idx - 1, rem_capacity - weights[idx])
                
            # Store and return optimal path
            memo[idx][rem_capacity] = max(exclude, include)
            return memo[idx][rem_capacity]
            
        return _helper(n - 1, capacity)

    # --- 2. BOTTOM-UP APPROACH (TABULATION WITH SPACE OPTIMIZATION) ---
    def solve_tabulation(self, weights: list[int], values: list[int], capacity: int) -> int:
        n = len(weights)
        if n == 0 or capacity == 0:
            return 0
            
        # We optimize space to 1D because dp[w] depends only on previous row dp[w - weight]
        dp = [0] * (capacity + 1)
        
        for i in range(n):
            curr_weight = weights[i]
            curr_value = values[i]
            # Traverse backward to ensure items are evaluated at most once
            for w in range(capacity, curr_weight - 1, -1):
                dp[w] = max(dp[w], curr_value + dp[w - curr_weight])
                
        return dp[capacity]

# --- Execution Driver ---
if __name__ == "__main__":
    solver = Knapsack()
    weights = [1, 2, 3, 5]
    values = [1, 6, 10, 16]
    capacity = 7
    
    print("--- 0/1 Knapsack Execution ---")
    print(f"Weights: {weights}, Values: {values}, Capacity: {capacity}")
    print(f"Memoization Result: {solver.solve_memoization(weights, values, capacity)}")
    print(f"Tabulation Result:  {solver.solve_tabulation(weights, values, capacity)}")
```

---

## C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class KnapsackSolver {
public:
    // --- 1. TOP-DOWN APPROACH (MEMOIZATION) ---
    int solveMemoization(const vector<int>& weights, const vector<int>& values, int capacity) {
        int n = weights.size();
        // Initialize memoization table with -1
        vector<vector<int>> memo(n, vector<int>(capacity + 1, -1));
        return memoizeHelper(n - 1, capacity, weights, values, memo);
    }

    // --- 2. BOTTOM-UP APPROACH (TABULATION WITH O(W) SPACE) ---
    int solveTabulation(const vector<int>& weights, const vector<int>& values, int capacity) {
        int n = weights.size();
        if (n == 0 || capacity == 0) return 0;

        vector<int> dp(capacity + 1, 0);

        for (int i = 0; i < n; ++i) {
            int currWeight = weights[i];
            int currValue = values[i];
            // Loop backwards to use values from the previous row/state
            for (int w = capacity; w >= currWeight; --w) {
                dp[w] = max(dp[w], currValue + dp[w - currWeight]);
            }
        }
        return dp[capacity];
    }

private:
    int memoizeHelper(int idx, int remCapacity, const vector<int>& weights, 
                      const vector<int>& values, vector<vector<int>>& memo) {
        // Base case
        if (idx < 0 || remCapacity <= 0) {
            return 0;
        }

        // Cache hit
        if (memo[idx][remCapacity] != -1) {
            return memo[idx][remCapacity];
        }

        // Exclude item
        int exclude = memoizeHelper(idx - 1, remCapacity, weights, values, memo);

        // Include item
        int include = 0;
        if (weights[idx] <= remCapacity) {
            include = values[idx] + memoizeHelper(idx - 1, remCapacity - weights[idx], weights, values, memo);
        }

        // Write to cache and return
        return memo[idx][remCapacity] = max(exclude, include);
    }
};

int main() {
    KnapsackSolver solver;
    vector<int> weights = {1, 2, 3, 5};
    vector<int> values = {1, 6, 10, 16};
    int capacity = 7;

    cout << "--- 0/1 Knapsack C++ Execution ---" << endl;
    cout << "Memoization Result: " << solver.solveMemoization(weights, values, capacity) << endl;
    cout << "Tabulation Result:  " << solver.solveTabulation(weights, values, capacity) << endl;

    return 0;
}
```

---

## Java Implementation

```java
import java.util.Arrays;

public class KnapsackSolver {

    // --- 1. TOP-DOWN APPROACH (MEMOIZATION) ---
    public int solveMemoization(int[] weights, int[] values, int capacity) {
        int n = weights.size();
        int[][] memo = new int[n][capacity + 1];
        for (int[] row : memo) {
            Arrays.fill(row, -1);
        }
        return memoizeHelper(n - 1, capacity, weights, values, memo);
    }

    private int memoizeHelper(int idx, int remCapacity, int[] weights, int[] values, int[][] memo) {
        if (idx < 0 || remCapacity <= 0) {
            return 0;
        }

        if (memo[idx][remCapacity] != -1) {
            return memo[idx][remCapacity];
        }

        int exclude = memoizeHelper(idx - 1, remCapacity, weights, values, memo);

        int include = 0;
        if (weights[idx] <= remCapacity) {
            include = values[idx] + memoizeHelper(idx - 1, remCapacity - weights[idx], weights, values, memo);
        }

        memo[idx][remCapacity] = Math.max(exclude, include);
        return memo[idx][remCapacity];
    }

    // --- 2. BOTTOM-UP APPROACH (SPACE-OPTIMIZED TABULATION) ---
    public int solveTabulation(int[] weights, int[] values, int capacity) {
        int n = weights.length;
        if (n == 0 || capacity == 0) return 0;

        int[] dp = new int[capacity + 1];

        for (int i = 0; i < n; i++) {
            int currWeight = weights[i];
            int currValue = values[i];
            for (int w = capacity; w >= currWeight; w--) {
                dp[w] = Math.max(dp[w], currValue + dp[w - currWeight]);
            }
        }
        return dp[capacity];
    }

    public static void main(String[] args) {
        KnapsackSolver solver = new KnapsackSolver();
        int[] weights = {1, 2, 3, 5};
        int[] values = {1, 6, 10, 16};
        int capacity = 7;

        System.out.println("--- 0/1 Knapsack Java Execution ---");
        System.out.println("Memoization Result: " + solver.solveMemoization(weights, values, capacity));
        System.out.println("Tabulation Result:  " + solver.solveTabulation(weights, values, capacity));
    }
}
```

---

## 3 Solved Examples

### Example 1: Longest Common Subsequence (LCS)

#### Problem Statement
Given two sequences $S1$ and $S2$, find the length of the longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguously.

*   **Input:** $S1 = \text{"text"}$, $S2 = \text{"testing"}$
*   **Output:** $4$ (The LCS is $\text{"test"}$, which has a length of 4)

#### Recurrence Formulation
Let $dp[i][j]$ represent the length of the LCS of substrings $S1[0 \dots i-1]$ and $S2[0 \dots j-1]$.

*   **Base Cases:**
    $$dp[i][0] = 0 \quad \forall \ i$$
    $$dp[0][j] = 0 \quad \forall \ j$$

*   **State Transition:**
    $$\text{If } S1[i-1] == S2[j-1]: \quad dp[i][j] = 1 + dp[i-1][j-1]$$
    $$\text{If } S1[i-1] \neq S2[j-1]: \quad dp[i][j] = \max(dp[i-1][j], \ dp[i][j-1])$$

#### Step-by-Step Transition Trace Table
Let $S1 = \text{"BAT"}$, $S2 = \text{"CAT"}$.

1.  Initialize a $4 \times 4$ array with $0$s.
2.  Compare characters iteratively:

```text
       -   C   A   T
   - [ 0   0   0   0 ]
   B [ 0   0   0   0 ]  (B != C, B != A, B != T) -> max(above, left)
   A [ 0   0   1   1 ]  (A == A) -> 1 + dp[1][1] = 1
   T [ 0   0   1   2 ]  (T == T) -> 1 + dp[2][2] = 2
```

The bottom-right cell contains the final answer, which is **$2$** ("AT").

#### Python Code
```python
def longest_common_subsequence(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[m][n]
```

---

### Example 2: Coin Change Problem (Minimum Coins)

#### Problem Statement
Given an array of coins representing different denominations and a total target amount of money, write a function to compute the fewest number of coins needed to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

*   **Input:** $\text{coins} = [1, 2, 5]$, $\text{amount} = 11$
*   **Output:** $3$ ($11 = 5 + 5 + 1$)

#### Recurrence Formulation
Let $dp[i]$ represent the minimum number of coins needed to make up amount $i$.

*   **Base Case:**
    $$dp[0] = 0 \quad (\text{0 coins needed to make amount 0})$$

*   **State Transition:**
    $$dp[i] = \min_{c \in \text{coins}} (dp[i - c] + 1) \quad \text{for } i \ge c$$
    Initialize all values in the DP table to $\infty$ (or a large value like `amount + 1`) to represent unreachable states.

#### Step-by-Step Transition Trace Table
Let $\text{coins} = [1, 2, 5]$, $\text{amount} = 5$.
*   Initialize `dp` table of size $6$: `[0, inf, inf, inf, inf, inf]`.
*   **$i = 1$**:
    *   coin = 1: `dp[1] = min(inf, dp[1-1] + 1) = min(inf, 0 + 1) = 1`
*   **$i = 2$**:
    *   coin = 1: `dp[2] = min(inf, dp[2-1] + 1) = min(inf, 1 + 1) = 2`
    *   coin = 2: `dp[2] = min(2, dp[2-2] + 1) = min(2, 0 + 1) = 1`
*   **$i = 3$**:
    *   coin = 1: `dp[3] = min(inf, dp[3-1] + 1) = min(inf, 1 + 1) = 2`
    *   coin = 2: `dp[3] = min(2, dp[3-2] + 1) = min(2, 1 + 1) = 2`
*   **$i = 4$**:
    *   coin = 1: `dp[4] = min(inf, dp[4-1] + 1) = min(inf, 2 + 1) = 3`
    *   coin = 2: `dp[4] = min(3, dp[4-2] + 1) = min(3, 1 + 1) = 2`
*   **$i = 5$**:
    *   coin = 1: `dp[5] = min(inf, dp[5-1] + 1) = min(inf, 2 + 1) = 3`
    *   coin = 2: `dp[5] = min(3, dp[5-2] + 1) = min(3, 2 + 1) = 3`
    *   coin = 5: `dp[5] = min(3, dp[5-5] + 1) = min(3, 0 + 1) = 1`

Final table: `[0, 1, 1, 2, 2, 1]`. The answer at index 5 is **$1$**.

#### Python Code
```python
def coin_change(coins: list[int], amount: int) -> int:
    # Initialize with float('inf')
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    return dp[amount] if dp[amount] != float('inf') else -1
```

---

### Example 3: Longest Increasing Subsequence (LIS)

#### Problem Statement
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

*   **Input:** `nums = [10, 9, 2, 5, 3, 7, 101, 18]`
*   **Output:** $4$ (The LIS is `[2, 3, 7, 101]` or `[2, 3, 7, 18]`, both of length 4)

#### Recurrence Formulation
Let $dp[i]$ represent the length of the LIS ending at index $i$.

*   **Base Case:**
    $$dp[i] = 1 \quad \forall \ i \quad (\text{Each element is an LIS of length 1 by itself})$$

*   **State Transition:**
    For each index $i$, iterate through all preceding indices $j < i$:
    $$\text{If } \text{nums}[i] > \text{nums}[j]: \quad dp[i] = \max(dp[i], \ dp[j] + 1)$$
    The final answer is $\max(dp[0], dp[1], \dots, dp[n-1])$.

#### Step-by-Step Transition Trace Table
Let `nums = [3, 1, 4, 2]`.
1.  Initialize `dp` array: `[1, 1, 1, 1]`.
2.  Iterate and compare elements:
    *   **$i = 0$** (`3`): `dp = [1, 1, 1, 1]`
    *   **$i = 1$** (`1`):
        *   $j = 0$ (`3`): `nums[1] < nums[0]` $\to$ no change.
    *   **$i = 2$** (`4`):
        *   $j = 0$ (`3`): `nums[2] > nums[0]` $\to$ `dp[2] = max(1, dp[0] + 1) = 2`
        *   $j = 1$ (`1`): `nums[2] > nums[1]` $\to$ `dp[2] = max(2, dp[1] + 1) = 2`
    *   **$i = 3$** (`2`):
        *   $j = 0$ (`3`): `nums[3] < nums[0]` $\to$ no change.
        *   $j = 1$ (`1`): `nums[3] > nums[1]` $\to$ `dp[3] = max(1, dp[1] + 1) = 2`
        *   $j = 2$ (`4`): `nums[3] < nums[2]` $\to$ no change.

The final state of `dp` is `[1, 1, 2, 2]`. The maximum value in the array is **$2$**.

#### Python Code
```python
def length_of_lis(nums: list[int]) -> int:
    if not nums:
        return 0
        
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)
```

---

## 5 Interview Questions with Answers

### Q1. What is the key difference between Dynamic Programming and Divide and Conquer?
**Answer:**  
The key difference lies in the **independence of the subproblems**.
*   **Divide and Conquer** partitions a problem into *independent (non-overlapping)* subproblems, solves them recursively, and combines their solutions. There is no sharing of state between recursive branches (e.g., Merge Sort, Quick Sort).
*   **Dynamic Programming** is applied when the subproblems are *overlapping*. It solves each common subproblem once and saves its result in a lookup table, preventing redundant work.

---

### Q2. How do you identify if a problem can be solved using Dynamic Programming?
**Answer:**  
A problem is likely solvable using DP if it meets the following criteria:
1.  **Optimization Language:** The problem asks for the *minimum*, *maximum*, *longest*, *shortest*, or *total number of ways* to achieve a target.
2.  **Optimal Substructure:** You can express the solution to a larger problem as a mathematical function of solutions to smaller subproblems.
3.  **Overlapping Subproblems:** If you trace a naive recursive solution on a small input, you notice the same function signature being called multiple times with identical arguments.

---

### Q3. Explain the concept of 'State Dimension Reduction' in Dynamic Programming with an example.
**Answer:**  
State Dimension Reduction (or space optimization) is a optimization technique used to reduce the memory footprint of a DP algorithm. 

If a transition relation for a state only depends on elements in its immediate vicinity (e.g., the current row in a 2D table only depends on values in the previous row), we do not need to keep the entire historical table in memory. 

For example, in the **0/1 Knapsack Problem**, the transition is:
$$dp[i][w] = \max(dp[i-1][w], \text{val} + dp[i-1][w - \text{wt}])$$
Because row $i$ depends *only* on row $i-1$, we can discard all rows before $i-1$. By iterating backward through the weight capacities, we can compress the 2D matrix of size $O(N \times W)$ into a single 1D array of size $O(W)$, reducing the space complexity significantly while keeping the time complexity the same.

---

### Q4. What is the 'Matrix Chain Multiplication' (MCM) problem, and why is its recurrence relation unique?
**Answer:**  
The Matrix Chain Multiplication problem asks for the most efficient way to multiply a given sequence of matrices. The goal is to find the multiplication order that minimizes the total number of scalar multiplications required.

It is a classic example of **Interval/Range DP**. Its recurrence relation is unique because it defines states based on subsections or intervals of the input array:
$$dp[i][j] = \min_{i \le k < j} \Big( dp[i][k] + dp[k+1][j] + (\text{row\_dim}[i] \times \text{col\_dim}[k] \times \text{col\_dim}[j]) \Big)$$
Here, we iterate a splitting coordinate $k$ across the range $[i, j]$ to find the optimal division point. This results in an $O(N^3)$ time complexity because we have $O(N^2)$ states, and calculating each state requires an $O(N)$ sweep.

---

### Q5. What is Bitmask Dynamic Programming? Give an example of a problem where it is used.
**Answer:**  
Bitmask DP is a technique that uses a bitmask (an integer whose binary representation represents a set of boolean states) as a parameter in the DP state. This is useful for NP-hard problems where we need to keep track of a subset of visited or selected elements, typically when $N \le 20$.

A classic example is the **Traveling Salesperson Problem (TSP)**. 
Let the state be $dp[\text{mask}][u]$, representing the minimum cost to visit all nodes represented by the set bits in `mask`, ending at node $u$. 
The state transition is:
$$dp[\text{mask}][u] = \min_{v \in \text{neighbors}(u), \text{ bit } v \text{ is set in mask}} \Big( dp[\text{mask} \setminus \{u\}][v] + \text{cost}(v, u) \Big)$$
This reduces the computational complexity of TSP from $O(N!)$ to $O(2^N \cdot N^2)$.

---

## Common Mistakes

1.  **Omitting Base Cases:** Neglecting to define base cases (such as $dp[0] = 0$) or boundary checks can lead to infinite recursion stack overflows (in Memoization) or Out-of-Bounds index exceptions (in Tabulation).
2.  **Passing the Memoization Cache by Value:** In languages like C++, passing the DP array or cache to recursive helper functions by value (e.g., `helper(vector<int> memo)`) creates a copy of the structure with each function call. This turns an $O(N)$ algorithm back into an exponential-time algorithm. Always pass by reference (`vector<int>& memo`).
3.  **Using Incorrect Placeholder Values:** Initializing a memoization array with `0` when `0` is a valid computed result can cause the algorithm to repeatedly recompute states, thinking they haven't been visited yet. Use distinct sentinels like `-1` or `Integer.MIN_VALUE`.
4.  **Incorrect Order of Loops in Bottom-Up Tabulation:** If you fill a DP table in an order that violates its dependencies (e.g., trying to calculate $dp[i]$ before $dp[i-1]$ has been populated), you will use uninitialized or stale data. Always trace the dependency graph of your recurrence relation first.
5.  **Confusing DP with Greedy Strategies:** Assuming a greedy choice (such as choosing the largest denomination first in the Coin Change problem) will yield an optimal result. A greedy strategy is often faster but does not guarantee global optimality for all inputs. Always verify if the problem has optimal substructure before using a greedy approach.

---

## Summary

Dynamic Programming is a powerful algorithmic paradigm used to solve complex optimization problems by breaking them down into simpler, overlapping subproblems. By storing the results of these subproblems, it avoids redundant computations and provides massive performance improvements over naive recursive approaches.

### Key Takeaways
*   **Two Core Prerequisites:** A problem must exhibit **Overlapping Subproblems** and **Optimal Substructure** to be solvable using DP.
*   **Two Core Approaches:** 
    *   **Top-Down (Memoization):** Uses recursion and a lookup cache.
    *   **Bottom-Up (Tabulation):** Uses iterative loops to fill a table from the base cases up.
*   **Space Optimization:** Many 2D DP formulations can be optimized to 1D arrays (or even variables) because states often only depend on their immediate predecessors.
*   **Versatility:** DP is widely used in real-world applications, including network routing, bioinformatics, financial planning, and text processing.