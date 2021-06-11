'''
740. Delete and Earn
Medium

Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points.
After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn
by applying such operations.

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points.
6 total points are earned.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.


Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
'''


class Solution:

    def deleteAndEarn(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        max_value = 0
        for i in range(len(nums)):
            if nums[i] > max_value:
                max_value = nums[i]

        array = [0] * max_value
        for n in nums:
            array[n - 1] += n

        # print(max_value)
        # print(array)

        global_max = [0] * max_value
        global_max[0] = array[0]
        global_max[1] = max(array[0], array[1])
        for i in range(2, max_value):
            take = array[i] + global_max[i - 2]
            not_take = global_max[i - 1]
            global_max[i] = max(take, not_take)

        # print(f'global_max = {global_max}')
        return global_max[-1]

    def deleteAndEarn(self, nums: List[int]) -> int:

        def helper(i):

            if i == 0:
                return array[0]
            if i == 1:
                return max(array[0], array[1])

            if i in cache:
                return cache[i]

            # take
            a = helper(i - 2) + array[i]

            # not take
            b = helper(i - 1)

            cache[i] = max(a, b)
            return cache[i]

        if len(nums) == 1:
            return nums[0]

        max_value = 0
        for i in range(len(nums)):
            if nums[i] > max_value:
                max_value = nums[i]

        array = [0] * max_value
        for n in nums:
            array[n - 1] += n

        cache = {}
        return helper(max_value - 1)

    def house_robber(points):
        size = len(points)
        if size == 1:
            return points[0]

        # index 1
        prepre = 0
        pre = points[0]
        cur = 0

        for i in range(1, size):
            cur = max(points[i] + prepre, pre)

            prepre = pre
            pre = cur

            # print(cur)

        return cur

    max_value = 1
    for num in nums:
        if num > max_value:
            max_value = num

    # print(max_value)
    points = [0] * max_value
    for num in nums:
        points[num - 1] += num

    # print(points)
    return house_robber(points)



