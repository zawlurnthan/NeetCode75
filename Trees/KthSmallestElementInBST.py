"""
    230. Kth Smallest Element in a BST
    Medium

    Given the root of a binary search tree, and an integer k, return the kth smallest value
    (1-indexed) of all the values of the nodes in the tree.



    Example 1:
            3
           /\
          1  4
          \
           2

    Input: root = [3,1,4,null,2], k = 1
    Output: 1


    Example 2:
                        5
                       /\
                      3  6
                     /\
                    2  4
                   /
                  1

    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3


    Constraints:

    The number of nodes in the tree is n.
    1 <= k <= n <= 104
    0 <= Node.val <= 104


    Follow up: If the BST is modified often (i.e., we can do insert and delete operations)
    and you need to find the kth smallest frequently, how would you optimize?
"""
from Trees.TreeNode import TreeNode


def kthSmallest(root: TreeNode, k: int) -> int:
    stack = []
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        # keep popping til reaching target number
        curr = stack.pop()
        k -= 1
        if k == 0:
            # return target value
            return curr.val
        curr = curr.right


head = TreeNode(3)
one = TreeNode(1)
head.left = one
head.right = TreeNode(4)
one.right = TreeNode(2)
print(kthSmallest(head, 1))

node = TreeNode(5)
three = TreeNode(3)
two = TreeNode(2)

node.left = three
node.right = TreeNode(6)
three.left = two
three.right = TreeNode(4)
two.left = TreeNode(1)
print(kthSmallest(node, 3))
