class Trie:

    def __init__(self):
        # Initialize the root node as an empty dictionary
        self.root = {}
        

    def insert(self, word: str) -> None:
        # Start at the root of the Trie
        node = self.root
        # Iterate through each character in the word
        for char in word:
            # If the character is not in the current node, add it
            if char not in node:
                node[char] = {}
            # Move to the next node
            node = node[char]
        # Mark the end of the word by setting a special key (e.g., None or a boolean)
        node[None] = True  # True indicates that this node marks the end of a word

    def search(self, word: str) -> bool:
        # Start at the root of the Trie
        node = self.root
        # Iterate through each character in the word
        for char in word:
            # If the character is not in the current node, the word doesn't exist
            if char not in node:
                return False
            # Move to the next node
            node = node[char]
        # Check if this node marks the end of a word
        return None in node

    def startsWith(self, prefix: str) -> bool:
        # Start at the root of the Trie
        node = self.root
        # Iterate through each character in the prefix
        for char in prefix:
            # If the character is not in the current node, the prefix doesn't exist
            if char not in node:
                return False
            # Move to the next node
            node = node[char]
        # If we successfully iterate through the entire prefix, it exists
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)