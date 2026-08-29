# Approach: Recursion - depth = 1 + max(left_depth, right_depth)
# Time: O(n) - visit all nodes
# Space: O(h) - recursion stack = height
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
