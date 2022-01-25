class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoStack = []
        answer = [0] * len(temperatures)
        for i in range(0, len(temperatures)):
            while(monoStack != [] and monoStack[-1][1] < temperatures[i]):
                pop = monoStack.pop()
                answer[pop[0]] = i - pop[0]
            monoStack.append([i, temperatures[i]])
        return answer
