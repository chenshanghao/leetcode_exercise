# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        list_node = [root]
        isEven = True
        while list_node:
            new_list_node = []
            row = []
            for node in list_node:
                row.append(node.val)
                if node.left:
                    new_list_node.append(node.left)
                if node.right:
                    new_list_node.append(node.right)
            if isEven:
                res.append(row)
            else:
                res.append(row[::-1])
            isEven = not isEven
            list_node = new_list_node
        return res
                
                
                

        