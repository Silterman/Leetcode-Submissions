#
#

class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        maxGap = 0
        if len(nums) < 2:
            return 0
        
        nums.sort()
        
        for i in range(len(nums)-1):
            maxGap = max(maxGap, abs(nums[i]-nums[i+1]))
        
        return maxGap
    
    def minGap(self, num: tuple[int, int], nums: list[int]) -> int:
        minGap = 0
        return minGap
    
s = Solution()

print(s.maximumGap([3,6,9,1]))