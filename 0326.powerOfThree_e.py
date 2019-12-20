"""
326. Power of Three
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?

Approach: Mathematics
n = 3^i
i = log3(n)
i = logb(n)/logb(3)
"""

from math import log, log10

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # int(logb(n)/logb(3)) - float(logb(n)/logb(3))
        # eg, n = 26, returns 2.96564727304425
        # n = 27. returns 3.0
        return n > 0 and (int(log10(n)/log10(3)) - log10(n)/log10(3) == 0)
        # return n > 0 and (round(log(n, 3), 9) == round(log(n, 3))  # better one

    def isPowerOfThreeLoop(self, n: int) -> bool:
        while n % 3 == 0 and n != 0:
            n /= 3
        if n == 1:
            return True
        return False

    def isPowerOfThreeLoopLoop2(self, n: int) -> bool:
        num = n
        if num == 1:
            return True
        while num > 3:
            num /= 3
        return num == 3


if __name__ == "__main__":
    print(Solution().isPowerOfThreeLoopLoop2(45))
