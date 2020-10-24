'''
448. Find All Numbers Disappeared in an Array
Easy

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements
appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned
list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''


class Solution:

    #         4,3,2,7,8,2,3,1
    #
    #         size = 8
    #         each item: 1, 2, ... 7, 8
    #
    #         Time O(N) Space O(1)
    #
    # index = 0   1   2   3   4   5   6   7
    #         4   3   2   7   8   2   3   1
    #
    #         e.g item = 4, update index 4-1=3
    #
    #         -4  -3  -2  -7  +8  +2  -3  -1   update index(item-1)
    #                         ------
    #                         num didn't appear in index 4, 5, so the result = 5,6

    # Time O(2N) Space O(1), runtime = 372, 56.55%
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            cur = abs(nums[i])
            nums[cur - 1] = -abs(nums[cur - 1])

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result