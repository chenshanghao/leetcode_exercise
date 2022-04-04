# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time complexity: O(n)
        # Space complexity: O(1)
        dummy = None
        cur = head
        while(cur):
            next = cur.next
            cur.next = dummy
            dummy = cur
            cur = next
        return dummy