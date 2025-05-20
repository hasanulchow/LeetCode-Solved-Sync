class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#step:1
        group_anagram = {}
        for word in strs:
            count = [0]*26

            for char in word:
                count[ord(char)-ord('a')] +=1

            key = tuple(count)
            if key in group_anagram:
                group_anagram[key].append(word)

            else:
                group_anagram[key] = [word]

        return list(group_anagram.values())