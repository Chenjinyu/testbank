"""
29. Divide Two Integers

Given two integers dividend(被除数) and divisor(除数), divide two integers without using multiplication(乘法), division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.

* Both dividend and divisor will be 32-bit signed integers.
* The divisor will never be 0.
* Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2**31,  2**31 − 1].
For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

Problem solving：
this problem divides to two parts:
1. take care of the edge cases, make sure the range: [−2**31,  2**31 − 1], and test them at the edge of them,
eg: 2147483648, -2147483648, 2147483647, -2147483647, -1, 1. when the dividend reach to 2147483647, the maximum.
2. take care of the basic logic, but make sure the large number brings the performance issue.
"""

import math


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max_value = int(math.pow(2, 31)) - 1
        min_value = -int(math.pow(2, 31))
        is_negative = ((dividend > 0) == (divisor < 0))
        if divisor == 0:
            return max_value
        if divisor == 1:
            if is_negative:
                return max(min_value, dividend)
            else:
                # make sure the Maximum is not out of range [-2 ** 31, 2 ** 31 - 1]
                return min(max_value, dividend)
        if divisor == -1:
            if is_negative:
                return -min(-min_value, dividend)
            else:
                return min(max_value, abs(dividend))

        divisor = abs(divisor)
        dividend = abs(dividend)
        deno_count = 0
        while dividend >= divisor:
            count, dividend = self.divideWhile(dividend, divisor)
            deno_count += count

        return -deno_count if is_negative else abs(deno_count)

    def divideWhile(self, dividend, divisor):
        res, count = 0, 1
        while dividend >= divisor:
            dividend -= divisor
            divisor += divisor

            res += count
            count += count
        return res, dividend


if __name__ == "__main__":
    dividend = 2147483649
    divisor = 1
    print(Solution().divide(dividend, divisor))

