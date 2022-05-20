# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(res, node):
            if node.left:
                helper(res, node.left)
            res.append(node.val)
            if node.right:
                helper(res, node.right)
            return res
            
        res = helper([], root)
        return res[k-1]
        
        