# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return l1 or l2
        
        dummy = ListNode(-1)
        cur = dummy
        carry = 0
        while l1 or l2:
            val = carry
            if l1:
                val = val + l1.val
            if l2:
                val = val + l2.val
                
            if val <= 9:
                cur.next = ListNode(val)
                cur = cur.next
                carry = 0
            else:
                cur.next = ListNode(val - 10)
                cur = cur.next
                carry = 1
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry != 0:
            cur.next = ListNode(carry)
        
        return dummy.next