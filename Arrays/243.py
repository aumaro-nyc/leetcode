class Solution:
    """
    Time: 91% (60ms)
    """
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        index_map = {}
        for i in range(len(words)):
            if words[i] not in index_map:
                index_map[words[i]] = [i]
            else:
                index_map[words[i]].append(i)

        min_distance = float('inf')
        for indx1 in index_map[word1]:
            for indx2 in index_map[word2]:
                if abs(indx1 - indx2) < min_distance:
                    min_distance = abs(indx1 - indx2)
        return min_distance
