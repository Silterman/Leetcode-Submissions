#https://leetcode.com/problems/ugly-number/
#https://leetcode.com/submissions/detail/1226996888/

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        for i in [2, 3, 5]:
            if n/i == int(n/i):
                return self.isUgly(int(n/i))
            
        return False
        
s = Solution()
print(s.isUgly(7))