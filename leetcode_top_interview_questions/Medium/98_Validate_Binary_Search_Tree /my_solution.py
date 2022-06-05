# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, min_val, max_val):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            return helper(node.left, min_val, min(max_val, node.val)) and helper(node.right, max(node.val, min_val), max_val)
        
        return helper(root, float('-inf'), float('inf'))