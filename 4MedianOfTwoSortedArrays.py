'''
4. Median of Two Sorted Arrays
Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the
median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

'''


class Solution:

    # Time O(log(min(M,N))), Space O(1), runtime = 88 ms
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if not nums1 and not nums2: return -1

        # assume nums1 is the smallest array
        size1 = len(nums1)
        size2 = len(nums2)
        if size1 > size2:
            size1, size2 = size2, size1
            nums1, nums2 = nums2, nums1

        # binary search to find the partition
        lo, hi = 0, size1
        while lo <= hi:
            mid1 = (lo + hi) // 2
            mid2 = (size1 + size2 + 1) // 2 - mid1

            l1_index = mid1 - 1
            r1_index = mid1
            l2_index = mid2 - 1
            r2_index = mid2

            l1 = nums1[l1_index] if mid1 != 0 else float('-inf')
            r1 = nums1[r1_index] if mid1 != size1 else float('inf')
            l2 = nums2[l2_index] if mid2 != 0 else float('-inf')
            r2 = nums2[r2_index] if mid2 != size2 else float('inf')

            if l2 <= r1 and l1 <= r2:
                # calculate the median value
                if (size1 + size2) % 2:
                    return max(l1, l2)
                else:
                    a = max(l1, l2)
                    b = min(r1, r2)
                    return (a + b) / 2

            elif l1 > r2:
                hi = mid1 - 1

            else:
                lo = mid1 + 1
