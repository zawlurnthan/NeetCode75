"""
    242. Valid Anagram
    Easy

    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.

    Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true
    Example 2:

    Input: s = "rat", t = "car"
    Output: false

    Constraints:

    1 <= s.length, t.length <= 5 * 10^4
    s and t consist of lowercase English letters.

    Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


def isAnagram(s: str, t: str) -> bool:
    # return false if two strings are different length
    if len(s) != len(t): return False
    # comparing two counting dictionary of each sentence
    countS, countT = {}, {}

    for i in range(len(s)):
        # count each letter and reassign it, zero is default value if there's no value to return
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))

s = "rat"
t = "car"
print(isAnagram(s, t))
