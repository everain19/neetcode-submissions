class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        empty_char_counts = {
            'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 
            'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 
            'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 
            'w': 0, 'x': 0, 'y': 0, 'z': 0
        }

        anagram_groups = defaultdict(list)

        for word in strs:
            char_counts = empty_char_counts.copy()
            for char in word:
                char_counts[char] += 1 
            
            group_key_array = []

            for k, v in char_counts.items():
                if v != 0:
                    group_key_array.append(f"{k}{v}")
            
            group_key = "".join(group_key_array)

            anagram_groups[group_key].append(word)
            
        output = []
        for k, v in anagram_groups.items():
            output.append(v)
        return output
