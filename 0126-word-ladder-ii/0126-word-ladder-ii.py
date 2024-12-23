from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)  # Convert the given wordList to a set for optimized lookup
        result = []  # List to store the final result (all transformation sequences)
        layer = set()  # Set to store the current layer of words during BFS
        layer.add(beginWord)  # Start BFS from the beginWord
        parent = defaultdict(set)  # A dictionary to store the parent of each word
        
        # Perform BFS
        while layer:
            new_layer = set()  # Set to store the next layer of words
            for word in layer:
                for i in range(len(beginWord)):  # Try changing each character in the word
                    for c in "abcdefghijklmnopqrstuvwxyz":  # Try replacing each character with 'a' to 'z'
                        new = word[:i] + c + word[i + 1:]
                        if new in wordList and new != word:  # If the transformed word is valid
                            parent[new].add(word)  # Add the current word as a parent of the new word
                            new_layer.add(new)  # Add the new word to the next layer
            wordList -= new_layer  # Remove the words in the new layer from the wordList
            layer = new_layer  # Move to the next layer
            
            # If we found the endWord, stop BFS to avoid unnecessary processing
            if endWord in parent:
                break
        
        # Function to recursively build paths using the parent map
        def build_path(last, lst):
            if last == beginWord:  # If we reached the beginWord, add the path to result
                result.append(list(reversed(lst)))  # Reverse the path as it was built bottom-up
                return
            for word in parent[last]:  # Recursively build the path for each parent word
                build_path(word, lst + [word])
        
        # Build all the paths from endWord to beginWord
        build_path(endWord, [endWord])
        return result  # Return the list of all transformation sequences
