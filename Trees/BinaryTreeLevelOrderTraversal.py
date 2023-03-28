"""
    102. Binary Tree Level Order Traversal
    Medium

    Given the root of a binary tree, return the level order traversal of its nodes' values.
    (i.e., from left to right, level by level).

    Example 1:
                3
               /\
              9 20
                /\
               15 7

    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

    Example 2:
    Input: root = [1]
    Output: [[1]]

    Example 3:
    Input: root = []
    Output: []


    Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
"""
from collections import deque
from typing import List
from Trees.TreeNode import TreeNode

def levelOrder(root: TreeNode) -> List[List[int]]:
    q = deque()
    if root: q.append(root)
    ans = []

    while q:
        level = []
        
        for i in range(len(q)):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
    return ans


root = TreeNode(3)
twenty = TreeNode(20)
root.left = TreeNode(9)
root.right = twenty

twenty.left = TreeNode(15)
twenty.right = TreeNode(7)
print(levelOrder(root))


root = TreeNode(1)
print(levelOrder(root))

root = TreeNode()
print(levelOrder(root))