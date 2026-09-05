class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        storage = {}

        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        
        if len(sorted_s) != len(sorted_t):
            return False

        storage[sorted_s] = True

        if sorted_t not in storage:
            return False

        return True

