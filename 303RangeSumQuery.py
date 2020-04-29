'''
303. Range Sum Query - Immutable
Easy

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
Example: 
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note: 
	1.	You may assume that the array does not change.
	2.	There are many calls to sumRange function.
'''


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.accNums = nums
        for i in range(1, len(self.nums)):
            self.accNums[i] = self.accNums[i - 1] + self.accNums[i]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.accNums[j]
        else:
            return self.accNums[j] - self.accNums[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# class NumArray:

#     def __init__(self, nums):
#         self.nums = nums
#         for i in range(1, len(nums)):
#             self.nums[i] += self.nums[i - 1]


#     def sumRange(self, i, j):
#         return self.nums[j] - self.nums[i - 1] if i else self.nums[j]