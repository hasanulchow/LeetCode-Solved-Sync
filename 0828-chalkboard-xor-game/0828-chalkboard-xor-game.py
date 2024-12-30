class Solution:
    def xorGame(self, nums):
        #create a variable 0 
        x = 0 
        #iterate over the elements in the nums
        for i in nums:
            #do xor of all the elements
            x ^= i 
        #Alice wins in two situations :
        #1.if the xor is already 0 (x == 0 )
        #2.if the length of nums is even because if alice got chance with even length and xor != 0 he will select a number so that he will leave the odd number of same integer 
        #if nums == [a,a,a,b] then alice erase b so bob must erase from [a,a,a] so he will lose if he erase any number 
        return x == 0 or len(nums)%2 == 0 
        #in other situations bob will win