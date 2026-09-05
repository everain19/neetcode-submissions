class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ltr_count_s = {}
        ltr_count_t = {}
        
        for i in range(len(s)):
            ltr_count_s[s[i]] = 1 if s[i] not in ltr_count_s else ltr_count_s[s[i]] + 1
            ltr_count_t[t[i]] = 1 if t[i] not in ltr_count_t else ltr_count_t[t[i]] + 1

        for k, v in ltr_count_s.items():
            if k not in ltr_count_t or ltr_count_s[k] != ltr_count_t[k]:
                return False

        return True 


