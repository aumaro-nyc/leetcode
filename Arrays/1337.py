class Solution:
    """
    Time: 74% (112ms)
    """
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldier_map = {}
        result = []
        for i in range(len(mat)):
            soldier_map[i] = sum(mat[i])
        for key in sorted(soldier_map.items(), key=lambda item: item[1])[:k]:
            result.append(key[0])
        return result
