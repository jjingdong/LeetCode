'''
1010. Pairs of Songs With Total Durations Divisible by 60
Medium

You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible
by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j])
% 60 == 0.



Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.


Constraints:

1 <= time.length <= 6 * 104
1 <= time[i] <= 500
'''


class Solution:

    #     index =     0   1   2   3   4
    #         time = [30,20,150,100,40]

    #     how many pairs of song, such that:
    #         time[i] = 30
    #         time[j] = 150
    #         30+150 = 180//60 = 3

    #     Solution I: Brute Force
    #     Time O(N^2) Space O(1)
    #         [30,20,150,100,40]
    #          i = 0
    #             j   j   j  j

    #             i=1
    #             j   j   j  j

    #                 i=2
    #                     j  j

    #                     i=3
    #                        j

    #     all the no. divided by 60 first

    #     divmod(30, 60)

    #             [30,20,150,100,40]
    # index   =    0   1  2   3  4
    # integer
    # remainder =   30 20 30  40  40
    #               |
    #               i     j               1 combination
    #                  |
    #                  i      j           1 combination
    #                  |
    #                  i      j           1 combination

    #                             total = 3 combination

    #     hashmap = {30:[0,2], 20:[1], 40:[3,4]}

    # Solution II, use a hashmap
    # Time O(N) Space O(1), since the max dict size is 60
    # runtime = 232 ms
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        if not time: return 0

        count = 0
        t_dict = collections.defaultdict(int)
        for t in time:

            remainder = t % 60
            if remainder == 0:
                count += t_dict[0]
            else:
                count += t_dict[60 - remainder]

            t_dict[t % 60] += 1

        return count

    # Solution III, use a hashmap
    # Time O(N) Space O(1), since the max dict size is 60
    # runtime = 348 ms
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        if not time: return 0

        count = 0
        t_dict = collections.defaultdict(int)
        for t in time:
            remainder = -t % 60
            count += t_dict[remainder]

            t_dict[t % 60] += 1

        return count

    # Solution IV, use an array
    # Time O(N), Space O(1)
    # runtime = 408ms
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        remainders = [0] * 60
        count = 0
        for t in time:
            re = t % 60
            if re == 0:
                count += remainders[0]
            else:
                count += remainders[60 - re]

            remainders[t % 60] += 1
        return count

    # Solution V, use a hashmap
    # Time O(N) Space O(N) -> Space O(1), since the max dict size is 60
    #     hashmap = {30:2, 20:1, 40:2}

    #     30 -> looking for (60-30), look for itself
    #     20 -> looking for (60-20)

    #       30, 30
    #        |  |
    #        i  j

    #       30, 30, 30
    #        |  |
    #        i  j
    #           |
    #           i    j

    #       only check value smaller than 30
    #       and equal to 30

    #         60, 60, 60     -> total combination = 3
    #         |   |
    #         i   j
    #         |
    #         i       j
    #             |   |
    #             i   j

    #         0               -> 0 comb
    #         0, 0            -> 1 comb
    #         0, 0, 0         -> 3 comb = 2+1
    #         0, 0, 0, 0      -> 3+2+1 = (1+3)*3/2
    #         0, 0, 0, 0, 0   -> 4+3+2+1 = 10 = (1+4)*4/2
    # Gauss formula = 100/2 ( 1 + 100 )

    #          30    -> 0 comb
    #          30,30 -> 1 comb
    #          30, 30, 30 -> 3 comb
    #          30, 30, 30, 30 -> 10 comb
    #          30, 30, 30, 30, 30 -> 15 comb
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        if not time: return 0

        t_dict = collections.defaultdict(int)
        for t in time:
            t_dict[t % 60] += 1

        count = 0
        for k, v in t_dict.items():
            if 0 < k < 30 and 60 - k in t_dict:
                count += v * t_dict[60 - k]

        count += (t_dict[0] - 1) * t_dict[0] / 2
        count += (t_dict[30] - 1) * t_dict[30] / 2

        return int(count)

