"""
    238. Product of Array Except Self

    Given an integer array nums, return an array answer such that answer[i] is equal to the product
    of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.

    Example 1:

    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

    Example 2:

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]


    Constraints:

    2 <= nums.length <= 10^5
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


    Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not
    count as extra space for space complexity analysis.)
"""
import math
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    # fill with 1 of newly created list res which is nums list long
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        # assign res list with prefix product of elements, starting from beginning of the nums list
        res[i] = prefix
        # keep multiply by elements
        prefix *= nums[i]

    postfix = 1
    # iterate nums from the end to beginning by decreasing 1
    for i in range(len(nums) - 1, -1, -1):
        # assign res list with postfix product of elements starting from the end of the nums list
        res[i] *= postfix
        # keep multiply by elements
        postfix *= nums[i]
    return res


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))

nums = [-1, 1, 0, -3, 3]
print(productExceptSelf(nums))

