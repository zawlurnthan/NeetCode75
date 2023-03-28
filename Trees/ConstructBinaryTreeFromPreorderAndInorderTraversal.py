"""
    105. Construct Binary Tree from Preorder and Inorder Traversal
    Medium

    Given two integer arrays preorder and inorder where preorder is the preorder traversal
    of a binary tree and inorder is the inorder traversal of the same tree, construct and
    return the binary tree.

    Example 1:
            3
           /\
          9 20
            /\
          15  7

    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]
    Example 2:

    Input: preorder = [-1], inorder = [-1]
    Output: [-1]


    Constraints:

    1 <= preorder.length <= 3000
    inorder.length == preorder.length
    -3000 <= preorder[i], inorder[i] <= 3000
    preorder and inorder consist of unique values.
    Each value of inorder also appears in preorder.
    preorder is guaranteed to be the preorder traversal of the tree.
    inorder is guaranteed to be the inorder traversal of the tree.
"""
from typing import List
from Trees.TreeNode import TreeNode


def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    # get index of the root in inorder list
    mid = inorder.index(preorder[0])
    # print("mid: ", mid, " root: ", preorder[0])
    #                      preorder[9 : 20], inorder[:9}
    # get rid of root from preorder and set it till to the index of root
    root.left = buildTree(preorder[1 : mid + 1], inorder[:mid])
    # print("Left Side -> Preorder: ", preorder[1:mid+1], " Inorder: ", inorder[:mid])
    # # star form 20 to the rest, preorder[20: ], inorder[20:]
    root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])
    # print("Right Side -> Preorder: ", preorder[mid + 1: ], " Inorder: ", inorder[mid + 1:])
    return root


# def buildTreeSomeoneElse(preorder: List[int], inorder: List[int]) -> TreeNode:
#     if inorder:
#         ind = inorder.index(preorder.pop(0))
#         print("Index: ", 0, " value: ", ind)
#         root = TreeNode(inorder[ind])
#         root.left = buildTreeSomeoneElse(preorder, inorder[0:ind])
#         root.right = buildTreeSomeoneElse(preorder, inorder[ind + 1:])
#         return root


def printTreePreorder(root: TreeNode):
    if not root:
        return

    print(root.val, end=' ')
    printTreePreorder(root.left)
    printTreePreorder(root.right)

def printTreeInorder(root: TreeNode):
    if not root:
        return

    printTreeInorder(root.left)
    print(root.val, end=' ')
    printTreeInorder(root.right)

def printTreePostorder(root: TreeNode):
    if not root:
        return

    printTreePostorder(root.left)
    printTreePostorder(root.right)
    print(root.val, end=' ')



preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

printTreePreorder(buildTree(preorder, inorder))
print()
# printTreeInorder(buildTree(preorder, inorder))
# print()
# printTreePostorder(buildTree(preorder, inorder))
# print()



preorder = [-1]
inorder = [-1]
