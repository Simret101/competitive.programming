# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left,right):
            if left is None and right is None:
                return True
            elif (left is None and right is not None) or(right is None and left is not None)  :
                return False
            
            elif right.val != left.val:
                return False
        
            return ((right.val == left.val) and helper(left.left,right.right) and helper(right.left,left.right))
        return helper(root.left,root.right)
        
        