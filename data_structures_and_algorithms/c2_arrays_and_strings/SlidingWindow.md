### Sliding Window

> Like two pointers, sliding windows work the same with arrays and strings - the important thing is that they're iterables with ordered elements. For the sake of brevity, the first part of this article up until the examples will be focusing on arrays. However, all the logic is identical for strings. You can swap every instance of the word "array" with "string" and it will make sense.

A subarray can be defined by two indices, the start and end. For example, with [1, 2, 3, 4], the subarray [2, 3] has a starting index of 1 and an ending index of 2. Let's call the starting index the **left bound** and the ending index the **right bound**. Another name for subarray in this context is **"window"**, which we will use from now on.

**The idea behind the sliding window technique is to efficiently find the "best" window that fits some constraint**. Usually, the problem description will define what makes a window "better" (shorter length, larger sum etc.) and the constraint. Imagine that a problem wanted the length of the longest subarray with a sum less than or equal to k for an array with positive numbers. In this case, the constraint is sum(window) <= k, and the longer the window, the better it is. The general algorithm behind sliding window is:

- Define a pointer for the left and right bound that represents the current window, usually both of them starting at 0.
- Iterate over the array with the right bound to "add" elements to the window.
- Whenever the constraint is broken, in this example if the sum of the window exceeds k, then "remove" elements from the window by incrementing the left bound until the condition is satisfied again.

and the window side is right - left + 1, since index starts at 0.

Here's some pseudocode illustrating the concept:
```java
function fn(arr):
    left = 0
    for right in [0, arr.length - 1]:
        Do some logic to "add" element at arr[right] to window

        while left < right AND condition from problem not met:
            Do some logic to "remove" element at arr[left] from window
            left++

        Do some logic to update the answer
```

With our "sum less than k" example, we can use a variable curr that keeps track of the current sum of the window. That way, we know when the sum exceeds k without needing to calculate the window sum from scratch every iteration. We can "add" elements by doing **curr += arr[right]** and "remove" elements by doing **curr -= arr[left]**. The data and logic needed to maintain information about a window will vary between problems.

>You may be thinking: there is a while loop inside of the for loop, isn't the time complexity O(n ^2)? The reason it is **still O(n)** is that the while loop can only iterate n times in total for the entire algorithm (left starts at 0, only increases, and never exceeds n). If the while loop were to run n times on one iteration of the for loop, that would mean it wouldn't run at all for all the other iterations of the for loop. This is what we refer to as amortized analysis - even though the worst case for an iteration inside the for loop is O(n), **it averages out to O(1) when you consider the entire runtime of the algorithm.**
>你可能会想：for循环里面有一个while循环，时间复杂度不高吗
之所以还是O(n)是因为while循环整个算法总共只能迭代n次（left从0开始，只增加，永远不会超过n）。 如果 while 循环在 for 循环的一次迭代中运行 n 次，则意味着它根本不会在 for 循环的所有其他迭代中运行。 这就是我们所说的摊销分析——尽管 for 循环内迭代的最坏情况是 O(n)，但当您考虑算法的整个运行时间时，它平均为 O(1)。

>对于sliding window 简单来讲，就是for loop for each item, inside of loop, doing the sliding window with while.
>Example 1: Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k.

```python
def find_length(nums, k):
    """Sliding Window"""
    left = curr = ans = 0
    max_len = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    return ans
```
>Given a subarray starting at left and ending at right, the length is right - left + 1. As mentioned before, this algorithm has a time complexity of O(n) since all work done inside the for loop is O(1), where n is the length of nums. The space complexity is constant because we are only using 3 integer variables.



#### Number of subarrays
If a problem asks for the number of subarrays that fit some constraint, we can still use sliding window, but we need to use a neat math trick to calculate the number of subarrays.

> Example 3: [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)

```html
Given an array of positive integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with products less than k are:

[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

Key idea: Whenever you see a problem asking for the number of subarrays, think of this: at each index, how many valid subarrays end at this index? Let's split the 8 subarrays by their ending indices:
```
[713. Subarray Product Less Than K](../../LC_2023/m0713_SubarrayProductLessThanK.py)Solution