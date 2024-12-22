from collections import defaultdict

class WordDictionary:

    def __init__(self):
        """ Initialize your data structure here. """
        # create a defaultdict of sets to store the words
        # keys are word lengths, values are sets of words of that length
        self.dic = defaultdict(set)

    def addWord(self, word: str) -> None:
        """ Adds a word into the data structure. """
        # add the word to the set of words with the same length
        self.dic[len(word)].add(word)

    def search(self, word: str) -> bool:
        """ Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. """
        # if the word doesn't contain dots, check if it exists in the set of words with the same length
        if '.' not in word:
            return word in self.dic[len(word)]
        # if the word contains dots, iterate over all words of the same length
        for v in self.dic[len(word)]:
            # check if each character in the word matches the corresponding character in the word being searched, except for the dots
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
        # if no matching word is found, return False
        return False