'''
106. Construct Binary Tree from Inorder and Postorder Traversal
Medium

Given inorder and postorder traversal of a tree, construct the binary tree.
Note: You may assume that duplicates do not exist in the tree.
For example, given
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #     From Eliot:
    #             def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    #         pointer = -1
    #         def helper(lo,hi):
    #             nonlocal pointer
    #             if hi-lo < 1: return None

    #             mid = inorder.index(postorder[pointer],lo,hi)
    #             pointer -= 1

    #             root = TreeNode(inorder[mid])
    #             root.right = helper(mid+1,hi)
    #             root.left = helper(lo,mid)

    #             return root

    # Time O(N*H) Space O(1), runtime = 244 ms
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def buildNode(inorder, postorder):

            if not inorder:
                return

            if len(inorder) == 1:
                return TreeNode(inorder[0])

            root_val = postorder[-1]
            root = TreeNode(root_val)
            i = inorder.index(root_val)

            root.left = buildNode(inorder[:i], postorder[:i])
            root.right = buildNode(inorder[i + 1:], postorder[i:-1])
            return root

        if not inorder or not postorder: return None
        if len(inorder) != len(postorder): return None

        return buildNode(inorder, postorder)


'''
    # Time O(N^N) Space O(N), runtime = 712ms, faster than 5% of Python3 submissions
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def buildNode(inorder, postorder):

            if not inorder:
                return

            if len(inorder) == 1:
                return TreeNode(inorder[0])

            root_val = postorder[-1]
            root = TreeNode(root_val)

            inorder_left = []
            for i in range(len(inorder)):
                if inorder[i] == root_val:
                    break
                inorder_left.append(inorder[i])
            inorder_right = inorder[i+1:]
            postorder_left = postorder[:i]
            postorder_right = postorder[i:-1]

            root.left = buildNode(inorder_left, postorder_left)
            root.right = buildNode(inorder_right, postorder_right)
            return root


        if not inorder or not postorder: return None
        if len(inorder) != len(postorder): return None

        return buildNode(inorder, postorder)
'''
