'''
15. 3Sum
Medium

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution:

    # Solution:
    # 3Sum problem = value + 2Sum problem
    # [-4, -1, -1, 0, 1, 2]
    # value = -4, rest = 4, looking for a + b = 4
    # value = -1, rest = 1, looking for a + b = 1
    # value = 0, rest = 0, looking for a + b = 0

    # Time O(N^2) Space O(N), runtime = 2384 ms
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if not nums: return []

        nums = sorted(nums)
        size = len(nums)
        results = []
        seen = set()
        for i in range(size - 2):
            rest = -nums[i]
            if rest >= 0:

                if i == 0 or nums[i] != nums[i - 1]:
                    a = nums[i]
                    lo = i + 1
                    hi = size - 1

                    while lo < hi:
                        b = nums[lo]
                        c = nums[hi]
                        sum = a + b + c
                        hash = f'{a}_{b}_{c}'
                        if sum == 0 and hash not in seen:
                            seen.add(hash)
                            results.append([a, b, c])
                            lo += 1
                            hi -= 1
                        elif sum < 0:
                            lo += 1
                        else:
                            hi -= 1

        return list(results)


'''
From Shohan
   def threeSum(self, nums: List[int]) -> List[List[int]]:        
        n = len(nums)
        sn = sorted(nums)
        answer = []
        # fix a and find all combinations of b, c which satisfy the equation
        l = 0
        while l < n-2:
            a = sn[l]
            if a > 0:
                break
            cache = {}
            used = set()
            for b in sn[l+1:]:
                c = -(a+b)
                if b in cache and not b in used:
                    answer.append([a, b, cache[b]])
                    used.add(b)
                cache[c] = b
            l += 1
            # skip duplicate values for a
            while l < n and sn[l] == sn[l-1]:
                l += 1
        return answer
'''

'''
    # Time O(N^2) Space O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        results = []
        size = len(nums)

        for i in range(size-2):
            rest = -nums[i]
            if rest >= 0:

                if i == 0 or nums[i] != nums[i-1]:
                    j = i + 1
                    k = size - 1
                    while j < k:
                        sum = nums[i] + nums[j] + nums[k]

                        if sum < 0:
                            j += 1
                        elif j > i + 1 and nums[j] == nums[j-1]:
                            j += 1
                        elif sum > 0:
                            k -= 1
                        elif k < size - 1 and nums[k] == nums[k + 1]:
                            k -= 1
                        elif sum == 0:
                            results.append([nums[i], nums[j], nums[k]])
                            j += 1
                            k -= 1

        return results
'''

'''
#         [-1, 0, 1, 2, -1, -4]
#        
#         step 1:
#         [-4, -1, -1, 0 1, 2]     0:
#        
#         step 2:
#         -4 [-1, -1, 0 1, 2 ]    4
#         -1 [-1, 0 1, 2]     1
#         -1 [0 1, 2]     1
#         0  [2]  0
#       
#         step 3:
#         -1 [-1, 0 1, 2]         5
#         -1 [0 1, 2]             5
#       
#         recursion:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def find(lst, target, result):

            print(f'lst = {lst} target = {target} result = {result}')

            if not lst: return
            if len(lst) < NO_ELEMENTS - len(results): return

            if len(result) == NO_ELEMENTS:
                if target == 0:
                    results.append(result)
                else:
                    return
            if NO_ELEMENTS - len(result) == 1:
                if target in lst:
                    result.append(target)
                else:
                    return

            else:
                while len(lst) > 1:
                    cur_val = lst[0]
                    target = -cur_val
                    temp = lst[1:]
                    lst.pop(0)
                    find(temp, target, result + [cur_val])


                # for i in range(len(lst)):
                #     cur_val = lst[i]
                #     target -= cur_val
                #     temp = lst[:i] + lst[i+1:]
                #     find(temp, target, result + [cur_val])
                #     target += cur_val

        NO_ELEMENTS = 3
        results = []
        # while len(nums) >= 1:
        #     cur_val = nums[0]
        #     nums.pop(0)
            # find(nums, -cur_val, [cur_val])
        find([0,1,2,-1], 1, [-1])

        return results

# lst = [0, 1, 2, -1] target = 1 result = [-1]
# lst = [1, 2, -1] target = 0 result = [0]
# lst = [2, -1] target = -1 result = [1]
# lst = [-1] target = -2 result = [2]
# lst = [] target = 1 result = [-1]
'''

