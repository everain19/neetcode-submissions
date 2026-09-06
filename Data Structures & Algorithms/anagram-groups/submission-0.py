class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        
        for el in strs:
            key = "".join(sorted(el))
            seen[key].append(el)

        output = []

        for el in seen.values():
            output.append(el)

        return output
