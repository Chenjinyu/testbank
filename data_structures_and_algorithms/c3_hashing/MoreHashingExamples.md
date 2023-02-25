## More Hashing Examples

Hash maps are nearly ubiquitous(无处不在). We've talked about some of the most common patterns, but there is an unlimited number of ways you can incorporate hash maps into an algorithm. Because of how important hash maps are, we'll look at a couple more examples of how hash maps can be used in various problems. It is crucial that you are comfortable with hash maps if you want to pass interviews.

```htnl
Example 1: 49. Group Anagrams
Given an array of strings strs, group the anagrams together.
For example, given strs = ["eat","tea","tan","ate","nat","bat"], return [["bat"],["nat","tan"],["ate","eat","tea"]].
```

How can we check if two strings are anagrams of each other? We could use two hash maps, count all the characters in each string, and then compare if the hash maps are the same. This is very cumbersome to implement and also doesn't help us with grouping strings together if a group has more than 2 strings. For each group, we need a way to uniquely identify the group.

The cleanest way to know if two strings are anagrams of each other is by checking if they are equal after both being sorted. Also, all strings in a group will be the same when sorted, so we can use the sorted version as a key. We can map these keys to the groups themselves in a hash map, and then our answer is just the values of the hash map.

Essentially, every group has its own "identifier" (the sorted string), and we can use this identifier to group them in a hash map easily.

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        
        return groups.values()
```

>Note for Python: dictionary.values() doesn't actually return a list, but actually a view object. However, the LeetCode judge accepts it as a valid format.

Given n as the length of strs and m as the average length of the strings, we iterate over each string sort it, which costs logO(n⋅m⋅logm). Then, we need to iterate over the keys. In the worst case scenario, when there are no matching anagrams, there will be n groups, which means this will cost O(n), giving an overall time complexity of logO(n⋅m⋅logm) (the final +n is dominated). The space complexity is O(n⋅m) as each string will be placed in an array within the hash map.

>Another way to solve this problem is to use a tuple of length 26 representing the count of each character as the key instead of the sorted string. This would technically solve the problem in O(n⋅m) because the 26 is a constant defined by the problem, but for test cases with smaller strings it would be slower due to the constant factor which is hidden by big O.

```html
Example 2: 2260. Minimum Consecutive Cards to Pick Up

Given an integer array cards, find the length of the shortest subarray that contains at least one duplicate. If the array has no duplicates, return -1.
```

The time complexity is still O(n) even though we have a nested loop in the algorithm. This is because the inner loop in the nested loop can only iterate n times in total, since it's iterating over indices of elements from the array,where n is the length of the input array.
```python
from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = defaultdict(int)
        ans = float("inf")
        for i in range(len(cards)):
            if cards[i] in dic:
                ans = min(ans, i - dic[cards[i]] + 1)
            
            dic[cards[i]] = i

        return ans if ans < float("inf") else -1
```

```html
Example 3: 2342. Max Sum of a Pair With Equal Sum of Digits

Given an array of integers nums, find the maximum value of nums[i] + nums[j], where nums[i] and nums[j] have the same digit sum (the sum of their individual digits). Return -1 if there is no pair of numbers with the same digit sum.
```
This problem is similar to the first example we looked at with grouping anagrams. In the first example, groups were identified by their sorted string. In this problem, we can identify a group by its digit sum. We can iterate through the array and group all the numbers with the same digit sum together in a hash map. Then we can iterate over that hash map and for each group with at least 2 elements, find the 2 max elements by sorting.

```python
from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10
            
            return digit_sum
        
        dic = defaultdict(list)
        for num in nums:
            digit_sum = get_digit_sum(num)
            dic[digit_sum].append(num)
        
        ans = -1
        for key in dic:
            curr = dic[key]
            if len(curr) > 1:
                curr.sort(reverse=True)
                ans = max(ans, curr[0] + curr[1])
        
        return ans
```

This algorithm is inefficient due to the sorting, which can potentially cost O(n⋅logn) if every number in the input has the same digit sum, where n is the length of the input array. Just like in the previous problem, we don't need to store all the numbers in the group. We can improve the time complexity and average space complexity by only saving the largest number seen so far for each digit sum.

```python
from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10
            
            return digit_sum
        
        dic = defaultdict(int)
        ans = -1
        for num in nums:
            digit_sum = get_digit_sum(num)
            if digit_sum in dic:
                ans = max(ans, num + dic[digit_sum])
            dic[digit_sum] = max(dic[digit_sum], num)

        return ans
```

Just like in the last example, the first algorithm always uses O(n) space because we store all the elements in the hash map's values, but with the improvement, the average case will use much less space since each key only stores an integer. We also save on an extra iteration and a sort in each iteration, giving us a time complexity of O(n), where n is the length of the input array.

```html
Example 4: 2352. Equal Row and Column Pairs

Given an n x n matrix grid, return the number of pairs (R, C) where R is a row and C is a column, and R and C are equal if we consider them as 1D arrays.
```
How can we calculate the number of equal pairs? Let's say there are three rows that look like [1, 2, 3], and there are two columns that look the same. For each of the three rows, there are two columns to pair with, so that means there are 3 * 2 = 6 pairs. We can use a hash map to count how many times each row occurs. We can use a second hash map to do the same thing with the columns. Then, we can iterate over the rows hash map, and for each row, check if the same array appeared as a column. If it did, then the product of the number of appearances is added to our answer.

The problem is, arrays can't be put in a hash map as a key because they are mutable. We need to convert the rows and columns into a hashable form such as a string or tuple. The best choice will depend on the language you're using.

```python
from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def convert_to_key(arr):
            # Python is quite a nice language for coding interviews!
            return tuple(arr)
        
        dic = defaultdict(int)
        for row in grid:
            dic[convert_to_key(row)] += 1
        
        dic2 = defaultdict(int)
        for col in range(len(grid[0])):
            current_col = []
            for row in range(len(grid)):
                current_col.append(grid[row][col])
            
            dic2[convert_to_key(current_col)] += 1

        ans = 0
        for arr in dic:
            ans += dic[arr] * dic2[arr]
        
        return ans
```

If the grid has a size of n⋅n, this algorithm has a time complexity of O(n 2) - there are elements and each element is iterated over twice initially (once for the row it occupies and once for the column it occupies). Populating and then interating over the hash maps will be dominated by this. The space complexity is O(n 2) - if all rows and columns are unique, then each of the two hash maps will both grow to a size of n, with each entry having a length of n.

### Closing notes

We could spend the rest of the course looking at hash map problems, but we have other topics to look at! If you love hash maps, the good news is that we will continue to use them for the rest of the course. As we said before they are almost ubiquitous - it's amazing how a hash map can find its way into so many algorithms. Before moving on, try the next few practice problems and the hashing quiz to test your knowledge.