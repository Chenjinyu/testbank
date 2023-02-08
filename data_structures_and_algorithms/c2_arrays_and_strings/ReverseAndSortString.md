### Reverse String/List
- list.reverse() reverse list in place 
- reversed(list) returns an iterator that yields items in reverse order. 

O(N) -> switch items pair with begin and end, and move close to center. 
the worse case is O(N)
```python
>>> lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> reversed_obj = reserved(lst)
>>> reversed_obj
<list_reverseiterator object at 0x7fca9999e790>>
>>> list(reversed_obj)
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```


### sort String/List
O(N Log N)
- list.sort() sort in place 
- sorted(lst) return new list.

```python
################################################################
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Follow up: Squaring each element and sorting the new array is very trivial, 
# could you find an O(n) solution using a different approach?
################################################################
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # O(N Log N)
        return sorted(x*x for x in nums)

    def sortedSquaresON(self, nums: List[int]) -> List[int]: 
        num_len = len(nums)
        res = [0] * num_len
        left, right = 0, num_len - 1
        # start with the rightest, since we only able to compare the biggest number.
        # the list is sorted with negative and postive. 
        # the rightmost is the biggest one.
        for n in range(num_len -1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            res[n] = square * square
        return res
```