class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res = 0 # taking a counter. 
        while target > startValue: # checking if target value is greater then startValue. 
            res += 1 # as if target is greater implies we`ll be having atleast one operation. 
            if target%2==0:
                target //=2 # in case number is even. 
            else:
                target += 1 # in case number odd. 
        return res + startValue - target# startValue - target is for (target<=staetValue). 