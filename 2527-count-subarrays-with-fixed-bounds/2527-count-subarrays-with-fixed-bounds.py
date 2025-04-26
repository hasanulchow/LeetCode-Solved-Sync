class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans=0
        maxi, mini, s, l=-1, -1, len(nums), 0
        for r, x in enumerate(nums):
            if x<minK or x>maxK:
                l=r+1
                continue
            if x==maxK: maxi=r
            if x==minK: mini=r
            ans+=max((min(maxi, mini)-l+1),0)
        return ans
        