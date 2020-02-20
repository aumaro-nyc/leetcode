class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max = 0
        count = 0
        left,right = 0,0
        freq_map = {}
        while right < len(s):
            if s[right] not in freq_map or freq_map[s[right]] == 0:
                freq_map[s[right]] = 1
                count += 1
                right += 1
            else:
                if count > max:
                    max = count
                while s[left] != s[right]:
                    freq_map[s[left]] -= 1
                    count -= 1
                    left += 1
                if left == right:
                    count += 1
                    right += 1
                else:
                    freq_map[s[left]] -= 1
                    count -= 1
                    left += 1
        if count > max:
            max = count
        return max
