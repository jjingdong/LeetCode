'''
701. Insert into a Binary Search Tree
Medium

1170

86

Add to List

Share
You are given the root node of a binary search tree (BST) and a value to insert
 into the tree. Return the root node of the BST after the insertion. It is
 guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as
the tree remains a BST after insertion. You can return any of them.



Example 1:


Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]


Constraints:

The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Solution I: recursion
    # Solution II: iteration

    #         no node -> insert the node
    #         one node: 7
    #             1. insert to the left
    #                     7
    #                   /
    #                 5
    #             2. insert to the right
    #                     7
    #                       \
    #                         8
    #         two or more nodes:
    #                     40
    #             20               70
    #         10       30
    #                     insert 50, 80, 25, 15, 5, 35

    #         basically binary search

    # Time O(H) Space O(1), runtime = 132 ms
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        to_insert = TreeNode(val)
        if not root:
            root = to_insert
            return root

        node = root
        while node:
            if val < node.val:
                if not node.left:
                    node.left = to_insert
                    return root
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = to_insert
                    return root
                else:
                    node = node.right

        return root


'''
    # Time O(H), average O(logN), if the tree is balanced O(logN) Space O(H), runtime = 128 ms
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        def search(node):
            if to_insert.val > node.val:
                if not node.right:
                    node.right = to_insert
                else:
                    search(node.right)
            elif to_insert.val < node.val:
                if not node.left:
                    node.left = to_insert
                else:
                    search(node.left)


        to_insert = TreeNode(val)

        if not root:
            root = to_insert

        search(root)
        return root
'''



