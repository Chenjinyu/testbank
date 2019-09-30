"""
941. Valid Mountain Array

Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]


Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true


Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
"""
from typing import List

class Solution:
    """
    this solution to get the max value and the position is not good to detail with.
    because it easy to out of index in second while.
    """
    def validMountainArray(self, A: List[int]) -> bool:
        length = len(A)
        if length == 0:
            return False
        max_int = max(A)
        max_pos = A.index(max_int)
        if max_pos == 0 or max_pos == length - 1:
            return False

        for i in range(max_pos):
            if A[i] > A[i + 1]:
                return False

        # if A[max_pos + 1] should be in the loop,
        # set the max_pos + 1 < length in the while condition directly
        while max_pos + 1 < length:
            if A[max_pos] <= A[max_pos + 1]:
                return False
            max_pos += 1

        return True

    def validMountainArrayImprove(self, A: List[int]) -> bool:
        """
        the solution of this function is straightful, becasuse up and down.
        """
        length = len(A)
        max_pos = 0

        # Up the mountain
        while max_pos + 1 < length and A[max_pos] < A[max_pos + 1]:
            max_pos += 1

        if max_pos == 0 or max_pos == length - 1:
            return False

        # the max_pos get from `Up the mountain` and keep to walk down the mountain
        while max_pos + 1 < length and A[max_pos] > A[max_pos + 1]:
            max_pos += 1

        return max_pos == length - 1



if __name__ == "__main__":
    # A = [1,3,7,5,2,0]
    # A = [0,1,1]
    A = [0,3,2,1]
    print(Solution().validMountainArray(A))