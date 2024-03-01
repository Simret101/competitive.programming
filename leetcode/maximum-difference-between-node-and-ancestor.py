# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans=0
        def helper(node,minmum,maximum):
            nonlocal ans
            if not node:
                return None
            ans=max(ans,abs(node.val-minmum),abs(node.val-maximum))
            minmum=min(node.val,minmum)
            maximum=max(node.val,maximum)

            helper(node.left,minmum,maximum)
            helper(node.right,minmum,maximum)
        helper(root,root.val,root.val)
        return ans

            
            
           