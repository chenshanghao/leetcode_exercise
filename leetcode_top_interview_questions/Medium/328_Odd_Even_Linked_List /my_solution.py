# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(-1)
        new_list_cur = dummy
        cur = head
        prev = None
        odd = True
        while cur:
            if odd:
                prev = cur
                cur = cur.next
                odd = False
            else:
                new_list_cur.next = cur
                cur = cur.next
                new_list_cur = new_list_cur.next
                new_list_cur.next = None
                prev.next = cur
                odd = True
        prev.next = dummy.next
        return head