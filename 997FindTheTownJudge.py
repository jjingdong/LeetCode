'''
997. Find the Town Judge
Easy

685

73

Add to List

Share
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.



Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3


Note:

1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
'''


class Solution:

    # Solution I: Hash table
    #
    # Solution II: Two Arrays
    #
    # Solution III: One Array

    # Time O(N) Space O(N), Solution III: One Array
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        if trust is None: return -1
        if len(trust) < N - 1: return -1

        count = [0] * (N + 1)

        for one, two in trust:
            count[one] -= 1
            count[two] += 1

        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i

        return -1


'''
    # Time O(N) Space O(N), Solution II: Two Arrays
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        if trust is None: return -1
        if len(trust) < N - 1: return -1

        vote_to = [0] * (N + 1)
        be_voted = [0] * (N + 1)

        for one, two in trust:
            vote_to[one] += 1 
            be_voted[two] += 1

        for i in range(1, N + 1):
            if be_voted[i] == N - 1 and vote_to[i] == 0:
                return i

        return -1
'''

'''   
    # Time O(MN) Space O(N), Solution I
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        if trust is None: return -1
        if trust == [] and N != 1: return -1  
        if len(trust) < N - 1: return -1

        if trust == [] and N == 1: return N

        trustees = [] 
        trust_count = {}
        for i in range(len(trust)):
            if trust[i][1] not in trust_count:
                trust_count[trust[i][1]] = 1
            else:
                trust_count[trust[i][1]] += 1

        for k, v in trust_count.items():
            if v == N - 1:
                trustees.append(k)

        newTrustees = trustees[:]
        for i in range(len(trustees)):
            for j in range(len(trust)):
                if trust[j][0] == trustees[i]:
                    if trustees[i] in newTrustees:
                        newTrustees.remove(trustees[i])

        if len(newTrustees) == 1:
            return newTrustees[0]
        else:
            return -1
'''









