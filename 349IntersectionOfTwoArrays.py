# 349. Intersection of Two Arrays
#
# Given two arrays, write a function to compute their intersection.
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:
# 	•	Each element in the result must be unique.
# 	•	The result can be in any order.

class Solution:

    # [1, 2, 2, 1]
    # [2, 2]
    # output = [2]

    # [4, 9, 5]
    # [9, 4, 9, 8, 4]
    # output = [4, 9]

    # Time O(M+N)
    # Space O(N+M)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        output = []

        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) <= len(set2):
            for s in set2:
                if s in set1:
                    output.append(s)
        else:
            for s in set1:
                if s in set2:
                    output.append(s)

        return output

#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

#         set1 = set(nums1)
#         set2 = set(nums2)

#         return list(set1 & set2)