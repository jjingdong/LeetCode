'''
1. Two Sum
Easy

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution:

    # Solution I: Brute Force
    # Time O(N^2), Space O(1)
    #
    # Solution II: Hash Table
    # Time O(N), Space O(N)
    # [2, 7, 11, 15]
    # dict = {2:0, 7:1, 11:2, 15:3}
    # find if the each item's complement is in the dict
    #

    # Time O(N) Space O(N), Use Hash Table
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if nums is None: return None

        index_dict = {}
        for i in range(len(nums)):
            index_dict[nums[i]] = i
        print(index_dict)

        for i in range(len(nums)):
            rest = target - nums[i]
            print(rest)
            if rest in index_dict and index_dict[rest] != i:
                return [i, index_dict[rest]]

        return []
