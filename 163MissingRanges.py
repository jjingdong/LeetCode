'''
163. Missing Ranges
Medium

Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
Example:
Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
'''


class Solution:

    # Note. There is a better solution to this
    # Time O(N) Space O(1)
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:

        def to_string(min, max):
            if min == max:
                return str(min)
            else:
                return str(min) + '->' + str(max)

        if lower > upper: return []
        if not nums:
            return [to_string(lower, upper)]

        ranges = []
        range_min, range_max = None, None

        nums = [lower - 1] + nums + [upper + 1]
        for i in range(1, len(nums)):

            num = nums[i]
            if num == nums[i - 1]:
                continue

            pre_next = nums[i - 1] + 1
            pre = nums[i] - 1

            if pre_next != num:
                range_min = pre_next
                range_max = pre
                ranges.append(to_string(range_min, range_max))

        return ranges


