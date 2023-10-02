# https://leetcode.com/problems/spiral-matrix/
# https://leetcode.com/submissions/detail/1065337261/

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        output = []
        while matrix != []:
            try:
                output += matrix[0] #append first row
                del matrix[0]

                for i in range(len(matrix[:-1])): #going down
                    output.append(matrix[i][-1])
                    del matrix[i][-1]

                output += matrix[-1][::-1] #append last row backwards
                del matrix[-1]

                for i in range(len(matrix[1:])): #going back up
                    output.append(matrix[-i-1][0])
                    del matrix[-i-1][0]

                while [] in matrix: #cleaning up incase you have single file lists
                    matrix.remove([])
            except IndexError:
                break
        return output
    
s = Solution()
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print([1,2,3,4,8,12,11,10,9,5,6,7])

print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
print([1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10])

print(s.spiralOrder([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]))
print([1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13])