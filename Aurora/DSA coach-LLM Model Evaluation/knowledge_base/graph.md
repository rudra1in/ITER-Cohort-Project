# Graph

---

## Definition

A **Graph** is a non-linear data structure consisting of a finite set of vertices (or nodes) and a set of edges that connect these vertices. 

Mathematically, a graph is defined as an ordered pair $G = (V, E)$, where:
*   $V$ is a set of vertices: $V = \{v_1, v_2, v_3, \dots, v_n\}$
*   $E$ is a set of edges: $E = \{e_1, e_2, e_3, \dots, e_m\}$, where each edge $e_i$ is a pair $(u, v)$ such that $u, v \in V$.

```
    (A) ----------- (B)
     |             / |
     |           /   |
     |         /     |
     |       /       |
    (C) ----------- (D)
```
*In the graph above:*
*   **Vertices ($V$):** $\{A, B, C, D\}$
*   **Edges ($E$):** $\{(A, B), (A, C), (B, C), (B, D), (C, D)\}$

---

## Why it is needed

Linear data structures (like arrays, linked lists, stacks, and queues) and hierarchical data structures (like trees) are insufficient for representing complex, many-to-many relationships. 

Graphs are needed to:
1.  **Model Complex Networks:** Real-world networks like social networks (friends connected to friends), telecommunication networks, and electrical grids do not have a single root or a sequential flow.
2.  **Solve Optimization Problems:** Finding the shortest path between two cities, optimizing shipping routes, or determining the least cost to connect multiple locations (Minimum Spanning Tree) requires graph representation.
3.  **Represent Dependencies:** Task scheduling, compiler build dependencies (like Makefiles), and package installations require representing directed dependencies, which can only be done using Directed Acyclic Graphs (DAGs).

---

## Characteristics

1.  **Degree of a Vertex:**
    *   **In-degree:** The number of edges coming into a vertex (relevant in directed graphs).
    *   **Out-degree:** The number of edges going out of a vertex (relevant in directed graphs).
    *   **Degree (Undirected):** The total number of edges connected to a vertex.
2.  **Path:** A sequence of alternating vertices and edges starting at a vertex and ending at another, where no edge is repeated.
3.  **Cycle:** A closed path where the start vertex and end vertex are the same, and no other vertices are repeated.
4.  **Connectivity:** A graph is connected if there is a path between every pair of vertices.
5.  **Density:** 
    *   **Sparse Graph:** A graph with relatively few edges (close to $|E| \approx |V|$).
    *   **Dense Graph:** A graph with close to the maximum possible number of edges ($|E| \approx |V|^2$).
6.  **Self-loop:** An edge that connects a vertex to itself.
7.  **Parallel Edges (Multi-edges):** Multiple edges between the same pair of vertices.

---

## Working

A graph works by storing entities (vertices) and their associations (edges). Algorithms traverse these networks by moving from vertex to vertex along the connecting edges.

To prevent infinite loops during traversal (especially since graphs can have cycles), algorithms maintain a auxiliary state—typically a **visited set or array**. 

```
Traversal Workflow:
[Start Node] ---> [Check Neighbors] ---> [Filter Unvisited] ---> [Enqueue/Push] ---> [Mark Visited]
```

When traversing:
1.  Start at a given source vertex.
2.  Mark the vertex as "visited".
3.  Explore its adjacent neighbors.
4.  For each unvisited neighbor, recursively or iteratively repeat the process depending on the strategy (Breadth-First Search or Depth-First Search).

---

## Memory Representation

There are two primary ways to represent a graph in memory:

### 1. Adjacency Matrix
An Adjacency Matrix is a 2D array of size $V \times V$ where $V$ is the number of vertices. A slot `matrix[i][j]` is 1 (or the edge weight) if there is an edge from vertex $i$ to vertex $j$, and 0 otherwise.

#### Visual Representation:
For the graph:
```
  (0) ---- (1)
   |      /
   |    /
  (2) 
```

**Matrix:**
```
     0  1  2
  0 [0, 1, 1]
  1 [1, 0, 1]
  2 [1, 1, 0]
```

*   **Pros:** Finding if an edge exists between $u$ and $v$ is extremely fast ($O(1)$).
*   **Cons:** Consumes $O(V^2)$ memory, which is highly inefficient for sparse graphs.

---

### 2. Adjacency List
An Adjacency List is an array of lists (or dynamic arrays/linked lists). The size of the array is equal to the number of vertices $V$. Each index `i` in the array contains a list of all vertices adjacent to vertex `i`.

