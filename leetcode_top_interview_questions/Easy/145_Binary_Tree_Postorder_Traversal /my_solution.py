# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(res, root):
            if root:
                helper(res, root.left)
                helper(res, root.right)
                res.append(root.val)
        res = []
        helper(res, root)
        return res