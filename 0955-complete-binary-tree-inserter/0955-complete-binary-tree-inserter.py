import collections
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.parents = collections.deque() # maintain parents candidates
        if self.root:
            self.init_parents()

    def init_parents(self):
        q = collections.deque([self.root])
        start_append_parents = False
        while q:
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            if not (cur.left and cur.right) or start_append_parents: # 1. cur doesn't have two children OR 2. start_append_parents = True
                self.parents.append(cur)
                start_append_parents = True

    def insert(self, val: int) -> int:
        if val is None:
            return -1
        new_node = TreeNode(val)
        ret_val = -1
        if len(self.parents) > 0:
            cur = self.parents[0]
            if cur.left:
                cur.right = new_node
                self.parents.popleft() # cur node is no longer a parent candidate
            else:
                cur.left = new_node
            ret_val = cur.val
        self.parents.append(new_node)
        return ret_val

    def get_root(self) -> Optional[TreeNode]:
        return self.root