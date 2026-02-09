- Develop ability to ask good questions .
- Develop ability to defend your answer .
- Answering without a thorough understanding of the requirements is a huge red flag .





- To achive strong consistancy wait write opreations until previous operation is completed .
```
If R = 1 and W = N, the system is optimized for a fast read.

If W = 1 and R = N, the system is optimized for fast write.

If W + R > N, strong consistency is guaranteed (Usually N = 3, W = R = 2).

If W + R <= N, strong consistency is not guaranteed.
where w is write qorum R is read qorum and n is number of replicas.
```
- Inconsistancy in data can be solve using versioning and vector lock .  
-  Versioning means treating each data modification as a new immutable version of data.
-  A vector clock is a [server, version] pair associated with a data item. It can be used to check if one version precedes, succeeds, or in conflict with others.
-  heartbit is used to find system failure.

