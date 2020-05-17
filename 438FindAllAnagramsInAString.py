'''
438. Find All Anagrams in a String
Medium

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.
Example 1:
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''


class Solution:

    # primes = 2, 3, 5, 7, 11, 13, 17...
    # Note. Using primes number is not the most efficient solution for this
    #
    # Solution I: Brute Force --- Time Limit Exceeded
    #
    # Solution II: value = value * s[i] / s[i-len(p)]
    #
    # Solution III: dict + sliding window
    #
    # Solution IV: two arrays

    # Time O(N) Space O(N), runtime = 432 ms
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(s) < len(p): return []
        indexes = []

        primes = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31,
                  'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
                  'w': 83, 'x': 89, 'y': 97, 'z': 101}

        p_primes = 1
        for char in p:
            p_primes *= primes[char]
        print(p_primes)

        s_primes = 1
        for j in range(0, len(p)):
            s_primes *= primes[s[j]]
        print(s_primes)
        if s_primes == p_primes: indexes.append(j - len(p) + 1)

        for i in range(len(p), len(s)):
            s_primes = s_primes * primes[s[i]] // primes[s[i - len(p)]]
            if s_primes == p_primes:
                indexes.append(i - len(p) + 1)

        return indexes


'''
    # Time O(MN) Space O(N), using brute force
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(s) < len(p): return []
        indexes = []

        primes = {'a' : 2, 'b' : 3, 'c' : 5, 'd' : 7, 'e' : 11, 'f' : 13, 'g' : 17, 'h' : 19, 'i' : 23, 'j' : 29, 'k' : 31, 'l': 37, 'm' : 41, 'n' : 43, 'o' : 47, 'p' : 53, 'q' : 59, 'r' : 61, 's' : 67, 't': 71, 'u' : 73, 'v' : 79, 'w' : 83, 'x' : 89, 'y' : 97, 'z' : 101}

        p_primes = 1
        for char in p:
            p_primes *= primes[char]

        for i in range(len(s) - len(p) + 1):
            s_primes = 1
            for c in s[i:len(p)+i]:
                s_primes *= primes[c]
            if s_primes == p_primes:
                indexes.append(i)

        return indexes
'''
