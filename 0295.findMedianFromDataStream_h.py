"""
295. Find Median from Data Stream
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""
import bisect

class MedianFinder:
    """
    Amazon OA Problem
    Facebook OA Problem
    Google OA Problem
    Microsoft OA Problem
    Apple OA Problem
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stream_data = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.stream_data, num)

    def findMedian(self) -> float:
        steam_data_len = len(self.stream_data)
        mid = steam_data_len // 2
        if steam_data_len % 2:
            return self.stream_data[mid]
        else:
            # the median is the mean of the two middle value.
            return (self.stream_data[mid] + self.stream_data[mid - 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

