class Solution:

    # Solution I: Sort, Time O(NlogK) Space O(1)
    #
    # Solution II: Heap, Time O(NlogK) Space O(K)
    #
    # Solution III: QuickSelect, Time Worse O(N^2), average O(N), Space O(1)
    
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     ls = sorted(nums)
    #     return ls[len(ls) - k]
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k,nums)[-1]
    
'''    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #minheap
        
        a = []
        for n in nums:
            heapq.heappush(a, n)
            heapq.heapify(a)
            if len(a)>k:
                heapq.heappop(a)
                
        ele = heapq.heappop(a)
        return ele
'''

'''
    # Time Worse O(N^2), average O(N)
    # Space O(1)
    # runtime = 2252 ms
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if not nums or not k: return None
        if k > len(nums): return None
        kk = len(nums) - k

        start, end = 0, len(nums) - 1
        while start < end:
            mid = start
            pivot = end
            for i in range(start, end):
                if nums[i] < nums[pivot]:
                    nums[i], nums[mid] = nums[mid], nums[i]
                    mid += 1

            nums[mid], nums[pivot] = nums[pivot], nums[mid]
            if mid == kk:
                return nums[kk]
            elif mid > kk:
                end = mid - 1
            else:
                start = mid + 1

        return None
'''

'''
    # Worse Time O(N^2), average O(N)
    # Space O(1)
    # runtime = 2192 ms
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
            if mid == kk:
                return
            elif mid > kk:
                divide(start, mid - 1)
            else:
                divide(mid + 1, end)

        if not nums or not k:return None
        if k > len(nums): return None
        kk = len(nums) - k

        divide(0, len(nums) - 1)
        return nums[kk]
'''
    

        
        
        