'''
368. Largest Divisible Subset
Medium

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
Si % Sj = 0 or Sj % Si = 0.
If there are multiple solutions, return any subset is fine.
Example 1:
Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:
Input: [1,2,4,8]
Output: [1,2,4,8]

'''


class Solution:

    # Solution I: dict + dfs, Time Limit Exceeded
    #         [3, 4, 8, 9, 16]
    #
    #         /3  ---> 9
    #         /4  ---> 8, 16
    #
    #         dict = {3: [9], 4:[8,16]}
    #         count =     1       2
    #         return [4, 8, 16]
    #
    # Solution II:
    #         [3, 4, 8, 9, 16]
    #          i               [[3], [4], [8], [3,9], [16]
    #             i            [[3], [4], [4,8], [3,9], [4,16]
    #                i         [[3], [4], [4,8], [3,9], [4,8,16]
    #                   i
    #                       i
    #

    # Time O(N^2) Space O(N^2)
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        if not nums: return []
        if len(nums) == 1: return nums
        nums = sorted(nums)

        results = [[nums[i]] for i in range(len(nums))]
        count = 1
        index = 0
        for i in range(len(nums) - 1):
            cur = nums[i]
            for j in range(i + 1, len(nums)):
                rest = nums[j]
                if rest % cur == 0 and len(results[i]) + 1 > len(results[j]):
                    results[j].append(cur)
                    if len(results[j]) > count:
                        count = max(count, len(results[j]))
                        index = j
        print(results)

        return results[j]

    # def largestDivisibleSubset(self, nums):
    #     if len(nums) == 0: return []
    #     nums.sort()
    #     sol = [[num] for num in nums]
    #     for i in range(len(nums)):
    #         for j in range(i):
    #             print(f'i = {i} j = {j} nums[i] = {nums[i]} nums[j] = {nums[j]} sol = {sol}')
    #             if nums[i] % nums[j] == 0 and len(sol[i]) < len(sol[j]) + 1:
    #                 sol[i] = sol[j] + [nums[i]]
    #     return max(sol, key=len)


'''
    # Time O(EV) Space O(N), Time Limit Exceeded
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        if not nums: return []
        if len(nums) == 1: return nums

        nums = sorted(nums)
        d_dict = collections.defaultdict(list)
        for i in range(len(nums)-1):
            cur = nums[i]
            for j in range(i+1, len(nums)):
                rest = nums[j]
                if rest % cur == 0:
                    d_dict[cur].append(rest)        
        if not d_dict: 
            return nums[0:1]

        def dfs(key, level, path):
            nonlocal global_level, results

            if key not in d_dict:
                if global_level < level:
                    results = copy.deepcopy(path)
                    global_level = level
                return

            for v in d_dict[key]:
                path += [v]
                dfs(v,level + 1, path)
                path.pop()

        global_level = 0
        results = None

        for key in d_dict.keys():
            dfs(key, 1, [key])

        return results
'''


