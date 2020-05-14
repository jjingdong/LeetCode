'''
402. Remove K Digits
Medium

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
Note: 
	•	The length of num is less than 10002 and will be ≥ k.
	•	The given num does not contain any leading zero.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''


class Solution:

    # '1 4 3 2 2 1 9'
    #  | | |
    #  use min heap, 2 < 1, so remove 2
    #
    # Solution I: Stack
    #
    # Solution II: Heap

    # Time O(N+K) Space O(N)
    def removeKdigits(self, num: str, k: int) -> str:
        num_stack = []

        # Construct a monotone increasing sequence of digits
        for digit in num:
            while k and num_stack and num_stack[-1] > digit:
                num_stack.pop()
                k -= 1

            num_stack.append(digit)

        # - Trunk the remaining K digits at the end
        # - in the case k==0: return the entire list
        if k:
            final_stack = num_stack[:-k]
        else:
            final_stack = num_stack

        # trip the leading zeros
        return "".join(final_stack).lstrip('0') or "0"


'''
    # Note this is not working, need to debug
    # Time O(N^2*logN) Space O(N)
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'

        results = ''

        lst = []
        for i in range(k+1):
            lst.append(int(num[i]))

        heapq.heapify(lst)

        i = k
        min = heapq.heappop(lst)
        while i <= len(num) - 1 and int(num[i]) >= min and min != 0:
            if min != '0':
                results += str(min)

            heapq.heappush(lst, int(num[i]))
            heapq.heapify(lst)
            min = heapq.heappop(lst)
            i += 1

        first_zeros = True
        for j in range(i, len(num)):

            if num[j] == '0' and first_zeros == True:
                first_zeros = True
            else:
                first_zeros = False
                results += num[j]

        if len(results) == 0:
            return '0'

        return results
'''