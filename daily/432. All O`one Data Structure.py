class AllOne:

    def __init__(self):
        self.stringCount = defaultdict(set)
        self.keys = defaultdict(int)
        self.maximum = 0
    
    def inc(self, key: str) -> None:
        
        self.keys[key] += 1
        self.stringCount[self.keys[key]].add(key)
        self.maximum = max(self.maximum, self.keys[key])
    
    def dec(self, key: str) -> None:
        
        self.stringCount[self.keys[key]].remove(key)
        
        if len(self.stringCount[self.maximum]) == 0:
            self.maximum -= 1
        
        self.keys[key] -= 1
        
        if self.keys[key] == 0:
            del self.keys[key]

    def getMaxKey(self) -> str:
        
        if self.keys:        
            for value in self.stringCount[self.maximum]:
                return value
        
        return ""

    def getMinKey(self) -> str:
                
        maxKey = ""
        count = sys.maxsize
        
        for key in self.keys:
            if self.keys[key] < count:
                maxKey = key
                count = self.keys[key]
            
        return maxKey



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
