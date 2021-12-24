class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        lowerBound = t - 3000
        upperBound = t
        self.queue.append(t)
        while not (lowerBound <= self.queue[0] <= upperBound):
            self.queue.pop(0)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
