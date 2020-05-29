'''
338. Counting Bits
Medium

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
Example 1:
Input: 2
Output: [0,1,1]
Example 2:
Input: 5
Output: [0,1,1,2,1,2]
Follow up:
	•	It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
	•	Space complexity should be O(n).
	•	Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''


class Solution:

    # Brian Kernighan's algorithm which is applied to turn off the rightmost bit of one in a number.
    # a & (a-1)

    # Time O(N) Space O(1), runtime = 20.6 ms
    def countBits(self, num: int) -> List[int]:
        results = [0] * (num + 1)
        for i in range(1, num + 1):
            count = i & (i - 1)
            results[i] = results[count] + 1

        return results


'''   
    # Time O(MN) Space O(N), runtime = 276 ms
    def countBits(self, num: int) -> List[int]:

        results = []
        for i in range(num + 1):
            count = 0
            for digit in bin(i)[2:]:
                count += int(digit)
            results.append(count)

        return results
'''