"""
398. Random Pick Index
Given an array of integers with possible duplicates, randomly output the index of a given target number.
You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);

"""

import random
from typing import List

# 记住这个公式。
class Solution:
    """
    题目：有一个网页抓取器每秒钟抓取一个网页，定义一个API，每次调用的时候要等概率的从目前已经抓取的网页中随机选取一个，应该怎么实现？

    分析：这题题目定义有一定迷惑性，最直接的思路貌似应该是先保存当前采集到的所有网页，然后随机采样，这显然不是这题的考点。
    这题想只用O（1）的空间。其实就等价于有一个很长的数据流，数据量大到无法载入内存，怎么做随机等概率采样？
    容易想到的思路是产生一个0到1之间的随机数，然后根据目前数据长度乘以随机数构成index取数，时间复杂度O（1），
    但是需要额外O（n）存储空间，不符合要求。用bitmap可以把空间减小若干倍数，但是还是O（n）的。
    怎么做到O（1）空间解决这个问题呢？这就需要从采样过程来思考，用到蓄水池抽样算法，
    基本道理和从n张彩票中抽奖（假设只有一张彩票中奖）无论先抽还是后抽中奖概率都是1/n类似。关于蓄水池抽样算法，摘要如下的经典解释（来源这里）

    蓄水池算法

    对这个问题我们首先从最简单的例子出发：
    数据流只有一个数据。我们接收数据，发现数据流结束了，直接返回该数据，该数据返回的概率为1。
    看来很简单，那么我们试试难一点的情况：假设数据流里有两个数据。
    我们读到了第一个数据，这次我们不能直接返回该数据，因为数据流没有结束。我们继续读取第二个数据，发现数据流结束了。
    因此我们只要保证以相同的概率返回第一个或者第二个数据就可以满足题目要求。
    因此我们生成一个0到1的随机数R,如果R小于0.5我们就返回第一个数据，如果R大于0.5，返回第二个数据。

    接着我们继续分析有三个数据的数据流的情况。
    为了方便，我们按顺序给流中的数据命名为1、2、3。
    我们陆续收到了数据1、2和前面的例子一样，我们只能保存一个数据，所以必须淘汰1和2中的一个。
    应该如何淘汰呢？不妨和上面例子一样，我们按照二分之一的概率淘汰一个，例如我们淘汰了2。
    继续读取流中的数据3，发现数据流结束了，我们知道在长度为3的数据流中，如果返回数据3的概率为1/3,那么才有可能保证选择的正确性。
    也就是说，目前我们手里有1,3两个数据，我们通过一次随机选择，以1/3的概率留下数据3，以2/3的概率留下数据1.那么数据1被最终留下的概率是多少呢？

    数据1被留下：（1/2）*(2/3) = 1/3
    数据2被留下概率：（1/2）*(2/3) = 1/3
    数据3被留下概率：1/3
    这个方法可以满足题目要求，所有数据被留下返回的概率一样！

    因此，我们做一下推论：假设当前正要读取第n个数据，则我们以1/n的概率留下该数据，否则留下前n-1个数据中的一个。以这种方法选择，所有数据流中数据被选择的概率一样。
    简短的证明：假设n-1时候成立，即前n-1个数据被返回的概率都是1/n-1,当前正在读取第n个数据，以1/n的概率返回它。
    那么前n-1个数据中数据被返回的概率为：(1/(n-1))*((n-1)/n)= 1/n，假设成立。
    这里用到了数学归纳法（中学数学内容），首先证明n=1成立，然后证明当n-1是成立时，n的情况也成立，于是对于所有n的情况都成立。

    所以，简而言之，就是每次以1/n（n是当前的值，会随着数据流到来不断变大）的概率留下当前数，以（n-1）/n的概率留下前面n-1次采样留下的那个数，
    只要保证不断如此采样，就可以用O（1）的空间做到随机等概率的采样，每个数被采到（留下来）的概率都是1/n.
    """
    
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        index = count = 0
        for i in range(len(self.nums)):
            if target == self.nums[i]:
                count += 1
                if random.random() < (1.0 / count):
                    index = i
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

if __name__ == "__main__":
    nums = [1,2,3,3,3]
    print(Solution(nums).pick(2))
