class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        array = [intervals[0]]
        for j in range(1, len(intervals)):
            if(array[-1][1] >= intervals[j][0]):
                array[-1][1] = max(array[-1][1], intervals[j][1])
            else:
                array.append(intervals[j])
        return array
