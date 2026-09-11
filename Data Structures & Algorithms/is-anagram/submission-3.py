class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        key_s = [0] * 26
        key_t = [0] * 26

        for char in s:
            key_s[ord(char) - ord('a')] += 1

        for char in t:
            key_t[ord(char) - ord('a')] += 1

        return key_s == key_t