#### Visual Representation:
For the same graph above:
```
  0 -> [1, 2]
  1 -> [0, 2]
  2 -> [0, 1]
```

*   **Pros:** Space-efficient ($O(V + E)$). Highly preferred for sparse graphs.
*   **Cons:** Checking if an edge exists between $u$ and $v$ requires traversing the list of $u$, taking $O(\text{degree}(u))$ time.

---

## Types

| Type | Description | Visual Example |
| :--- | :--- | :--- |
| **Undirected Graph** | Edges have no direction. If edge $(A, B)$ exists, you can travel $A \to B$ and $B \to A$. | `A <---> B` |
| **Directed Graph (Digraph)** | Edges have arrows indicating direction. Travel is only allowed in the direction of the arrow. | `A ----> B` |
| **Weighted Graph** | Each edge has a numerical cost or weight associated with it (e.g., distance, cost, time). | `A --(5)--> B` |
| **Unweighted Graph** | All edges are treated equally; no weights are assigned. | `A ----> B` |
| **Cyclic Graph** | Contains at least one cycle (a path starting and ending at the same node). | `A -> B -> C -> A` |
| **Directed Acyclic Graph (DAG)**| A directed graph with absolutely no cycles. Crucial for scheduling tasks. | `A -> B -> C` |
| **Bipartite Graph** | A graph whose vertices can be divided into two independent sets $U$ and $V$ such that every edge connects a vertex in $U$ to one in $V$. | `U1 - V1`, `U2 - V2` |
| **Complete Graph** | Every vertex is connected directly to every other vertex. | A triangle or clique |

---

## Operations

### 1. `addVertex(v)`
Adds a new vertex `v` to the graph.
*   **Adjacency List:** Adds a new entry/key to the map or array.
*   **Adjacency Matrix:** Resizes the 2D array to $(V+1) \times (V+1)$.

### 2. `addEdge(u, v)`
Connects vertex `u` and vertex `v`.
*   **Example (Undirected):** Add `v` to `u`'s list, and add `u` to `v``s list.

### 3. `removeEdge(u, v)`
Removes the connection between `u` and `v`.
*   **Example:** Remove `v` from `u`'s adjacency list, and `u` from `v`'s list.

### 4. `removeVertex(v)`
Removes vertex `v` and all edges connected to it.
*   **Example:** Delete the vertex `v` list, and search all other vertices' lists to remove references to `v`.

### 5. `BFS(start_vertex)` (Breadth-First Search)
Traverses the graph level-by-level starting from a source vertex. Uses a **Queue** data structure.

```
Queue: [Start]
While Queue is not empty:
  Pop node 'current' from front.
  For neighbor in neighbors(current):
    If neighbor not visited:
      Mark visited
      Push neighbor to Queue
```

### 6. `DFS(start_vertex)` (Depth-First Search)
Traverses the graph by going as deep as possible along each branch before backtracking. Uses a **Stack** (or recursion).

```
Stack: [Start]
While Stack is not empty:
  Pop node 'current' from top.
  If current not visited:
    Mark visited
    For neighbor in neighbors(current) in reverse order:
      Push neighbor to Stack
```

---

## Time Complexity Table

| Operation | Adjacency Matrix | Adjacency List |
| :--- | :--- | :--- |
| **Add Vertex** | $O(V^2)$ (due to matrix resizing) | $O(1)$ |
| **Add Edge** | $O(1)$ | $O(1)$ |
| **Remove Vertex** | $O(V^2)$ | $O(V + E)$ |
| **Remove Edge** | $O(1)$ | $O(V)$ (or $O(1)$ if using Hash Sets) |
| **Query Edge $(u, v)$** | $O(1)$ | $O(\text{degree}(u))$ |
| **BFS Traversal** | $O(V^2)$ | $O(V + E)$ |
| **DFS Traversal** | $O(V^2)$ | $O(V + E)$ |

---

## Space Complexity

*   **Adjacency Matrix:** $O(V^2)$
    *   *Explanation:* Requires a $V \times V$ matrix regardless of the number of edges.
*   **Adjacency List:** $O(V + E)$
    *   *Explanation:* Stores $V$ vertex array pointers and a total of $E$ edge nodes (or $2E$ for undirected graphs).

---

## Advantages

