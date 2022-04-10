# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Time Complexity: O(m+n)
        # Space Complexity: O(m)
        hashmap = {}
        dummy = headA
        while(dummy):
            hashmap[dummy] = True
            dummy = dummy.next
        
        dummy = headB
        while(dummy):
            if dummy in hashmap:
                return dummy
            dummy = dummy.next
        return None