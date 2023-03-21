from typing import List


def splitArray(nums: List[int]):
    even, odd = [], []

    for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return [even, odd]


nums = [1,2,3,4,5,6,7,8,9,0]
even, odd = splitArray(nums)
print(even)
print(odd)