# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        root = ListNode()
        main = root

        while head and head.next:
            one = head
            two = head.next

            temp = two.next
            two.next = None

            root.next = two
            root = root.next

            one.next = None
            root.next = one
            root = root.next

            root.next = temp

            head = head.next

        return main.next
