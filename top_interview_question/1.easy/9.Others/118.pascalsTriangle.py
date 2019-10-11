"""
Pascal's Triangle

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]

        triangle_list = numRows * [[0]]
        triangle_list[0] = [1]
        triangle_list[1] = [1, 1]

        def getSum(i):
            tmp = []
            prev_index = i - 1
            for index in range(len(triangle_list[prev_index]) - 1):
                tmp.append(triangle_list[prev_index][index] + triangle_list[prev_index][index + 1])
            return tmp

        for i in range(2, numRows):
            triangle_list[i] = [1] + getSum(i) + [1]

        return triangle_list

if __file__ == "__main__":
    n = 30
    print(Solution().generate(n))
