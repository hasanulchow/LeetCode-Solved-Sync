# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        sol = []
        temp = []

        def dfs(curr):

            if not curr:
                return
            temp.append(curr.val)

            if not curr.right and not curr.left and sum(temp) == targetSum:
                sol.append(temp.copy())
            else:
                dfs(curr.left)
                dfs(curr.right)
            temp.pop()
            
        dfs(root)
        return sol       
        