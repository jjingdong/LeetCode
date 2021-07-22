'''
748. Shortest Completing Word
Easy

Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.



Example 1:

Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"
Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
"step" contains 't' and 'p', but only contains 1 's'.
"steps" contains 't', 'p', and both 's' characters.
"stripe" is missing an 's'.
"stepple" is missing an 's'.
Since "steps" is the only word containing all the letters, that is the answer.
Example 2:

Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
Output: "pest"
Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.
Example 3:

Input: licensePlate = "Ah71752", words = ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]
Output: "husband"
Example 4:

Input: licensePlate = "OgEu755", words = ["enough","these","play","wide","wonder","box","arrive","money","tax","thus"]
Output: "enough"
Example 5:

Input: licensePlate = "iMSlpe4", words = ["claim","consumer","student","camera","public","never","wonder","simple","thought","use"]
Output: "simple"


Constraints:

1 <= licensePlate.length <= 7
licensePlate contains digits, letters (uppercase or lowercase), or space ' '.
1 <= words.length <= 1000
1 <= words[i].length <= 15
words[i] consists of lower case English letters.
'''


class Solution:


# step, steps
# s:1, t:1, e:1, p:1


'''
    # note. solution from discussion session
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        pc = Counter(filter(lambda x : x.isalpha(), licensePlate.lower()))
        return min([w for w in words if Counter(w) & pc == pc], key=len)

    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        d = Counter(x for x in licensePlate.lower() if x.isalpha())
        return min([w for w in words if not d - Counter(w)], key = len)

    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate = Counter([c for c in licensePlate.lower() if c.isalpha()])
        ans = ""
        for word in words:
            if (ans == "" or len(word) < len(ans)) and not plate - Counter(word):
                ans = word
        return ans

    def shortestCompletingWord(self, lp, words):
        cntr_lp, res = collections.defaultdict(int), None
        for char in lp:
            if char.isalpha():
                cntr_lp[char.lower()] += 1
        for word in words:
            check = dict(cntr_lp)
            for char in word:
                char = char.lower()
                if char in check:
                    check[char] -= 1
                    if not check[char]:
                        del check[char]
            if not check and (not res or len(word) < len(res)):
                res = word
        return res
'''

'''
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        c_dict = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}

        target = 1
        for char in licensePlate:
            if char.isalpha():
                target *= c_dict[char.lower()]

        result = ''
        for w in words:
            if result == '' or len(w) < len(result):
                value = 1
                for char in w:
                    value *= c_dict[char.lower()]
                if value % target == 0:
                    result = w

        return result

'''

'''                  
    # Note. didn't implement the following algorithm
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        c_dict = collections.defaultdict(int)
        for char in licensePlate:
            if char.isalpha():
                c_dict[char.lower()] += 1

        print(c_dict)




        return ''
'''