1.  **Natural Representation:** Perfectly captures complex relational architectures (e.g., network typologies, molecular structures).
2.  **Highly Versatile:** Can model symmetric (undirected) and asymmetric (directed) relationships.
3.  **Powerful Algorithms:** Benefit from well-established pathfinding and flow algorithms (Dijkstra, A*, Floyd-Warshall, Prim's, Kruskal's).

---

## Disadvantages

1.  **High Memory Overhead:** Adjacency matrices consume vast space for sparse graphs. Adjacency lists have overhead associated with linked lists or dynamic arrays (pointers/references).
2.  **Implementation Complexity:** Graphs are significantly harder to implement, debug, and optimize compared to linear data structures or binary search trees.
3.  **Query Overhead:** Finding if a specific edge exists in an adjacency list takes linear time in terms of the degree of the node.

---

## Real World Applications

1.  **Social Networks:** Suggesting friends on LinkedIn or Facebook (vertices are users, edges are connections/friendships).
2.  **Google Maps / GPS:** Vertices are intersections, edges are roads. Edge weights represent physical distance or real-time traffic delay.
3.  **Web Crawling and Search Engines:** Pages are vertices; hyperlinks are directed edges. PageRank algorithm determines the importance of a vertex based on incoming links.
4.  **Recommendation Engines:** Amazon or Netflix uses bipartite graph models to map users to products they purchase/view to recommend items bought by similar users.
5.  **Git Version Control:** Commits form a Directed Acyclic Graph (DAG) where child commits point to parent commits.

---

## Python Implementation

This implementation represents an **Adjacency List-based Graph** supporting directed/undirected configurations, edge/vertex additions, and both BFS and DFS traversals.

```python
from collections import deque

class Graph:
    def __init__(self, directed=False):
        # Using a dictionary to map vertices to their set of neighbors
        self.adj_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        """Adds a vertex to the graph if it doesn't already exist."""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = set()

    def add_edge(self, u, v):
        """Adds an edge between vertex u and vertex v."""
        self.add_vertex(u)
        self.add_vertex(v)
        
        self.adj_list[u].add(v)
        if not self.directed:
            self.adj_list[v].add(u)

    def remove_edge(self, u, v):
        """Removes the edge between vertex u and vertex v."""
        if u in self.adj_list and v in self.adj_list[u]:
            self.adj_list[u].remove(v)
        if not self.directed:
            if v in self.adj_list and u in self.adj_list[v]:
                self.adj_list[v].remove(u)

    def remove_vertex(self, vertex):
        """Removes vertex and all edges associated with it."""
        if vertex in self.adj_list:
            # Remove all incoming edges pointing to this vertex
            for other_vertex in list(self.adj_list):
                if vertex in self.adj_list[other_vertex]:
                    self.adj_list[other_vertex].remove(vertex)
            # Remove the vertex mapping itself
            del self.adj_list[vertex]

    def bfs(self, start_vertex):
        """Breadth-First Search traversal."""
        if start_vertex not in self.adj_list:
            return []

        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        result = []

        while queue:
            current = queue.popleft()
            result.append(current)

            for neighbor in sorted(self.adj_list[current]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start_vertex):
        """Depth-First Search traversal (Iterative)."""
        if start_vertex not in self.adj_list:
            return []

        visited = set()
        stack = [start_vertex]
        result = []

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                result.append(current)
                # Sort in reverse order to explore smaller-valued nodes first
                for neighbor in sorted(self.adj_list[current], reverse=True):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

# Demonstration
if __name__ == "__main__":
    g = Graph(directed=False)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)

    print("BFS starting from 0:", g.bfs(0))  # Expected: [0, 1, 2, 3, 4]
    print("DFS starting from 0:", g.dfs(0))  # Expected: [0, 1, 3, 4, 2]
```

---

## C++ Implementation

