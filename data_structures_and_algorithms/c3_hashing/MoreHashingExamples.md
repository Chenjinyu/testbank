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
