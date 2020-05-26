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

    # Time O(N!) Space O(N!)
    def permute(self, nums: List[int]) -> List[List[int]]:

        def mutation(build, lst):

            if len(build) == len(nums):
                results.append(build)
                return

            for i in range(len(lst)):
                mutation(build + [lst[i]], lst[:i] + lst[i + 1:])

        results = []
        mutation([], nums)
        return results


