# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        root = ListNode(0)

        pre = root

        array = defaultdict(lambda: 0)

        while head:
            array[head.val] += 1
            head = head.next

        for i in array:
            if array[i] == 1:
                root.next = ListNode(i)
                root = root.next
        return pre.next
