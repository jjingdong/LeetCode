'''
76. Minimum Window Substring
Hard

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:
	•	If there is no such window in S that covers all characters in T, return the empty string "".
	•	If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''


class Solution:

    # index = 0 1 2 3 4 5 6 7 8 9 10 11 12
    #        "A D O B E C O D E B A  N  C", t = "ABC" ----> use count_dict = {A: 0, B: 0, C: 0}
    #         i         j
    #               i   j
    #               i             j

    # Time O(N) Space O(N)
    def minWindow(self, s: str, t: str) -> str:

        if s is None or t is None: return None
        if s == [] or t == []: return ""

        i, start_i, end_j = 0, 0, 0
        # t_dict = count_dict = {A: 1, B: 1, C: 1}
        t_dict = collections.Counter(t)
        missing_char_no = len(t_dict)
        window_len = float('inf')
        count_dict = {}
        for c in t:
            # count_dict = {A: 0, B: 0, C: 0}
            count_dict[c] = 0

        for j in range(len(s)):

            if s[j] in t:
                count_dict[s[j]] += 1
                if count_dict[s[j]] == t_dict[s[j]]:
                    missing_char_no -= 1

                while missing_char_no == 0:
                    if window_len > j - i + 1:
                        window_len = j - i + 1
                        start_i = i
                        end_j = j

                    if s[i] in count_dict:
                        count_dict[s[i]] -= 1
                        if count_dict[s[i]] < t_dict[s[i]]:
                            missing_char_no += 1

                    i += 1

        if window_len == float('inf'): return ''
        return s[start_i:end_j + 1]




