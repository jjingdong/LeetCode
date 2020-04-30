'''
3. Longest Substring Without Repeating Characters
Medium

Given a string, find the length of the longest substring without repeating characters.
Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution:

    # p w w k e w
    # i j            dict = {'p': 1, 'w' : 1}
    # i   j          count = 2
    #   i j
    #     i j
    #     i     j    count = 3
    # ......
    # Hashmap to count chars

    # Note. this is not optimal solution

    # Time O(N^2) Space O(N)
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s is None: return None
        if s == '': return 0

        i, j = 0, 0
        count_dict = {}
        count = 0

        while i <= j and j < len(s):

            cur_char = s[j]
            if s[j] in count_dict:

                if count_dict[cur_char] == 0:
                    count_dict[cur_char] += 1
                    j += 1
                else:
                    i += 1
                    j = i
                    count_dict = {}

            else:
                count_dict[cur_char] = 1
                j += 1

            count = max(count, j - i)

        return count

