"""
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.


Input: num = 8
Output: 4
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.


Input: num = 123
Output: 12
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        remaining = num
        _is_odd = lambda x: x&1
        _is_even = lambda x: True if x % 2 == 0 else False
        # def _is_odd(x):
        #     return lambda x: x&1
        
        while remaining:
            steps += 1
            remaining = remaining - 1 if _is_odd(remaining) else remaining>>1
        
        return steps

# print(3&1)
# print(5&1)
# print(4&1)
# print(6&1)    

is_odd = lambda x: x&1
remaining = 18
remaining >>= 1 #  it's binary equivalent, eg: 
print(remaining)
# remaining = remaining - 1 if is_odd(remaining) else remaining / 2
# print(remaining)


#### NOTE ####
# binary equivalent. 
# >>= 1 -> bitwise shift right 1  int(18) 0001 0010 -> 0000 1001 int(9)
# >>=2 -> bitwise shift right 2  (int 100) -> 0110 0100 >>2  bit(25) -> 0001 1001 
