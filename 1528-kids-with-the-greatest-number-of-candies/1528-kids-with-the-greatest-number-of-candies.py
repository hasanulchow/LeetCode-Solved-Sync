class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy=max(candies)
        ans=[]

        for i in range(len(candies)):
            ans.append(candies[i] + extraCandies >= maxCandy)
        
        return ans