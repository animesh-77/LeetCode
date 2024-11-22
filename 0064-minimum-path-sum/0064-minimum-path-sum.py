class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        import numpy as np
        m, n= len(grid), len(grid[0]) 
        
        costs = np.array(grid)
        

        for row in range(m-2, -1, -1):
            costs[row, -1] = grid[row][-1]+ costs[row+1, -1]
            
        for col in range(n-2, -1, -1):
            costs[-1, col] = grid[-1][col]+ costs[-1, col+1]
            
        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                costs[row, col]= costs[row, col] + min(costs[row+1, col], costs[row, col+1])
        
        # print(costs)
        return int(costs[0, 0])