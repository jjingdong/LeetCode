'''
287. Find the Duplicate Number
Medium

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
Example 1:
Input: [1,3,4,2,2]
Output: 2
Example 2:
Input: [3,1,3,4,2]
Output: 3
Note:
	1.	You must not modify the array (assume the array is read only).
	2.	You must use only constant, O(1) extra space.
	3.	Your runtime complexity should be less than O(n2).
	4.	There is only one duplicate number in the array, but it could be repeated more than once.

'''


class Solution:

    # Time O(N) Space O(1), runtime = 11.65%
    def findDuplicate(self, nums: List[int]) -> int:

        # x, nums[x], nums[nums[x]], nums[nums[nums[x]]], ....
        # pigeonhold principle
        # floyd's tortoise and hare (cycle detection)

        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Find the "entrance" to the cycle.
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast


'''
    # Time O(NlogN) Space O(N)
    def findDuplicate(self, nums: List[int]) -> int:

        # sort - time: O(NlogN) Space O(N)
        # loop O(N)
        if not nums: return

        nums = sorted(nums)
        pre = None
        for num in nums:
            if pre == num:
                return num
            pre = num

        return None

    # Time O(NlogN) Space O(N)
    def findDuplicate(self, nums: List[int]) -> int:

        # sort - time O(NlogN) Space O(N)
        # binary search - time O(logN) Space O(1)

    # Time O(NlogN) Space O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        # quickselect in place: Time average O(N), worst O(N^N) Space O(1)

    # Time O(NlogN), Space O(1)
    def findDuplicate(self, nums: List[int]) -> int:

        # heapsort in place - Time O(NlogN) Space O(1)
        # binary search - Time O(NlogN) Space O(1)
'''


