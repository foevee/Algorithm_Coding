"""
Implement a trie (i.e. prefix tree) with insert, search, and startsWith methods.

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


Method 1: Save all single characters of the word in the trie (a, ap, app, appl, apple):
Define an extra class TreeNode to save each node on the trie
  this class uses dictionary to save its children (key->value as: prefix->TreeNode)
  also uses an bool variable is_word to track if the current prefix is saved as a word 
  (i.e. insert only 'apple' and search 'app' will return False since 'app' is not saved as word)

Complexity: Time O(N), Space O(N^2)


Method 2 (less efficient): Save all prefix of the word in the trie (a, p, p, l, e):
Define an extra class TreeNode to save each node on the trie
  this class uses dictionary to save its children (key->value as: single character->TreeNode)
  also uses an bool variable is_word to track if the current character is saved as a word 
  (i.e. insert only 'apple' and search 'app' will return False since 'app' is not saved as word)

Complexity: Time O(N), Space O(N)
"""
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

import collections

### Method 1: save all single characters
class TrieNode:
    def __init__(self, is_word=False):
        self.val = None #the root node save empty string
        self.children = {} #each dict key->value saves string->TreeNode
        self.is_word = is_word #use a bool to save if the current node is word (or prefix)

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root.children
        # search chracter in the prefix tree (dictionary)
        for i, c in enumerate(word): 
            if c not in curr:
                curr[c] = TrieNode()
            if i==len(word)-1:
                # last step insert the word, need to specify is a word
                curr[c].is_word = True
            curr = curr[c].children   
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root.children
        for i, c in enumerate(word):
            if c not in curr:
                return False
            if i==len(word)-1: #last step, check if word in tree and also as a word
                return curr[c].is_word
            curr = curr[c].children
        

    def startsWith(self, start_with: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root.children
        for c in start_with:
            if c not in curr:
                return False
            curr = curr[c].children
        return True
    

### Method 2: save all prefix
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root.children
        prefix = ""
        #1. search prefix tree (dictionary)
        for c in word: 
            prefix += c
            if prefix not in curr:
                curr[prefix] = TrieNode()
            if prefix==word: #last step insert the word, need to specify is a word
                curr[prefix].is_word = True
            curr = curr[prefix].children
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """  
        curr = self.root.children
        prefix = ""
        for c in word:
            prefix += c
            if prefix not in curr:
                return False
            if prefix==word: #last step, check if word in tree and also as a word
                return (word in curr) and curr[word].is_word
            curr = curr[prefix].children
        

    def startsWith(self, start_with: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root.children
        prefix = ""
        for c in start_with:
            prefix += c
            if prefix not in curr:
                return False
            curr = curr[prefix].children
        return True
        


