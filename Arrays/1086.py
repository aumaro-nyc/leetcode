import heapq
class Solution:
    """
    Time: 82% (72ms)
    """
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        score_map = {}
        result = []

        for score in items:
            if score[0] not in score_map:
                heap = []
                heapq.heappush(heap,-1 * score[1])
                score_map[score[0]] = heap
            else:
                heapq.heappush(score_map[score[0]], -1 * score[1])

        for key in sorted(score_map):
            total = 0
            for i in range(5):
                total += -1 * heapq.heappop(score_map[key])
            result.append([key,total // 5])
        return result

class Solution:
    """
    Solution without using heap is comparable (seems to do better on average with leetcode metrics)
    Time: 54% - 94% (80ms-68ms)
    """
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        result = []
        items = sorted(items, reverse=True)
        i = 0
        current_id = -1
        while i < len(items):
            while i < len(items) and current_id == items[i][0]:
                i += 1
            if i > len(items) - 5: break
            result.append([items[i][0], sum(x[1] for x in items[i:i+5]) // 5])
            current_id = items[i][0]
        return result[::-1]
