# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = [0]  
        
        def helper(node):
            if node is None:
                return None
            left = helper(node.left)
            if left is not None:
                return left
            
            ans[0] += 1
            if ans[0] == k:
                return node.val
            
            return helper(node.right)
        
        return helper(root)