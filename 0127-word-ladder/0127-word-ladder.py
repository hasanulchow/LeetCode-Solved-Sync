class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Find the length of the shortest transformation sequence from beginWord to endWord.
        Each transformation must change exactly one letter at a time, and each intermediate word
        must be in the word list.
        
        :param beginWord: str - The starting word in the transformation sequence.
        :param endWord: str - The target word that we need to transform into.
        :param wordList: List[str] - The list of valid words to use in the transformation.
        :return: int - The length of the shortest transformation sequence, or 0 if no transformation is possible.
        """
        # Create a set of all words in the word list for quick lookup.
        wordSet = set(wordList)

        # If endWord is not in the word set, no valid transformation exists.
        if endWord not in wordSet:
            return 0

        # Use a queue to perform BFS (Breadth-First Search).
        word_queue = deque()
        word_queue.append(beginWord)

        # Distance from the beginWord (initially 1 since beginWord is counted).
        distance = 1

        # Perform BFS
        while word_queue:
            # Get the number of words at the current level (each word represents one mutation step)
            level_size = len(word_queue)

            for _ in range(level_size):
                current_word = word_queue.popleft()  # Get the current word to process

                # If the current word is the endWord, return the current distance (length of transformation path).
                if current_word == endWord:
                    return distance

                # Try changing each character in the current word.
                for i in range(len(current_word)):  # Iterate over each character in the word
                    # Try replacing the current character with every letter in the alphabet
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == current_word[i]:
                            continue  # Skip if the new character is the same as the old one

                        # Form the new word by changing the character
                        new_word = current_word[:i] + c + current_word[i+1:]

                        # If the new word is in the word set, add it to the queue for further exploration.
                        if new_word in wordSet:
                            word_queue.append(new_word)  # Add the mutated word to the queue
                            wordSet.remove(new_word)  # Remove the word from the set to avoid revisiting

            # Increment distance after processing the current level.
            distance += 1

        # If no transformation sequence leads to the endWord, return 0.
        return 0
