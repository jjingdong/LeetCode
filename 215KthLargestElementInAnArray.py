'''
215. Kth Largest Element in an Array
Medium

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: You may assume k is always valid, 1 ≤ k ≤ array's length.

'''


class Solution:

    # Solution I: Sort
    #
    # Solution II: Heap
    #
    # Solution III: QuickSelect

    # Worse Time O(N^2), average O(NlogK)
    # Space Worse O(N), average O(logN)
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def divide(start, end):
            if (start >= end):
                return

            mid = start
            pivot = end
            for i in range(start, end):
                if nums[i] < nums[pivot]:
                    nums[i], nums[mid] = nums[mid], nums[i]
                    mid += 1

            nums[mid], nums[pivot] = nums[pivot], nums[mid]
            if mid == len(nums) - k:
                return
            divide(start, mid - 1)
            divide(mid + 1, end)

        if not nums or not k: return None
        if k > len(nums): return None

        divide(0, len(nums) - 1)
        return nums[len(nums) - k]


