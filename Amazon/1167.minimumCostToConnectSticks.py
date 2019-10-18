"""
You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.
You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.



Example 1:
Input: sticks = [2,4,3]
Output: 14

Example 2:
Input: sticks = [1,8,3,5]
Output: 30


Constraints:

1 <= sticks.length <= 10^4
1 <= sticks[i] <= 10^4
"""
from typing import List
import heapq


class Solution:
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