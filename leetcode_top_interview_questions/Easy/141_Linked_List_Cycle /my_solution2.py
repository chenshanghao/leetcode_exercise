# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = {}
        pointer = head
        while(pointer):
            if pointer in hashmap:
                return True
            hashmap[pointer] = True
            pointer = pointer.next
        return False
        