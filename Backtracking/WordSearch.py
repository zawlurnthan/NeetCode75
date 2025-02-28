"""
    79. Word Search
    Medium

    Given an m x n grid of characters board and a string word, return true if word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
    horizontally or vertically neighboring. The same letter cell may not be used more than once.

    Example 1:


    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true
    Example 2:


    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: true
    Example 3:


    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: false


    Constraints:

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.


    Follow up: Could you use search pruning to make your solution faster with a larger board?
"""
from collections import defaultdict, Counter
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])
    path = set()

    def dfs(r, c, i):
        # if word is found (doesn't make sense ! for me)
        if i == len(word):
            return True

        # if out of bound
        if (
            min(r, c) < 0 or
            r >= ROWS or
            c >= COLS or
            # if word is not same
            word[i] != board[r][c] or
            (r, c) in path
        ):
            return False

        # add word if it's found
        path.add((r, c))
        # search in 4 different directions of current node
        res = (
            dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1)
        )
        path.remove((r, c))
        return res

    # To prevent TLE, reverse the word if frequency of the first letter is more than last letter's
    count = defaultdict(int, sum(map(Counter, board), Counter()))
    if count[word[0]] > count[word[-1]]:
        word = word[::-1]

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True
    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(exist(board, word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(exist(board, word))


