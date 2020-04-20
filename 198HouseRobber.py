# 198. House Robber
#
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
# Example 1:
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.


class Solution:

    # E.g. [1, 2, 3, 1]

    #      1, 1 or 2, 1+3 or 2, 1 + 2 or 4
    # pre:
    # global:1, 2, 4, 4

    # E.g. [2, 7, 9, 3, 1]
    #         2, 2 or 7, 2+9 or 7, 3+7, or 11, 11+1 or 11
    # global: 2, 7, 11, 11, 12

    # Time: O(N)
    # Space: O(1)
    def rob(self, nums: List[int]) -> int:

        if nums is None: return None
        if nums == []: return 0

        preMax = nums[0]  # 2
        result = nums[0]  # 2
        prepre = 0  # 0

        for i in range(1, len(nums)):

            cur = nums[i]  # 7

            if pre > cur + prepre:
                result = pre  #

            elif pre <= cur + prepre:
                result = cur + prepre  # result = 7

            prepre = pre  #
            pre = result  #

        return result




