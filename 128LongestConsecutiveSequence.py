'''
128. Longest Consecutive Sequence
Hard

Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.

Follow up: Could you implement the O(n) solution?



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
 Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 104
-109 <= nums[i] <= 109
'''


class Solution:

    # Solution I: sort, then find. Time O(NlogN)
    # Solution II: use set

    # Time O(N) Space O(n)
    # runtime = 52 ms
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        result = 0
        for n in nums:
            # find the start of the sequence
            if n - 1 not in nums:
                m = n + 1
                count = 1
                while m in nums:
                    m += 1
                    count += 1
                result = max(result, count)
        return result