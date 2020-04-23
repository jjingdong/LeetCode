'''
127. Word Ladder
Medium

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
	1.	Only one letter can be changed at a time.
	2.	Each transformed word must exist in the word list.
Note:
	•	Return 0 if there is no such transformation sequence.
	•	All words have the same length.
	•	All words contain only lowercase alphabetic characters.
	•	You may assume no duplicates in the word list.
	•	You may assume beginWord and endWord are non-empty and are not the same.
Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation
'''


class Solution:

    # beginWord = 'hit'
    # wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    # create undirection Graph from it:
    #   hit -- hot -- dot -- dog -- cog
    #                         |     /
    #                         |   /
    #                          log -- lot
    # traverse the graph ---> Donot need to create the graph
    #
    # Find the next word:
    # Solution I:
    # dog -> *og
    # dog -> d*g
    # dog -> do*
    # dog --> d*g <-- dig
    # having a common generic transformation means two words are connected and differ by one letter
    # create a hashmap
    # all_combo_dict = {'*ot':['hot','dot'], 'h*t':['hot'], 'ho*':['hot'],
    #                   'd*t':['dot'], 'do*':['dot'],.......
    #                  }
    # Solution II:
    # string = 'abcdefghijklmnopqrstuvwxyz'
    # newWord = word[:i] + string[j] + word[i+1:]

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if beginWord == None or endWord == None or wordList == None:
            return None

        length = len(beginWord)
        if length != len(endWord):
            return 0

        findEndWord = False
        for word in wordList:
            if len(word) != length:
                return 0
            if word == endWord:
                findEndWord = True

        if findEndWord == False:
            return 0

        combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                # Note. it will display an empty string not in the range
                newWord = word[:i] + '*' + word[i + 1:]
                combo_dict[newWord].append(word)

        # traverse the graph --> donot need to create the graph

        level = 0
        queue = collections.deque([(beginWord, 0)])
        visited = {beginWord: True}
        while queue:
            curWord, level = queue.popleft()
            if curWord == endWord:
                return level + 1
            else:
                for i in range(length):
                    lookWord = curWord[:i] + '*' + curWord[i + 1:]
                    for word in combo_dict[lookWord]:
                        if word not in visited:
                            queue.append((word, level + 1))
                            visited[word] = True

        return 0







