"""
    297. Serialize and Deserialize Binary Tree
    Hard

    Serialization is the process of converting a data structure or object into a sequence of
    bits so that it can be stored in a file or memory buffer, or transmitted across a network
    connection link to be reconstructed later in the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. There is no restriction on
    how your serialization/deserialization algorithm should work. You just need to ensure that
    a binary tree can be serialized to a string and this string can be deserialized to the
    original tree structure.

    Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
    You do not necessarily need to follow this format, so please be creative and come up with
    different approaches yourself.

    Example 1:
            1
           /\
          2  3
            /\
           4  5

    Input: root = [1,2,3,null,null,4,5]
    Output: [1,2,3,null,null,4,5]

    Example 2:

    Input: root = []
    Output: []


    Constraints:

    The number of nodes in the tree is in the range [0, 10^4].
    -1000 <= Node.val <= 1000
"""
from Trees.TreeNode import TreeNode


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string"""
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree"""
        vals = data.split(",")
        self.i = 0

        def dfs():
            # skip if node is null
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

def printTreePreorder(root):
    if not root:
        return
    print(root.val, end=' ')
    printTreePreorder(root.left)
    printTreePreorder(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
three = TreeNode(3)
root.right = three
three.left = TreeNode(4)
three.right = TreeNode(5)

ser = Codec()
print(ser.serialize(root))
deser = Codec()
ans = deser.deserialize(ser.serialize(root))

printTreePreorder(ans)
