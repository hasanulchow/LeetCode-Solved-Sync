class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        countBitsNum2 = 0
        temp2 = num2
        while temp2 > 0:
            if temp2 % 2 != 0:
                countBitsNum2 += 1
            temp2 >>= 1
        
        result = 0
        for i in range(31, -1, -1):
            if num1 & (1 << i) and countBitsNum2 > 0:
                result |= (1 << i)
                countBitsNum2 -= 1

        for i in range(32):
            if countBitsNum2 > 0 and not (result & (1 << i)):
                result |= (1 << i)
                countBitsNum2 -= 1
        
        return result