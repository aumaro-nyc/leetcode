import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        min_heap = []
        min_time = 0
        for stick in sticks:
            heapq.heappush(min_heap, stick)
             
        while len(min_heap) > 1:
            s1 = heapq.heappop(min_heap)
            s2 = heapq.heappop(min_heap)
            new_s = s1 + s2
            min_time += new_s
            heapq.heappush(min_heap, new_s)

        return min_time
