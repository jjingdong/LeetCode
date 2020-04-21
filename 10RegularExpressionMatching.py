'''
10. Regular Expression Matching
Hard

3820

660

Add to List

Share
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
Note:
	•	s could be empty and contains only lowercase letters a-z.
	•	p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''


class Solution:

    # Python:
    #     first_match = bool(text) and pattern[0] in {text[0], '.'}
    # Java:
    #     boolean first_match = (!text.isEmpty() && (pattern.charAt(0) == text.charAt(0) || pattern.charAt(0) == '.'));

    # if it has *
    # aabb
    # a*b*
    # compare aabb with b* Eg. bb with a*b*
    #            ---> delete matching character in the text
    #                 assume there is 0 a's
    # or compare bb with a*b*  E.g. aabb with a*b*
    #            ---> ignore this part of the pattern
    #                 assume there is 1 a's

    # Dynamic programming:
    # to save match(text[i:], pattern[j:])
    # memo = {} -> matrix

    # Solution is done
    # Code is not done

    def isMatch(self, s: str, p: str) -> bool:
