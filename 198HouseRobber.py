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

    # E.g.    [2, 7, 9, 3, 1]
    #         2, 2 or 7, 2+9 or 7, 3+7, or 11, 11+1 or 11
    # global: 2, 7, 11, 11, 12

    # Time O(N) Space O(1), basically a fibnacchi
    # runtime = 32 ms
    def rob(self, nums: List[int]) -> int:

        if nums is None: return None
        if nums == []: return 0
        if len(nums) == 1: return nums[0]

        cur, pre, prepre = 0, nums[0], 0
        for i in range(1, len(nums)):
            cur = max(pre, nums[i] + prepre)
            prepre = pre
            pre = cur

        return cur


'''                  
    def rob_elliott(nums: List[int]) -> int:
        dp = [0, 0]
        for n in nums:
            dp[0], dp[1] = dp[1], max(dp[0] + n, dp[1])
        return dp[1]

    def rob_gregory(nums: List[int]) -> int:
        house_0, house_1 = 0, 0
        for house in nums:
            house_1, house_0 = max(house_0 + house, house_1), house_1
        return house_1

    def rob_hugh(nums: List[int]) -> int:
        # 28ms beats 85%
        # memory beats 48%
        N = len(nums)
        if N <= 2:
            return N and max(nums)
        nums[2] = max(nums[0] + nums[2], nums[1])
        for i in range(3, N):
            nums[i] += max(
                nums[i - 3],
                nums[i - 2],
                nums[i - 1] - nums[i]
            )
        return nums[-1]
'''