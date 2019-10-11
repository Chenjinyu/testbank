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

Note: 
generateMostEfficient uses list.append(), it's more efficient than create the two dimensional list first.
because, compare with generateFirstAccpeted(what i did), it create items with the same length of item.
think about if the length is too much long, it not only comsume a lot of space, aslo the time to search the memory
and return a pointer to you.

1). list[index] = [1,2,3] vs 2). list.append([1,2,3])
1). first of all, python will search the address of index points to, and delete the connection between of them, 
and assgin new space for you.
2). find a space and return/assgin the ponter back, it's much faster than 1).

"""

class Solution:
    def generateMostEfficient(self, numRows: int) :
        if numRows == 0:
            return None
        for i in range(numRows):
            if i < 1:
                result = [[1]]
            else:
                result.append([0] * (i + 1))
                result[i][0], result[i][-1] = 1, 1
                for j in range(1, i):
                    result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result
    
    
    def generateMyIdeaFirstInMind(self, numRows: int):
        # this is what I want to implement at the beginning of thinking.
        result = []
        for i in range(numRows):
            if not result:
                result.append([1])
            else:
                result.append(
                    [1] + [result[i - 1][j - 1] + result[i - 1][j] for j in range(1, len(result[i - 1]))] + [1])
        return result
    
    
    def generateFirstAccpeted(self, numRows: int):
        # test = 5 * [0] ==> [0, 0, 0, 0, 0] vs test = 5 * [[0]] ==> [[0], [0], [0], [0], [0]]
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


    def generateLogicImprove(self, numRows):
        triangle = []

        for row_num in range(numRows):
            # set item are None, and the first and last row elements are ALWAYS 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle

    
if __file__ == "__main__":
    n = 30
    print(Solution().generate(n))
