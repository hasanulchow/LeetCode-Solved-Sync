# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        def generateADFS(node):
            if not node:
                return []
            a=generateADFS(node.left)
            a.append(node.val)
            a.extend(generateADFS(node.right))
            return a
        arr=generateADFS(root)
        arr.append(val)
        def generateBDFS(arr):
            if arr:
                m=max(arr)
                ind=arr.index(m)
                return TreeNode(m,generateBDFS(arr[:ind]),generateBDFS(arr[ind+1:]))
        return generateBDFS(arr)