'''
159. Longest Substring with At Most Two Distinct Characters
Medium

Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.
Example 1:
Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:
Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.

'''


class Solution:

    # Time O(N)) Space O(1), runtime = 52 ms
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        if not s: return 0
        if len(s) <= 2: return len(s)

        i, max_len = 0, 2
        char1, char2 = s[0], None
        num1, num2 = 1, 0
        for j in range(1, len(s)):
            cur_char = s[j]
            if cur_char in (char1, char2):
                if cur_char == char1:
                    num1 += 1
                else:
                    num2 += 1
                max_len = max(max_len, j - i + 1)
            elif char1 == None:
                char1 = cur_char
                num1 += 1
                max_len = max(max_len, j - i + 1)
            elif char2 == None:
                char2 = cur_char
                num2 += 1
                max_len = max(max_len, j - i + 1)
            else:
                max_len = max(max_len, j - i)
                while char1 is not None and char2 is not None:
                    if s[i] == char1:
                        num1 -= 1
                        if num1 == 0:
                            char1 = None
                    else:
                        num2 -= 1
                        if num2 == 0:
                            char2 = None
                    i += 1

                if char1 is None:
                    char1 = cur_char
                    num1 += 1
                elif char2 is None:
                    char2 = cur_char
                    num2 += 1

        return max_len



