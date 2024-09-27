class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=0
        c=0
        new=x
        for i in range(0,len(str(x))):
            c=x%10
            x//=10
            temp=temp*10+c
        if temp==new:
            return True
        else:
            return False