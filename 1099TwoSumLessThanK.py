'''
1099. Two Sum Less Than K
Easy

Given an array A of integers and integer K, return the maximum S such that
 there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying
  this equation, return -1.



Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation:
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation:
In this case it's not possible to get a pair sum less that 15.


Note:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
'''


class Solution:

    # Note. Can also use binary search to solve this problem

    # O(N^2)
    def twoSumLessThank(self, A: List[int], K: int) -> int:

        if A is None: return -1
        if len(A) == 0: return -1

        sum = A[0]
        max = -1
        for i in range(1, len(A)):
            for j in range(i, len(A)):
                sum = A[i - 1] + A[j]
                if sum > max and sum < K:
                    max = sum

        return max


'''
    #O(N+NlogN) -> NlogN for sorting
    def twoSumLessThanK(self, A: List[int], K: int) -> int:

        if A is None: return -1
        if len(A) == 0: return -1

        b = sorted(A)
        i = 0
        j = len(b) - 1
        result = -1
        while i<j:
            sum = b[i] + b[j]
            if sum > K:
                j -= 1
            elif sum < K:
                result = max(result, b[i]+b[j])
                i += 1

        return result
'''
