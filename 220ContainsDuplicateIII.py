'''
220. Contains Duplicate III
Medium

Given an array of integers, find out whether there are two distinct
indices i and j in the array such that the absolute difference between
 nums[i] and nums[j] is at most t and the absolute difference between
 i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
'''


class Solution:

    #     [1,5,9,1,5,9], k = 2, t = 3
    #      i.  j
    #        i   j
    #           i   j
    #
    #     [1,2,3,1], k = 3, t = 0
    # index   0   1   2   3
    #         1   2   3   1
    #     sort
    # index  0,3      1   3
    #         1   1   2   3
    #
    # diff     0 1 2

    # nums = [-1,-1], k = 1, t = 0

    # index = 0   1   2   3
    #         1   2   3   1     k = 3       t = 0
    #         |
    #          b_dict = {1.0: 1}
    #             |
    #              b_dict = {1.0: 1, 2.0: 2}
    #                 |
    #                  b_dict = {1.0: 1, 2.0: 2, 3.0: 3}

    # Time O(N) Space O(N), runtime = 56 ms
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        if not nums or k < 0 or t < 0: return False

        b_dict = {}
        for i in range(len(nums)):
            v = nums[i] // (t + 1)
            # print(f'i = {i} nums[i] = {nums[i]} v = {v} b_dict = {b_dict}')
            if v in b_dict:
                return True
            if v - 1 in b_dict and abs(nums[i] - b_dict[v - 1]) <= t:
                return True
            if v + 1 in b_dict and abs(nums[i] - b_dict[v + 1]) <= t:
                return True
            b_dict[v] = nums[i]
            if i - k >= 0:
                b_dict.pop(nums[i - k] // (t + 1))
        return False


'''
    # Time O(N^2) Space O(1), Time Limit Exceeded
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        for i in range(len(nums)):
            right = min(i+k+1, len(nums))
            for j in range(i+1, right):

                if abs(nums[i] - nums[j]) <= t:
                    return True

        return False
'''

