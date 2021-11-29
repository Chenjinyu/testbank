"""
You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.
You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.



Example 1:
Input: sticks = [2,4,3]
Output: 14
Explanation: You start with sticks = [2,4,3].
1. Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4].
2. Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9].
There is only one stick left, so you are done. The total cost is 5 + 9 = 14.

Example 2:
Input: sticks = [1,8,3,5]
Output: 30
Explanation: You start with sticks = [1,8,3,5].
1. Combine sticks 1 and 3 for a cost of 1 + 3 = 4. Now you have sticks = [4,8,5].
2. Combine sticks 4 and 5 for a cost of 4 + 5 = 9. Now you have sticks = [9,8].
3. Combine sticks 9 and 8 for a cost of 9 + 8 = 17. Now you have sticks = [17].
There is only one stick left, so you are done. The total cost is 4 + 9 + 17 = 30.


Constraints:

1 <= sticks.length <= 10^4
1 <= sticks[i] <= 10^4
"""
from typing import List
import heapq


class Solution:
    """
    Amazon OA Problem
    """
    def connectSticks(self, sticks: List[int]) -> int:
        """
        Space complexity: O(n)
        the time complexity:
        for the liner order, the time complexity should be:
        the heapq.heapify(sticks) is O(N)
        in the while loop: the time complexity is: N * 2 * LogN = NLogN
        max(O(N), O(NlogN)) = O(NlogN)
        :param sticks:
        :return:
        """
        res = 0
        heapq.heapify(sticks)  # time: O(N)
        while len(sticks) > 1:  # O(N)
            c = heapq.heappop(sticks) + heapq.heappop(sticks)  # 2 * O(logN)
            res += c
            heapq.heappush(sticks, c)
        return res


if __name__ == "__main__":
    sticks = [8, 4, 6, 12]
    print(Solution().connectSticks(sticks))