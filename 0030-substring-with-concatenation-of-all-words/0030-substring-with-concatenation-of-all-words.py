from collections import defaultdict
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Finds starting indices of all substrings in `s` that are concatenations of every word in `words` exactly once.
        
        Args:
        s (str): The input string.
        words (List[str]): List of words to concatenate.
        
        Returns:
        List[int]: Starting indices of substrings in `s` matching the criteria.
        """
        if not s or not words:
            return []

        # Count occurrences of each word in `words`
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1

        # Calculate the total length of the concatenated substring
        word_len = len(words[0])  # All words are assumed to be the same length
        substr_len = len(words) * word_len
        result = []

        # Iterate through the string to find valid substrings
        for i in range(len(s) - substr_len + 1):
            seen = defaultdict(int)
            for j in range(i, i + substr_len, word_len):
                word = s[j:j + word_len]  # Extract a word-sized substring
                if word in word_count:
                    seen[word] += 1
                    # Break if a word appears more times than allowed
                    if seen[word] > word_count[word]:
                        break
                else:
                    break
            else:
                # If all words match correctly, add starting index to result
                result.append(i)

        return result
