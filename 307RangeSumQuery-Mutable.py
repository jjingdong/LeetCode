'''
307. Range Sum Query - Mutable
Medium

Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right
inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums
between indices left and right inclusive (i.e. nums[left] + nums[left + 1]
+ ... + nums[right]).


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


# solution from Discuss session
# Note. there is an error on this
class Node():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None


class NumArray:
    def __init__(self, nums: List[int]):

        def build_tree(nums, l, r):
            if l > r:
                return None

            if l == r:
                node = Node(l, r)
                node.total = nums[l]
                return node

            m = (l + r) // 2
            root = Node(l, r)

            root.left = build_tree(nums, l, m)
            root.right = build_tree(nums, m + 1, r)
            root.total = root.left.total + root.right.total

            return root

        self.root = build_tree(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:

        def update_tree(root, i, val):
            if root.start == root.end:
                root.total = val
                return val

            mid = (root.start + root.end) // 2

            if i <= mid:
                update_tree(root.left, i, val)
            else:
                update_tree(root.right, i, val)
            root.total = root.left.total + root.right.total

            return root.total

        return update_tree(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:

        def tree_range_sum(root, i, j):

            if root.start == i and root.end == j:
                return root.total

            mid = (root.start + root.end) // 2

            if j <= mid:
                return tree_range_sum(root.left, i, j)
            elif i >= mid + 1:
                return tree_range_sum(root.left, i, mid) + tree_range_sum(root.right, mid + 1, j)

        return tree_range_sum(self.root, left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

