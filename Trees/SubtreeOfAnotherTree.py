"""
    572. Subtree of Another Tree
    Easy

    Given the roots of two binary trees root and subRoot, return true if there is a subtree of
    root with the same structure and node values of subRoot and false otherwise.

    A subtree of a binary tree tree is a tree that consists of a node in tree and all of this
    node's descendants. The tree tree could also be considered as a subtree of itself.


    Example 1:
            root
              3
             /\         subroot
            4  5            4
           / \             /\
         1    2           1  2
    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: true
    Example 2:


    Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    Output: false


    Constraints:

    The number of nodes in the root tree is in the range [1, 2000].
    The number of nodes in the subRoot tree is in the range [1, 1000].
    -10^4 <= root.val <= 10^4
    -10^4 <= subRoot.val <= 10^4
"""
from Trees.TreeNode import TreeNode


def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    if not subRoot:
        return True
    if not root:
        return False

    # check if two trees are same
    if sameTree(root, subRoot):
        return True
    # continue checking for similarity
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

def sameTree(s: TreeNode, t: TreeNode) -> bool:
    # if both trees are null, it can be saied both trees are same.
    if not s and not t:
        return True

    if s and t and s.val == t.val:
        return sameTree(s.left, t.left) and sameTree(s.right, t.right)
    else:
        return False


root = TreeNode(3)
four = TreeNode(4)
root.right = TreeNode(5)
root.left = four
four.left = TreeNode(1)
four.right = TreeNode(2)

head = TreeNode(4)
head.left = TreeNode(1)
head.right = TreeNode(2)
print(isSubtree(root, head))