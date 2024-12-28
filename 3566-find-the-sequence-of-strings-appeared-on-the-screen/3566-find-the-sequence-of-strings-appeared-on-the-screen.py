class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = ["a"]
        while res[-1] != target:
            last = res[-1]
            if last[len(last) - 1] != target[len(last) - 1]: last = last[:-1] + chr(ord(last[-1]) + 1)
            else: last += "a"
            res.append(last)
        return res