class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        res = []
        for i in range(len(arr) -1, -1, -1):
            res.append(arr[i])
        return ' '.join(res)
        