"""
    125. Valid Palindrome
    Easy

    A phrase is a palindrome if, after converting all uppercase letters into lowercase
    letters and removing all non-alphanumeric characters, it reads the same forward and
    backward. Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

    Example 1:

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

    Example 2:

    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.
    
    Example 3:

    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

    Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
"""


def alphanum(c):
    return (
        ord("A") <= ord(c) <= ord("Z") or
        ord("a") <= ord(c) <= ord("z") or
        ord("0") <= ord(c) <= ord("9")
    )


def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not alphanum(s[l]):
            l += 1
        while l < r and not alphanum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


def isPalindromeAnotherWay(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        # skip if char is not alpha or number
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        # check if two chars of left and right are same or not
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


def isPalindromeMyWay(s: str) -> bool:
    # remove special characters and convert to lowercase
    s = "".join(c for c in s if c.isalnum()).lower()
    # check if it's palindrome by comparing normal and reverse string
    return s == s[::-1]



s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
print(isPalindromeMyWay(s))
print(isPalindromeAnotherWay(s))


# s = "race a car"
# print(isPalindrome(s))
# print(isPalindromeMyWay(s))
#
# s = " "
# print(isPalindrome(s))
# print(isPalindromeMyWay(s))


