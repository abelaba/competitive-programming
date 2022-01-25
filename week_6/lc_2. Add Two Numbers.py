# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        current = head

        while l1 or l2 or carry:
            l1_val = 0
            l2_val = 0
            if l1:
                l1_val = l1.val
            if l2:
                l2_val = l2.val

            su_m = l1_val + l2_val

            if su_m + carry > 9:
                su_m = su_m % 10 + carry
                su_m = su_m % 10
                carry = 1
            else:
                su_m = su_m + carry
                carry = 0
            current.next = ListNode(su_m)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next
