# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            while lists[i]:
                heap.append(lists[i].val)
                lists[i] = lists[i].next

        if not heap:
            return
        heapq.heapify(heap)

        sorted_list = ListNode(heapq.heappop(heap))
        temp = sorted_list
        while heap:
            temp.next = ListNode(heapq.heappop(heap))
            temp = temp.next

        return sorted_list
