class Solution:
    def isNumber(self, s: str) -> bool:
        dfa = {
            1: {'sign':7, 'dig':2, 'dot':3},
            2: {'dig':2, 'exp':5, 'dot':4},
            3: {'dig':4},
            4: {'dig':4, 'exp':5},
            5: {'sign':5, 'dig':6},
            6: {'dig':6},
            7: {'dig':2, 'dot':3}
        }
        state = 1
        for i, char in enumerate(s):
            if char == "+" or char == '-':
                act = "sign"
            elif char.isdigit():
                act = "dig"
            elif char == '.':
                act = "dot"
            elif char == "e" or char == "E":
                act = "exp"
            else:
                return False
            if act not in dfa[state]:
                return False
            state = dfa[state][act]
        if state in [2,4,6]:
            return True
        return False