"""
    100. Same Tree
    Easy

    Given the roots of two binary trees p and q, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



    Example 1:
            1           1
           /\          /\
          2  3        2  3

    Input: p = [1,2,3], q = [1,2,3]
    Output: true
    Example 2:


    Input: p = [1,2], q = [1,null,2]
    Output: false
    Example 3:


    Input: p = [1,2,1], q = [1,1,2]
    Output: false


    Constraints:

    The number of nodes in both trees is in the range [0, 100].
    -104 <= Node.val <= 104
"""
from Trees.TreeNode import TreeNode


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    # if both trees are null, it can be saied both trees are same.
    if not p and not q:
        return True

    if p and q and p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)

print(isSameTree(root, head))