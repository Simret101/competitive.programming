from queue import Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def helper(node,cur):
          
            if node is None:
                return 0
            cur=cur*10+node.val
            if node.left is None and node.right is None:
                return cur
           
            left_num=helper(node.left,cur)
        
            right_num=helper(node.right,cur)
            return left_num + right_num
        return helper(root,0)

