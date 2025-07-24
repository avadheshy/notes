# Union by Rank Patterns (with Path Compression)

##  What is Union by Rank?

Union by Rank (or Union by Size) is an optimization used with the **Disjoint Set Union (DSU)** or **Union-Find** data structure to efficiently track and merge disjoint sets.

Combined with **Path Compression**, it reduces time complexity to near constant:  
**O(α(n)) ≈ O(1)**, where α is the inverse Ackermann function.

---

##  Use Cases

- Detecting **cycles** in an undirected graph.
- Checking **connected components**.
- **Kruskal's algorithm** for Minimum Spanning Tree.
- Dynamic **connectivity queries**.
- **2D grid** problems where merging regions/cells is needed.

---

## DSU Template with Union by Rank + Path Compression

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n  # or size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False  # Already connected
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1
        return True



# Easy / Medium LeetCode Problems
- 684. Redundant Connection
- Find an edge that can be removed to make the graph a tree.

- 547. Number of Provinces
- Count the number of connected components in an adjacency matrix.

- 959. Regions Cut By Slashes
- Convert grid into graph, use DSU to count distinct regions.

- 1319. Number of Operations to Make Network Connected
- Count extra edges and components.

- 721. Accounts Merge
- Merge accounts with shared emails using DSU.

# Hard LeetCode Problems
- 990. Satisfiability of Equality Equations
- DSU to process equality and inequality constraints.

- 128. Longest Consecutive Sequence
- Can be solved with DSU (alternative to HashSet approach).

- 924. Minimize Malware Spread
I- dentify component sizes and track malware spread using DSU.

- 1135. Connecting Cities With Minimum Cost
- Kruskal's MST algorithm using Union by Rank.

