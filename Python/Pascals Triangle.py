#https://leetcode.com/problems/pascals-triangle/description/
#https://leetcode.com/submissions/detail/1224936524/

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1], [1,1]]
        if numRows == 1:
            return triangle[:1]
        if numRows == 2:
            return triangle[:2]
        
        for row in range(2, numRows):
            triangle.append([1, 1])
            for i in range(1, row):
                target = triangle[-2][i-1]+triangle[-2][i]
                triangle[row].insert(i, target)
        
        return triangle
          
s = Solution()

print(s.generate(1)) #[[1]]
print(s.generate(2)) #[[1], [1,1]]
print(s.generate(3)) #[[1], [1,1], [1,2,1]]
print(s.generate(4)) #[[1], [1,1], [1,2,1], [1,3,3,1]]
print(s.generate(5)) #[[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]