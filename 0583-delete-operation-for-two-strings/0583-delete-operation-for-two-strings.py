class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def rec(i, j):
            # reached end of both words, nothing to compare or delete
            if i == len(word1) and j == len(word2):
                return 0
            # word1 ends, word2 doesn't. So, delete all remaining chars from word2
            if i == len(word1):
                return len(word2) - j

            # word2 ends, word1 doesn't. So, delete all remaining chars from word1
            if j == len(word2):
                return len(word1) - i
            
            # word1[i] and word2[j] matches, check from the next index of both words
            if word1[i] == word2[j]:
                res = rec(i + 1, j + 1)

            # word1[i] and word2[j] don't match, delete and move next
            else:
                res = 1 + min(     # 1 because of deleting
                    rec(i + 1, j), # delete word1[i], check from next index of word1   
                    rec(i, j + 1)  # delete word2[j], check from next index of word2
                )
            return res
        return rec(0, 0)