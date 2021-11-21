"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2**31,  2**31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""


class Solution:
    def reverse(self, x: int) -> int:
        reversed = int("".join(list(str(abs(x)))[::-1]))
        if x < 0:
            return max(-reversed, -2**31)  #if max(-reversed, -2**31) > -2**31 else 0
        return min(reversed, 2**31 - 1)  #if min(reversed, 2**31 - 1) < 2**31 - 1 else 0


if __name__ == "__main__":
    x = -123
    print(Solution().reverse(x))


