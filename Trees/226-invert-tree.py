# Time: O(n) - visit each node once
# Space: O(h) - h = height of tree O(log n) balanced, O(n) worst skewed

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
            
        root.left,root.right = root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
