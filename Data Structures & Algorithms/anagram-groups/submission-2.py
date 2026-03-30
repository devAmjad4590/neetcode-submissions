class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in hashMap:
                hashMap[key].append(word)
                continue
            hashMap[key] = [word]
        array = []
        return list(hashMap.values())