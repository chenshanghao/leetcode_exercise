# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def helper(res, node):
            if not node:
                return
            helper(res, node.left)
            res.append(node)
            helper(res, node.right)
            return res
        res = helper([], root)
        if p in res and res.index(p) < len(res) - 1:
            return res[res.index(p) + 1]
        else:
            return None
            
        