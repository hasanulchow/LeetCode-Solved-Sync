class Solution:
    def convertToBase7(self, num: int) -> str:
        s=""
        if num>0:
            while num!=0:
                n=num//7
                a=num%7
                s+=str(a)
                num=n
            return s[::-1]
        elif num==0:
            return '0'
        else:
            num=num*-1
            while num!=0:
                n=num//7
                a=num%7
                s+=str(a)
                num=n
            
            return '-'+s[::-1]