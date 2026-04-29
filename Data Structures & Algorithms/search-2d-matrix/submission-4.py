class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        nums = matrix
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m][-1] == target:
                return True
            elif nums[m][0] < target and nums[m][-1] < target:
                l = m + 1
            elif nums[m][0] > target and nums[m][-1] > target:
                r = m - 1
            else:
                return self.binarySearch(nums[m], target)
            
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