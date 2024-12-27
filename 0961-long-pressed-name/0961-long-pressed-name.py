class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        if len(name) > len(typed):
            return False

        tracker = ""
        index = 0
        output = True
        
        while output and index < len(name):
            if len(name) > len(typed):
                return False
            if name[index] == typed[index]:
                tracker = name[index]
                index += 1
            elif (name[index] != typed[index]) and (typed[index] == tracker):
                    typed = typed[0: index] + typed[index + 1: ]
            else:
                output = False
        
        typed_end = set(typed[len(name): ])
        if len(typed_end) != 0:
            if set(name[-1]) != typed_end:
                output = False
                
        return output