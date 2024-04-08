#https://leetcode.com/problems/contains-duplicate/
#

#very slow, good memory efficiency
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False
    
s = Solution()

print(s.containsDuplicate([3,3]))