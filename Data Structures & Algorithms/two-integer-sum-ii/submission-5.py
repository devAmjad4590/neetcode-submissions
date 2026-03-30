class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0

        while l < len(numbers):
            r = len(numbers)-1
            
            while r - l > 0:
                print('R: '+ str(r))
                print('L: '+ str(l))
                if numbers[l] + numbers[r] == target:
                    return [l+1,r+1]
                r -= 1
            l += 1
            
        return []
