#Time Complexity: O(n) - number of nodes.
#Space Complexity: O(h) - recursion stack height, O(log n) for balanced tree and O(n) for skewed tree. In worst case O(n).
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(p,q):
            if not p and not q: 
                return True
            if not p or not q or p.val != q.val:
                return False
            return check(p.left,q.right) and check(q.left,p.right)
        
        
        return check(root.right,root.left)
