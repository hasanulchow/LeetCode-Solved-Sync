class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if not A:
            return False
        p1=0
        p2=len(A)-1
        peak=max(A)
        peakAt=A.index(peak) #index complexity O(n)
        
        if peakAt==p2 or peakAt==p1: #peak cant be first or last
            return False
        
        while p1<peakAt: #making sure going up is OK
            if A[p1] >=A[p1+1]:
                return False
            p1+=1 
            
        while p2>peakAt: #making sure going down is OK
            if A[p2]>=A[p2-1]:
                return False
            p2-=1   
            
        return True    

            