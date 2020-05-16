'''
918. Maximum Sum Circular Subarray
Medium

Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.
Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)
Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
 
Example 1:
Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:
Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:
Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:
Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:
Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
 
Note:
	1.	-30000 <= A[i] <= 30000
	2.	1 <= A.length <= 30000
'''


class Solution:

    # Solution I: Brute Force on the circle array --> Time Limit Exceeded
    #
    # Solution II:
    #

    # Time O(N) Space O(1)
    def maxSubarraySumCircular(self, A: List[int]) -> int:

        cur_sum = float('-inf')
        global_sum = float('-inf')
        cur_min = float('inf')
        global_min = float('inf')
        for cur in A:
            cur_sum = max(cur, cur_sum + cur)
            global_sum = max(global_sum, cur_sum)
            cur_min = min(cur, cur_min + cur)
            global_min = min(global_min, cur_min)

        if global_sum > 0:
            return max(global_sum, sum(A) - global_min)
        return global_sum


'''
    # Time O(N^2) Space O(1)
    def maxSubarraySumCircular(self, A: List[int]) -> int:

        # Time O(N) Space O(1)
        def max_subarray(A):
            cur_sum = float('-inf')
            global_sum = float('-inf')
            for i in range(len(A)):

                cur = lst[i]
                cur_sum = max(cur, cur_sum + cur) 
                global_sum = max(global_sum, cur_sum)

            return global_sum

        max_value = float('-inf')
        for i in range(len(A)):
            new_lst = A[i:] + A[:i]
            max_value = max(max_value, max_subarray(new_lst))

        return max_value
'''


