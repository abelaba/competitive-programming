# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def pairSum(self, head: Optional[ListNode]) -> int:

        # Find middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse list after middle
        middle = slow.next
        prev = None
        while middle:
            nex_t = middle.next
            middle.next = prev
            prev = middle
            if nex_t:
                middle = nex_t
            else:
                break

        # Find max twin sum
        maxTwinSum = 0

        while middle:
            twinSum = middle.val + head.val
            maxTwinSum = max(maxTwinSum, twinSum)
            middle = middle.next
            head = head.next
        return maxTwinSum
