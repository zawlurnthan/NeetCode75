"""
    49. Group Anagrams
    Medium

    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.

    Example 1:

    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Example 2:

    Input: strs = [""]
    Output: [[""]]

    Example 3:

    Input: strs = ["a"]
    Output: [["a"]]


    Constraints:

    1 <= strs.length <= 10^4
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""
import collections
from typing import List, Any


def groupAnagramsByCounting(strs: List[str]) -> List[List[str]]:
    ans = collections.defaultdict(list)

    for str in strs:
        # create a list, fill with zero 26 time for a through z
        count = [0] * 26
        # iterate through each letter of a word
        for char in str:
            # assign each index of (c) in count list with 1
            # get each index of char by subtracting ascii value a from current letter
            count[ord(char) - ord("a")] += 1
    # group same anagram words with same key (indices of list)
        ans[tuple(count)].append(str)
    return list(ans.values())


def groupAnagramsBySortedString(strs):
    ans = collections.defaultdict(list)
    for word in strs:
        # grouping same anagram words with sorted word as a key
        # as sorted word of current word
        # list can't be a key of a dictionary, change list to a tuple
        ans[tuple(sorted(word))].append(word)
    return list(ans.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagramsByCounting(strs))
print(groupAnagramsBySortedString(strs))


strs = [""]
print(groupAnagramsByCounting(strs))
print(groupAnagramsBySortedString(strs))


strs = ["a"]
print(groupAnagramsByCounting(strs))
print(groupAnagramsBySortedString(strs))

