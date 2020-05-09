'''
126. Word Ladder II
Hard

1584

229

Add to List

Share
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''


class Solution:

    # hit -> *it, h*t, hi*
    # hot -> *ot, h*t, ho*
    # dict = {'*ot', [dot, lot], ..., ...}
    #
    # Solution I: BFS

    # Time O(MNK) Space O(MN), M = len(wordList), N = len(word), K = len(paths)
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        if beginWord is None or endWord is None or wordList is None: return None

        results = []

        # word_dict = {'*ot': ['hot', 'dot', 'lot'], 'h*t': ['hot'], ..., ...}
        word_dict = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                word_dict[key].append(word)

        # traverse the Graph
        queue = collections.deque()
        queue.append((beginWord, 0, []))
        shortest_depth = None
        while len(queue) >= 1:

            node, depth, path = queue.popleft()
            if shortest_depth != None and shortest_depth < depth:
                return results

            if node == endWord:
                if (shortest_depth) is None:
                    shortest_depth = depth
                if shortest_depth == depth:
                    results.append(path + [node])

            for i in range(len(node)):
                node_key = node[:i] + '*' + node[i + 1:]

                if node_key in word_dict:
                    for node_value in word_dict[node_key]:

                        if node_value not in path and node_value != node:
                            queue.append((node_value, depth + 1, path + [node]))

        return results









