'''
1283. Find the Smallest Divisor Given a Threshold
Medium

Given an array of integers nums and an integer threshold, we will choose a positive
integer divisor and divide all the array by it and sum the result of the division.
Find the smallest divisor such that the result mentioned above is less than or
equal to threshold.

Each result of division is rounded to the nearest integer greater than or equal
to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.



Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum
will be 5 (1+1+1+2).
Example 2:

Input: nums = [2,3,5,7,11], threshold = 11
Output: 3
Example 3:

Input: nums = [19], threshold = 5
Output: 4


Constraints:

1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6
'''


class Solution:

    # Solution: Binary search
    #
    #         nums = [1,2,5,9], threshold = 6
    #         divisor = 1: total = 1+2+5+9 = 17
    #         divisor = 4: total = 1+1+2+3 = 7
    #         divisor = 7: total = 1+1+1+2 = 5
    #         divisor = 9: total = 1+1+1+1 = 4
    #
    #         smallest divisor that total < threshold

    # Time O(logN) Space O(1)
    # runtime = 388 ms
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def count_total(divisor):
            return sum(ceil(n / divisor) for n in nums)

        if not nums: return None
        size = len(nums)
        hi = max(nums)
        total = sum(nums)

        lo = 1
        while lo <= hi:
            mid = (hi + lo) // 2
            total = count_total(mid)
            if total <= threshold:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo


'''
    # Time O(logN) Space O(1)
    # runtime = 520 ms
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def count_total(divisor):
            total = 0
            for n in nums:
                a,b = divmod(n,divisor)
                total += a
                if b != 0:
                    total += 1

            return total

        if not nums: return None
        size = len(nums)
        hi = max(nums)
        total = sum(nums)

        lo = 1
        while lo <= hi:
            mid = (hi+lo)//2
            total = count_total(mid)
            if total <= threshold:
                hi = mid - 1 
            else:
                lo = mid + 1

        return lo
'''
