# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(head):
            if not head or not head.next:
                return head
            tmp = ListNode(-1)
            tmp.next = head.next
            head.next = tmp.next.next
            tmp.next.next = head
            next_head = tmp.next.next.next
            tmp.next.next.next = helper(next_head)
            return tmp.next
        return helper(head)
            