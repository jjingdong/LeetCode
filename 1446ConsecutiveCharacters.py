'''
1446. Consecutive Characters
Easy

Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.



Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Example 3:

Input: s = "triplepillooooow"
Output: 5
Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11
Example 5:

Input: s = "tourist"
Output: 1


Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.
'''


class Solution:

    #         leetcode
    #         ee -> 2
    #
    #         abbcccddddeeeeedcba
    #         eeeee -> 5
    #
    #         triplepillooooow
    #         ooooo -> 5
    #
    #         hooraaaaaaaaaaay
    #         aaaaaaaaaaa -> 11
    #
    #         tourist"
    #         t->1

    # Time O(N) Space O(1)
    # runtime = 40ms, 75%
    def maxPower(self, s: str) -> int:

        max_count = 1
        count = 1

        pre = Nones
        for char in s:

            if pre == char:
                count += 1
            else:
                count = 1

            max_count = max(max_count, count)
            pre = char

        return max_count
