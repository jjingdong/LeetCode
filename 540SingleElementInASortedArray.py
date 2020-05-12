'''
540. Single Element in a Sorted Array
Medium

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.
 
Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
 
Note: Your solution should run in O(log n) time and O(1) space.
'''


class Solution:

    # Solution I: nums[i] != nums[i-1]. Time O(N)
    #
    # Solution II: Boyer-Moore Voting Algorithm. Time O(N)
    #
    # Soltuion III: binary search
    # index = 0  1  2  3  4  5  6  7  8,   len(nums) = 9
    #        [1, 1, 2, 3, 3, 4, 4, 8, 8]
    #                     |

    # Time O(logN) Space O(1)
    def singleNonDuplicate(self, nums: List[int]) -> int:

        i, j, mid = 0, len(nums) - 1, 0
        while i < j:
            mid = i + (j - i) // 2

            if nums[mid - 1] == nums[mid]:
                if mid % 2 == 0:
                    j = mid - 2
                else:
                    i = mid + 1
            elif nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    i = mid + 2
                else:
                    j = mid - 1
            else:
                return nums[mid]

        return nums[i]


'''
    # Time O(N) Space O(1)
    def singleNonDuplicate(self, nums: List[int]) -> int:

        if nums is None: return None
        if nums == []: return None

        count = 0
        value = None
        for i in range(len(nums)):

            if value == None or value != nums[i]:
                value = nums[i]  
                count += 1
            elif value == nums[i]:
                count -= 1

            if count == 2:
                return nums[i-1]

        return nums[len(nums) - 1]
'''







