# https://leetcode.com/problems/remove-element/
# https://leetcode.com/submissions/detail/1065253719/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        print(nums)
        return i

s = Solution()
print(s.removeElement([3,2,2,3], 3))