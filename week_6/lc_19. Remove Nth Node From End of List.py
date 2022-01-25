# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        curr = head

        while curr:
            count += 1
            curr = curr.next
        index = count - n
        curr = head
        if index == 1:
            curr = head.next
            return curr

        for i in range(1, index - 1):
            head = head.next
        head.next = head.next.next

        return curr
