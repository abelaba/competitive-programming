class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        rQueue = collections.deque()
        dQueue = collections.deque()

        length = len(senate)

        for i in range(0, length):
            if senate[i] == 'R':
                rQueue.append(i)
            else:
                dQueue.append(i)

        while rQueue and dQueue:
            r = rQueue.popleft()
            d = dQueue.popleft()

            if r < d:
                rQueue.append(r + length)
            else:
                dQueue.append(d + length)

        if rQueue:
            return 'Radiant'
        return 'Dire'
