# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(preorder, inorder):
            if not preorder:
                return None
            root_val = preorder[0]
            node = TreeNode(root_val)
            
            idx = inorder.index(root_val)
            node.left = helper(preorder[1:idx+1], inorder[0: idx])
            node.right = helper(preorder[idx+1:], inorder[idx+1:])
            return node
        root = helper(preorder, inorder)
        return root
        
        
        

            
        