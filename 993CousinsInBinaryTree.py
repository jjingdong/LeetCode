'''
993. Cousins in Binary Tree
Easy

649

39

Add to List

Share
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.



Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

# Solution I: BFS
#
# Solution II: DFS
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Solution I: BFS
    #
    # Solution II: DFS
    #

    # Time O(N) Space O(N)
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        def BFS(root):
            queue = collections.deque([(root, 0, None)])
            found_parent_val = None
            found_depth = None
            while queue != []:
                node, depth, parent_val = queue.popleft()

                if node.val == x or node.val == y:
                    if found_depth == None:
                        found_depth = depth
                        found_parent_val = parent_val
                    else:
                        if found_depth == depth and found_parent_val != parent_val:
                            return True
                        else:
                            return False

                if node.left is not None:
                    queue.append((node.left, depth + 1, node.val))
                if node.right is not None:
                    queue.append((node.right, depth + 1, node.val))

            return False

        if root is None: return None
        return BFS(root)



