class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        # target - nums = x
        # 7 - 3 = 4 | 4: 0
        # 7 - 4 = 3 | 
        # x: num
        # if x in map then return [map[x], i]

        for i in range(len(nums)):
            x = target - nums[i]
            if nums[i] in map:
                return [map[nums[i]], i]
            map[x] = i
        return []
                