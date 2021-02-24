'''
424. Longest Repeating Character Replacement
Medium

Given a string s that consists of only uppercase English letters, you can perform
at most k operations on that string.

In one operation, you can choose any character of the string and change it to any
other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can
 get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.


Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''


class Solution:

    # Time O(N) Space O(1), it's O(1) since we only have 26 characters
    def characterReplacement(self, s: str, k: int) -> int:

        size = len(s)
        max_value = 0
        l = 0
        result = 0
        count = collections.defaultdict(int)
        for r in range(size):

            count[s[r]] += 1
            max_value = max(max_value, count[s[r]])

            while r - l + 1 - max_value > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1);

        return result


    # Time O(N) Space O(1), it's O(1) since we only have 26 characters
    def characterReplacement(self, s: str, k: int) -> int:

        max_value = 0
        result = 0
        count = collections.defaultdict(int)
        for r in range(len(s)):

            count[s[r]] += 1
            max_value = max(max_value, count[s[r]])
            if result - max_value < k:
                result += 1
            else:
                count[s[r - result]] -= 1

        return result

