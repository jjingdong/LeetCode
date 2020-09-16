'''
269. Alien Dictionary
Hard

There is a new alien language which uses the latin alphabet. However, the order among
letters are unknown to you. You receive a list of non-empty words from the dictionary,
where words are sorted lexicographically by the rules of this new language. Derive the
order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".
'''


class Solution:

    # Time O(P), P = no. of chars in all input string
    # Space O(V+E), for dictionary. Since dictionary only has 26 keys, relations maximum is 26^2. It's O(1). N = total lenght of all words. so O(V+min(V^2, N))
    # runtime = 36 ms
    def alienOrder(self, words: List[str]) -> str:

        # Time O(P), P = no. of chars to compare in order to create the dictionary
        # Space O(V+E), for dictionary
        def create_dict():

            chars = set(''.join(words))
            g_dict = {char: [] for char in chars}
            reverse_dict = {char: [] for char in chars}

            for w1, w2 in zip(words, words[1:]):

                if len(w1) > len(w2) and w1[:len(w2)] == w2:
                    return {}, {}

                for char1, char2 in zip(w1, w2):
                    if char1 != char2:

                        if char2 not in g_dict[char1]:
                            g_dict[char1].append(char2)
                            reverse_dict[char2].append(char1)
                        break

            return g_dict, reverse_dict

        # Time O(V+E), V = no. of letters, E = no. of connections, so it's O(N)
        # Space O(V+E), for dictionary
        def topological_sort(g_dict, reverse_dict):
            todo = collections.deque([k for k, v in reverse_dict.items() if not v])
            result = ''

            while todo:
                node = todo.popleft()
                result += str(node)

                for next_node in g_dict[node]:
                    reverse_dict[next_node].remove(node)
                    if not reverse_dict[next_node]:
                        todo.append(next_node)

            if len(result) < len(reverse_dict):
                return ''

            return result

        if not words: return ''
        g_dict, reverse_dict = create_dict()
        if g_dict == {}:
            return ''
        return topological_sort(g_dict, reverse_dict)

