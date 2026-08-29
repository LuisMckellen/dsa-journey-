#Time: O(n) visit each of n nodes once.
#Space: O(h) recursion stack height, O(log n) balanced, O(n) skewed.
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(node,low,high):
            if not node:
                return True 
            if not (low<node.val<high):
                return False 
            return bst(node.left,low,node.val) and bst(node.right,node.val,high)
        return bst(root,float('-inf'),float('inf'))
        
        
