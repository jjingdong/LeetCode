'''
442. Find All Duplicates in an Array
Medium

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''


class Solution:

    # Time O(N) Space O(1), runtime = 392 ms
    def findDuplicates(self, nums: List[int]) -> List[int]:

        #         index = 0, 1, 2, 3, 4, 5, 6, 7
        #                 |  || ||          |  |
        #         nums =  4, 3, 2, 7, 8, 2, 3, 1

        results = []

        for n in nums:
            index = abs(n) - 1
            if nums[index] < 0:
                results.append(abs(n))
            nums[index] *= -1

        return results


'''
    # Time O(N) Space O(N), runtime = 356 ms
    def findDuplicates(self, nums: List[int]) -> List[int]:

        results = []

        seen = set()
        for n in nums:
            if n in seen:
                results.append(n)
            else:
                seen.add(n)

        return results
'''

'''
    # Time O(NlogN) Space O(1), runtime = 384 ms
    def findDuplicates(self, nums: List[int]) -> List[int]:

        results = []
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if (nums[i] == nums[i-1]):
                results.append(nums[i])

        return results
'''

'''
    # Time O(N) Space O(N), runtime = 352 ms
    def findDuplicates(self, nums: List[int]) -> List[int]:

        n_dict = collections.Counter(nums)      
        return [k for k in n_dict if n_dict[k] == 2]
'''