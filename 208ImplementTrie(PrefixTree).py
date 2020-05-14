'''
208. Implement Trie (Prefix Tree)
Medium

Implement a trie with insert, search, and startsWith methods.
Example:
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:
	•	You may assume that all inputs are consist of lowercase letters a-z.
	•	All inputs are guaranteed to be non-empty strings.
'''


class Trie:

    # {'a': {'p' : {'p': {'l': {'e': {'#': True}}}}}}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end = '#'

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for w in word:
            if w not in root:
                root[w] = {}
            root = root[w]
        root[self.end] = True
        print(root)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for w in word:
            if w in root:
                root = root[w]
            else:
                return False

        if self.end in root:
            return root[self.end]
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for p in prefix:
            if p in root:
                root = root[p]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)