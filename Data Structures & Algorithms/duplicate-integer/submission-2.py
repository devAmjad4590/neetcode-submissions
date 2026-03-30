class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    #   array = []  
    #   for i in range(len(nums)):
    #     if nums[i] not in array:
    #         array.append(nums[i])
    #     else:
    #         return True
    #   return False
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False