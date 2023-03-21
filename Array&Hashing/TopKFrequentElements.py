"""
    347. Top K Frequent Elements
    Medium

    Given an integer array nums and an integer k, return the k most frequent elements. You may return the
    answer in any order.

    Example 1:

    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

    Example 2:

    Input: nums = [1], k = 1
    Output: [1]


    Constraints:

    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.


    Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
import heapq
from collections import Counter
from typing import List


def topKFrequentByHeapSort(nums: List[int], k: int) -> List[int]:
    if k == len(nums):
        return 
    # create a Counter (counting hashable dictionary) from the list nums
    count = Counter(nums)
    # return a list of the k largest elements from the dictionary keys
    return heapq.nlargest(k, count.keys()) # , key=count.get


def topFrequent(nums: List[int], k: int) -> List[int]:
    return list(dict(Counter(nums).most_common(k)).keys())


def topKFrequentByBucketSort(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        # count each num
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        # assign count key with number value
        freq[c].append(n)

    res = []
    # iterate descending order from last to begin
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


nums = [1, 1, 1, 2, 2, 3]
print(topKFrequentByHeapSort(nums, 2))
print(topKFrequentByBucketSort(nums, 2))
print(topFrequent(nums, 2))
print()

# nums = [1]
# print(topKFrequentByHeapSort(nums, 1))
# print(topKFrequentByBucketSort(nums, 1))
# print(topFrequent(nums, 1))
# print()
#
# nums = []
# print(topFrequent(nums, 1))