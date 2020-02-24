class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return
        i,j = 0,1
        result = []
        while j < len(intervals):
            start, end = 0,1
            if intervals[i][end] >= intervals[j][start]:
                intervals[i][end] = intervals[j][end]
                j += 1
            else:
                result.append(intervals[i])
                i = j
                j += 1
        result.append(intervals[i])
        return result
