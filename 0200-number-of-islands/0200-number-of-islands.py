class Solution:
    
    def makeIsland(self, row: int, col: int, grid: List[List[str]])-> List[List[str]]:
        
        m, n = len(grid), len(grid[0])
        if grid[row][col]== "0":
            return grid
        else:
            grid[row][col]= "0"
        
        # go left
        if col>0:
            grid= self.makeIsland(row, col-1, grid)
            
        # go right
        if col< (n-1):
            grid= self.makeIsland(row, col+1, grid)
            
        # go up
        if row>0:
            grid= self.makeIsland(row-1, col, grid)
            
        # go down
        if row< (m-1):
            grid= self.makeIsland(row+1, col, grid)
            
        return grid
                

        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islandCount= 0
        
        m, n = len(grid), len(grid[0])
        
        
        for row in range(m):
            for col in range(n):
                
                if grid[row][col] == "1":
                    
                    grid= self.makeIsland(row, col, grid)
                    islandCount += 1
                
        
        return islandCount
                    
                    