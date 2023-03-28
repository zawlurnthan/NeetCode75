"""
    104. Maximum Depth of Binary Tree
    Easy

    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path from the root node
    down to the farthest leaf node.



    Example 1:
            3
           /\
          9 20
            /\
           15 7

    Input: root = [3,9,20,null,null,15,7]
    Output: 3
    Example 2:

    Input: root = [1,null,2]
    Output: 2


    Constraints:

    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
"""
from collections import deque
from Trees.TreeNode import TreeNode


def maxDepthDfsIterative(root: TreeNode) -> int:
    stack = [(root, 1)]
    res = 0

    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))
    return res


def maxDepthBfs(root: TreeNode) -> int:
    q = deque()
    if root: q.append(root)
    level = 0

    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level


# [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
twenty = TreeNode(20)
root.right =  twenty

twenty.left = TreeNode(15)
twenty.right = TreeNode(7)

print(maxDepthDfsIterative(root))
print(maxDepthBfs(root))
