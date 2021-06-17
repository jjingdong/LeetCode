'''
795. Number of Subarrays with Bounded Maximum
Medium

We are given an array nums of positive integers, and two positive integers left
and right (left <= right).

Return the number of (contiguous, non-empty) subarrays such that the value of
the maximum array element in that subarray is at least left and at most right.

Example:
Input:
nums = [2, 1, 4, 3]
left = 2
right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Note:

left, right, and nums[i] will be an integer in the range [0, 109].
The length of nums will be in the range of [1, 50000].

'''


class Solution:

    #                         x   x   x   x
    #                         -
    #                  ans =  1
    #                             _
    #                         -----
    #                  ans =  1 + 2
    #                                 -
    #                            ------
    #                         ---------
    #                  ans = 1 + 2 + 3
    #                                    -
    #                                -----

    #                     2   1   4   3       left=2, right=3

    #                 a = 1   1   0   1

    #                 i = 0   1   2   3
    #                     2   1   4   3       i=3, cur=3
    #                                 -
    #                         /               \                          \
    #                     cur < left       cur in [left, right]     cur > right
    #                   cur_ans=cur_ans                   /    \           cur_ans = 0
    #                                 pre=4 >right   else:
    #                                 cur_ans = 1    cur_ans=pre_ans+1

    #                     i = 0   1   2   3
    #                         2   1   4   3
    #             cur_ans   = 1   1   0   1
    #             ans = 3

    #             index = 0   1   2   3   4
    #                 i = -1  0   1   2   3
    #               cur =     2   1   4   3
    #             cur_ans   = 1   1   0   1
    #             ans = 3

    # Time O(N) Space O(N)
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:

        size = len(nums)
        cur_ans = [0] * (size + 1)
        s = 0

        pre = right + 1
        for index in range(1, size + 1):
            i = index - 1
            cur = nums[i]
            if i > 0:
                pre = nums[i - 1]

            if pre > right:
                s = index

            if cur < left:
                cur_ans[index] = cur_ans[index - 1]
            elif cur > right:
                cur_ans[index] = 0
            else:
                cur_ans[index] = index - s + 1

        return sum(cur_ans)

    # Time O(N) Space O(1)
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:

        size = len(nums)
        result = 0

        pre = right + 1
        cur_ans = 0
        pre_ans = 0
        for index in range(1, size + 1):
            i = index - 1
            cur = nums[i]
            if i > 0:
                pre = nums[i - 1]

            if pre > right:
                s = index

            if cur < left:
                cur_ans = pre_ans
            elif cur > right:
                cur_ans = 0
            else:
                cur_ans = index - s + 1

            result += cur_ans
            pre_ans = cur_ans

        return result

    # Note. this is from solution
    # Time O(N) Space O(1)
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:

        def count(bound):
            ans = cur = 0
            for x in nums:
                cur = cur + 1 if x <= bound else 0
                ans += cur
            return ans

        print(count(right))
        return count(right) - count(left - 1)


