class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["neet", "code", "love", "you"]
        # ["4#neet4#code4#love3#you"]
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + '#' + s
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i != len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1 : j + 1 + length]
            res.append(word)
            i = j + 1 + length
        return res


