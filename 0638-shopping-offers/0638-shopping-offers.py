class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        dp = {}
        def dfs(needs):
            if sum(needs)==0: return 0
            key = tuple(needs)
            if key in dp: return dp[key]

            best = self.buyOut(needs,price)
            for offer in special:
                new_needs = self.canTake(offer,needs[:])
                
                if new_needs: best = min(best,offer[-1] + dfs(new_needs))
            
            dp[key] = best
            return best

        return dfs(needs)

    def buyOut(self,needs,prices):
        return sum([n*p for n,p in zip(needs,prices)])

    def canTake(self,offer,needs):
        for i in range(len(needs)):
            needs[i] -= offer[i]
            if needs[i] < 0: return []
        return needs
            