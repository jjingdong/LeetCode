'''
967. Numbers With Same Consecutive Differences
Medium

Return all non-negative integers of length N such that the absolute difference
between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the
number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.



Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


Note:

1 <= N <= 9
0 <= K <= 9
'''


class Solution:

    #         N = 3 no. of digits
    #         K = 7
    #
    #         1 8 1
    #         2 9 2
    #         3 10--> invalid
    #         ...  donot consider
    #         7 0 7
    #         8 1 8
    #         9 2 9
    #
    #         N = 2
    #         K = 1
    #
    #         12
    #         23
    #         34
    #         45
    #         56
    #         67
    #         78
    #         89
    #         9 10 ---> invalid
    #         10
    #         21
    #         32
    #         43
    #         54
    #         65
    #         76
    #         87
    #         98

    #               1                          N = 1, K = 2
    #           /      \
    #         3         X                      N= 2, (1) 1 + K  (2) 1 - K
    #       /     \
    #     4        1                           N = 3
    #  /   \       /  \
    # 6     2      3   X                       N = 4

    # Time O(2^N) Space O(2^N), runtime = 48 ms
    # If K >= 5, time and Space O(N)
    # If K <= 4, time and space O(2^N)
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:

        def create_num(build, count, d):

            if count == N:
                results.add(build)
                return

            if build == 0:
                return

            if d + K in range(0, 10):
                create_num(build * 10 + d + K, count + 1, d + K)
            if d - K in range(0, 10):
                create_num(build * 10 + d - K, count + 1, d - K)

        if not N: return None

        results = set()
        for i in range(0, 10):
            create_num(i, 1, i)

        return list(results)
