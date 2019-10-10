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

def generate(numRows: int):
    def getSum(i):
        tmp = []
        for index in range(len(triangle_list[i - 1]) - 1):
            tmp.append(triangle_list[i - 1][index] + triangle_list[i - 1][index + 1])

        return tmp

    triangle_list = []
    triangle_list.append([1])
    triangle_list.append([1, 1])
    for i in range(2, numRows):
        triangle_list.append([[1] + getSum(i) + [1]])

    return triangle_list

print(generate(5))
        
