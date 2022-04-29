# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        curr = head
        stack = []

        dictionary = {}
        i = 0
        while head:
            while(stack and stack[-1][1] < head.val):
                popped = stack.pop()
                dictionary[popped] = head.val

            stack.append((i, head.val))
            dictionary[(i, head.val)] = 0

            head = head.next
            i += 1

        return dictionary.values()
