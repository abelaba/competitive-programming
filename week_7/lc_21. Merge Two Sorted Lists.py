# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        curr = head

        if not list1:
            return list2
        elif not list2:
            return list1

        while list1 or list2:
            if not list1:
                head.val = list2.val
                head.next = list2.next
                break
            elif not list2:
                head.val = list1.val
                head.next = list1.next
                break

            if list1.val <= list2.val:
                head.val = list1.val
                list1 = list1.next
            else:
                head.val = list2.val
                list2 = list2.next

            head.next = ListNode()
            head = head.next
        return curr
