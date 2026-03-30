class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 7: 0, start = 0
        # start = 1, maxArea = 7, start = 0
        # 1 : 0
        # start = 3, 7 : 3
        # start = 4, 7:3 popped, start = 3
        # 2: 3
        # 2: 5
        # 4: 6

        maxArea = 0
        stack = [] # pairs (index, height)
        for i,t in enumerate(heights):
            start = i
            while stack and stack[-1][1] > t:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, t))

        for index, height in stack:
            maxArea = max(maxArea, height * (len(heights) - index))
        return maxArea

        # 4, 4, 8 , 7