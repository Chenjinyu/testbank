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

"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')
       
    def hammingDistanceIDid(self, x: int, y: int) ->:
        x1 = bin(x)[2:]
        x2 = x1.zfill(32)
        y1 = bin(y)[2:]
        y2 = y1.zfill(32)
        h = 0
        for i in range(32):
            if x2[i] != y2[i]:
                h += 1
        return h

if __name__ == "__main__":
    print(Solution().hammingDistance(3,2))
