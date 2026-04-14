from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # fix sized window
        # grow by default
        # shrink if sum of frequencies is greater than the len of sub string

        anchor = 0
        freq_map = {}
        l =  len(s1)
        s1_set = set(s1)
        counts = Counter(s1)

        if len(s2) < l:
            return False

        for i in range(l):
            c = s2[i]
            if c in s1_set:
                freq_map[c] = freq_map.get(c, 0) + 1
        
        if freq_map == counts:
            return True

        for j in range(l,len(s2)):
            c = s2[j]
            c2 = s2[anchor]
            if c in s1_set:
                freq_map[c] = freq_map.get(c, 0) + 1

            if c2 in freq_map:
                freq_map[c2] -= 1
            anchor+=1

            if freq_map == counts:
                return True

        return False



