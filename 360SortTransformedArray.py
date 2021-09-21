'''
360. Sort Transformed Array
Medium

Given a sorted integer array nums and three integers a, b and c, apply a quadratic function of the form f(x) = ax2 + bx + c to each element nums[i] in the array, and return the array in a sorted order.



Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]


Constraints:

1 <= nums.length <= 200
-100 <= nums[i], a, b, c <= 100
nums is sorted in ascending order.


Follow up: Could you solve it in O(n) time?
'''


class Solution:


'''
    # Time O(NlogN)
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:

        size = len(nums)
        arr = [1] * size
        for i in range(size):
            x = nums[i]
            arr[i] = -a*x*x + b*x + c

        print(arr)
        return sorted(arr)
'''


# Solution from discussion
def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
    def quadratic(x):
        return a * x * x + b * x + c

    n = len(nums)
    index = 0 if a < 0 else n - 1
    l, r, ans = 0, n - 1, [0] * n
    while l <= r:
        l_val, r_val = quadratic(nums[l]), quadratic(nums[r])
        if a >= 0:
            if l_val > r_val:
                ans[index] = l_val
                l += 1
            else:
                ans[index] = r_val
                r -= 1
            index -= 1
        else:
            if l_val > r_val:
                ans[index] = r_val
                r -= 1
            else:
                ans[index] = l_val
                l += 1
            index += 1
    return ans