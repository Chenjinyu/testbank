"""
Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

^: 按位异或运算符：当两对应的二进位相异时，结果为1
|: 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1
&: 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0

"""


class Solution:

    def hammingDistance(self, x: int, y: int) -> int:
        # bin(n) convert integer to binary string. which starts with '0b'
        # which idenfied it is binary.
        return bin(x ^ y).count('1')

    def hammingDistanceIDid(self, x: int, y: int) ->int:
        # bin() return string, and treat them as a string to compare.
        x1 = bin(x)[2:]
        x2 = x1.zfill(32) # zfill with 32 bits.
        y1 = bin(y)[2:]
        y2 = y1.zfill(32)
        h = 0
        for i in range(32):
            if x2[i] != y2[i]:
                h += 1
        return h


if __name__ == "__main__":
    print(Solution().hammingDistance(3, 2))
