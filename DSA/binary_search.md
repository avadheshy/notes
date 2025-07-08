# Binary search templates


# Template 1: Classic Binary Search (Search Target in Sorted Array)
Use when you're searching for a specific value in a sorted array.

```
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid  # target found
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1  # target not found
```
## Problems:

- 704. Binary Search (Easy)

- 278. First Bad Version (Easy)

- 34. Find First and Last Position of Element in Sorted Array (Medium)

# Template 2: Lower Bound (First Element ≥ target)
Use when you need to find the first index such that nums[i] >= target.

```
def lower_bound(nums, target):
    left, right = 0, len(nums)
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
            
    return left
```
## Problems:
- 35. Search Insert Position (Easy)

- 300. Longest Increasing Subsequence (Medium)

- 162. Find Peak Element (Medium)
     

- 852. Peak Index in a Mountain Array (Medium)

- 1901. Find a Peak Element II (Medium)

- 287. Find the Duplicate Number (Medium - tricky binary search on value)



# Template 3: Upper Bound (First Element > target)
Use when you need the index of the first element greater than the target.

```
def upper_bound(nums, target):
    left, right = 0, len(nums)
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
            
    return left
```
## Problems:

Finding ranges/counts in sorted arrays

## Template 4: Binary Search on Answer
Use when you're trying to maximize/minimize something under constraints.

```
def binary_search_answer():
    left, right = 1, 10**9  # based on problem constraints
    
    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid  # minimize
        else:
            left = mid + 1
            
    return left
```
## Problems:

- 875. Koko Eating Bananas (Medium)

- 1011. Capacity To Ship Packages Within D Days (Medium)

- 410. Split Array Largest Sum (Hard)

- 1482. Minimum Number of Days to Make m Bouquets (Medium)

- 2141. Maximum Running Time of N Computers (Hard)

# Template 5: Find First or Last Occurrence
First Occurrence:
```
def find_first(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            right = mid - 1  # look on left side
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return result
```
Last Occurrence:
```
def find_last(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            left = mid + 1  # look on right side
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return result
```
# Problems:

Find First and Last Position of Element in Sorted Array

#  Template 6: Search in Rotated Sorted Array
```
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:  # left half sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # right half sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1
```
# Problems:

- 33. Search in Rotated Sorted Array (Medium)

- 81. Search in Rotated Sorted Array II (Medium)

# Template 7: Binary Search Over Intervals (Search in Events, Schedules, etc.)
Problem: Find next non-overlapping event, or earliest start > end of current.
```
def find_next_event(events, current_end):
    left, right = 0, len(events) - 1
    ans = len(events)
    
    while left <= right:
        mid = (left + right) // 2
        if events[mid][0] > current_end:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans
```
## Problems:

Maximum Profit in Job Scheduling (DP + Binary Search)

Non-overlapping Intervals

# Template 8: Binary Search on Monotonic Functions (Advanced Check Function)
Problem: You have a function check(x) that returns True/False. Binary search the minimum x such that check(x) is True.
```
def binary_search_check():
    left, right = 1, 1e9
    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left
```
# Hard Problems:

Split Array Largest Sum

Find the Smallest Divisor Given a Threshold

Maximum Running Time of N Computers

# Template 9: Binary Search on Floating Point Values
Problem: Maximize/Minimize a floating point value up to precision ε.
```
def binary_search_float():
    left, right = 0.0, 1e6
    eps = 1e-6
    
    while right - left > eps:
        mid = (left + right) / 2
        if check(mid):
            right = mid
        else:
            left = mid
            
    return left  # or right
```
# Problems:

Maximum Average Subarray II

Koko Eating Bananas (with floats)

Split Array Largest Sum (float version)
644. Maximum Average Subarray II (Hard)

410. Split Array Largest Sum (Hard, float version)

# Template 10: Matrix Binary Search
Problem: Matrix is sorted either row-wise or fully like 1D.
```
def search_matrix(matrix, target):
    if not matrix:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        val = matrix[mid // n][mid % n]
        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
```
# Problems:

- 74. Search a 2D Matrix (Medium)

- 240. Search a 2D Matrix II (Medium)

# Template 11: Binary Search + Greedy
Problem: Find minimum max-group size, max distance, etc.
```
def can_split(nums, max_sum, k):
    count, total = 1, 0
    for num in nums:
        if total + num > max_sum:
            count += 1
            total = 0
        total += num
    return count <= k

def min_largest_sum(nums, k):
    left, right = max(nums), sum(nums)
    
    while left < right:
        mid = (left + right) // 2
        if can_split(nums, mid, k):
            right = mid
        else:
            left = mid + 1
    return left
```
✅ Problems:

- 1283. Find the Smallest Divisor Given a Threshold (Medium)

- 1201. Ugly Number III (Hard)

- 2226. Maximum Candies Allocated to K Children (Medium)

# Template 12: Multi-Dimensional Binary Search (2 Pointers + Binary Search)
Use when your search space is over two or more arrays, or a combination of i and j.

```
for i in range(len(arr1)):
    j = binary_search(arr2, arr1[i])
    # combine results
```
✅ Problems:

Median of Two Sorted Arrays (very advanced binary search)

Find K-th Smallest Pair Distance

# Extra Pattern: Binary Search + DP (with Memoization)
```
def solve(index):
    if index >= len(arr):
        return 0
    if index in memo:
        return memo[index]
    
    # Binary search to find next valid index
    next_index = binary_search(...)
    
    take = profit[index] + solve(next_index)
    skip = solve(index + 1)
    
    memo[index] = max(take, skip)
    return memo[index]
```
# Problems:

- 1235. Maximum Profit in Job Scheduling (Hard)

- 982. Triples with Bitwise AND Equal To Zero (Hard)

- 1547. Minimum Cost to Cut a Stick (Hard)

# Final Tips for Hard Problems:
- Always think: Is the answer space sorted? Is it numeric?
- Use check(x) pattern where result depends on a value being too small or too big
- Try combining binary search with greedy, DP, or sliding window
# Find peak in mountain array
Array could be
- arr=[1,2,3,4,5,3,1]
- arr=[0,1,2,4,2,1]
- arr=[0,1,2,3,4,5,6,7]
- arr=[9,8,7,6,5,4,3,2,1,0]
  
```
def find_peak_in_mountain_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid 
    return left 
```


- 4. Median of Two Sorted Arrays (Hard)

- 378. Kth Smallest Element in a Sorted Matrix (Medium)

- 719. Find K-th Smallest Pair Distance (Hard)
- 435. Non-overlapping Intervals (Medium)

- 452. Minimum Number of Arrows to Burst Balloons (Medium)

- 1353. Maximum Number of Events That Can Be Attended (Hard)

- 1235. Maximum Profit in Job Scheduling (Hard)