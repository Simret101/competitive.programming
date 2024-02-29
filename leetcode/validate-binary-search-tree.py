# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       
        def isBST(node):
            if node is None:
                return [True,float(inf),float(-inf)]
            
            l_BST,l_min,l_max=isBST(node.left)
            r_BST,r_min,r_max=isBST(node.right)
            is_BST=False
            if l_BST and r_BST and l_max<node.val and r_min>node.val:
                is_BST=True
            return [is_BST,min(r_min,node.val,l_min),max(l_max,node.val,r_max) ]
            
        return isBST(root)[0]

        
        
        