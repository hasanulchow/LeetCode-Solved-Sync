class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            num=x
        else:
            num=-x
        result=0
        while num>0:
            ld=num%10
            result=(result*10)+ld
            num=num//10
        if x>0:
            if result>(2**31)+1:
                return 0
            return result
        else:
            if -result<(-2)**31:
                return 0
            return -result