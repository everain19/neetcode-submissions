class Solution:

    def encode(self, strs: List[str]) -> str:
        prepared_str = ""
        for word in strs:
            prepared_str += str(len(word)) + '#' + word
        return prepared_str
        
    def decode(self, s: str) -> List[str]:
        def find_separator(idx, sep, row):
            if row[idx] == sep:
                return idx
            else:
                return find_separator(idx + 1, sep, row)
        
        output = []
        i = 0
        j = i
        while i < len(s):
            j = find_separator(j, '#', s)
            length_str = int(s[i:j])
            word = s[j + 1: j + 1 + length_str]
            output.append(word)
            i = j + 1 + length_str
            j = i

        return output
