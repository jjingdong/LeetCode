'''
1560. Most Visited Sector in a Circular Track
Easy

Given an integer n and an integer array rounds. We have a circular track which
consists of n sectors labeled from 1 to n. A marathon will be held on this track,
the marathon consists of m rounds. The ith round starts at sector rounds[i - 1]
and ends at sector rounds[i]. For example, round 1 starts at sector rounds[0]
and ends at sector rounds[1]

Return an array of the most visited sectors sorted in ascending order.

Notice that you circulate the track in ascending order of sector numbers in the
counter-clockwise direction (See the first example).



Example 1:


Input: n = 4, rounds = [1,3,1,2]
Output: [1,2]
Explanation: The marathon starts at sector 1. The order of the visited sectors
is as follows:
1 --> 2 --> 3 (end of round 1) --> 4 --> 1 (end of round 2) --> 2 (end of round
3 and the marathon)
We can see that both sectors 1 and 2 are visited twice and they are the most
visited sectors. Sectors 3 and 4 are visited only once.
Example 2:

Input: n = 2, rounds = [2,1,2,1,2,1,2,1,2]
Output: [2]
Example 3:

Input: n = 7, rounds = [1,3,5,7]
Output: [1,2,3,4,5,6,7]


Constraints:

2 <= n <= 100
1 <= m <= 100
rounds.length == m + 1
1 <= rounds[i] <= n
rounds[i] != rounds[i + 1] for 0 <= i < m
'''


class Solution:

    #        Input: n = 4, rounds = [1,3,1,2]
    #        Output: [1,2]
    #        n = 4, sections: 1, 2, 3, 4
    #        m = 3 rounds
    #        1, 2, 3
    #        4, 1
    #        2
    #
    #        4 -> 2
    #        4 5 6 7 8 1 2 -> [1, 2] + [4, 5, 6, 7, 8]

    # Time O(N) Space O(N), runtime = 44 ms
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:

        if not rounds: return None
        if len(rounds) == 1: return rounds

        if rounds[0] <= rounds[-1]:
            return range(rounds[0], rounds[-1] + 1)
        else:
            return list(range(1, rounds[-1] + 1)) + list(range(rounds[0], n + 1))


'''
    # Time O(NlogN) Space O(N), runtime = 184 ms
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:

        lst = [x for x in range(1, n+1)] * 2
        count = [0] * (n)
        max_count = 0
        for i in range(1, len(rounds)):
            s = lst.index(rounds[i-1])
            e = lst.index(rounds[i])
            if rounds[i-1] > rounds[i]:
                e += n
            if i != 1:
                s += 1 

            for j in range(s, e+1):
                count[j%n] += 1
                max_count = max(max_count, count[j%n])

        results = []
        for i in range(len(count)):
            if count[i] == max_count:
                results.append(i+1)

        return sorted(results)
'''