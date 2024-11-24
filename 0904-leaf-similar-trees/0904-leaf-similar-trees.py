class Solution:
    def leafSimilar(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        return (f:=lambda n:f(n.left)+f(n.right) or [n.val] if n else [])(r1)==f(r2)