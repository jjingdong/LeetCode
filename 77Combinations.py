'''
77. Combinations
Medium

Given two integers n and k, return all possible combinations of k numbers
out of 1 ... n.

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]


Constraints:

1 <= n <= 20
1 <= k <= n
'''


class Solution:

    # Solution I
    #                       1,2,3,4
    #                    /               \
    #        1x                                xx(not 1)                        --- 1 or not 1
    #    /     \                             /         \
    # 12         1x                       2x             xx(not 2)              --- 2 or not 2
    #          /   \                     /   \            /   \
    #        13      1x(not 3)        23  2x(not 3)     3x  xx(not 3)           --- 3 or not 3
    #               /   \                 /  \                /  \
    #            14  1x(not 4)           24  2x(not 4)       34  4x(not 4)      --- 4 or not 4
    #
    # Solution II
    #                                 1,2,3,4
    #             /                      |               \           \
    #         1x(i=0)                 2x(i=1)         3x(i=3)      4x(i=4)->stop    --- position at 1
    #     /       |        \           /   \             |
    # 12(i=1)  13(i=2)  14(i=3)   23(i=1)  24(i=3)    34(i=3)                       --- position at 2
    #
    #                                 1,2,3,4
    #             /                      |               \           \
    #        1xx(i=0)                          2xx(i=1)             3xx(i=3)      4xx(i=4)->stop    --- position at 1
    #     /       |        \                    /   \                   |
    # 12x(i=1) 13x(i=2) 14x(i=3)->stop   23x(i=1) 24x(i=3)->stop   34x(i=3)->stop                   --- position at 2
    #   / \      |                           |
    # 123 124   134                         234                                                     --- position at 3
    #
    # n!/(k!(n-k)!)
    # (n) = n(n-1)...(n-k+1)
    # (k) = k(k-1)...1
    # n!/(k!(n-k)!) = 6 when n = 4, k = 2
    # n!/(k!(n-k)!) = 4 when n = 4, k = 2

    # Time O(k * n!/(k!(n-k)!))
    # Space O(K)
    # runtime = 548 ms
    def combine(self, n: int, k: int) -> List[List[int]]:

        if not k or k < 0: return None
        if not n or n < 0: return None

        def helper(build, index):

            if len(build) == k:
                result.append(build)
                return

            for i in range(index, n + 1):
                helper(build + [i], i + 1)

        result = []
        helper([], 1)
        return result


'''    
    # Time O(2^N) Space O(N)
    # runtime = 616 ms
    # S
    def combine(self, n: int, k: int) -> List[List[int]]:

        if not k or k < 0: return None
        if not n or n < 0: return None

        def helper(build, index):

            if len(build) == k:
                result.append(build)
                return
            if index > n:
                return 

            helper(build + [index], index+1)
            helper(build, index+1)

        result = []
        helper([],1)
        return result
'''

'''  
    # Time O(K^N) Space O(N)
    # runtime = 676 ms
    def combine(self, n: int, k: int) -> List[List[int]]:

        if not k or k < 0: return None
        if not n or n < 0: return None

        lst = [x for x in range(1,n+1)]
        def helper(build, index):

            if len(build) == k:
                result.append(build)
                return
            if index >= len(lst):
                return 

            helper(build + [lst[index]], index+1)
            helper(build, index+1)

        result = []
        helper([],0)
        return result
'''