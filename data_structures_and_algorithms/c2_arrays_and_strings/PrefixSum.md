### Prefix Sum

A prefix sum is a technique that can be used with integer arrays. The idea is to create an array **prefix** where **prefix[i]** is the sum of all elements up to the index **i** (inclusive). For example, given **nums = [5, 2, 1, 6, 3, 8]**, we would have **prefix = [5, 7, 8, 14, 17, 25]**.

Prefix sums allow us to find the sum of any subarray in O(1). If we want the sum of the subarray from i to j (inclusive), then the answer is **prefix[j] - prefix[i - 1]**, or **prefix[j] - prefix[i] + nums[i]** if you don't want to deal with the out of bounds case when i = 0.

Building a prefix sum is very simple. Here's some pseudocode:
```java
Given an integer array nums,

prefix = [nums[0]]
for i in [1, len(nums) - 1]:
    prefix.append(nums[i] + prefix[prefix.length - 1])
```

Initially, we start with just the first element. Then we iterate with i starting from index 1. At any given point, the last element of prefix will represent the sum of all the elements in the input up to but not including index i. So we can add that value plus the current value to the end of prefix and continue to the next element.

A prefix sum is a great tool whenever a problem involves sums of a subarray. It only costs O(n) to build but allows all future subarray queries to be O(1), so it can usually improve an algorithm's time complexity by a factor of O(n), where n is the length of the array. Let's look at some examples.

```html
Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

For example, given nums = [1, 6, 3, 2, 7, 2] and queries = [[0, 3], [2, 5], [2, 4]] and limit = 13, the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].
```
Let's build a prefix sum and then use the method described above to answer each query in O(1).
```python
def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        # the prefix[-1] always is the last one item from the prefix array which be appended as below.
        prefix.append(nums[i] + prefix[-1])
    
    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans
```

Without the prefix sum, answering each query would be **O(n)** in the worst case, where n is the length of nums. If **m = queries.length**, that would give a time complexity of **O(n∗m)**. With the prefix sum, it costs **O(n)** to build, but then answering each query is **O(1)**. This gives a much better time complexity of **O(n+m)**. We use O(n) space to build the prefix sum.
