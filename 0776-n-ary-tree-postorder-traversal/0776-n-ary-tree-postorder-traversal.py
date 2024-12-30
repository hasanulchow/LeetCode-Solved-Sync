"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def helper(self, root: 'Node', res: List[int]) -> None:
        if root is None:
            return
        for child in root.children:
            self.helper(child, res)
        res.append(root.val)

    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self.helper(root, res)
        return res