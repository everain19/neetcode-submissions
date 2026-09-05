class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        
        if len(list_s) != len(list_t):
            return False

        list_s.sort()
        list_t.sort()

        for idx, el in enumerate(list_s):
            if el != list_t[idx]:
                return False

        return True
