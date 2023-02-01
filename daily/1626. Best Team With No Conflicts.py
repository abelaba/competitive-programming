

class Solution:
    
    
    def findTotalScore(self, memo, playerInfo, index, age, score):
        
        state = (index, score)
        
        if state in memo:
            return memo[state]
        
        if index == len(playerInfo):
            return 0
        
        indexAge, indexScore = playerInfo[index]
        
        answer = 0
        
        if score <= indexScore:
            value = indexScore + self.findTotalScore(memo, playerInfo, index+1, indexAge, indexScore)
            value2 = self.findTotalScore(memo, playerInfo, index+1, age, score)
            
            answer = max(value2, value)
        
        else:
            value = self.findTotalScore(memo, playerInfo, index+1, age, score)
            answer = value
        
        memo[state] = answer
        
        return answer
        
        
    
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        N = len(scores)
        
        playerInfo = [[ages[i], scores[i]] for i in range(N)]
        playerInfo.sort()
        memo = {}
        
        return self.findTotalScore(memo, playerInfo, 0, 0, 0)
        
        
        
        
