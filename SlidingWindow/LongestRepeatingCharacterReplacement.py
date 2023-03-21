"""
    424. Longest Repeating Character Replacement
    medium

    You are given a string s and an integer k. You can choose any character of the string and
    change it to any other uppercase English character. You can perform this operation at most k times.

    Return the length of the longest substring containing the same letter you can get after
    performing the above operations.

    Example 1:

    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.

    Example 2:

    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.


    Constraints:

    1 <= s.length <= 10^5
    s consists of only uppercase English letters.
    0 <= k <= s.length
"""

def characterReplacement(s: str, k: int) -> int:
    count = {}
    l, maxfq, res = 0, 0, 0

    for r in range(len(s)):
        # count characters
        count[s[r]] = 1 + count.get(s[r], 0)
        # get max count
        maxfq = max(maxfq, count[s[r]])

        # check if different between total length and max count is greater than k value
        while (r - l + 1) - maxfq > k:
            # shrink window by moving left pointer and decreasing count
            # if different is bigger than k value
            count[s[l]] -= 1
            l += 1
        # get max window
        res = max(res, r - l + 1)
    return res



s = "ABAB"
print(characterReplacement(s, 2))
print()

s = "AABABBA"
print(characterReplacement(s, 1))