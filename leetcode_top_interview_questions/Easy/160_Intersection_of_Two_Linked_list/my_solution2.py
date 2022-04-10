# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time Complexity: O(m + n)
    # Space Complexity: O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def get_linked_list_length(head: ListNode):
            dummy = head
            length = 0
            while(dummy):
                length += 1
                dummy = dummy.next
            return length
        def get_common_length_head(headA: ListNode, length_a: int, headB: ListNode, length_b: int):
            dummy_a, dummy_b = headA, headB 
            if length_a < length_b:
                dummy_a, dummy_b = dummy_b, dummy_a
                length_a, length_b = length_b, length_a
            delta = length_a - length_b
            for i in range(delta):
                dummy_a = dummy_a.next
            return dummy_a, dummy_b
                
            
        length_a, length_b = get_linked_list_length(headA), get_linked_list_length(headB)
        dummy_a, dummy_b = get_common_length_head(headA, length_a, headB, length_b)
        while(dummy_a):
            if dummy_a == dummy_b:
                return dummy_a
            else:
                dummy_a = dummy_a.next
                dummy_b = dummy_b.next
        return None