'''
340. Longest Substring with At Most K Distinct Characters
Medium

Given a string s and an integer k, return the length of the longest substring of s t
hat contains at most k distinct characters.



Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.


Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50

'''


class Solution:

    #           k = 2 distinct characters

    #    output = longest
    #    sliding O(N)
    #                 e   c   e   b   e    e              k = 2
    #                 ||
    #                 lr                    {e:1}
    #                 |   |
    #                 l   r                    {e:1, c:1}  -> find the 1st result = 2
    #                 |       |
    #                 l       r                    {e:2, c:1}  -> find the 1st result = 3
    #                 |           |
    #                 l           r              b is not in {e:2, c:1} , stop moving
    #                     |       |
    #                     l       r               {e:1, c:1, b:1} not
    #                         |    |
    #                         l     r               {e:1, b:1}   result = 2
    #                         |        |
    #                         l        r               {e:2, b:1}   result = 3
    #                         |              |
    #                         l              r               {e:3, b:1}   result = 4

    #                                                                            | at the end output = 4

    #     1. l,r points ---> iterate
    #     2. r point: to find available result
    #     3. l point: once you find the 1st result, the l pointer move to make it not valid
    #     4. r go one step
    #         for (r = 0, ......, r = size-1)

    #                 # do something here

    #                 while ???:

    #                     l++
    #     5 l pointer is a while loop

    # Time O(N) Space O(N)
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        if not s or not k: return 0

        size = len(s)
        l = 0
        r = 0
        c_dict = collections.defaultdict(int)
        result = 1
        count = 0
        for r in range(size):
            char_r = s[r]
            if c_dict[char_r] == 0:
                count += 1
            c_dict[char_r] += 1

            while count > k:
                char_l = s[l]
                c_dict[char_l] -= 1
                if c_dict[char_l] == 0:
                    count -= 1
                    del c_dict[char_l]
                l += 1

            result = max(result, r - l + 1)

        return result



