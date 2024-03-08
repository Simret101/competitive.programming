# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def helper(nodes):
            if not nodes:
                return None

            mid = len(nodes) // 2
            root = TreeNode(nodes[mid])
            root.left = helper(nodes[:mid])
            root.right = helper(nodes[mid + 1:])
            return root

        def inorder_traversal(node, values):
            if node:
                inorder_traversal(node.left, values)
                values.append(node.val)
                inorder_traversal(node.right, values)

        values = []
        inorder_traversal(root, values)
        return helper(values)
    
