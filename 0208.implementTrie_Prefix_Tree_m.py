"""
208. Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""

"""
Amazon OA Problem
Google OA Problem
Facebook OA Problem
Microsoft OA Problem
"""


class Trie:
    """
    prefix tree, each node store one char, the root is empty.
    each node has 26 nodes to store 26 chars(assume there only care about lowercase latin letters).
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # new_val = list or dict, the pointer points to the same address
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c] = dict()
            cur = cur[c]

        cur["*"] = True
        print(self.trie)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.trie
        for c in word:
            if c not in cur:
                return False
            else:
                cur = cur[c]

        if "*" in cur and cur["*"] is True:
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.trie
        for c in prefix:
            if c not in cur:
                return False
            else:
                cur = cur[c]

        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
word = "chenjinyu"
obj.insert(word)
param_2 = obj.search(word)
prefix = "chen"
param_3 = obj.startsWith(prefix)
