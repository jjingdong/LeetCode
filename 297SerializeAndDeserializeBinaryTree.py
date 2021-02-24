'''
297. Serialize and Deserialize Binary Tree
Hard

Serialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no
restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes
a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.



Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,2]
Output: [1,2]


Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        # output = '1,2,3,None,None,4,None,None,5,None,None,.'
        # preorder: opeartion on the node, l subtree, r subtree
        def helper(node):
            nonlocal result

            if node is None:
                result += 'None,'
                return

            result += str(node.val) + ','
            helper(node.left)
            helper(node.right)

        result = ''
        helper(root)
        return result + '.'

    #         None None 5     None None  4     3      None None 2  1
    #          |    |
    #          r    l  node
    #                         |      |
    #                         r      l  node

    #             |                 |          |       |    |
    #             r                 l         node     r    l  node

    #                            |                        |        |
    #                            r                        l       node

    #                 1
    #                / \
    #               2   3
    #                  / \
    #                 4   5
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode

        """

        def helper(q):
            item = q.popleft()
            if item == 'None':
                return

            node = TreeNode(item)
            node.left = helper(q)
            node.right = helper(q)
            return node

        lst = data.split(',')
        q = collections.deque(lst)
        return helper(q)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))