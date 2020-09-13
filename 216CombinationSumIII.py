'''
216. Combination Sum III
Medium

Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination
should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''


class Solution:

    #         1   2   3   4   5   6   7   8   9
    #         |   |
    #         |       |
    #         |           |
    #         |               |
    #
    #         1   2
    #         1   3
    #         1   4
    #         1   5
    #         1   6
    #         1   7
    #         1   8
    #         1   9
    #             2   1

    # Time O(min(9,n) choose k) Space O(k), runtime = 32 ms
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        if not k or not n: return None

        lst = [x for x in range(1, min(n + 1, 10))]
        if not (sum(lst[:k]) <= n <= sum(lst[-k:])):
            return []

        def helper(lst, left, start):

            if len(lst) == k:
                if left == 0:
                    result.append(lst)
                return

            if left < 0:
                return

            for i in range(start, min(n + 1, 10)):
                if sum(lst) <= n:
                    helper(lst + [i], left - i, i + 1)

        result = []
        helper([], n, 1)
        return result


'''
    # Time O(C(n,k)) = O(n choose k) = n!/(k!(n-k)!) = 9!/(k!(9-k)!), 
    # Space O(C(n,k)) 
    # runtime = 32 ms
    def combinationSum3(self, k: int, n: int) -> List[List[int]]: 

        if not k or not n: return None

        result = []
        lst = [x for x in range(1, 10)]
        for p in itertools.combinations(lst, k):
            if sum(p) == n:
                result.append(p)
        return result
'''