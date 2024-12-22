from collections import defaultdict

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        We use a defaultdict where the keys are the lengths of the words,
        and the values are sets of words that have that particular length.
        """
        self.dic = defaultdict(set)  # Initialize a defaultdict of sets to store words by length

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        This function adds the given word to the set of words that have the same length.
        """
        self.dic[len(word)].add(word)  # Add the word to the set of words with the same length

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        We handle the case where the word has '.' by checking all possible matching words.
        """
        # If the word does not contain any dots, check if it exists in the set of words of the same length
        if '.' not in word:
            return word in self.dic[len(word)]  # Directly check if the word exists in the set

        # If the word contains dots, iterate over all words of the same length
        for v in self.dic[len(word)]:
            # Check if each character in the word matches the corresponding character in the word being searched
            # Except for the dots, which can match any character
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':  # If the character does not match and is not a dot, break
                    break
            else:
                # If we finished checking the word without breaking, it means the word matches
                return True
        
        # If no matching word is found, return False
        return False
