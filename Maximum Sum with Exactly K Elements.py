#https://leetcode.com/problems/maximum-sum-with-exactly-k-elements  
#https://leetcode.com/submissions/detail/998869492/

class Solution:
    def maximizeSum(self, nums: list[int], k: int):
        return int(max(nums)*k + (k-1)*k/2)