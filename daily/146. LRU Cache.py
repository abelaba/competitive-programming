class Node:
    def __init__(self, next_=None, previous=None, value=None, key=None):
        self.key = key
        self.next = next_
        self.previous = previous
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.previous = self.head
        
        
    def removeNode(self, key):
        
        
        node = self.cache[key]
                
        previousNode = node.previous
        nextNode = node.next
        
        previousNode.next = nextNode
        nextNode.previous = previousNode
        
        value = self.cache[key].value
        
        del self.cache[key]
        
        return value
    
    def addToTail(self, key, value):
        
                
        self.cache[key] = Node()
        self.cache[key].value = value
        self.cache[key].key = key
        
        beforeLastNode = self.tail.previous
                
        beforeLastNode.next = self.cache[key]
        
        self.cache[key].previous = beforeLastNode
        self.cache[key].next = self.tail
        
        
        
        self.tail.previous = self.cache[key]
        
      
        
        

    def get(self, key: int) -> int:
        
        
        if key not in self.cache:
            return -1
        
        value = self.removeNode(key)
        self.addToTail(key, value)
        
        return self.cache[key].value
        
        
        
        

    def put(self, key: int, value: int) -> None:
        
        
        if key in self.cache:
            
            self.removeNode(key)
            self.capacity += 1
        
        elif self.capacity == 0:
            
            self.removeNode(self.head.next.key)
            self.capacity += 1
        
        self.addToTail(key, value)
        self.capacity -= 1
        
        
            
        
            
            
            
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
