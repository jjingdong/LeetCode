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
    # .              i   j
    # Solution is not done

    # Time O(N) Space O(1)
    def minWindow(self, s: str, t: str) -> str:

        if s is None or t is None: return None
        if s == [] or t == []: return ""

        i, j, startIndex = 0, 0, 0
        length = 0
        count_dict = {}
        for c in t:
            count_dict[c] = 0

        while i <= j and j < len(s):

            if s[j] not in count_dict:
                j += 1
            if s[i] not in count_dict:
                i += 1
            else:

                count_dict[s[j]] += 1
                hasAllChars = True
                for v in count_dict.values():
                    if v < 1:
                        hasAllChars = False
                if hasAllChars == True:
                    rangeSize = len(s[i:j + 1])
                    if length = 0:
                        length = rangeSize
                        startIndex = i
                    elif rangeSize < length:
                        length = rangeSize
                        startIndex = i
                    i += 1

                else:
                    print('there')
                    j += 1

        return s[startIndex:startIndex + length]

