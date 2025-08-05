#  Segment Tree - LeetCode Prep

Segment Tree is a powerful data structure used to perform efficient range queries and updates in logarithmic time.

---

##  When to Use

Use Segment Tree when:
- You have an array
- You need to **query a range** (e.g., sum, min, max, GCD, etc.)
- You need to **update** values (single or range)

---

##  Basic Idea

- It's a binary tree where each node represents a segment `[start, end]` of the array.
- Leaf nodes store individual elements.
- Internal nodes store the result of a function (e.g., sum, min) over a segment.

---

##  Segment Tree Template (Range Sum Query)

```python
class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, node, l, r):
        if l == r:
            self.tree[node] = nums[l]
        else:
            mid = (l + r) // 2
            self.build(nums, 2 * node + 1, l, mid)
            self.build(nums, 2 * node + 2, mid + 1, r)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, index, val, node=0, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            self.tree[node] = val
        else:
            mid = (l + r) // 2
            if index <= mid:
                self.update(index, val, 2 * node + 1, l, mid)
            else:
                self.update(index, val, 2 * node + 2, mid + 1, r)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, i, j, node=0, l=0, r=None):
        if r is None:
            r = self.n - 1
        if j < l or i > r:
            return 0  # no overlap
        if i <= l and r <= j:
            return self.tree[node]  # total overlap
        mid = (l + r) // 2
        return self.query(i, j, 2 * node + 1, l, mid) + \
               self.query(i, j, 2 * node + 2, mid + 1, r)

# Lazy Propagation (for range updates)
class SegmentTreeLazy:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, node, l, r):
        if l == r:
            self.tree[node] = nums[l]
        else:
            mid = (l + r) // 2
            self.build(nums, 2 * node + 1, l, mid)
            self.build(nums, 2 * node + 2, mid + 1, r)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update_range(self, start, end, val, node=0, l=0, r=None):
        if r is None:
            r = self.n - 1
        if self.lazy[node] != 0:
            self.tree[node] += (r - l + 1) * self.lazy[node]
            if l != r:
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            self.lazy[node] = 0
        if end < l or start > r:
            return
        if start <= l and r <= end:
            self.tree[node] += (r - l + 1) * val
            if l != r:
                self.lazy[2 * node + 1] += val
                self.lazy[2 * node + 2] += val
            return
        mid = (l + r) // 2
        self.update_range(start, end, val, 2 * node + 1, l, mid)
        self.update_range(start, end, val, 2 * node + 2, mid + 1, r)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query_range(self, start, end, node=0, l=0, r=None):
        if r is None:
            r = self.n - 1
        if self.lazy[node] != 0:
            self.tree[node] += (r - l + 1) * self.lazy[node]
            if l != r:
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            self.lazy[node] = 0
        if end < l or start > r:
            return 0
        if start <= l and r <= end:
            return self.tree[node]
        mid = (l + r) // 2
        return self.query_range(start, end, 2 * node + 1, l, mid) + \
               self.query_range(start, end, 2 * node + 2, mid + 1, r)


#  Segment Tree - LeetCode Core Questions

Segment Trees are used for efficient range queries and updates. Below are 4 handpicked problems to master Segment Trees on LeetCode.

---

##  1. [307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)

**Type:** Point Update + Range Sum Query  
**Description:**  
Implement a mutable array with support for updating an element and calculating the range sum efficiently.

 Use basic segment tree template for sum  
 Operations: `update(index, val)` and `sumRange(left, right)`

---

##  2. [715. Range Module](https://leetcode.com/problems/range-module/)

**Type:** Range Update + Range Query  
**Description:**  
Design a data structure to add/remove/query ranges.

 Use Segment Tree with Lazy Propagation  
Supports operations like `addRange`, `removeRange`, `queryRange`

---

##  3. [699. Falling Squares](https://leetcode.com/problems/falling-squares/)

**Type:** Range Max Query + Range Update  
**Description:**  
Each square falls and stacks on the highest point in its range.

Requires Coordinate Compression  
Use segment tree for tracking max heights in a range

---

##  4. [732. My Calendar III](https://leetcode.com/problems/my-calendar-iii/)

**Type:** Range Count / Max Overlap  
**Description:**  
Track the maximum number of overlapping events.

Use Segment Tree with Lazy Propagation  
Each booking increases a count over a range

---

##  Summary

| Problem | Key Operation | Difficulty |
|--------|----------------|------------|
| 307 | Point Update + Range Sum | Medium |
| 715 | Range Update + Query | Hard |
| 699 | Range Max Update/Query | Hard |
| 732 | Range Count / Max | Hard |

Segment Tree skills are essential for range-based queries in coding interviews and contests.

