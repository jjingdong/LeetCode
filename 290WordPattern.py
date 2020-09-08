'''
290. Word Pattern
Easy

Given a pattern and a string str, find if str follows the same pattern.


Here follow means a full match, such that there is a bijection between
 a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains
 lowercase letters that may be separated by a single space.
'''


class Solution:

    #         pattern = "abba", str = "dog cat cat dog"
    #
    #         a: dog
    #         b: cat
    #
    #         abba
    #           |
    #         dog cat cat dog
    #                  |
    #         a:dog
    #         b:cat

    # Time O(N) Space O(N) runtime = 28 ms
    def wordPattern(self, pattern: str, str: str) -> bool:

        if not pattern or not str: return False

        lst = str.split()
        if len(pattern) != len(lst): return False

        w_dict = {}
        reverse_w_dict = {}
        for i in range(len(pattern)):
            p = pattern[i]
            s = lst[i]
            if p not in w_dict:
                if s not in reverse_w_dict:
                    w_dict[p] = s
                    reverse_w_dict[s] = p
                else:
                    return False
            else:
                if w_dict[p] != s:
                    return False

        return True