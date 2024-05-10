#https://leetcode.com/problems/search-insert-position
#https://leetcode.com/submissions/detail/1037590777/

class Solution(object):
    def searchInsert(self, nums, target):
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        for i in range(len(nums)):
            if nums[i] >= target:
                return i