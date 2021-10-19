'''
41. First Missing Positive

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1


Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
'''


class Solution:

    # Time O(N) Space O(1)
    def firstMissingPositive(self, nums: List[int]) -> int:

        one_exist = False
        size = len(nums)
        for i in range(size):
            ele = nums[i]
            if ele == 1:
                one_exist = True
            if ele <= 0:
                nums[i] = 1

        # print(f'step 1 nums = {nums}')
        if one_exist == False:
            return 1

        for i in range(size):
            ele = abs(nums[i])
            if ele - 1 <= size - 1:
                # print(f'ele = {ele}')
                nums[ele - 1] = -abs(nums[ele - 1])

        # print(f'step 2 nums = {nums}')

        for i in range(size):
            if nums[i] > 0:
                return i + 1

        return size + 1


'''      
        [1,2,0]  -> 3

         |
         1 -> 2
           |
           2 -> 3
             |
             0 -> 1

        # Time O(N)  Space O(N)
        [3,4,-1,1]
         |
         3 -> 4                3, 4     -1, 1
           |
           4 -> 5  
              |
              -1 -> 0    
                 |
                 1 -> 2         (3,4), (-1, -1), (1, 1)

        # Time O(N)   Space O(N)  ---> output 1
        [7,8,9,11,12]
         |                     8, 
           |                    9,
             |                     10
                |                   10, 12
                   |                  10, 13

        From the solution
        3, 4, -1, -2, 1, 5, 16, 0, 2, 0
if there is a 1:
        3, 4, 1, 1, 1, 5, 1, 0, 2, 0
if there is no 1:
        return 1

index = 0  1  2  3  4  5  6   7  8  9
        3, 4, 1, 1, 1, 5, 1, 0, 2, 0

index = 0  1    2   3   4  5   6  7  8  9
        3, -4, -1, -1, -1, -5, 1, 1, 2, 1
                               * output

'''