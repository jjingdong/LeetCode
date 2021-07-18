'''
272. Closest Binary Search Tree Value II
Hard

Given the root of a binary search tree, a target value, and an integer k,
 return the k values in the BST that are closest to the target. You may
 return the answer in any order.

You are guaranteed to have only one unique set of k values in the BST that
 are closest to the target.



Example 1:


Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]
Example 2:

Input: root = [1], target = 0.000000, k = 1
Output: [1]


Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104.
0 <= Node.val <= 109
-109 <= target <= 109


Follow up: Assume that the BST is balanced. Could you solve it in less than
 O(n) runtime (where n = total nodes)?


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Solution I, inorder traversal + sorting
    # Time O(NlogN) Space O(N)
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:

        def dfs(node):
            # base case
            if not node:
                return

            # recursive case
            dfs(node.left)
            lst.append((abs(node.val - target), node.val))
            dfs(node.right)

        lst = []
        dfs(root)
        ll = [b for a, b in sorted(lst, key=lambda x: x[0])]

        return ll[:k]

    # Solution II: inorder traversal + sorting
    # Time O(NlogN) Space O(N)
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:

        def dfs(node):
            # base case
            if not node:
                return

            # recursive case
            dfs(node.left)
            lst.append(node.val)
            dfs(node.right)

        lst = []
        dfs(root)
        lst.sort(key=lambda x: abs(x - target))

        return lst[:k]

    # Solution III: dfs + heap
    # Time O(NlogK) Space O(K+N)
    import heapq
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:

        def dfs(node):
            # base case
            if not node:
                return

            # recursive case
            tu = (-abs(node.val - target), node.val)
            heapq.heappush(lst, tu)
            dfs(node.left)
            dfs(node.right)
            while len(lst) > k:
                heapq.heappop(lst)

        lst = []
        dfs(root)

        return [b for _, b in lst]

    # Solution IV: inorder traversal + quickselect
    # Note. didn't implement here
    # Time average O(N), worst O(N^2) Space O(N)
    import heapq
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:

        def dfs(node):
            # base case
            if not node:
                return

            # recursive case
            dfs(node.left)
            lst.append((abs(node.val - target), node.val))
            dfs(node.right)

        lst = []
        dfs(root)
        # quick select here
        # didn't implement

        return ll[:k]