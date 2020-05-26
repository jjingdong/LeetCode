'''
1035. Uncrossed Lines
Medium

We write the integers of A and B (in the order they are given) on two separate horizontal lines.
Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:
	•	A[i] == B[j];
	•	The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.
Return the maximum number of connecting lines we can draw in this way.
 
Example 1:
Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
Example 2:
Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
Example 3:
Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2
 
Note:
	1.	1 <= A.length <= 500
	2.	1 <= B.length <= 500
	3.	1 <= A[i], B[i] <= 2000

'''


class Solution:

    # Solution: Dynamic Programming
    # A = [1,4,2]
    # B = [1,2,4]
    #           1   4   2
    #       1   1   0.  0
    #       2   0.  0.  1
    #       4   0.  1   0
    #
    #           1   4   2
    #       1   1   1.  1
    #       2   1.  1.  2
    #       4   1.  2   2
    #
    # A = [1,3,7,1,7,5], B = [1,9,2,5,1]
    #     [1,3,7,1,7,5]
    # .   1 1
    # .   9
    # .   2
    # .   5           1
    # .   1 1
    #
    #     [1,3,7,1,7,5]
    # .   0 0 0 0 0 0 0 0
    # .   1 0 1.1.1 1 1 1
    # .   9 0 1.1.1.1.1 1
    # .   2 0 1 1 1 1 1 1
    # .   5 0 1 1 1 1 1 2
    # .   1 0 1 1 2 2 2 2
    #
    #     [1,3,7,1,7,5]
    # .   0 0 0 0 0 0 0 0
    # .   1 0 1.1.1 1 2 2
    # .   9
    # .   2
    # .   5
    # .   1

    # Time O(MN) Space O(MN), runtime = 308 ms
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:

        if not A or not B: return None

        size, col_size = len(B), len(A)
        dp = [[0 for _ in range(col_size + 1)] for _ in range(size + 1)]

        for i in range(size):
            for j in range(col_size):
                if B[i] == A[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j])

        return dp[-1][-1]
