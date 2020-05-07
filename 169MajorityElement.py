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
    # Solution III: Boyer-Moore Voting Algorithm
    #
    #       [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 7, 7, 7, 7]
    # count: 1  2  1  2  1  0. 1. 0. 1. 2. 1. 0  1. 2. 3. 4
    #       [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 5, 5, 5, 5]
    # count: 1  2. 1. 2. 1. 0. 1. 0. 1. 2. 1. 0. 1  2. 3. 4

    # Time O(N) Space O(1), Using Boyer-Moore Voting Algorithm
    def majorityElement(self, nums: List[int]) -> int:

        count = 0
        majority = None

        for num in nums:
            if count == 0:
                majority = num
            if majority == num:
                count += 1
            else:
                count -= 1

        return majority

    # Time O(N) Space O(N), use HashMap
    def majorityElement(self, nums: List[int]) -> int:

        counts = collections.Counter(nums)
        return max(counts.keys, key=counts.get)


'''  
    # Time O(NlogN) Space O(1), Using Sort
    def majorityElement(self, nums: List[int]) -> int:

        nums = sorted(nums)
        return nums[len(nums)//2]
'''






