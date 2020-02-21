class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        if k == 0: return 0
        if k > len(s):
            return len(s)
        letter_count = 0
        max = 1
        count = 0
        freq_map = {}
        left,right = 0,0

        while right < len(s):
            if s[right] not in freq_map:
                freq_map[s[right]] = 1
                letter_count += 1
                count += 1
            else:
                freq_map[s[right]] += 1
                count += 1
            right += 1
            if letter_count > k:
                if count > max:
                    max = count - 1
                while letter_count > k:
                    if freq_map[s[left]] - 1 == 0:
                        del freq_map[s[left]]
                        letter_count -= 1
                    else:
                        freq_map[s[left]] -= 1
                    count -= 1
                    left += 1
            if count > max:
                max = count
        return max
