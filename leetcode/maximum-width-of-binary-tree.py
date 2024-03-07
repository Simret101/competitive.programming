# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
         
            level=[(root,0)]
            res=0
            while level:
                res=max(res,level[-1][1]-level[0][1]+1)
                next=[]
                for node,pos in level:
                    if node.left:
                        next.append((node.left,pos*2))
                    if node.right:
                        next.append((node.right,pos*2+1))
                level=next[:]
            return res
                