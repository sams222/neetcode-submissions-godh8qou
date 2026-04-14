class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set(s)
        max_substring = len(unique_chars)

        current_greatest_substring = 0
        freq_map = {}
        
        anchor = 0

        for i, c in enumerate(s):
            

            if c not in freq_map:
                freq_map[c] = 1

            else:
                freq_map[c] += 1

            while freq_map[c] > 1 and anchor < i:
                freq_map[s[anchor]] -= 1
                anchor+=1
            current_greatest_substring = max((i-anchor + 1), current_greatest_substring)

        return current_greatest_substring

