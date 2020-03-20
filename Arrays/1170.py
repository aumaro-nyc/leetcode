class Solution:
    """
    Time: 20% (800ms)
    """
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        word_vals = []
        answer = []
        for word in words:
            word_vals.append(word.count(min(word)))

        for query in queries:
            min_count = query.count(min(query))
            count = 0
            for val in word_vals:
                count += 1 if min_count < val else 0
            answer.append(count)
        return answer
