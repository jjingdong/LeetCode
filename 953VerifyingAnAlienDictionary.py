'''
953. Verifying an Alien Dictionary
Easy

In an alien language, surprisingly they also use english lowercase letters, but possibly
in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence
the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter
(in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
'''


class Solution:

    # Time O(N), N = length of words, Space O(1), runtime = 36 ms
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        for w1, w2 in zip(words, words[1:]):

            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return False

            for char1, char2 in zip(w1, w2):
                if char1 != char2:
                    if order.index(char1) > order.index(char2):
                        return False
                    break

        return True
