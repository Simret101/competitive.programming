from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dict=defaultdict()
        def  helper(node):
            if not node:
                return
            if node.val in dict:
                dict[node.val]+=1
            else:
                dict[node.val]=1
        
            helper(node.left)
            helper(node.right)
        helper(root)
        res=[]
        max_val=max(dict.values())
        for i in dict:
            if dict[i]==max_val:
                res.append(i)
    

        return res
