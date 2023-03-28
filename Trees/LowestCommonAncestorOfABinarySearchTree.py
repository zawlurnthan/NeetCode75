"""
    235. Lowest Common Ancestor of a Binary Search Tree
    Medium

    Given a binary search tree (BST), find the lowest common ancestor (LCA) node
    of two given nodes in the BST.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor
    is defined between two nodes p and q as the lowest node in T that has both p
    and q as descendants (where we allow a node to be a descendant of itself).”

    Example 1:
                6
               /\
             2    8
            /\   /\
           0  4 7  9
             /\
            3  5

    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    Output: 6
    Explanation: The LCA of nodes 2 and 8 is 6.

    Example 2:
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    Output: 2
    Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of
    itself according to the LCA definition.

    Example 3:
    Input: root = [2,1], p = 2, q = 1
    Output: 2


    Constraints:

    The number of nodes in the tree is in the range [2, 105].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q will exist in the BST.
"""

from Trees.TreeNode import TreeNode


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    curr = root
    while curr:
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        else:
            return curr


head = TreeNode(6)
two = TreeNode(2)
eight = TreeNode(8)
four = TreeNode(4)

head.left = two
head.right = eight

two.left = TreeNode(0)
two.right = four

four.left = TreeNode(3)
four.right = TreeNode(5)

eight.left = TreeNode(7)
eight.right = TreeNode(9)

print(lowestCommonAncestor(head, TreeNode(2), TreeNode(8)).val)
print(lowestCommonAncestor(head, TreeNode(2), TreeNode(4)).val)

node = TreeNode(2)
node.left = TreeNode(1)
print(lowestCommonAncestor(head, TreeNode(2), TreeNode(1)).val)


