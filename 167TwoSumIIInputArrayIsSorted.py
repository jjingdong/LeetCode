'''
167. Two Sum II - Input array is sorted
Easy

1461

572

Add to List

Share
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''


class Solution:

    # Solution: Use 2 pointers

    # Time O(N) Space O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i, j = 0, len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i + 1, j + 1]
            elif sum > target:
                j -= 1
            else:
                i += 1

        return [-1, -1]
