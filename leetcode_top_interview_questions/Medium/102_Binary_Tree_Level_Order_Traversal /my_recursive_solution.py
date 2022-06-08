# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        cur = root
        while stack:
            while cur.left:
                stack.append(cur.left)
                cur = cur.left
            
            node = stack.pop()
            res.append(node.val)
            
            if node.right:
                stack.append(node.right)
                cur = node.right
                
        return res
                