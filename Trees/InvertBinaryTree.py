"""
    226. Invert Binary Tree
    Easy

    Given the root of a binary tree, invert the tree, and return its root.



    Example 1:
            4                   4
           /\                  /\
         2   7      ->       7   2
        /\   /\             /\  /\
       1  3 6  9           9 6 3  1

    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]
    Example 2:


    Input: root = [2,1,3]
    Output: [2,3,1]
    Example 3:

    Input: root = []
    Output: []


    Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
"""
from collections import deque
from Trees.TreeNode import TreeNode


def invertTree(root: TreeNode) -> TreeNode:
    if not root: return None

    # swap children
    temp = root.left
    root.left = root.right
    root.right = temp

    invertTree(root.left)
    invertTree(root.right)
    return root

def printTreeBFS(root: TreeNode):
    if not root: return
    queue = deque([root])

    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            print(node.val, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


# [4,2,7,1,3,6,9]
root = TreeNode(4)
two = TreeNode(2)
seven = TreeNode(7)
root.left, root.right = two, seven

two.left = TreeNode(1)
two.right = TreeNode(3)

seven.left = TreeNode(6)
seven.right = TreeNode(9)

printTreeBFS(root)
print()
printTreeBFS(invertTree(root))


