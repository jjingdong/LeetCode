'''
1426. Counting Elements
Easy

Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.
 
Example 1:
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
Example 2:
Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.
Example 3:
Input: arr = [1,3,2,3,5,0]
Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.
Example 4:
Input: arr = [1,1,2,2]
Output: 2
Explanation: Two 1s are counted cause 2 is in arr.
Example 5:
Input: arr = [1,1,2]
Output: 2
Explanation: Both 1s are counted because 2 is in the array.
'''


class Solution:

    # Time O(N) Space O(N)
    def countElements(self, arr: List[int]) -> int:

        eleMap = {}
        for a in arr:
            if a in eleMap:
                eleMap[a] += 1
            else:
                eleMap[a] = 1

        count = 0
        for a in arr:
            if a + 1 in eleMap:
                if eleMap[a + 1] >= 1:
                    count += 1

        return count