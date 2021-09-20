'''
274. H-Index
Medium

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return compute the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index.



Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1


Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
'''


class Solution:

    # Time O(NlogN) Space O(1)
    def hIndex(self, citations: List[int]) -> int:

        citations.sort()
        size = len(citations)

        for i in range(size - 1, -1, -1):
            cur = citations[i]
            no_paper = i + 1
            # if cur > size-i:
            #     6     size-(size-1) = 1
            #     5     2
            #     3     3
            #     # do nothing'
            if cur < size - i:
                return size - i - 1

        return size

    # Time O(NlogN) Space O(1)
    def hIndex(self, citations: List[int]) -> int:

        citations.sort()
        size = len(citations)

        # O(logN)
        lo = 0
        hi = size - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if citations[mid] == size - mid:
                return size - mid
            elif citations[mid] < size - mid:
                lo = mid + 1
            else:
                hi = mid - 1

        return size - lo

    # Time O(N) Space O(N)
    def hIndex(self, citations: List[int]) -> int:
        size = len(citations)
        arr = [0] * (size + 1)
        for c in citations:
            if c > size:
                arr[size] += 1
            else:
                arr[c] += 1
        print(arr)

        total = 0
        for i in range(size, -1, -1):
            total += arr[i]
            print(f'total = {total} i = {i}')
            if total >= i:
                return i 