#https://leetcode.com/problems/pascals-triangle-ii/
#https://leetcode.com/submissions/detail/1224946372/

class Solution:
    def getRow(self, n: int) -> list[int]:
        row = [1]
        
        for i in range(n):
            row.append(int(row[i]*(n-i)/(i+1)))
        
        return row
    
s = Solution()

print(s.getRow(1))
print(s.getRow(2))
print(s.getRow(3))
print(s.getRow(4))
print(s.getRow(5))