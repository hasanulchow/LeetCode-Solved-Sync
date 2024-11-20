class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        Set1, Set2 = set(nums1), set(nums2)
        ans = [[], []]

        for i in Set1:
            if i not in Set2:
                ans[0].append(i)
        for i in Set2:
            if i not in Set1:
                ans[1].append(i)

        return ans
        


        
        