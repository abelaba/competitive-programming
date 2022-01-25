# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []
        while head:
            array.append(head)
            head = head.next
        index = int(len(array) / 2)
        return array[index]
