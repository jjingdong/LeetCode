'''
78. Subsets
Medium

Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''


class Solution:

    # Eg.1.[] -> []

    # Eg.2  [1] -> [], [1]

    # Eg.2.
    #   []
    #  |   |
    # [], [1]

    # Eg.2. [1, 2] -> [], [2], [1], [1, 2]

    #        [],i = 0
    #      /          \
    #   [],i=1     [1],i=1
    #  /   \      /     \
    # [],i=2, [2],i=2, [1],i=2, [1,2],i=2
    # [], [2], [1], [1, 2]

    # Solution I: Backtracking
    #
    # Solution II: Bit Mapping

    # bitmask: presence / absence
    # 1 2 3
    # 0 0 0
    # 0 0 1
    # 0 1 0
    # 0 1 1
    # . . .
    # . . .

    # Time O(2^N * N) Space O(2^N * N), using bitmask, runtime = 36 ms
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        output = []
        for i in range(2 ** n, 2 ** (n + 1)):
            bitmask = bin(i)[3:]

            value = []
            for j in range(n):
                if bitmask[j] == '1':
                    value.append(nums[j])
            output.append(value)

        return output


'''
    # Time O(N * 2^N) Space O(N * 2^N), Using backtracking, runtime = 32 ms
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if nums is None: return None

        results = []

        def traverse(build, index):

            if index == len(nums):
                results.append(build)
                return

            traverse(build, index+1)
            traverse(build + [nums[index]], index+1)

        traverse([], 0)
        return results
'''







