class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort in-place
        sortedNums = nums  # Now sortedNums references the sorted array
        res = []
        for i in range(len(sortedNums) - 2):
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue
            j = i + 1
            k = len(sortedNums)-1
            while j < k:
                if sortedNums[i] + sortedNums[j] + sortedNums[k] < 0:
                    j = j+1
                elif sortedNums[i] + sortedNums[j] + sortedNums[k] > 0:
                    k = k - 1
                else:
                    res.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                    while j < k and sortedNums[j] == sortedNums[j+1]:
                        j = j+1
                    while j < k and sortedNums[k] == sortedNums[k-1]:
                        k = k -1
                    j = j+1
                    k = k - 1
        return res
