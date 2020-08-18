'''
119. Pascal's Triangle II
Easy

Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Follow up:

Could you optimize your algorithm to use only O(k) extra space?



Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]


Constraints:

0 <= rowIndex <= 40
'''


class Solution:


# 1                       k=0
# 1,1                     k=1
# 1,2,1                   k=2
# 1,3,3,1                 k=3
# 1,4,6,4,1               k=4
# 1,5,10,10,5,1           k=5         1, k, 10=(k-1)+3+3
# 1,6,15,20,15,6,1        k=6         1, k, 15=(k-1)+(k-2)+6
# 1,7,21,35,35,21,7,1     k=7         1, k, 21=(k-1)+(k-2)+10

# 1, 3, 3, 1
# <---------
# 1, 4, 6, 4, 1
# ------------------>
# 1, 5, 10, 5, 1

# Time O(KN), k = rowIndex Space O(1), runtime = 24 ms
def getRow(self, rowIndex: int) -> List[int]:
    if not rowIndex: return [1]

    result = collections.deque([1, 1])
    for i in range(1, rowIndex):

        result.appendleft(1)
        for j in range(1, len(result) - 1):
            result[j] += result[j + 1]

    return result


'''
    # The first value is 1. The next is n / 1. 
    # The next is n(n - 1)/1*2. Then n(n - 1)(n - 2)/1*2*3. etc
    # runtime = 28 ms
    def getRow(self, rowIndex: int) -> List[int]:

        result = [1] * (rowIndex + 1)
        upper, lower = rowIndex, 1
        for i in range(1, rowIndex // 2 + 1):
            result[i] = result[rowIndex - i] = (result[i - 1] * upper) // lower
            upper -= 1
            lower += 1
        return result
'''

'''
    # Time O() Space O(), runtime = 28 ms
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0: return [1]
        result = [1]
        for _ in range(rowIndex):
            tmp = 1
            for i in range(1, len(result)):
                 result[i], tmp = tmp + result[i], result[i]
            result.append(1)
        return result
'''

'''
    # Time O() Space O(), runtime = 28 ms
    def getRow(self, rowIndex: int) -> List[int]:

        result = [1] * (rowIndex + 1)

        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                result[j] += result[j - 1]

        return result
'''

