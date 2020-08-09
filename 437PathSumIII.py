'''
437. Path Sum III
Medium

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Time O(N) Space O(N), runtime = 52 ms
    def pathSum(self, root: TreeNode, target: int) -> int:

        def one_path(node, cur_sum):
            nonlocal count

            if not node:
                return

            cur_sum += node.val
            if cur_sum - target in c_dict:
                count += c_dict[cur_sum - target]
            if cur_sum in c_dict:
                c_dict[cur_sum] += 1
            else:
                c_dict[cur_sum] = 1

            one_path(node.left, cur_sum)
            one_path(node.right, cur_sum)
            c_dict[cur_sum] -= 1

        count = 0
        c_dict = {0: 1}
        one_path(root, 0)
        return count


'''
    # Time O(N) Space O(N), runtime = 52 ms
    def pathSum(self, root: TreeNode, target: int) -> int:

        def one_path(node, cur_sum):
            nonlocal count

            if not node:
                return

            cur_sum = node.val + cur_sum
            if cur_sum == target:
                count += 1

            count += h[cur_sum - target]
            h[cur_sum] += 1    
            one_path(node.left, cur_sum)
            one_path(node.right, cur_sum)
            h[cur_sum] -= 1

        count = 0
        h = collections.defaultdict(int)
        one_path(root, 0)
        return count
'''

'''
    # Time O(N) Space O(N)
    def subarraySum(self, nums: List[int], k: int) -> int:

        sum_count_dict = {0: 1}
        s, count = 0, 0
        for n in nums:
            s += n
            if s - k in sum_count_dict:
                count += sum_count_dict[s - k]
            if s in sum_count_dict:
                sum_count_dict[s] += 1
            else:
                sum_count_dict[s] = 1
        return count
'''