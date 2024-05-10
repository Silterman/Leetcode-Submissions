#https://leetcode.com/problems/longest-alternating-subarray
#https://leetcode.com/submissions/detail/998864948/

class Solution:
    def isAlternating(self, subArray):
        if len(subArray)%2 == 0:
            if subArray == [subArray[0], subArray[0]+1]*int(len(subArray)/2):
                return True
        if subArray == ([subArray[0], subArray[0]+1]*(len(subArray)//2))+[subArray[0]]:
            return True
        return False
    
    def alternatingSubarray(self, nums: list[int]):
        for i in range(0, len(nums)-1):
            subArrayLength = (len(nums)-i)
            for j in range(len(nums)-(len(nums)-i)+1):
                s = nums[j:subArrayLength+j]
                #print(s)
                if Solution.isAlternating(0, s):
                    #print(s)
                    return subArrayLength
        return -1