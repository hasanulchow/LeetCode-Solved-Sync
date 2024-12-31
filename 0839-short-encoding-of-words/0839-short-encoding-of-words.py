class TriNode:
    def __init__(self, val):
        self.val = val
        self.children = [0]*26

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = TriNode("")
        result = [0]
        
        def insertInTrie(word):
            curr = root
            for letter in word[::-1]:
                index = ord(letter)%97
                if curr.children[index] == 0:
                    curr.children[index] = TriNode(letter)
                curr= curr.children[index]
            
        def traverseTrie(root,choosen):
            flag = 0
            for node in root.children:
                if node != 0:
                    traverseTrie(node,choosen+node.val)
                    flag=1
            if flag == 0:
                result[0]+=len(choosen)+1
        
        for word in words:
            insertInTrie(word)
        
        traverseTrie(root,"")
        
        return result[0]