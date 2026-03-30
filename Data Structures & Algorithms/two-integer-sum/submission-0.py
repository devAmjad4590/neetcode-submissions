class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            n1 = target - nums[i]
            if n1 not in map:
                map.update({nums[i]: i})
                continue
            return [map.get(n1), i]
        return []
            

        