'''
264. Ugly Number II
Medium

Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
Example:
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  
	1.	1 is typically treated as an ugly number.
	2.	n does not exceed 1690.
'''


class Solution:

    #     Input: n = 10
    #     Output: 12
    #     1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

    #     2, 3, 5

    #     1, 2, 3, 2*2, 5, 2*3, 2*2*2*2, 3*3, 2*5, 2*2*3

    #         2   3   5
    #     2   4   6   10
    #     3       9   15
    #     5           25

    #         4   6   9  10   15  25
    #     2   8   12  18 20   30  50
    #     3           27 30   45  75
    #     5                       125

    #     use minheap

    #     2   3   5
    #         3   5   4   6   10      result = [1, 2]
    #             5   4   6   10  15  12  18  30      result = [1, 2, 3]

    # Time O(N) Space O(N), runtime = 192 ms, using pointer
    def nthUglyNumber(self, n: int) -> int:

        if not n: return None

        lst = [1] * 1690
        i, j, k = 0, 0, 0
        count = 1
        value = 1
        while count < n:

            value = min(lst[i] * 2, lst[j] * 3, lst[k] * 5)

            if value == lst[i] * 2:
                i += 1
            if value == lst[j] * 3:
                j += 1
            if value == lst[k] * 5:
                k += 1

            lst[count] = value
            count += 1

        return value


'''
    # Time O(N) Space O(N), runtime = 272 ms, using pointer
    def nthUglyNumber(self, n: int) -> int:

        if not n: return None

        lst = [1]
        i,j,k = 0,0,0
        count = 1
        value = 1
        while count < n:
            value = min(lst[i] * 2, lst[j] * 3, lst[k] * 5)
            lst.append(value)
            count += 1

            if value == lst[i] * 2:
                i += 1
            if value == lst[j] * 3:
                j += 1
            if value == lst[k] * 5:
                k += 1

        return value
'''

'''
    # Time O(NlogK) Space O(N), runtime = 860 ms, using heap
    def nthUglyNumber(self, n: int) -> int:

        import collections

        if not n: return None
        if n < 4:
            lst = [1, 2, 3, 5]
            return lst[n-1]

        lst = [2, 3, 5]
        count = 1
        values = [2,3,5]
        while count < n:
            num = heapq.heappop(lst)
            count += 1
            for value in values:
                a = num*value
                if a not in lst:
                    heapq.heappush(lst, a)

        return num
'''
