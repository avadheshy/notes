# Most Used Patterns
# Fixed-size window (window of size k)
```
for right in range(len(nums)):
    # Expand window
    if right >= k - 1:
        # Process result
        window_sum -= nums[left]
        left += 1
```
# Variable-size window (expand → contract)
```
for right in range(len(s)):
    count[s[right]] += 1

    while invalid(count):  # shrink to make it valid
        count[s[left]] -= 1
        left += 1

    # Process result: window size = right - left + 1
```
# Two sliding windows (for “exactly K” problems)
```
def at_most_k(nums, k):
    count = {}
    left = 0
    res = 0
    for right in range(len(nums)):
        count[nums[right]] = count.get(nums[right], 0) + 1
        while len(count) > k:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1
        res += right - left + 1
    return res

# Total = at_most_k(k) - at_most_k(k-1)
```

---
|  # | Problem                                                  | Type                     | Pattern                             | Link                                                                                                   |
| -: | -------------------------------------------------------- | ------------------------ | ----------------------------------- | ------------------------------------------------------------------------------------------------------ |
|  1 | **Maximum Average Subarray I**                           | Fixed Size               | Max sum of window                   | [643](https://leetcode.com/problems/maximum-average-subarray-i/)                                       |
|  2 | **Sliding Window Maximum**                               | Fixed Size + Deque       | Maintain max in window              | [239](https://leetcode.com/problems/sliding-window-maximum/)                                           |
|  3 | **Minimum Size Subarray Sum**                            | Variable Size            | Shrinking when sum ≥ target         | [209](https://leetcode.com/problems/minimum-size-subarray-sum/)                                        |
|  4 | **Longest Substring Without Repeating Characters**       | Variable Size            | Unique chars                        | [3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)                     |
|  5 | **Longest Repeating Character Replacement**              | Variable Size            | Most frequent char                  | [424](https://leetcode.com/problems/longest-repeating-character-replacement/)                          |
|  6 | **Permutation in String**                                | Fixed Size + Freq Map    | Anagram match in window             | [567](https://leetcode.com/problems/permutation-in-string/)                                            |
|  7 | **Minimum Window Substring**                             | Variable Size + Freq Map | Shrinking valid window              | [76](https://leetcode.com/problems/minimum-window-substring/)                                          |
|  8 | **Longest Substring with At Most K Distinct Characters** | Variable Size            | Shrink if > K distinct              | [340](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) *(Premium)* |
|  9 | **Fruit Into Baskets**                                   | Variable Size            | At most 2 types                     | [904](https://leetcode.com/problems/fruit-into-baskets/)                                               |
| 10 | **Count Number of Nice Subarrays**                       | Prefix Sum + Sliding     | Exactly k odds                      | [1248](https://leetcode.com/problems/count-number-of-nice-subarrays/)                                  |
| 11 | **Subarrays with K Different Integers**                  | Two sliding windows      | Exactly k = atMost(k) - atMost(k-1) | [992](https://leetcode.com/problems/subarrays-with-k-different-integers/)                              |
---

|  # | Problem                                              | Level     | Type                                | Link                                                                                                   |
| -: | ---------------------------------------------------- | --------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------ |
|  1 | Maximum Average Subarray I                           | 🟢 Easy   | Fixed-size                          | [643](https://leetcode.com/problems/maximum-average-subarray-i/)                                       |
|  2 | Sliding Window Maximum                               | 🔴 Hard   | Fixed-size + Deque                  | [239](https://leetcode.com/problems/sliding-window-maximum/)                                           |
|  3 | Minimum Size Subarray Sum                            | 🟡 Medium | Variable-size                       | [209](https://leetcode.com/problems/minimum-size-subarray-sum/)                                        |
|  4 | Longest Substring Without Repeating Characters       | 🟡 Medium | Variable-size                       | [3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)                     |
|  5 | Permutation in String                                | 🟡 Medium | Fixed-size + Frequency Map          | [567](https://leetcode.com/problems/permutation-in-string/)                                            |
|  6 | Minimum Window Substring                             | 🔴 Hard   | Variable-size + Frequency Map       | [76](https://leetcode.com/problems/minimum-window-substring/)                                          |
|  7 | Longest Repeating Character Replacement              | 🟡 Medium | Variable-size + Count               | [424](https://leetcode.com/problems/longest-repeating-character-replacement/)                          |
|  8 | Max Consecutive Ones III                             | 🟡 Medium | Variable-size (flipping zeros)      | [1004](https://leetcode.com/problems/max-consecutive-ones-iii/)                                        |
|  9 | Fruit Into Baskets                                   | 🟡 Medium | At most 2 distinct                  | [904](https://leetcode.com/problems/fruit-into-baskets/)                                               |
| 10 | Longest Substring with At Most K Distinct Characters | 🔴 Hard   | Variable-size                       | [340](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) *(Premium)* |
| 11 | Count Number of Nice Subarrays                       | 🟡 Medium | Sliding Window + Prefix             | [1248](https://leetcode.com/problems/count-number-of-nice-subarrays/)                                  |
| 12 | Subarrays with K Different Integers                  | 🔴 Hard   | Two Pointers                        | [992](https://leetcode.com/problems/subarrays-with-k-different-integers/)                              |
| 13 | Find All Anagrams in a String                        | 🟡 Medium | Fixed-size + Count                  | [438](https://leetcode.com/problems/find-all-anagrams-in-a-string/)                                    |
| 14 | Repeated DNA Sequences                               | 🟡 Medium | Fixed-size sliding window (size 10) | [187](https://leetcode.com/problems/repeated-dna-sequences/)                                           |
| 15 | Grumpy Bookstore Owner                               | 🟡 Medium | Fixed-size (window of X minutes)    | [1052](https://leetcode.com/problems/grumpy-bookstore-owner/)                                          |
| 16 | Max Consecutive Ones                                 | 🟢 Easy   | Basic count                         | [485](https://leetcode.com/problems/max-consecutive-ones/)                                             |
| 17 | Binary Subarrays With Sum                            | 🔴 Hard   | At most K trick                     | [930](https://leetcode.com/problems/binary-subarrays-with-sum/)                                        |
| 18 | Subarray Product Less Than K                         | 🟡 Medium | Two Pointers / Variable-size        | [713](https://leetcode.com/problems/subarray-product-less-than-k/)                                     |
| 19 | Shortest Subarray with Sum at Least K                | 🔴 Hard   | Monotonic Queue                     | [862](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)                            |
| 20 | Maximum Points You Can Obtain from Cards             | 🟡 Medium | Reverse Sliding Window              | [1423](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)                        |
