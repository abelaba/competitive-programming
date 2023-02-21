# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cache = set()
        pointer = headA
        while pointer:
            cache.add(pointer)
            pointer = pointer.next
        
        pointer = headB
        while pointer:
            if pointer in cache:
                return pointer
            pointer = pointer.next
