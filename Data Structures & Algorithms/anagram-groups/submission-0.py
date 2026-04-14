class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        
        for word in strs:
            count = [0] * 26
            for c in word:
                c_index = ord(c) - ord('a')
                count[c_index] += 1

            if tuple(count) in result:
                result[tuple(count)].append(word)
            else:
                result[tuple(count)] = [word]

        return list(result.values())