class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
    
        for word in strs:
            count = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                count[idx] += 1
            anagram_groups[tuple(count)].append(word)
        
        return list(anagram_groups.values())

