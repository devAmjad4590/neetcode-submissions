class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1 = sorted(s)
        f2 = sorted(t)
        return f1 == f2


        