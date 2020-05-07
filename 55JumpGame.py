'''
55. Jump Game
Medium

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
 
Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 
Constraints:
	•	1 <= nums.length <= 3 * 10^4
	•	0 <= nums[i][j] <= 10^5
'''


class Solution:

    #      [2, 3, 1, 1, 4]
    # index 0  1  2  3  4
    # index 0, jump to index = 1, value = 3
    #                                        jump to index = 2, vlaue = 1,
    #                                                                      jump to index = 3, value = 1  ----> jump to index = 4
    #                                        jump to index = 3, value = 1,
    #                                                                      jump to index = 4
    #                                        jump to index = 4,
    #                  index = 2, value = 1,
    #                                        jump to index = 3, value = 1,
    #                                                                      jump to index = 4
    # Solution I: Greedy
    #

    # Time O(N) Space O(1)
    def canJump(self, nums: List[int]) -> bool:

        pos = len(nums) - 1
        for j in range(len(nums) - 1, -1, -1):
            if j + nums[j] >= pos:
                pos = j

        return pos == 0
