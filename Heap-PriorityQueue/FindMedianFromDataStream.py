"""
    295. Find Median from Data Stream
    Hard

    The median is the middle value in an ordered integer list. If the size of the list is even, there is no
    middle value, and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
    Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer
    will be accepted.


    Example 1:

    Input
    ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    [[], [1], [2], [], [3], []]
    Output
    [null, null, null, 1.5, null, 2.0]

    Explanation
    MedianFinder medianFinder = new MedianFinder();
    medianFinder.addNum(1);    // arr = [1]
    medianFinder.addNum(2);    // arr = [1, 2]
    medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3);    // arr[1, 2, 3]
    medianFinder.findMedian(); // return 2.0


    Constraints:

    -105 <= num <= 105
    There will be at least one element in the data structure before calling findMedian.
    At most 5 * 104 calls will be made to addNum and findMedian.


    Follow up:

    If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""
import heapq
from heapq import *


class MedianFinderMyWay:
    def __init__(self):
        self.list = []
        self.size = len(self.list)

    def addNumber(self, num: int) -> None:
        self.list.append(num)


    def findMedian(self) -> float:
        mid = self.size // 2
        # self.list.sort()

        if self.size % 2 == 0:
            # index starts from 0, mid become one less than regular number
            return (self.list[mid - 1] + self.list[mid]) / 2
        else:
            return float(self.list[mid])



obj = MedianFinderMyWay()
obj.addNumber(1)
obj.addNumber(2)
print(obj.findMedian())
obj.addNumber(3)
print(obj.findMedian())

#################################################################################################
class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []

    def addNumber(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2


obj = MedianFinder()
obj.addNumber(1)
obj.addNumber(2)
print(obj.findMedian())
obj.addNumber(3)
print(obj.findMedian())


#################################### This is better !!! ################################################
class MedianFinderOther:
    def __init__(self):
        self.small = [] # max heap, smaller half of list
        self.large = [] # min heap, larger half of list

    def addNumber(self, num):
        if len(self.small) == len(self.large):
            """ Max Heap: add negative number, convert positive number when it return """
            # 1. push new number into small,
            # 2. pop max number from small,
            # 3. push max number into large
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            # min out from large, min into small.
            heappush(self.small, -heappushpop(self.large, num))


    def findMedian(self):
        # if length of both heaps are even number
        if len(self.small) == len(self.large):
            # add them and divide by 2 to get median value
            # watch out sign,
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


obj = MedianFinderOther()
obj.addNumber(1)
obj.addNumber(2)
print(obj.findMedian())
obj.addNumber(3)
print(obj.findMedian())


