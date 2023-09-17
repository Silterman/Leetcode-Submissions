#https://leetcode.com/problems/shift-2d-grid/
#https://leetcode.com/submissions/detail/1047899645/

class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        groupL = len(grid[0])
        grid = [num for group in grid for num in group]
        grid = grid[(-k)%len(grid):] + grid[:(-k)%len(grid)]
        return [grid[i:i+groupL] for i in range(0, len(grid), groupL)]