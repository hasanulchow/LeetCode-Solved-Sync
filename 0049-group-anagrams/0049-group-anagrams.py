from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a defaultdict with a default type of list to store grouped anagrams
        ans = defaultdict(list)

        # Iterate over each string in the input list
        for s in strs:
            # Sort the characters of the string to generate a key that represents its anagram group
            key = "".join(sorted(s))
            # Append the original string to the list corresponding to the sorted key
            ans[key].append(s)

        # Convert the defaultdict values to a list and return it
        return list(ans.values())
