class Solution:
    """
    Given an array A of strings made only from lowercase letters,
    return a list of all characters that show up in all strings within t
    he list (including duplicates).

    Time: 97% (36ms)
    """
    def commonChars(self, A: List[str]) -> List[str]:
        result = []
        first_map = {}
        for ch in A[0]:
            if ch not in first_map:
                first_map[ch] = 1
            else:
                first_map[ch] += 1

        for ch in first_map:
            min_val = first_map[ch]
            for i in range(1,len(A)):
                count = A[i].count(ch)
                if count > 0:
                    min_val = min(min_val, count)
                else:
                    min_val = 0
            result += [ch] * min_val

        return result
