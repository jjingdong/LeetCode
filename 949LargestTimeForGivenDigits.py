'''
949. Largest Time for Given Digits
Easy

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00,
 a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return
an empty string.



Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""


Note:

A.length == 4
0 <= A[i] <= 9
'''


class Solution:

    #         00:00
    #         23:59
    #
    #         0-2     0-9 or 0-3      0-5     0-9
    #
    #         1, 2, 3, 4
    #
    #         find 0-2: 2    1,2,3,4
    #         find 0-3: 3    1,3,4
    #         find 0-5: 4    1,4
    #         find 0-9: 5    5
    #             23:41
    #
    #         sort: 4, 3, 2, 1
    #         boundary: 2, 3, 5, 9
    #                         4
    #                      3
    #                   2
    #                            1
    #             23:41

    # Time O(1) Space O(1), runtime = 32 ms
    def largestTimeFromDigits(self, A: List[int]) -> str:

        if not A: return ''

        A = sorted(A, reverse=True)
        for a, b, c, d in itertools.permutations(A):
            if a in range(0, 3) and b in range(0, 10) and c in range(0, 6) and d in range(0, 10):
                if a * 10 + b < 24:
                    return f'{a}{b}:{c}{d}'
        return ''


'''
    # Note. this is not a solution
    def largestTimeFromDigits(self, A: List[int]) -> str:

        h1 = float('-inf')
        index1 = None
        for i in range(len(A)):
            if A[i] in range(0,3):
                if A[i] > h1:
                    h1 = A[i]
                    index1 = i

        if h1 == float('-inf'):
            return ''

        if h1 in (0,1):
            bound = [9,5,9]
        else:
            bound = [3,5,9]

        print(f'h1 = {h1}')
        A = A[:index1]+A[index1+1:]
        A = sorted(A, reverse = True)
        queue = collections.deque(A)
        result = [None] * 3
        while queue:
            allocated = False
            cur = queue.popleft()
            for i in range(len(bound)):
                if result[i] is None:
                    if cur <= bound[i]:
                        result[i] = cur
                        allocated = True
                        break
            if not allocated:
                return ''

        r = str(h1)
        for i in range(len(result)):
            r += str(result[i])
            if i == 0:
                r += ':'
        return r           
'''