```cpp
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>

class Graph {
private:
    std::unordered_map<int, std::unordered_set<int>> adjList;
    bool directed;

public:
    Graph(bool isDirected = false) : directed(isDirected) {}

    void addVertex(int v) {
        if (adjList.find(v) == adjList.end()) {
            adjList[v] = std::unordered_set<int>();
        }
    }

    void addEdge(int u, int v) {
        addVertex(u);
        addVertex(v);
        adjList[u].insert(v);
        if (!directed) {
            adjList[v].insert(u);
        }
    }

    void removeEdge(int u, int v) {
        if (adjList.find(u) != adjList.end()) {
            adjList[u].erase(v);
        }
        if (!directed) {
            if (adjList.find(v) != adjList.end()) {
                adjList[v].erase(u);
            }
        }
    }

    void removeVertex(int v) {
        if (adjList.find(v) == adjList.end()) return;
        
        // Remove incoming connections
        for (auto& pair : adjList) {
            pair.second.erase(v);
        }
        adjList.erase(v);
    }

    std::vector<int> bfs(int startVertex) {
        std::vector<int> result;
        if (adjList.find(startVertex) == adjList.end()) return result;

        std::unordered_set<int> visited;
        std::queue<int> q;

        q.push(startVertex);
        visited.insert(startVertex);

        while (!q.empty()) {
            int current = q.front();
            q.pop();
            result.push_back(current);

            // Sort neighbors for deterministic execution order
            std::vector<int> neighbors(adjList[current].begin(), adjList[current].end());
            std::sort(neighbors.begin(), neighbors.end());

            for (int neighbor : neighbors) {
                if (visited.find(neighbor) == visited.end()) {
                    visited.insert(neighbor);
                    q.push(neighbor);
                }
            }
        }
        return result;
    }

    std::vector<int> dfs(int startVertex) {
        std::vector<int> result;
        if (adjList.find(startVertex) == adjList.end()) return result;

        std::unordered_set<int> visited;
        std::stack<int> s;

        s.push(startVertex);

        while (!s.empty()) {
            int current = s.top();
            s.pop();

            if (visited.find(current) == visited.end()) {
                visited.insert(current);
                result.push_back(current);

                std::vector<int> neighbors(adjList[current].begin(), adjList[current].end());
                std::sort(neighbors.begin(), neighbors.end(), std::greater<int>());

                for (int neighbor : neighbors) {
                    if (visited.find(neighbor) == visited.end()) {
                        s.push(neighbor);
                    }
                }
            }
        }
        return result;
    }
};

int main() {
    Graph g(false);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 4);
    g.addEdge(3, 4);

    std::cout << "BFS starting from 0: ";
    for (int node : g.bfs(0)) std::cout << node << " ";
    std::cout << "\n";

    std::cout << "DFS starting from 0: ";
    for (int node : g.dfs(0)) std::cout << node << " ";
    std::cout << "\n";

    return 0;
}
```

---

## Java Implementation

```java
import java.util.*;

public class Graph {
    private final Map<Integer, Set<Integer>> adjList;
    private final boolean directed;

    public Graph(boolean directed) {
        this.adjList = new HashMap<>();
        this.directed = directed;
    }

    public void addVertex(int v) {
        adjList.putIfAbsent(v, new HashSet<>());
    }

    public void addEdge(int u, int v) {
        addVertex(u);
        addVertex(v);
        adjList.get(u).add(v);
        if (!directed) {
            adjList.get(v).add(u);
        }
    }

    public void removeEdge(int u, int v) {
        if (adjList.containsKey(u)) {
            adjList.get(u).remove(v);
        }
        if (!directed) {
            if (adjList.containsKey(v)) {
                adjList.get(v).remove(u);
            }
        }
    }

    public void removeVertex(int v) {
        if (!adjList.containsKey(v)) return;
        
        for (Integer other : adjList.keySet()) {
            adjList.get(other).remove(v);
        }
        adjList.remove(v);
    }

    public List<Integer> bfs(int startVertex) {
        List<Integer> result = new ArrayList<>();
        if (!adjList.containsKey(startVertex)) return result;

        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();

        queue.add(startVertex);
        visited.add(startVertex);

        while (!queue.isEmpty()) {
            int current = queue.poll();
            result.add(current);

            List<Integer> sortedNeighbors = new ArrayList<>(adjList.get(current));
            Collections.sort(sortedNeighbors);

            for (int neighbor : sortedNeighbors) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.add(neighbor);
                }
            }
        }
        return result;
    }

    public List<Integer> dfs(int startVertex) {
        List<Integer> result = new ArrayList<>();
        if (!adjList.containsKey(startVertex)) return result;

        Set<Integer> visited = new HashSet<>();
        Stack<Integer> stack = new Stack<>();

        stack.push(startVertex);

        while (!stack.isEmpty()) {
            int current = stack.pop();

            if (!visited.contains(current)) {
                visited.add(current);
                result.add(current);

                List<Integer> sortedNeighbors = new ArrayList<>(adjList.get(current));
                sortedNeighbors.sort(Collections.reverseOrder());

                for (int neighbor : sortedNeighbors) {
                    if (!visited.contains(neighbor)) {
                        stack.push(neighbor);
                    }
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Graph g = new Graph(false);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 3);
        g.addEdge(2, 4);
        g.addEdge(3, 4);

        System.out.println("BFS starting from 0: " + g.bfs(0));
        System.out.println("DFS starting from 0: " + g.dfs(0));
    }
}
```

