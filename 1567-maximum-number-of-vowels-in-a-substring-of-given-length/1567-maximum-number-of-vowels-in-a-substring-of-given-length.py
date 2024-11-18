class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        left = 1
        right = k
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1

        ans = count

        while right < len(s):
            if s[left -1] in vowels:
                count -= 1
            
            if s[right] in vowels:
                count += 1

            ans = max(ans,count)

            left += 1
            right += 1

        return ans

        