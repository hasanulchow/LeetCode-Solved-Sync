class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        vowels = 'aeiouAEIOU'
        goat_latin_words = []

        for index, word in enumerate(words):
            if word[0] in vowels:
                goat_word = word + "ma"
            else:
                goat_word = word[1:] + word[0] + "ma"
            
            # Add 'a' based on the word index (1-indexed)
            goat_word += 'a' * (index + 1)
            goat_latin_words.append(goat_word)

        return ' '.join(goat_latin_words)



        