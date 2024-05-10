#https://leetcode.com/problems/permutations/
#https://leetcode.com/submissions/detail/1226803810/

from itertools import permutations

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return [list(i) for i in list(permutations(nums, len(nums)))]
          
s = Solution()

print(s.permute([1,2,3]))