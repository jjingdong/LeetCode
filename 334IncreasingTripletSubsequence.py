'''
334. Increasing Triplet Subsequence
Medium

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.
Example 1:
Input: [1,2,3,4,5]
Output: true
Example 2:
Input: [5,4,3,2,1]
Output: false
'''


class Solution:

    # Time O() Space O()
    def increasingTriplet(self, nums: List[int]) -> bool:

        if not nums: return False

        count = 0
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                count += 1
            else:
                count = 0

            print(count)
            if count == 2:
                return True

        return False


