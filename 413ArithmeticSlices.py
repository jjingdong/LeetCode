'''
413. Arithmetic Slices
Medium

A sequence of numbers is called arithmetic if it consists of at least
three elements and if the difference between any two consecutive elements
 is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that
array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of the array A is called arithmetic if the sequence:
A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this
means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
'''


class Solution:

    #         A = [1, 2, 3, 4]

    #         p = 1
    #         p = 1+1 = 2 < q = 3

    #         [1,2,3] [2,3,4] [1,2,3,4]
    #         3 slices

    #         1,  2,  3,  4,  6,  8,  10,  12,  14
    # diff =    1   1   1   2   2   2     2    2
    #           -----
    #               ------
    #           ---------
    #                       -----                        size = 2, no slice = 4 = repeat -1
    #                           -----
    #                               --------
    #                                     -------
    #                        ---------                   size = 3, no. slice = 3 = repeat - 2
    #                             ----------
    #                                -------------
    #                      -----------------
    #                            -------------------     size = 4, no. slice = 2 = repeat - 3
    #                       ----------                   size = 5, no. slice = 1 = repeat - 4
    #                                                 total = repeat * 4 - 1 -2 - 3 -4
    #                                                       = repeat * 4 - (1+2+3+4)
    #                                                       = repeat * (repeat-1) - repeat * (repeat-1) / 2
    #                                                       = repeat * (repeat-1) / 2
    #                                                       = (repeat_count+1) * repeat_count / 2

    # Time O(N) Space O(1)
    def numberOfArithmeticSlices(self, A: List[int]) -> int:

        diff = None
        pre_diff = None
        re_count = 0
        total = 0
        for i in range(1, len(A)):

            diff = A[i] - A[i - 1]
            if pre_diff == diff:
                re_count += 1
            else:
                total += re_count * (re_count + 1) / 2
                re_count = 0
                pre_diff = diff

        total += re_count * (re_count + 1) / 2
        return int(total)

