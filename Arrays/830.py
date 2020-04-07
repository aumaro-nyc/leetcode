class Solution:
    """
    Time: 8% (44ms)
    """
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        result = []
        i = 1
        prev = S[0]
        start = 0
        count = 1
        while i < len(S):
            if S[i] == prev:
                count += 1
                if i == len(S) - 1 and count > 2:
                    result.append([start,i])
                i += 1
            else:
                if count > 2:
                    result.append([start,i - 1])
                prev = S[i]
                start = i
                count = 1
                i += 1
        return result
