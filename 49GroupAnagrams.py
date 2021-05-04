
'''
49. Group Anagrams
Medium

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''


class Solution:

    # a  b  c  d  e  f  g  h  i  j  k  l  m  n
    # o  p  q  r  s  t  u  v  w  x  y  z

    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,

    # Time O(KN)
    # Space O(KN)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        primes = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31,
                  'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
                  'w': 83, 'x': 89, 'y': 97, 'z': 101}

        countMap = {}

        for word in strs:  # word
            count = 1
            for c in word:
                count *= primes[c]
            if count not in countMap:
                countMap[count] = [word]
            else:
                countMap[count].append(word)

        return countMap.values()

    class Solution:

        # Time O(NK), Space O(NK)
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

            c_dict = collections.defaultdict(list)

            for word in strs:

                # Space O(1), Time O(1)
                array = [0] * 26
                for char in word:
                    array[ord(char) - ord('a')] += 1

                # print(array)
                string = ' '.join([str(ele) for ele in array])

                c_dict[string].append(word)

            # print(c_dict)
            return c_dict.values()

    '''
        # Time O(NKlogK), Space O(NK)
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

            # Space O(NM)
            c_dict = collections.defaultdict(list)
            #O(NKlogK)
            for word in strs:
                # O(klogK)
                new_word = sorted(word)
                # print(new_word)
                c_dict[str(new_word)].append(word)

            # print(c_dict)
            return c_dict.values()

    '''

    '''

    # a  b  c  d  e  f  g  h  i  j  k  l  m  n
    # o  p  q  r  s  t  u  v  w  x  y  z

    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,

    # primes = {'a' : 2, 'b' : 3, 'c' : 5, 'd' : 7, 'e' : 11, 'f' : 13, 'g' : 17, 'h' : 19, 'i' : 23, 'j' : 29, 'k' : 31, 'l': 37, 'm' : 41, 'n' : 43, 'o' : 47, 'p' : 53, 'q' : 59, 'r' : 61, 's' : 67, 't': 71, 'u' : 73, 'v' : 79, 'w' : 83, 'x' : 89, 'y' : 97, 'z' : 101}

        #Time O(KN)
        #Space O(KN)
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

            chars = 'abcdefghijklmnopqrstuvwxyz'
            primes = {}


            index = 0
            for possiblePrime in range(2, 1000):

                if index == 26:
                    break

                isPrime = True
                for num in range(2, possiblePrime):
                    if possiblePrime % num == 0:
                        isPrime = False
                        break

                if isPrime:
                    primes[chars[index]] = possiblePrime
                    index += 1

            print(primes)

            countMap = {}

            for word in strs: #word 
                count = 1
                for c in word:
                    count *= primes[c]
                if count not in countMap:
                    countMap[count] = [word]
                else:
                    countMap[count].append(word)

            return countMap.values()

    '''



