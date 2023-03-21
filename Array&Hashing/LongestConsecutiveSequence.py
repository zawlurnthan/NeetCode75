"""
    128. Longest Consecutive Sequence
    Medium

    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.

    Example 1:

    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

    Example 2:

    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9


    Constraints:

    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""
from typing import List


def longestConsecutive(nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in nums:
        # check if it's the start of a sequence
        # do not take a bigger number which has consecutive numbers
        if (n - 1) not in numSet:
            length = 1
            # keep counting if a number has next numbers
            while (n + length) in numSet:
                # increase length while there is next consecutive number of current number
                length += 1
                # keep record longest consecutive numbers by adding 1 each repeat
            longest = max(length, longest)
    return longest


nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))

nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))