class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            sortedKey = "".join(sorted(s))
            if sortedKey in map:
                map[sortedKey].append(s)
                continue
            map[sortedKey] = [s]
        return list(map.values())