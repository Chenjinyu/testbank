"""
896. Monotonic Array
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.



Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true


Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000

"""

from typing import List

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        pos = 0
        length = len(A)

        if length == 0:
            return False

        while pos + 1 < length:
            if A[pos] >= A[pos + 1]:
                pos += 1
            else:
                break

        if pos == length - 1:
            return True

        pos = 0
        while pos + 1 < length:
            if A[pos] <= A[pos + 1]:
                pos += 1
            else:
                break
        if pos == length - 1:
            return True

        return False

    def isMonotonicImprove(self, A: List[int]) -> bool:
        # all: return True if all values are True, return False if all values are False, or at least one is False
        return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
                all(A[i] >= A[i + 1] for i in range(len(A) - 1)))


if __name__ == "__main__":
    # nums = [4, 5, 0, -2, -3, 1]
    # nums = [1,2,4,5]
    nums = [1,1,1]
    print(Solution().isMonotonicImprove(nums))