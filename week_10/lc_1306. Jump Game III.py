class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        queue = collections.deque([start])
        visited = set()

        while queue:
            popped = queue.popleft()
            if arr[popped] == 0:
                return True
            visited.add(popped)

            addition, subtraction = popped + arr[popped], popped - arr[popped]

            if 0 <= addition < len(arr) and addition not in visited:
                queue.append(addition)
            if 0 <= subtraction < len(arr) and subtraction not in visited:
                queue.append(subtraction)

        return False
