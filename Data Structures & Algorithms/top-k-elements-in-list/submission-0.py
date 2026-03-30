class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        map = {}
        for word in sorted(words):
            if word not in map:
                map[word] = 1
                continue
            map[word] += 1
        sortedMap = sorted(map, key=lambda x: map[x], reverse=True)
        answerArray = []
        for i in range(k):
            answerArray.append(sortedMap[i])

        return answerArray
