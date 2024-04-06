#https://leetcode.com/problems/valid-sudoku/description/
#https://leetcode.com/submissions/detail/1223423435/

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        columns = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        boxes = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        
        for y in range(9):
            curRow = {}
            for x in range(9):
                curNum = board[y][x]
                
                if curNum == ".":
                    continue
                
                #can I reduce the boilerplate?      
                if curNum in curRow:
                    return False
                curRow.update({curNum:0})
                
                if curNum in columns[x]:
                    return False
                columns[x].update({curNum:0})
                
                if curNum in boxes[x//3 + (y//3)*3]:
                    return False
                boxes[x//3 + (y//3)*3].update({curNum:0})            
        return True
        
s = Solution()

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(s.isValidSudoku(board))

board = [["7",".",".",".","4",".",".",".","."]
 ,[".",".",".","8","6","5",".",".","."]
 ,[".","1",".","2",".",".",".",".","."]
 ,[".",".",".",".",".","9",".",".","."]
 ,[".",".",".",".","5",".","5",".","."]
 ,[".",".",".",".",".",".",".",".","."]
 ,[".",".",".",".",".",".","2",".","."]
 ,[".",".",".",".",".",".",".",".","."]
 ,[".",".",".",".",".",".",".",".","."]]

print(s.isValidSudoku(board))