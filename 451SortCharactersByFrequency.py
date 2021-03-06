'''
451. Sort Characters By Frequency
Medium

Given a string, sort it in decreasing order based on the frequency of characters.
Example 1:
Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

'''


class Solution:

    # Time O(N) Space O(1), not Time O(NlogN) Space O(N)
    # Not counting output size in your space analyses. Also sorting a dict with 26 keys can be considered constant time—learned
    def frequencySort(self, s: str) -> str:
        result = ''
        count_dict = collections.Counter(s)

        for k, v in count_dict.most_common():
            result += ''.join(k * v)

        return result