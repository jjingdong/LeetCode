'''
35. Search Insert Position
Easy

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Example 1:
Input: [1,3,5,6], 5
Output: 2
Example 2:
Input: [1,3,5,6], 2
Output: 1
Example 3:
Input: [1,3,5,6], 7
Output: 4
Example 4:
Input: [1,3,5,6], 0
Output: 0

'''


class Solution:

    #     index = 0, 1, 2, 3
    #            [1, 3, 5, 6], 0
    #                |
    #            [1] 0
    #
    #     index = 0, 1, 2, 3
    #            [1, 3, 5, 6], 7
    #                |
    #            [5, 6] 7
    #
    #     index = 0, 1, 2, 3
    #            [1, 3, 5, 6], 2
    #                |
    #            [1] 2

    # Time O(NlogN) Space O(1), runtime = 104 ms
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


'''
    # Time O(NlogN) Space O(1), runtime - 40 ms
    def searchInsert(self, nums: List[int], target: int) -> int:

        if not nums or not target: return 0

        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            m_value = nums[mid]
            if m_value == target:
                return mid
            elif m_value > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
'''

