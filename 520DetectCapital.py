'''
520. Detect Capital
Easy

Given a word, you need to judge whether the usage of capitals in it is
 right or not.

We define the usage of capitals in a word to be right when one of the
following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.


Example 1:

Input: "USA"
Output: True


Example 2:

Input: "FlaG"
Output: False


Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
'''


class Solution:

    # Time O(N) Space O(1), runtime = 32 ms
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


'''
    # Time O(N) Space O(1), runtime = 52 ms
    def detectCapitalUse(self, word: str) -> bool:

#         USA
#         re = [A-Z]+

#         leetcode
#         re = [a-z]+

#         Google
#         re = [A-Z][a-z]+

#         re = [A-Z]*|[A-Z]?[a-z]*

        pattern = '[A-Z]*|[A-Z]?[a-z]*'
        return re.fullmatch(pattern, word)
'''

