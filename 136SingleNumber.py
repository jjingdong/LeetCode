# 136. Single Number
# Easy
#
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Example 1:
# Input: [2,2,1]
# Output: 1
# Example 2:
# Input: [4,1,2,1,2]
# Output: 4

class Solution:

    # [4, 1, 2, 1, 2]

    # XOR gate -> if it's odd number
    # XOR: (a and not b) or (not a and b)
    # bool(a) ^ bool(b)
    # a XOR 0 = 0, a XOR a = 0
    # a XOR b XOR a  = b
    # Time O() Space O()
    def singleNumber(self, nums: List[int]) -> int:
        output = 0
        for i in range(len(nums)):
            cur = nums[i]
            output = output ^ cur

        return output

    # 2 * (a + b + c) - (a + a + b + b + c) = c
    # Time O(N) Space O(N)
#     def singleNumber(self, nums: List[int]) -> int:

#         return 2 * sum(set(nums)) - sum(nums)


# Time O(N) Space O(N)
#     def singleNumber(self, nums: List[int]) -> int:
#         map = {}

#         for i in range(len(nums)):
#             cur = nums[i]
#             if cur in map:
#                 map[cur] += 1
#             if cur not in map:
#                 map[cur] = 1

#         for k,v in map.items():
#             if v == 1:
#                 return k

#         return None


# Time: O(N^2), Space O(N)
#     def singleNumber(self, nums: List[int]) -> int:
#         non_duplicated = []

#         for i in range(len(nums)):
#             if nums[i] not in non_duplicated:
#                 non_duplicated.append(nums[i])
#             else:
#                 non_duplicated.remove(nums[i])

#         return non_duplicated[0]








