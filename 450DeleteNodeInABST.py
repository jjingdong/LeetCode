'''
450. Delete Node in a BST
Medium

2141

90

Add to List

Share
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # BST, inorder traverse in ascending order, L node R
    # successor = the smallest node after the current one, after node
    #           = one step left and then right till you can
    # predecessor = before node, the previous node, the largest node before the current one
    #             = one step right and then left till you can

    # Remove node:
    #     senario I: node is a leaf, delete it straightforward
    #     senario II: node has a right child, node replaced by successor
    #     senario III: node has not right child, but has a left child, node replaced by predecessor

    # Time O(logN) Space O(H), runtime = 80 ms
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        def successor(node):
            node = node.right
            while node.left:
                node = node.left
            return node.val

        def predecessor(node):
            node = node.left
            while node.right:
                node = node.right
            return node.val

        def delete(node, key):

            if not node:
                return None

            if node.val == key:
                # remove
                if not node.left and not node.right:
                    node = None
                elif node.right:
                    node.val = successor(node)
                    node.right = delete(node.right, node.val)
                else:
                    node.val = predecessor(node)
                    node.left = delete(node.left, node.val)
            elif node.val > key:
                node.left = delete(node.left, key)
            else:
                node.right = delete(node.right, key)

            return node

        return delete(root, key)