---

## 3 Solved Examples

### Example 1: Find if Path Exists in Graph
**Problem Statement:** Given a directed graph, find if there is a path from a given source vertex to a destination vertex.

```
Graph:
(0) ----> (1) ----> (2)
 |                   ^
 |                   |
 v                   |
(3) -----------------+
```
**Inputs:** `Source = 0`, `Destination = 2`

#### Step-by-Step Execution (Using BFS):
1.  Initialize empty `visited` set and a queue: `queue = [0]`, `visited = {0}`.
2.  De-queue `0`. It is not the destination.
    *   Find neighbors of `0`: `[1, 3]`.
    *   Add to queue and mark visited: `queue = [1, 3]`, `visited = {0, 1, 3}`.
3.  De-queue `1`. It is not the destination.
    *   Find neighbors of `1`: `[2]`.
    *   Add to queue and mark visited: `queue = [3, 2]`, `visited = {0, 1, 2, 3}`.
4.  De-queue `3`. It is not the destination.
    *   Find neighbors of `3`: `[2]`. `2` is already visited. No action.
5.  De-queue `2`. This matches the destination. Return **True**.

---

### Example 2: Cycle Detection in an Undirected Graph
**Problem Statement:** Detect if a cycle exists in the given undirected graph.

```
Graph:
(0) ---- (1)
 |      /
 |    /
(2) 
```

#### Step-by-Step Execution (Using DFS with parent tracking):
We need to track the parent of the node we came from. If we encounter a visited node that is **not** the parent of the current node, a cycle exists.

1.  Start DFS from `0`. Mark `0` as visited. Parent of `0` is `null`.
2.  Move to neighbor of `0`: Node `1`. Mark `1` as visited. Parent of `1` is `0`.
3.  Move to neighbor of `1`: Node `2`. Mark `2` as visited. Parent of `2` is `1`.
4.  Check neighbors of `2`:
    *   `0`: It is already visited. Is `0` the parent of `2`? No (parent is `1`).
    *   Since we visited `0` through a path not immediately leading back to its parent, a cycle is detected. Return **True**.

---

### Example 3: Dijkstra's Shortest Path Algorithm
**Problem Statement:** Find the shortest path from vertex `A` to all other vertices in a weighted graph.

```
Graph:
      [2]
 (A) ---- (B)
  |      / |
 [4]   [1] [7]
  |    /   |
 (C) ---- (D)
      [3]
```

#### Step-by-Step Execution:
1.  **Initialize:** Distances table: `A: 0`, `B: inf`, `C: inf`, `D: inf`. Priority Queue (Min-Heap): `{(0, A)}`.
2.  Pop closest element: `A` (dist: `0`).
    *   Check neighbor `B`: New dist = $0 + 2 = 2$. Update `B: 2`. Push `(2, B)`.
    *   Check neighbor `C`: New dist = $0 + 4 = 4$. Update `C: 4`. Push `(4, C)`.
    *   *Distance state:* `A:0, B:2, C:4, D:inf`
3.  Pop closest element: `B` (dist: `2`).
    *   Check neighbor `C`: New dist = $2 + 1 = 3$. $3 < 4$. Update `C: 3`. Push `(3, C)`.
    *   Check neighbor `D`: New dist = $2 + 7 = 9$. Update `D: 9`. Push `(9, D)`.
    *   *Distance state:* `A:0, B:2, C:3, D:9`
4.  Pop closest element: `C` (dist: `3`).
    *   Check neighbor `D`: New dist = $3 + 3 = 6$. $6 < 9$. Update `D: 6`. Push `(6, D)`.
    *   *Distance state:* `A:0, B:2, C:3, D:6`
5.  Pop closest element: `D` (dist: `6`). All paths resolved.
6.  **Final Result:** Shortest path distances from `A`:
    *   `A` $\to$ `A`: 0
    *   `A` $\to$ `B`: 2
    *   `A` $\to$ `C`: 3
    *   `A` $\to$ `D`: 6

---

## 5 Interview Questions with Answers

### Q1. What is the difference between DFS and BFS? When should you use which?
*   **BFS (Breadth-First Search)** explores neighbors level-by-level using a **Queue**. It guarantees finding the shortest path in terms of edge count in unweighted graphs.
    *   *Use-case:* Shortest path in unweighted graphs, finding closest friends/nodes.
