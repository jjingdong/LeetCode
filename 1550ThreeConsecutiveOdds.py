'''
1550. Three Consecutive Odds
Easy

Given an integer array arr, return true if there are three consecutive
 odd numbers in the array. Otherwise, return false.


Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.


Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
'''


class Solution:

    # Time O(N) Space O(1), runtime = 32 ms
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        count = 0
        for a in arr:
            if a % 2 == 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0

        return False
