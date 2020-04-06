class Solution:
    """
    Time: 52% (104ms)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for word in strs:
            s_word = str(sorted(word))
            if s_word in maps:
                maps[s_word].append(word)
            else:
                maps[s_word] = [word]
        return maps.values()
