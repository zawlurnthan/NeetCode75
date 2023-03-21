import heapq
from typing import List


def splitArray(nums: List[int]) -> List[int]:
    nums.sort(reverse=True)
    total = 0
    # get total sum of the list
    for i in nums:
        total += i

    # get sub list which is greater than rest of the list
    leftSum = 0
    res = []
    for i in nums:
        leftSum += i
        res.append(i)
        if leftSum > total - leftSum:
            return res






nums = [1, 2, 3, 4, 5, 6]
print(splitArray(nums))