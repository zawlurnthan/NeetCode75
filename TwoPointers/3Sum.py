"""
    15. 3Sum
    Medium

    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such
    that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

    Example 1:

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation:
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

    Example 2:

    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

    Example 3:

    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.


    Constraints:

    3 <= nums.length <= 3000
    -10^5 <= nums[i] <= 10^5
"""
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    res =  []
    nums.sort()

    for i, a in enumerate(nums):
        # skip positive integers
        # if a > 0:
        #     break
        # skip same number (eliminate duplicate)
        if i > 0 and a == nums[i - 1]:
            continue
        # start from the current next index to the end of the list
        l, r = i + 1, len(nums) - 1
        while l < r:
            three_sum = a + nums[l] + nums[r]
            if three_sum > 0:
                # move right pointer to the left if sum is greater than zero
                r -= 1
            elif three_sum < 0:
                # move left pointer to the right if sum is less than zero
                l += 1
            else:
                # add all elements as a list if three sum is zero
                res.append([a, nums[l], nums[r]])
                l += 1
                r -= 1

                # if pointer is same as previous value (value is duplicate)
                while nums[l] == nums[l - 1] and l < r:
                    # move left pointer to the right
                    l += 1
    return res


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))


nums = [0,1,1]
print(threeSum(nums))

nums = [0,0,0]
print(threeSum(nums))

nums = [-2,0,0,2,2]
print(threeSum(nums))