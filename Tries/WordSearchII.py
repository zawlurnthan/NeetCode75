"""
    212. Word Search II
    Hard

    Given an m x n board of characters and a list of strings words, return all words on the board.

    Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells
    are horizontally or vertically neighboring. The same letter cell may not be used more than once
    in a word.


    Example 1:
    |o|a|a|n|
    |e|t|a|e|
    |i|h|k|r|
    |i|f|l|v|

    Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words
    = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]

    Example 2:
    |a|b|
    |c|d|

    Input: board = [["a","b"],["c","d"]], words = ["abcb"]
    Output: []


    Constraints:

    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] is a lowercase English letter.
    1 <= words.length <= 3 * 104
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.
    All the strings of words are unique.
"""
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        curr = self
        curr.refs += 1
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.refs += 1
        curr.isWord = True

    def removeWord(self, word):
        curr = self
        curr.refs -= 1
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
                curr.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            # add all word from the list to the TrieNode Data Structure
            # create TrieNodes for each word of list
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            # skip if a node is out of bound or visited
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                # if word is not same
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visit
            ):
                return

            # mark as visited
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                # remove the node from the TrieNode (list) to avoid repeatedly search
                root.removeWord(word)

            # search in four directions (N, S, E, W) of current node
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            # remove after visiting
            visit.remove((r, c))

        # loop through all rows by cols of matrix to find how many words match
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)



board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
obj = Solution()
print(obj.findWords(board, words))

board = [["a", "b"], ["c", "d"]]
words = ["abcb"]
print(obj.findWords(board, words))