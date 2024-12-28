
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        count=0
        prevNum=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            currNum=nums[i]
            while currNum>prevNum:
                largestDivisor=self.getLargestDivisor(currNum)
                if largestDivisor==-1:
                    return -1
                currNum=currNum//largestDivisor
                
                count+=1
            prevNum=currNum
            
        return count
        
    def getLargestDivisor(self,num):
        n=int(math.sqrt(num))
        ans=-1
        for i in range(n,1,-1):
            if num%i==0:
                ans=max(ans,i,num//i)
        
        return ans
        
        
            
            