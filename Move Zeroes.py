#https://leetcode.com/problems/move-zeroes
#https://leetcode.com/submissions/detail/1038357755/

class Solution:
    def moveZeroes(self, nums):
        index = 0

        # Place non-zero elements at the start of the list
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1

        # Fill the remaining positions with zeroes
        while index < len(nums):
            nums[index] = 0
            index += 1