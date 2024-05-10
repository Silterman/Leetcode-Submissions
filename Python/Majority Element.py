# https://leetcode.com/problems/majority-element/
#

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majEle = nums[0]
        n = 1
        
        for element in nums[1:]:
            if majEle != element:
                if n == 0:
                    majEle = element
                    n = 1
                else:
                    n -= 1
            else:
                n += 1
            
        return majEle
    
s = Solution()

print(s.majorityElement([2,2,1,1,1,1,2]))