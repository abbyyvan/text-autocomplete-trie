# implement Trie data structure here
# the Trie data structure is a tree-like data structure used for storing a dynamic set of strings
## 1. every node represents a char
## 2. every char is extended from the root node, till all chars are presented
## 3. every word ends with 'is_end_of_word' symbol
class TrieNode:
    def __init__(self) -> None:
        self.children = {} # Dicitionary to store child nodes
        self.is_end_of_word = False # Flag to mark the end of the word

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode() # Initialize the root node
    
    def insert(self, word) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode() # Add new node if character not found
            node = node.children[char] # Move to child node
        node.is_end_of_word = True # Mark the end of the word

    def search(self, word) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False # Word not found
            node = node.children[char] # Move to the child node
        return node.is_end_of_word # Return if it is the end of a word
   

    def starts_with(self, prefix) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False # Prefix not found
            node = node.children[char] # Move to the child node
        return True