class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        i = 0
        j = len(heights)-1
        while i < j:
            minHeight = min(heights[i], heights[j])
            distance = (j + 1) - (i + 1)
            area = minHeight * distance
            largest = max(largest, area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return largest