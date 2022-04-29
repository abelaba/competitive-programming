class MyLinkedList:

    def __init__(self, val=None, nex_t=None):
        self.val = val
        self.next = nex_t
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index > self.length - 1:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.head = MyLinkedList(val, self.head)
        self.length += 1

    def addAtTail(self, val: int) -> None:
        temp = self.head
        if not self.head:
            self.head = MyLinkedList(val)
            self.length += 1
            return

        while self.head.next:
            self.head = self.head.next
        self.head.next = MyLinkedList(val)
        self.length += 1

        self.head = temp

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return

        if index == 0:
            self.head = MyLinkedList(val, self.head)
            self.length += 1
            return

        temp = self.head

        for i in range(index - 1):
            self.head = self.head.next

        self.head.next = MyLinkedList(val, self.head.next)
        self.length += 1

        self.head = temp

    def deleteAtIndex(self, index: int) -> None:
        if index > self.length - 1:
            return

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        temp = self.head
        for i in range(index - 1):
            self.head = self.head.next

        self.head.next = self.head.next.next
        self.length -= 1

        self.head = temp


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
