# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        m = defaultdict(list)
        queue = deque()

        min_col = inf
        max_col = -inf

        if root:
            queue.append((root,0))
        
        while queue:
            level_m = defaultdict(list)
            for _ in range(len(queue)):
                node,col = queue.popleft()
                level_m[col].append(node.val)

                min_col = min(min_col,col)
                max_col = max(max_col,col)

                if node.left:
                    queue.append((node.left,col-1))
                if node.right:
                    queue.append((node.right,col+1))
            
            for key,value in level_m.items():
                m[key] += sorted(value)

        output = []
        for i in range(min_col,max_col+1):
            output.append(m[i])
        
        return output

        

        