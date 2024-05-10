#https://leetcode.com/problems/height-checker/
#https://leetcode.com/submissions/detail/1234926079/

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        output = 0
        
        for i, height in enumerate(heights):
            if height != expected[i]:
                output += 1
                
        return output
    
s = Solution()

print(s.heightChecker([1,1,4,2,1,3]))