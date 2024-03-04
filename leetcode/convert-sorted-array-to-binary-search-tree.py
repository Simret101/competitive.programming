# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(l,r):
           
            if l==r:
                return TreeNode(nums[l])
            if l>r:
                return
            mid=(l+r)//2
            root=TreeNode(nums[mid])
            left_val=helper(l,mid-1)
            right_val=helper(mid+1,r)
            root.left=left_val
            root.right=right_val
            return root
        return helper(0,len(nums)-1)