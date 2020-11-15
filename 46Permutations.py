'''
46. Permutations
Medium

Given a collection of distinct integers, return all possible permutations.
Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''


class Solution:

    # Recursion Tree
    #         1
    #         |
    #         1
    #
    #         1, 2
    #     /         \
    #   1,2         2,1
    #
    #               1, 2, 3
    #     i=0          i=1          i=2
    #      1xx             2xx            3xx                1 digit in 1st position
    #
    #   i=1  i=2      i=0  i=2         i=0  i=1
    #   12x   13x        21x   23x     31x   32x            1 digit in 2nd position
    #
    #   i=2  i=1      i=2  i=0    i=1  i=0
    #   123  132      213  231    312  321

    # Time O(N!) Space O(N)
    def permute(self, nums: List[int]) -> List[List[int]]:

        def mutation(build, index_set):

            if len(build) == len(nums):
                results.append(build)
                return

            for i in range(len(nums)):
                if i not in index_set:
                    index_set.add(i)
                    mutation(build + [nums[i]], index_set)
                    index_set.remove(i)

        results = []
        mutation([], set())
        return results


'''
    # Time O(N!) Space O(N!)
    def permute(self, nums: List[int]) -> List[List[int]]:

        def mutation(build, lst):

            if len(build) == len(nums):
                results.append(build)
                return

            for i in range(len(lst)):
                mutation(build + [lst[i]], lst[:i] + lst[i+1:])

        results = []
        mutation([], nums)
        return results
'''

