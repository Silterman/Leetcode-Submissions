#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        self.nums = nums
        return j
    
s = Solution()

print(s.removeDuplicates([1,1,2]), s.nums) #[1,2,_]