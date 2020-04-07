class Solution:
    """
    Time: 55% (52ms)
    """
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1:
            return bits[0] == 0
        prev = bits[0]
        i = 1
        new_word = True if prev == 0 else False
        while i < len(bits) - 1:
            if prev == 1 and not new_word:
                i += 1
                new_word = True
            else:
                prev = bits[i]
                new_word = True if bits[i] == 0 else False
                i += 1
        return new_word
