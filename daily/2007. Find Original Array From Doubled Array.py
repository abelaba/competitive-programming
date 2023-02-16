class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort() # => nlogn 
        
        count = Counter(changed)
        if count[0] % 2 != 0: return []
        answer = []
        for c in changed:
            if count[c] == 0:
                answer.append(c // 2)
                continue
            if count[2*c] == 0:
                return []
            
            count[c] -= 1
            count[2*c] -= 1
        return answer
            
        
