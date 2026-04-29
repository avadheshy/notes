# Database Concurrency & Locking Guide

This guide explains how databases manage simultaneous access to data to ensure consistency and prevent conflicts.

## 1. Understanding Concurrency
Concurrency occurs when multiple transactions attempt to access or modify the same data at the same time. Without proper controls, this can lead to:
*   **Dirty Reads**: Reading data that hasn't been committed yet.
*   **Non-repeatable Reads**: Reading the same row twice and getting different results because another transaction modified it.
*   **Phantom Reads**: New rows appearing in a result set because another transaction inserted them during your process.

## 2. Row-Level Locking
Row-level locking is the most granular form of locking. It locks only the specific rows being modified, allowing other users to work on different rows in the same table.

*   **How it Works**: When a transaction updates a row, the database places a lock on that specific record.
*   **Pros**: High concurrency; many users can edit the table simultaneously.
*   **Cons**: Higher memory overhead for the database engine to track thousands of individual locks.
*   **Common Usage**: 
    ```sql
    -- Explicitly locking a row for update in many SQL dialects
    SELECT * FROM orders WHERE order_id = 101 FOR UPDATE;
    ```

## 3. Page/Block & Table Level Locking
*   **Page Level**: Locks a "page" or "block" of data (usually 4KB or 8KB). All rows on that page are locked. This is a middle ground between row and table locking.
*   **Table Level**: Locks the entire table. One user writing prevents all others from writing to any part of that table. 
    *   *Usage*: Best for bulk data imports or schema changes.

## 4. Label-Level (Label-Based) Access Control (LBAC)
While "locking" usually refers to concurrency, **Label-Based** control refers to security and visibility at a granular level.

*   **Definition**: Data is tagged with a "security label." Users can only see or modify rows if their security credentials match the row's label.
*   **Concurrency Impact**: LBAC acts as a filter. If a user doesn't have the label to see a row, the database treats it as if it doesn't exist, preventing "Lock Contention" on data the user isn't even authorized to see.
*   **Key Components**:
    *   **Security Policies**: Rules governing how labels are applied.
    *   **User Labels**: The "clearance" level assigned to a database user.

## 5. Optimistic vs. Pessimistic Locking
*   **Pessimistic Locking**: Assumes conflict will happen. It locks the record the moment it is read, preventing anyone else from touching it until the transaction finishes.
*   **Optimistic Locking**: Assumes conflict is rare. It doesn't lock the row during the read. Instead, it checks a **version number** or **timestamp** right before saving. If the version has changed, the update fails.

## 6. Deadlocks
A deadlock occurs when Transaction A holds a lock Transaction B needs, while Transaction B holds a lock Transaction A needs.
*   **Resolution**: The database engine detects this cycle and "kills" one of the transactions (the victim) to allow the other to proceed.
*   **Prevention**: Always access tables/rows in the same consistent order across your application code.
