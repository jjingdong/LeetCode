# 217. Contains Duplicate
# Easy
#
# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#
# Example 1:
#
# Input: [1,2,3,1]
# Output: true
# Example 2:
#
# Input: [1,2,3,4]
# Output: false
# Example 3:
#
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution:

    # [1,2,3,1]
    # [1, 1, 2, 3]
    # pre null, 1
    # cur null, 1
    # pre == cur -> yes

    # Time: O(NlogN)
    # Space: O(1)
    def containsDuplicate(self, nums: List[int]) -> bool:

        if nums is None: return False
        if nums == []: return False

        sortedNums = sorted(nums)
        pre = sortedNums[0]
        cur = sortedNums[0]
        for i in range(1, len(sortedNums)):

            cur = sortedNums[i]
            if pre == cur:
                return True

            pre = cur

        return False



