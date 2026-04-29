# B-Tree: Structure and Operations

A **B-Tree of order _m_** is a balanced multi-way search tree optimized for reading and writing large data blocks. It builds upon all the features of an M-Way tree and adds additional rules to ensure balance and performance.

---

## 📘 Key Features of B-Tree (Order _m_)

- A B-Tree of order `m` can have **a maximum of `m` children** per node.
- **Each node** (except the root and leaves) must have **at least ⌈m/2⌉ children**.
- The **root node** must have at least **two children** (if it is not a leaf).
- **All leaf nodes must appear at the same level** — ensuring the tree remains balanced.
- **Nodes are not required to have the same number of children**, but each internal node must have **at least ⌈m/2⌉ children** and **at most `m`**.
- Each node with `k` children will have `k-1` keys stored in sorted order.

---

## 🔄 Insertion in B-Tree

1. **Start at the root** and traverse down to the appropriate leaf.
2. **Insert** the key in sorted order in the leaf node.
3. If the leaf becomes **overfull**:
   - **Split** it into two nodes.
   - Push the middle key up to the parent node.
4. Repeat the split recursively **upwards** if needed.

---

## 📝 Update in B-Tree

- Locate the key via a **standard B-Tree search**.
- Replace the value associated with the key.
- Structure remains unchanged unless the key is replaced, in which case deletion + insertion is used.

---

## ❌ Deletion in B-Tree

1. If the key is in a **leaf**, remove it directly.
2. If the key is in an **internal node**:
   - Replace with **in-order predecessor or successor**.
   - Recursively delete that replacement key.
3. If deletion causes a node to have **too few keys**:
   - **Borrow** a key from a sibling (rotation).
   - Or **merge** with a sibling node and move a key down from the parent.
4. Continue rebalancing the tree **upward** if required.

---

## 📊 Summary

| Property                     | Description                                      |
|-----------------------------|--------------------------------------------------|
| Max Children per Node       | `m`                                              |
| Min Children per Internal   | ⌈m/2⌉                                            |
| Min Keys per Node           | ⌈m/2⌉ - 1                                        |
| Balanced Tree               | All leaves on same level                         |
| Use Cases                   | Databases, File Systems, Indexed Storage         |

---

B-Trees are fundamental to system design where balanced search, efficient insert/delete, and disk-based indexing are critical.

# B+ Tree: Structure and Operations

A **B+ Tree of order _m_** is an extension of the B-Tree where all records are stored only at the leaf level, and internal nodes are used only as a navigational index. It is commonly used in **databases** and **file systems** for efficient range queries and fast data access.

---

## 📘 Key Features of B+ Tree (Order _m_)

- A B+ Tree of order `m` has **a maximum of `m` children per internal node**.
- Each **internal (non-leaf) node** must have **at least ⌈m/2⌉ children**, except for the root.
- The **root node** must have **at least two children** if it is not a leaf.
- **All values are stored at the leaf level**, not in internal nodes.
- **All leaf nodes are linked** together in a **singly/doubly linked list** to support fast range queries.
- **All leaves must appear at the same level**, ensuring balance.
- Internal nodes **only store keys** (not actual data).

---

## 🔄 Insertion in B+ Tree

1. **Search** the appropriate **leaf node** where the new key belongs.
2. **Insert the key and value** into that leaf in sorted order.
3. If the leaf becomes **overfull**:
   - **Split** it into two leaf nodes.
   - Move the **first key of the new node** to the parent internal node.
4. If the parent also overflows, repeat the **split-and-promote** process upward recursively.

---

## 📝 Update in B+ Tree

- Find the key in the **leaf node** via index traversal.
- Update its associated value.
- The tree structure is **not affected** as only values (not keys) are updated in leaf nodes.

---

## ❌ Deletion in B+ Tree

1. **Locate and delete** the key from the appropriate **leaf node**.
2. If the leaf node **underflows** (has fewer than ⌈m/2⌉ keys):
   - **Borrow** from a sibling node if possible.
   - Or **merge** with a sibling and update the parent.
3. Update the **internal index nodes** if a promoted key is removed from the leaf.
4. Continue rebalancing **up the tree** if necessary.

---

## 📊 Summary

| Property                     | Description                                       |
|-----------------------------|---------------------------------------------------|
| Max Children per Node       | `m`                                               |
| Min Children per Internal   | ⌈m/2⌉                                             |
| Leaf Node Structure         | Stores all data and are linked in a list         |
| Internal Node Structure     | Stores keys only for routing                     |
| Range Query Efficiency      | High (thanks to linked leaves)                   |
| Use Cases                   | Databases, File systems, Indexing engines        |

---

## 🔁 Key Differences from B-Tree

- Data is **only stored in leaves**, making internal nodes smaller and faster to scan.
- Better for **range queries** because of **linked leaf nodes**.
- Slightly **taller trees**, but more **efficient indexing**.

---

The B+ Tree is a preferred choice for systems that rely heavily on disk-based data access and large-scale indexing due to its optimized structure and predictable performance.
