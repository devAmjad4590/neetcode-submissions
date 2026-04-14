class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        short = fast = 0


        while True:
          short = nums[short]
          fast = nums[nums[fast]]
          if short == fast:
               break
     
        short2 = 0
        while True:
          short2 = nums[short2]
          short = nums[short]
          if short == short2:
               return short
        return 0