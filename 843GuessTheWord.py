'''
843. Guess the Word

This is an interactive problem.

You are given an array of unique strings wordlist where wordlist[i] is 6
letters long, and one word in this list is chosen as secret.

You may call Master.guess(word) to guess a word. The guessed word should
have type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact
matches (value and position) of your guess to the secret word. Also, if
your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have exactly 10 guesses to guess the word. At the
end of any number of calls, if you have made 10 or fewer calls to Master.guess
 and at least one of these guesses was secret, then you pass the test case.



Example 1:

Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"],
numguesses = 10
Output: You guessed the secret word correctly.
Explanation:
master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6
matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
Example 2:

Input: secret = "hamada", wordlist = ["hamada","khaled"], numguesses = 10
Output: You guessed the secret word correctly.


Constraints:

1 <= wordlist.length <= 100
wordlist[i].length == 6
wordlist[i] consist of lowercase English letters.
All the strings of wordlist are unique.
secret exists in wordlist.
numguesses == 10
'''

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:

    # Note. there is no solution can guarantee to find the secret word within 10 guesses. Just finding a reasonable solution.

    # Solution I, pick first 10 numbers
    # Time O(1) Space O(1), 10/100 = 10% -> chance to be right
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:

        for w in wordlist:
            if master.guess(w) == 6:
                break

    # Solution II, pick 10 random numbers
    # Time O(1) Space O(1), 10/100 = 10% -> chance to be right, evenly distributed
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:

        for i in range(10):
            cur = random.choice(wordlist)
            if master.guess(cur) == 6:
                break

    # Solution III
    # Time O(N) Space O(N)
    # 100 words
    # possibility = 0, 1, 2, 3, 4, 5, 6, no of possibility = 7, if it's evenly distributed
    # 1 guess:
    #     100/7 = 14.29 ~ 15 words
    # 2 guess:
    #     15 words, no. of word to guess = 14
    #     ....
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:

        # same function as below
        #         def similar(w1, w2):
        #             count = 0
        #             for i in range(6):
        #                 if(w1[i] == w2[i]):
        #                     count += 1

        #             return count

        def similar(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        used = set()
        new_list = []
        for i in range(10):

            random.shuffle(wordlist)
            cur = random.choice(wordlist)
            while cur in used:
                cur = random.choice(wordlist)
            used.add(cur)

            match = master.guess(cur)
            if match == 6:
                break

            for j in range(len(wordlist)):
                w = wordlist[j]
                if w not in used:
                    if similar(cur, w) == match:
                        new_list.append(w)

            wordlist = new_list
            new_list = []

        # Solution IIII
        # Time O() Space O()
        # Calculate occurance
        def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:

            def similar(w1, w2):
                count = 0
                for i in range(6):
                    if w1[i] == w2[i]:
                        count += 1
                return count

            size = len(wordlist)
            counts = []
            n = 0
            while n != 6:

                for i in range(6):
                    lst = []
                    for w in wordlist:
                        lst.append(w[i])
                    c_dict = collections.Counter(lst)
                    counts.append(c_dict)

                top_score = 0
                top_word = None
                for w in wordlist:
                    score = 0
                    for i in range(6):
                        cur = w[i]
                        score += counts[i][w[i]]
                    if top_score < score:
                        top_score = score
                        top_word = w

                # print(top_word)
                n = master.guess(top_word)

                wordlist_new = []
                for w in wordlist:

                    if similar(w, top_word) == n:
                        wordlist_new.append(w)
                wordlist = wordlist_new