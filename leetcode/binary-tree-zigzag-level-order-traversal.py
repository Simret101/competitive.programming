# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        ans = []

        def helper(node, i):
            nonlocal ans 
            if node :
                if len(ans) <= i:
                    ans.append([node.val])
                

                else:
                    
                    ans[i].append(node.val)

                i+=1
                helper(node.left, i )
            
                helper(node.right, i)
            return ans
        val=helper(root, 0)
        for i in range(len(val)):
            if i%2==1:
                val[i].reverse()

        return val

        
      