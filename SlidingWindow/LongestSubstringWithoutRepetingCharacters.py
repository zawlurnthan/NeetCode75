"""
    3. Longest Substring Without Repeating Characters
    medium

    Given a string s, find the length of the longest substring without repeating characters.

    Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.


    Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.


    Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


    Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(s: str) -> int:
    l, res = 0, 0
    unique = set()

    for r in range(len(s)):
        while s[r] in unique:
            # remove same letter from the set if current letter is in the set
            unique.remove(s[l])
            l += 1
        unique.add(s[r])
        # get max window
        # can use different way like max size of set or different between left and right
        # res = max(res, r - l + 1)
        res = max(res, len(unique))
    return res


s = "abcabcbb"
print(lengthOfLongestSubstring(s))

s = "bbbbb"
print(lengthOfLongestSubstring(s))

s = "pwwkew"
print(lengthOfLongestSubstring(s))
