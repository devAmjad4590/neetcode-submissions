class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[-1] < target:
                continue
            else:
                return self.binarySearch(i, target)
        return False


    def binarySearch(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return True
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False