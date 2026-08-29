# Time: O(N), Space: O(H) worst O(N)
# Pattern: DFS / Recursion Stack
# Idea: BFS view [1,2,None] - check structure + value
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False 
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
