"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        cur_level = [root]
        while cur_level:
            next_level = []
            for i in range(len(cur_level)):
                if i < len(cur_level) - 1:
                    cur_level[i].next = cur_level[i+1]
                if cur_level[i].left:
                    next_level.append(cur_level[i].left)
                    next_level.append(cur_level[i].right)
            cur_level = next_level
        return root