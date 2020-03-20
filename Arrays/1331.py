class Solution:
    """
    Time: 58% (384ms) O(n log n)
    """
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        index_map = {}
        rank = 1
        current = None
        for ele in sorted(arr):
            if ele != current and ele not in index_map:
                index_map[ele] = rank
                rank += 1

        result = []
        for ele in arr:
            result.append(index_map[ele])
        return result
