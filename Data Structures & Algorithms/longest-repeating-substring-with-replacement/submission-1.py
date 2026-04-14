class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # two pointers to create a substring
        # min(freq_char1, freq_char2) <= k

        freq_map = {}
        j = 0
        solution = 0
       
        # s="AAABABB"k=1
        for i, c in enumerate(s):
            print(freq_map)
            window_size = i-j+1
            
            #build freq map
            if c not in freq_map:
                freq_map[c] = 1
            else:
                freq_map[c] += 1

            max_frequency = max(freq_map.values())
            if window_size-max_frequency <= k and solution < window_size:
                solution = window_size
                
            while window_size-max_frequency > k:        
                freq_map[s[j]] -= 1
                j+=1
                window_size = i-j+1

            
        return solution
