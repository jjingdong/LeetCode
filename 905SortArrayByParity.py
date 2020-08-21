'''
905. Sort Array By Parity
Easy

Given an array A of non-negative integers, return an array consisting of all the even
elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.



Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000

'''


class Solution:

    #         3   1   2   4   5   6   7   8
    #
    #         i ---->
    #         mid            even    |   odd
    #
    #         iterate through the loop, i++
    #         3   1   2   4   5   6   7   8
    #
    #         3
    #         i,mid
    #         3
    #         mid i
    #         3   1
    #         mid     i
    #         2   1   3
    #            mid      i
    #         2   4   3   1
    #                mid      i
    #         2   4   3   1   5
    #                mid          i
    #         2   4   6   1   5   3
    #                     mid         i

    # Time O(N) Space O(1), runtime = 80 - 156 ms (get different time submitting diffent time)
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        if not A: return A

        mid = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[mid], A[i] = A[i], A[mid]
                mid += 1

        return A


'''
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return sorted(A, key = lambda x: x%2)
'''

'''
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [x for x in A if x%2 == 0] + [x for x in A if x%2 == 1]
'''


