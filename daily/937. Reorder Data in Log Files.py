class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        answer = []
        
        digitLogs = []
        letterLogs = []
        
        for i in range(len(logs)):
            log = logs[i].split(" ")
            if log[1].isdigit():
                digitLogs.append(logs[i])
            else:
                letterLogs.append(logs[i].split(' ', 1))
        
        letterLogs.sort(key=lambda x: (x[1], x[0]))
        
        letterLogs = [' '.join(letterLogs[i]) for i in range(len(letterLogs))]
        
        return letterLogs + digitLogs
        
        
        
        
        
