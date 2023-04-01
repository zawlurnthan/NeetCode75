"""
    39. Combination Sum
    Medium

    Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

    The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
    frequency
     of at least one of the chosen numbers is different.

    The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



    Example 1:

    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.
    Example 2:

    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]
    Example 3:

    Input: candidates = [2], target = 1
    Output: []


    Constraints:

    1 <= candidates.length <= 30
    2 <= candidates[i] <= 40
    All elements of candidates are distinct.
    1 <= target <= 40
"""
from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    def backtracting(i, curr, total):
        # Base case
        # return if target is found
        if total == target:
            res.append(curr.copy())
            return
        # stop recursion if pointer is over the length or addition is over the target
        if i >= len(candidates) or total > target:
            return
        # collect elements while adding
        curr.append(candidates[i])
        # 1. do job
        # keep adding elements to get total
        backtracting(i, curr, total + candidates[i])
        curr.pop()
        # 2. move
        # increase pointer i
        backtracting(i + 1, curr, total)

    backtracting(0, [], 0)
    return res



candidates = [2,3,6,7]
print(combinationSum(candidates, 7))


#candidates = [2,3,5]
#print(combinationSum(candidates, 8))

#candidates = [2]
#print(combinationSum(candidates, 1))
