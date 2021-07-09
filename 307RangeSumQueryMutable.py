'''
307. Range Sum Query - Mutable
Medium

Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive
 where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between
indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8


Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.
'''


# index =     0   1   2
#             1,  3,  5

#     range 0-2   1+3+5 = 9


# index =     0   1   2   3   4
#             1,  3,  5,  7,  9
#             _
#             ------
#             ---------
#     acc_sum 1   4   9   16  25

#                     (2,4) = 5+7+9 = 21 = (2)+(3)+(4) = (0-4)- (0-1) = 21 - 4 = 21

#         range(i,j) = acc_sum(j) - acc_sum(i-1)

# class NumArray:
#     # Time Limit Exceeded
#     def __init__(self, nums: List[int]):

#         self.nums = nums
#         size = len(nums)
#         self.acc_sum = [0] * size
#         self.acc_sum[0] = self.nums[0]
#         for i in range(1, size):
#             self.acc_sum[i] = self.acc_sum[i-1] + nums[i]

#     def update(self, index: int, val: int) -> None:

#         pre_val = self.nums[index]
#         self.nums[index] = val
#         diff = val - pre_val
#         for i in range(index, len(self.nums)):
#             self.acc_sum[i] += diff

#     def sumRange(self, left: int, right: int) -> int:

#         if left == 0:
#             return self.acc_sum[right]

#         return self.acc_sum[right] - self.acc_sum[left-1]

# ------------------------------------------------------------------------


# StefanPochmann's solution
#     def __init__(self, nums: List[int]):

#         self.update = nums.__setitem__
#         self.sumRange = lambda i, j: sum(nums[i:j+1])


# --------------------------------------------------------------------------
#               total = 16
#     index =  0  1   2   3
#             [1, 3,  5,  7]
#                 /   \
#     total = 4            total = 12
#     index = 0   1        index = 2  3
#            [1,  3]              [5  7]
#         /          \           /           \
# total = 1      total = 3     total = 5     total = 7
# index = 0      index = 1     index = 2     index = 3
#        [1]            [3]           [5]           [7]

# Note. use Segment Tree
class TreeNode:
    def __init__(self, s, e, total=0, left=None, right=None):
        self.total = total
        self.s = s
        self.e = e
        self.left = None
        self.right = None


class NumArray:

    # O(N) -> O(logN)
    def __init__(self, nums: List[int]):
        # i        j
        # [2, 4, 6, 8]

        def create_tree(i, j):

            # base case
            if i > j:
                return None
            if i == j:
                return TreeNode(i, j, nums[i])

            # recursive case
            node = TreeNode(i, j)
            m = (i + j) // 2
            node.left = create_tree(i, m)
            node.right = create_tree(m + 1, j)
            node.total = node.left.total + node.right.total
            return node

        self.root = create_tree(0, len(nums) - 1)

    # O(1) -> O(logN)
    def update(self, index: int, val: int) -> None:

        def update_tree(node, index, val):

            # base case
            if node.s == node.e == index:
                node.total = val
                return val

            # recursive case
            m = (node.s + node.e) // 2
            #             1, 3, 5, 7, 9
            #                m     i

            #             1, 3, 5, 7, 9
            #                i  m

            #             1, 3, 5, 7, 9
            #                   m
            #                   i

            if index > m:
                update_tree(node.right, index, val)
            elif index <= m:
                update_tree(node.left, index, val)

            node.total = node.left.total + node.right.total
            return node.total

        return update_tree(self.root, index, val)

        # O(N) -> O(logN)

    def sumRange(self, left: int, right: int) -> int:

        def cal_tree(node, i, j):

            # base case
            if node.s == i and node.e == j:
                return node.total

            # recursive case
            m = (node.s + node.e) // 2

            # ..., 1, 3, 5, 7]
            #         l     r
            #      |
            #      m

            if i >= m + 1:
                return cal_tree(node.right, i, j)
            # ..., 1, 3, 5, 7, .....
            #         l     r
            #                 |
            #                 m
            if m >= j:
                return cal_tree(node.left, i, j)

            return cal_tree(node.left, i, m) + cal_tree(node.right, m + 1, j)

        return cal_tree(self.root, left, right)


'''   
# Note. Use binary index tree
    def __init__(self, nums):
        self.arr = [0] * len(nums)
        self.BIT = [0] * (len(nums) + 1)
        for i, n in enumerate(nums): self.update(i, n)
        self.sumRange = lambda i, j: self.Sum(j + 1) - self.Sum(i)

    def update(self, i, val):
        diff, self.arr[i] = val - self.arr[i], val
        i += 1
        while i < len(self.BIT):
            self.BIT[i] += diff
            i += (i & -i)

    def Sum(self, k):
        res = 0
        while k:
            res += self.BIT[k]
            k -= (k & -k)
        return res    
'''

'''  
# Pythong NumPy solution
import numpy as np

class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = np.array(nums)

    def update(self, index: int, val: int) -> None:
        self.arr[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return np.sum(self.arr[left:right+1])
'''

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

