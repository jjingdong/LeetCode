'''
169. Majority Element
Easy

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
'''


class Solution:

    # Solution I: HashMap
    # Time O(N) Space O(N)
    #
    # Solution II: Sorting
    # The item at index n/2
    # Time O(NlogN) Space O(1)
    #
    # Solution III: Randomization
    # Time O(N) Space O(1)
    #
    # Solution IV: Divide and Conquer
    # Time O() Space O()
    #
    # Solution V: Boyer-Moore Voting Algorithm
    #
    # [2,2,1,1,1,2,2]
    #  0 1 0 1 2 2 3

    # Time O() Space O()
    def majorityElement(self, nums: List[int]) -> int:


'''
    # Time O(NlogN) Space O(1), Using Sort
    def majorityElement(self, nums: List[int]) -> int:

        nums = sorted(nums)
        return nums[len(nums)//2]
'''


