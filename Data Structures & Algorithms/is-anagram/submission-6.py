class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = [0] * 26
        countT = [0] * 26

        for i in s:
            countS[ord(i) - ord('a')] += 1

        for i in t:
            countT[ord(i) - ord('a')] += 1

        return countS == countT