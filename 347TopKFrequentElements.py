'''
347. Top K Frequent Elements
Medium

Given a non-empty array of integers, return the k most frequent elements.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
Input: nums = [1], k = 1
Output: [1]
Note:
	•	You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
	•	Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
	•	It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
	•	You can return the answer in any order.

'''


class Solution:

    # Solution I: dictionary Time O(NlogN)
    #
    # Solution II: heapq Time O(NlogK)
    #
    # Solution III: quickselect

    #     # Time O(N^2), average O(NlogK)
    #     # Space O(N), average O(logN)
    #     # This is not done
    #     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    #         def divide(start, finish):
    #             if (start >= finish):
    #                 return

    #             mid = start
    #             pivot = finish
    #             for i in range(start, finish):
    #                 if nums[i] < nums[pivot]:
    #                     nums[i], nums[mid] = nums[mid], nums[i]
    #                     mid += 1

    #             nums[mid], nums[pivot] = nums[pivot], nums[mid]

    #             if mid == pivot:
    #                 return

    #             divide(start, mid - 1)
    #             divide(mid + 1, finish)

    #         divide(0, len(nums) - 1)
    #         print(nums)
    #         return nums[len(nums)-k-1:]

    # Time O(NlogK) Space O(N), runtime = 100 ms
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = collections.Counter(nums)
        return heapq.nlargest(k, count_dict, key=count_dict.get)


'''
    # Time O(NlogN) Space O(N), runtime = 100 ms
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_dict = collections.Counter(nums)    
        results = []
        count = 0
        for key,value in count_dict.most_common():
            count += 1
            if count <= k:
                results.append(key)

        return results
'''

