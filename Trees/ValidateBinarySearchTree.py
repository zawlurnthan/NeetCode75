"""
    98. Validate Binary Search Tree
    Medium

    Given the root of a binary tree, determine if it is a valid binary search tree (BST).

    A valid BST is defined as follows:

    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.


    Example 1:


    Input: root = [2,1,3]
    Output: true

    Example 2:
            5
           /\
          1  4
            /\
           3  6

    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.


    Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1
"""
from Trees.TreeNode import TreeNode


def isValidBST(root: TreeNode) -> bool:
    def valid(node, left, right):
        if not node:
            return True

        if not (right > node.val > left):
            return False
        # continue checking for left and right subtree
        #            (node, left, right = parent)        and     (node, left = parent, right)
        return valid(node.left, left, node.val) and valid(node.right, node.val, right)
    #           (root, left, right)
    return valid(root, float('-inf'), float('inf'))



root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(isValidBST(root))

root = TreeNode(5)
root.left = TreeNode(1)
four = TreeNode(4)
root.right = four

four.left = TreeNode(3)
four.right = TreeNode(6)
print(isValidBST(root))