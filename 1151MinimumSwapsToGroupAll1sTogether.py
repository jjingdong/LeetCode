# 1151. Minimum Swaps to Group All 1's Together
# Medium
#
# Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.
#  
# Example 1:
# Input: [1,0,1,0,1]
# Output: 1
# Explanation:
# There are 3 ways to group all 1's together:
# [1,1,1,0,0] using 1 swap.
# [0,1,1,1,0] using 2 swaps.
# [0,0,1,1,1] using 1 swap.
# The minimum is 1.
# Example 2:
# Input: [0,0,0,1,0]
# Output: 0
# Explanation:
# Since there is only one 1 in the array, no swaps needed.
# Example 3:
# Input: [1,0,1,0,1,0,0,1,1,0,1]
# Output: 3
# Explanation:
# One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].

class Solution:

    # [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]
    #                  3 * 0 position until now
    #                     4
    #                        3
    #                           3
    #                              4
    #                                 3

    # Time O(N)
    # Space O(1)
    def minSwaps(self, data: List[int]) -> int:

        if data is None: return None
        if data == []: return 0

        noOf1s = 0

        for num in data:
            if num == 1:
                noOf1s += 1

        if noOf1s == 1: return 0

        mini = 0
        result = 0

        for i in range(len(data)):

            cur = data[i]
            if i < noOf1s:
                result += not cur
                mini = result
            else:
                result += not cur
                result -= not data[i - noOf1s]

            mini = min(result, mini)

        return mini





