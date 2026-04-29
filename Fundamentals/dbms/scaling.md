# Horizontal Scaling vs Vertical Scaling

| Feature | Horizontal Scaling | Vertical Scaling |
|--------|--------------------|------------------|
| **Definition** | When new server racks are added to the existing system to meet the higher expectation | When new resources are added in the existing system to meet the expectation |
| **Expansion Direction** | Expands the size of the existing system horizontally | Expands the size of the existing system vertically |
| **Upgrade Complexity** | Easier to upgrade | Harder to upgrade and may involve downtime |
| **Implementation Difficulty** | Difficult to implement | Easy to implement |
| **Cost** | Costlier, as new server racks comprise a lot of resources | Cheaper, as we need to just add new resources |
| **Time Requirement** | Takes more time to be done | Takes less time to be done |
| **Fault Tolerance** | High resilience and fault tolerance | Single point of failure |
| **Examples of Databases** | Cassandra, MongoDB, Google Cloud Spanner | MySQL, Amazon RDS |

# Indexing
What is the difference between key & index?

Although the terms key & index are used interchangeably, key means a constraint imposed on the behaviour of the column. In this case, the constraint is that primary key is non null-able field which uniquely identifies each row. On the other hand, index is a special data structure that facilitates data search across the table.