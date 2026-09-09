class Solution:

    def encode(self, strs: List[str]) -> str:
        prepared_list = []
        for word in strs:
            prepared_list.append(f'{len(word)}#{word}')
        return "".join(prepared_list)
        
    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        j = i
        while i < len(s): 
            while s[j] != '#':
                j += 1
            length_str = int(s[i:j])
            word = s[j + 1: j + 1 + length_str]
            
            output.append(word)
            i = j + 1 + length_str
            j = i
        
        return output
