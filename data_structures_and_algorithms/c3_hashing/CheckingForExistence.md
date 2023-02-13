## Checking for existence

One of the most common applications of a hash table or set is determining if an element exists in O(1). Since an array needs O(n) to do this, using a hash map or set can improve the time complexity of an algorithm greatly, usually from O(n ^ 2) to O(n). Let's look at some example problems.

```html
Example 1: 1. Two Sum
Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target. You cannot use the same index twice.
```

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic: # This operation is O(1)!
                return [i, dic[complement]]
            
            dic[num] = i
        
        return [-1, -1]
```
This solution also uses O(n) space as the number of keys the hash map will store scales linearly with the input size.

>If the question wanted us to return a boolean indicating if a pair exists or to return the numbers themselves, then we could just use a set. However, since it wants the indices of the numbers, we need to use a hash map to "remember" what indices the numbers are at.

```html
Example 2: 2351. First Letter to Appear Twice

Given a string s, return the first character to appear twice. It is guaranteed that the input will have a duplicate character.
```

>Anytime you find your algorithm running if ... in ..., then consider using **a hash map or set to store elements to have these operations run in O(1)**. Try these upcoming practice problems with what was learned here.