"""
    208. Implement Trie (Prefix Tree)
    Medium

    A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently
    store and retrieve keys in a dataset of strings. There are various applications of this
    data structure, such as autocomplete and spellchecker.

    Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was
    inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string
    word that has the prefix prefix, and false otherwise.


    Example 1:

    Input
    ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    Output
    [null, null, true, false, true, null, true]

    Explanation
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // return True
    trie.search("app");     // return False
    trie.startsWith("app"); // return True
    trie.insert("app");
    trie.search("app");     // return True


    Constraints:

    1 <= word.length, prefix.length <= 2000
    word and prefix consist only of lowercase English letters.
    At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""
class TrieNode:
    def __init__(self):
        # create a list with spot 26 for each alphabet
        self.children = [None] * 26
        # mark if a word is end or not
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            # get alphabetical order (1 - 26) of current char
            i = ord(c) - ord("a")
            if curr.children[i] is None:
                # create a node of each char of word
                # if current node is not created
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        # mark if end of the word
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            # return false if each letter of the word (spot) is empty
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        # check and return if it's end of the word as well
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            # return false if current spot is empty
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple")) # return True
print(trie.search("app")) # return False
print(trie.startsWith("app")) # return True
trie.insert("app")
print(trie.search("app")) # return True