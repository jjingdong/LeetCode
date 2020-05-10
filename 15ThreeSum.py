'''
15. 3Sum
Medium

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution:

    # Solution:
    # 3Sum problem = value + 2Sum problem
    # [-4, -1, -1, 0, 1, 2]
    # value = -4, rest = 4, looking for a + b = 4
    # value = -1, rest = 1, looking for a + b = 1
    # value = 0, rest = 0, looking for a + b = 0

    # Time O(N^2) Space O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        results = []
        size = len(nums)

        for i in range(size - 2):
            rest = -nums[i]
            if rest >= 0:

                if i == 0 or nums[i] != nums[i - 1]:
                    j = i + 1
                    k = size - 1
                    while j < k:
                        sum = nums[i] + nums[j] + nums[k]

                        if sum < 0:
                            j += 1
                        elif j > i + 1 and nums[j] == nums[j - 1]:
                            j += 1
                        elif sum > 0:
                            k -= 1
                        elif k < size - 1 and nums[k] == nums[k + 1]:
                            k -= 1
                        elif sum == 0:
                            results.append([nums[i], nums[j], nums[k]])
                            j += 1
                            k -= 1

        return results