*   **DFS (Depth-First Search)** goes down a single branch as deeply as possible before backtracking, using a **Stack** or recursion.
    *   *Use-case:* Topological sorting, cycle detection, finding strongly connected components, or solving puzzles (like mazes) where we must traverse to completion before trying options.

### Q2. What is topological sorting, and can it be done on any graph?
**Topological Sort** is a linear ordering of vertices in a directed graph such that for every directed edge $u \to v$, vertex $u$ comes before $v$ in the ordering.
*   It is **only** possible on **Directed Acyclic Graphs (DAGs)**.
*   If the graph has a cycle, topological sorting is impossible because dependencies would resolve in circles ($A$ depends on $B$, $B$ depends on $C$, $C$ depends on $A$).

### Q3. How do you detect a cycle in a Directed Graph?
Unlike undirected graphs, we cannot simply use the parent-node tracking trick. We must keep track of nodes currently in the **active recursion stack** (or processing path).
*   Use three states for each vertex:
    1.  **Unvisited (0):** Node has not been touched yet.
    2.  **Visiting (1):** Node is in the current DFS path.
    3.  **Visited (2):** Node and all its descendants have been fully processed.
*   If during DFS exploration of a neighbor, we encounter a node in state **Visiting (1)**, we have detected a back-edge, which means a cycle exists.

### Q4. Explain the difference between Kruskal’s and Prim’s algorithms.
Both algorithms find the **Minimum Spanning Tree (MST)** of a connected, weighted graph, but they work differently:
*   **Kruskal’s Algorithm:** An edge-centric greedy algorithm. It sorts all edges in ascending order of weight and adds them to the MST one by one, using a **Disjoint-Set (Union-Find)** data structure to ensure no cycles are created.
*   **Prim’s Algorithm:** A vertex-centric greedy algorithm. It starts from an arbitrary node and grows the tree by continuously picking the minimum-weight edge that connects a vertex in the tree to a vertex outside the tree using a **Min-Heap**.

### Q5. What is a "Bridge" in a graph, and how do you find one?
A **Bridge** (or cut-edge) is an edge in a graph whose removal increases the number of connected components (i.e., it disconnects the graph).
*   Bridges can be found in $O(V + E)$ time using **Tarjan's Algorithm** (based on DFS).
*   During DFS, we track the discovery time of each node and the lowest discovery time reachable from that node (`low` value). An edge $u \to v$ is a bridge if and only if the lowest reachable node from $v$ can only be reached after $u$ was discovered: `low[v] > disc[u]`.

---

## Common Mistakes

1.  **Infinite Loops due to Unmarked Visited Nodes:**
    *   Because graphs can contain cycles, failing to mark nodes as "visited" immediately when putting them in a traversal queue or stack will lead to infinite recursion or memory exhaustion.
2.  **Confusing Directed vs. Undirected Edges:**
    *   When constructing an adjacency list for an undirected graph, developers often add the edge only once (`adj[u].append(v)`), forgetting that undirected edges must be stored symmetrically (`adj[v].append(u)`).
3.  **Using Adjacency Matrix for Sparse Graphs:**
    *   Using a $V \times V$ matrix when $V = 10^5$ and $E = 10^5$ is a critical mistake. It consumes $10^{10}$ integers ($\approx 40$ GB RAM), whereas an adjacency list would use negligible memory.
4.  **Inefficient Edge Existence Queries:**
    *   If your code frequently checks if an edge $(u, v)$ exists, using a naive adjacency list of type `Map<Integer, List<Integer>>` requires scanning the entire list of $u$ ($O(V)$ in worst case). For constant-time edge queries, use a set instead: `Map<Integer, Set<Integer>>`.

---

## Summary

*   A **Graph** is a non-linear data structure modeling relationships among entities via nodes (vertices) and connections (edges).
*   **Adjacency Lists** are space efficient ($O(V + E)$) and preferred for sparse graphs, while **Adjacency Matrices** are space-heavy ($O(V^2)$) but allow $O(1)$ edge-existence checks.
*   **Breadth-First Search (BFS)** uses a queue, traversing level-by-level, finding shortest paths in unweighted graphs.
*   **Depth-First Search (DFS)** uses stack/recursion to go deep, which is ideal for cycle detection, topological sorting, and connectivity checks.
*   Graphs are critical to modern applications including social networking connection maps, routing algorithms, game pathfinding, and compiler optimization.