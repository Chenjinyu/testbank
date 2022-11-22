"""
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k of elements.

Example 1:
Input: arr = [5,5,4], k = 1 -> remove one element
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3 -> remove three elements
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
 

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
"""
from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """
        1. find out a way, the frequence is the key, the item is the value, 
        2. sort arr by key. 
        3. delete the key equals 1, but if the k > (key == 1), count the left, if the k < (key == 1), moving to the 2nd. 
        """
        count_val = Counter(arr)
        
        # count_val.sort(key=lambda x: x.value) # --> counter does not have sort attribute
        sorted_count_val = sorted(count_val.values())
        ans = len(sorted_count_val)
        for val in sorted_count_val:
            k -= val # coz remove more elemenet is the way to get the least number of unqiue. 
            if k < 0:
                break
            ans -= 1
        return ans
        
    def findLeastNumOfUniqueInts2(self, arr: List[int], k: int) -> int:
        count_val = Counter(arr)
        ordered = sorted(count_val.values(), reverse=True)
        while ordered and ordered[-1] <= k:
            k -= ordered.pop() # pop(index=optional) Returns The last value or the given index value from the list.
            
        return len(ordered)
        
import unittest
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_findLeastNumOfUniqueInts(self):
        arr = [4,3,1,1,3,3,2]
        k = 3
        result = self.solution.findLeastNumOfUniqueInts(arr, k)
        expect = 2
        self.assertEqual(result, expect)
        
        
    def test_findLeastNumOfUniqueInts2(self):
        arr = [4,3,1,1,3,3,2,2,4]
        k = 3
        result = self.solution.findLeastNumOfUniqueInts2(arr, k)
        expect = 3
        self.assertEqual(result, expect)
        

if __name__ == "__main__":
    unittest.main()

        