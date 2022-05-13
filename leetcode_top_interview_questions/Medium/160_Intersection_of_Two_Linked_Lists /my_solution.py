# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getListLength(head):
            res = 0
            cur = head
            while cur:
                res += 1
                cur = cur.next
            return res
        lenA, lenB = getListLength(headA), getListLength(headB)
        curA, curB = headA, headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                curA = curA.next
        
        if lenB > lenA:
            for i in range(lenB-lenA):
                curB = curB.next
        
        while curA:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None
        