"""
    20. Valid Parentheses

    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.


    Example 1:

    Input: s = "()"
    Output: true
    Example 2:

    Input: s = "()[]{}"
    Output: true
    Example 3:

    Input: s = "(]"
    Output: false


    Constraints:

    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'.
"""

def isValidByNeetCode(s: str) -> bool:
    mapping = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        if c not in mapping:
            # collect opening brackets if it's not dictionary key
            stack.append(c)
            continue
            # check if current opening bracket matches with previous bracket
        if not stack or stack[-1] != mapping[c]:
            return False
        stack.pop()
    # stack should be empty after each match
    return not stack


def isValid(s: str) -> bool:
    mapping = {'(': ')', '{': '}','[': ']'}
    stack = []

    for c in s:
        if c in mapping:
            # collect opening brackets if it's in dictionary
            stack.append(c)

        # check if current closing bracket matches with previous opening bracket
        # and stack is not empty
        elif not stack or mapping[stack.pop()] != c:
            return False

    return not stack


s = "()"
print(isValid(s))

s = "()[]{}"
print(isValid(s))

s = "(]"
print(isValid(s))

s = "]"
print(isValid(s))

s = "){"
print(isValid(s))

s = ")(){}"
print(isValid(s))

