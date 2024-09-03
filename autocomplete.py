#implement autocomplete logic here
from trie import Trie

class AutoCompleteSystem:
    def __init__(self) -> None:
        self.trie = Trie() # Initialize the Trie

    def add_word(self, word) -> None:
        self.trie.insert(word) # Add a word to the Trie
    
    def get_suggestions(self, prefix):
        results = []  # List to store suggestions
        node = self.trie.root

        for char in prefix:
            if char not in node.children:
                return results
            node = node.children[char]
        
        self._dfs(node, prefix,'', results)
        return results

    def _dfs(self, node, prefix, path, results):
        if node.is_end_of_word:
            results.append(path)  # Add completed word to results
        for char, next_node in node.children.items():
            self._dfs(next_node, prefix, path + char, results)  # Continue DFS for each child
