#  Two Pointer Pattern - LeetCode Questions

# 1. Opposite Ends (Start and End Pointers)
 Pattern:
Use one pointer at the beginning and one at the end of the array.

Move them toward each other based on some condition.

## Common Use Cases:
Check if array can be a palindrome.

Find pairs with a target sum in a sorted array.

Container With Most Water (maximize area between pointers).

Example:
```
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
```
# 2. Fast and Slow Pointers (aka Floyd’s Cycle Detection)
    Pattern:
Use two pointers: one moves twice as fast as the other.

Great for detecting cycles, middle of a list, etc.

#  Common Use Cases:
Detect a cycle in a linked list.

Find the middle of a linked list.

Remove N-th node from end.

Example:
```
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```
# 3. Sliding Window
## Pattern:
Move both pointers in the same direction to maintain a window.

Resize the window to satisfy constraints.

## Common Use Cases:
Longest substring without repeating characters.

Minimum size subarray sum.

Max average subarray.

🧠 Example:
```
def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
```
# 4. Merge Pattern (like in merge sort)
Pattern:
Used to merge two sorted arrays/lists.

Move pointers in both arrays simultaneously.

## Common Use Cases:
Merge two sorted lists.

Intersection of two sorted arrays.

## Example:
```
def merge_sorted(arr1, arr2):
    i = j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result += arr1[i:]
    result += arr2[j:]
    return result
```
# 5. Partitioning Around a Pivot (Used in Quicksort, Dutch National Flag)
📌 Pattern:
Rearrange array elements with two (or three) pointers to partition around a pivot.

## Common Use Cases:
Quicksort

Sort colors (Dutch National Flag problem)

Example:
```
def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
```
Summary Table

This document lists commonly asked LeetCode problems that follow the **Two Pointer** approach.

---

## 1. Opposite Ends Pattern (Start and End Pointers)

- 🔹 [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- 🔹 [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
- 🔹 [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- 🔹 [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)
- 🔹 [344. Reverse String](https://leetcode.com/problems/reverse-string/)
- 🔹 [15. 3Sum](https://leetcode.com/problems/3sum/)
- 🔹 [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/)

---

## 2. Fast and Slow Pointers (Floyd’s Cycle)

- 🔹 [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- 🔹 [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
- 🔹 [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
- 🔹 [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
- 🔹 [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

---

## 3. Sliding Window (Two Pointers Moving in Same Direction)

- 🔹 [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- 🔹 [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- 🔹 [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/)
- 🔹 [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
- 🔹 [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
- 🔹 [2958. Length of Longest Subarray With at Most K Frequency](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/)

---

## 4. Merge Pattern (Two Arrays)

- 🔹 [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- 🔹 [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
- 🔹 [986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)
- 🔹 [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

---

## 5. Partitioning (Dutch National Flag / Quicksort Variant)

- 🔹 [75. Sort Colors](https://leetcode.com/problems/sort-colors/)
- 🔹 [280. Wiggle Sort](https://leetcode.com/problems/wiggle-sort/)
- 🔹 [905. Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/)
- 🔹 [922. Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/)
- 🔹 [Partition List (LeetCode 86)](https://leetcode.com/problems/partition-list/)

---

##  Tips
- Use **Opposite Ends** for sorted arrays when searching for pairs.
- Use **Fast/Slow** for cycle detection and middle finding in linked lists.
- Use **Sliding Window** for substring/array problems with a condition.
- Use **Merge** for sorted array/list combination.
- Use **Partitioning** to reorganize array elements with O(1) space.

---
