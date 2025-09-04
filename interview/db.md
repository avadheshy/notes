# Database Query Optimization Cheat Sheet

## 🔹 General Best Practices
- **Use Indexes Effectively**  
  Speed up retrieval with proper indexes, but avoid over-indexing (slows writes).  
- **Choose Appropriate Data Types**  
  Smaller, precise types = faster storage, comparisons, and less overhead.  
- **Normalize Tables**  
  Reduce redundancy for write efficiency; denormalize selectively for reads.  
- **Partitioning & Sharding**  
  Split large datasets by range, hash, or key for scalability.

---

## 🔹 Query Writing Tips
- **Select Only Needed Columns**  
  Avoid `SELECT *`, fetch only required fields.  
- **Use EXISTS Instead of IN**  
  More efficient for subqueries.  
- **Prefer UNION ALL Over UNION**  
  UNION ALL skips duplicate elimination = faster.  
- **Avoid SELECT DISTINCT**  
  Ensure uniqueness via schema/index design.  
- **Avoid OR Conditions**  
  Replace with `UNION` or `IN` where possible.  
- **Limit Use of Subqueries**  
  Prefer joins or CTEs (common table expressions).  
- **Minimize Wildcards**  
  Use `LIKE 'abc%'` instead of `LIKE '%abc%'`.

---

## 🔹 Joins & Aggregations
- **Refine JOIN Operations**  
  Index join keys, avoid unnecessary joins.  
- **Optimize ORDER BY / GROUP BY**  
  Use indexes to support sorting and grouping.  
- **Avoid Unnecessary Calculations**  
  Precompute or handle in application layer if possible.  
- **Optimize Temporary Tables**  
  Use when beneficial, but avoid excessive temp table creation.  

---

## 🔹 Pagination & Result Sets
- **Use LIMIT (Keyset Pagination over OFFSET)**  
  Example:  
  ```sql
  SELECT * FROM orders WHERE id > 1000 ORDER BY id LIMIT 50;
