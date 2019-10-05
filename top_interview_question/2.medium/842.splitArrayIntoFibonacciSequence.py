"""
842. Split Array into Fibonacci Sequence

Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
Note:

1 <= S.length <= 200
S contains only digits.

Note：
每一次递归调用，都用一个特殊的数据结构"栈"记录当前算法的执行状态，
特别地设置地址栈，用来记录当前算法的执行位置，以备回溯时正常返回。
递归模块的形式参数是普通变量，每次递归调用得到的值都是不同的，他们也是由"栈"来存储

stack vs heap:
Variables stored in stacks are only visible to the owner Thread
while objects created in the heap are visible to all thread
"""
from typing import List


class Solution:
    result = []
    max_int = 2 ** 31 - 1
    o_t = 0

    def splitIntoFibonacci(self, S:str) -> List[int]:
        self.findFibRecursion(S, [])
        return self.result

    def isFib(self, cur_num, fib_list):
        # only for if the num starts with 0, return false.
        if len(cur_num) > 1 and cur_num[0] == "0":
            return False
        if len(fib_list) >= 2:
            if (fib_list[-1] + fib_list[-2]) == int(cur_num):
                return True
            else:
                return False
        else:
            return True

    def findFibRecursion(self, nums, fib_list):
        # nums reduces to "" in the end of loop.
        # also the fibonacci-like sequence was found in flb_list.
        if nums is "" and len(fib_list) > 2:
            self.result = fib_list
            return
        else:
            for i in range(len(nums)):
                if int(nums[:i + 1]) > self.max_int:
                    break
                cur_num = nums[:i + 1]
                print(str(i) + " -- " + cur_num)
                if self.isFib(cur_num, fib_list):
                    self.findFibRecursion(nums[i + 1:], fib_list + [int(cur_num)])


if __name__ == "__main__":
    """
    for the recursion, every time os will create a temp stack for the recursion variables. 
    once it done, or break, it will back to last recursion position. 
    and until the main function(findFibRecursion) finishes the loop
    """
    nums = "1101111"
    print(Solution().splitIntoFibonacci(nums))
