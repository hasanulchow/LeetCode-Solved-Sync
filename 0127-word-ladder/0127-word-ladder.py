class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
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

        while word_queue:
            level_size = len(word_queue)

            for _ in range(level_size):
                current_word = word_queue.popleft()

                # If the current word is the endWord, return the distance.
                if current_word == endWord:
                    return distance

                # Try changing each character in the current word.
                for i in range(len(current_word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == current_word[i]:
                            continue  # Skip same character

                        new_word = current_word[:i] + c + current_word[i+1:]

                        # If the new word is in the word set, add it to the queue.
                        if new_word in wordSet:
                            word_queue.append(new_word)
                            wordSet.remove(new_word)  # Remove to prevent revisiting

            # Increment distance after processing the current level.
            distance += 1

        # If no transformation sequence leads to the endWord, return 0.
        return 0