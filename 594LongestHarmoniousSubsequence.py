'''
594. Longest Harmonious Subsequence

We define a harmonious array as an array where the difference between its maximum value
 and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among
 all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or
 no elements without changing the order of the remaining elements.



Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]
Output: 2
Example 3:

Input: nums = [1,1,1,1]
Output: 0


Constraints:

1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109
'''


class Solution:

    #         [1,3,2,2,5,2,3,7]
    #
    # hashmap {1:1, 3:2, 2:3, 5:1, 7:1}
    #                    ---
    # sort hashmap
    #          find pre, and next in the hashmap
    #
    # time O(NlogN)
    #
    # -
    # Used a single loop in O(N), and update the global_max on the fly
    # no need to sort

    # Time O(N) Space O(N)
    def findLHS(self, nums: List[int]) -> int:

        h_dict = collections.defaultdict(int)
        global_count = 0
        for n in nums:
            count = 0
            h_dict[n] += 1
            count = h_dict[n]
            if n - 1 in h_dict:
                global_count = max(global_count, count + h_dict[n - 1])
            if n + 1 in h_dict:
                global_count = max(global_count, count + h_dict[n + 1])

        return global_count

