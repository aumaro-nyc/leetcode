class Solution:
    """
    You are given an array of strings words and a string chars.
    A string is good if it can be formed by characters from chars
    (each character can only be used once).

    Return the sum of lengths of all good strings in words.

    Time: 17% (320ms)
    """
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        char_map = {}
        for ch in chars:
            if ch not in char_map:
                char_map[ch] = 1
            else:
                char_map[ch] += 1
        for word in words:
            flag = True
            for ch in word:
                if ch not in char_map or char_map[ch] < word.count(ch):
                    flag = False
            total += len(word) if flag else 0
        return total
