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

    # Time O(NlogN) Space O(N), runtime = 108 ms
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums).most_common(k)
        return [v1 for v1, _ in c]


'''
    # Time O(NlogN) Space O(N), runtime = 180 ms      
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        c = collections.Counter(nums)
        results = []
        for (v1,v2) in c.most_common()[:k]:
            results.append(v1)
        return results
'''

'''
    # Time O(NlogK) Space O(N), runtime = 100 ms
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_dict = collections.Counter(nums)
        return heapq.nlargest(k, count_dict, key=count_dict.get)
'''

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