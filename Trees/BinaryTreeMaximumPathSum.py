"""
    124. Binary Tree Maximum Path Sum
    Hard

    A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the
    sequence has an edge connecting them. A node can only appear in the sequence at most once.
    Note that the path does not need to pass through the root.

    The path sum of a path is the sum of the node's values in the path.

    Given the root of a binary tree, return the maximum path sum of any non-empty path.

    Example 1:
            1
           /\
          2  3
    Input: root = [1,2,3]
    Output: 6
    Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

    Example 2:
            -10
             /\
            9  20
              /\
            15  7

    Input: root = [-10,9,20,null,null,15,7]
    Output: 42
    Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


    Constraints:

    The number of nodes in the tree is in the range [1, 3 * 104].
    -1000 <= Node.val <= 1000
"""
from Trees.TreeNode import TreeNode


def maxPathSum(root: TreeNode) -> int:
    res = [root.val]
    # return max path sum without split
    def dfs(root):
        if not root:
            return 0

        leftMax = dfs(root.left)
        rightMax = dfs(root.right)
        #leftMax = max(leftMax, 0)
        #rightMax = max(rightMax, 0)

        # compute max path sum with split
        res[0] = max(res[0], root.val + leftMax + rightMax)
        return root.val + max(leftMax, rightMax)

    dfs(root)
    return res[0]

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
print(maxPathSum(head))

node = TreeNode(-10)
node.left = TreeNode(9)
twenty = TreeNode(20)
node.right = twenty

twenty.left = TreeNode(15)
twenty.right = TreeNode(7)
print(maxPathSum(node))
