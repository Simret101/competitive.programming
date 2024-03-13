# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q = deque()
        ans = []
        if root is None:
            return 0
        if root:
            q.append(root)
            while len(q) != 0:
                node = q.popleft()
                if node.val >= low and node.val <= high:
                    ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return sum(ans)
