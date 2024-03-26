#https://leetcode.com/problems/word-search/description/
#

import numpy as np


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        word = list(word)
        board = np.array(board)
        print(board)
        
        for (y,x), letter in np.ndenumerate(board):
            if letter == word[0]:
                curPath = [(x, y)]
                if checkNext(curPath, word, board):
                    return True
                
        return False
    
def checkNext(curPath: list[tuple], word: list[str], board: list[list[str]]) -> bool:
    print(curPath)
    if len(curPath) == len(word):
        return True
    
    x, y = curPath[-1]
    adjacents = checkAdjacents(x, y, board, curPath)
    print(f"Looking for {word[len(curPath)]} in {adjacents}")
    
    for key in adjacents.keys():
        letter = adjacents[key]
        if letter == word[len(curPath)]:
            curPath.append(key)
            if checkNext(curPath, word, board):
                return checkNext(curPath, word, board)
        
    return False
    
#results dictionary with all adjacent letters
def checkAdjacents(x: int, y: int, board: list[list[str]], curPath:list[tuple]) -> dict[str:tuple[int]]:
        adjacents = {}
        
        if x-1 >= 0: #not in left-most column
            if (x-1, y) not in curPath:
                adjacents.update({(x-1, y):board[y][x-1]})
        if y-1 >= 0: #not in top-most row
            if (x, y-1) not in curPath:
                adjacents.update({(x, y-1): board[y-1][x]})
        if x+1 < len(board[0]): #not in right-most column
            if (x+1, y) not in curPath:
                adjacents.update({(x+1, y):board[y][x+1]})
        if y+1 < len(board): #not in bottom-most row
            if (x, y+1) not in curPath:
                adjacents.update({(x, y+1):board[y+1][x]})
            
        return adjacents  
    
s = Solution()

#print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
#print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
#print(s.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))
#print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
#print(s.exist([["A","B"],["C","D"]], "ABCD"))
print(s.exist([["A", "B", "C"],["X", "C", "X"], ["X", "D", "X"]], "ABCD"))