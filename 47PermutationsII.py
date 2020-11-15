'''
47. Permutations II
Medium

Given a collection of numbers, nums, that might contain duplicates, return all possible
unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

'''


class Solution:

    # index =  0 1 2
    #         [1,2,3]
    #
    #         1xx             2xx             3xx
    #
    #         12x 13x         21x 23x         31x 32x
    #
    #         123 132         213 231         312 321
    #
    # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    # index =  0 1 2
    #         [1,1,2]
    #
    # sort:       1,1,2
    #
    #     1xx         1xx->remove         2xx
    #
    #     11x 12x                         21x 21x-> remove
    #
    #     112 121                         211
    #
    #     Output: [[1,1,2],[1,2,1],[2,1,1]]

    # Time O(N!) Space O(N)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def mutation(build, index_set):

            if len(build) == len(nums):
                result.append(build)
                return

            item_set = set()
            for i in range(len(nums)):
                if i not in index_set and nums[i] not in item_set:
                    index_set.add(i)
                    item_set.add(nums[i])
                    mutation(build + [nums[i]], index_set)
                    index_set.remove(i)

        if not nums: return None
        result = []
        mutation([], set())
        return result


'''
    # Time O(N!) Space O(N)
    # runtime = 48 ms
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def permutate(build, lst):

            if len(build) == len(nums):
                result.append(build)
                return

            item_set = set()
            for i in range(len(lst)):
                if lst[i] not in item_set:
                    permutate(build+[lst[i]], lst[:i]+lst[i+1:])
                    item_set.add(lst[i])


        if not nums: return None
        result = []
        permutate([], nums)
        return result
'''
