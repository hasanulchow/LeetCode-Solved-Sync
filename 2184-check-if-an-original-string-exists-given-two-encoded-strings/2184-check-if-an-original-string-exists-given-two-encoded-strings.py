class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        # approach
        
        # split the string into a list of chars and numbers
        def split(string):
            res = []
            num = []
            for c in string:
                if c.isalpha():
                    if num:
                        res.append(num)
                        num=[]
                    res.append(c)
                else:
                    num.append(c)
            if num:
                res.append(num)

            return res

        @lru_cache(maxsize=None)
        def possibilites(n):
            # returns combos of results of numbers
            # use dp to make the combos
            nums = {int(n)}

            for i in range(1,len(n)):
                for x in possibilites(n[:i]):
                    for y in possibilites(n[i:]):
                        nums.add(x+y)

            return nums

        l1 = split(s1)
        l2 = split(s2)

        @lru_cache(maxsize=None)
        def dfs(i,j, diff):
            if i == len(l1) and j == len(l2):
                if diff == 0:
                    return True
                return False

            if i < len(l1) and type(l1[i]) == list:
                # we must try all possiblities
                n = "".join(l1[i])
                pos = possibilites(n)
                for p in pos:
                    if dfs(i+1, j, diff+p):
                        return True
                return False

            if j< len(l2) and type(l2[j]) == list:
                # we must try all possibilites
                n = "".join(l2[j])
                pos = possibilites(n)
                for p in pos:
                    if dfs(i, j+1, diff-p):
                        return True
                return False

            if i == len(l1) and j < len(l2):
                return dfs(i, j+1, diff-1)
            if j == len(l2) and i < len(l1): 
                return dfs(i+1,j, diff+1)

            if diff == 0:
                if l1[i] != l2[j]:
                    return False
                return dfs(i+1, j+1, diff)
            if diff <0:
                return dfs(i+1, j,  diff+1)
            if diff >0:
                return dfs(i,j+1, diff-1)
       

        return dfs(0,0,0)