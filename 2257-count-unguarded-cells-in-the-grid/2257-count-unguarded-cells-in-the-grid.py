class Solution:
    
    def fill_up(self, row: int, col: int , maze:List[List[int]], total_spaces: int ):
        
        # up direction
        row -= 1
        while row >= 0:
            if maze[row][col] in [1, 2, 3, 5, 7, 8, 9, 10]:
                break
            elif maze[row][col]== 4:
                maze[row][col] = 7
            elif maze[row][col]== 6:
                maze[row][col] = 8
            elif maze[row][col]== 0:
                total_spaces -= 1
                maze[row][col] = 3
                # print("removed ",row, col)
            row -= 1 
        return maze, total_spaces
    
    def fill_right(self, row: int, col: int , maze:List[List[int]], total_spaces: int ):
        
        m, n = len(maze), len(maze[0])
        # right direction
        col += 1
        while col< n:
            if maze[row][col] in [1, 2, 4, 6, 7, 8, 9, 10]:
                break
            elif maze[row][col]== 3:
                maze[row][col] = 7
            elif maze[row][col]== 5:
                maze[row][col] = 9
            elif maze[row][col]== 0:
                total_spaces -= 1
                maze[row][col] = 4
                # print("removed ",row, col)
            col += 1 
        return maze, total_spaces
    
    def fill_down(self, row: int, col: int , maze:List[List[int]], total_spaces: int ):
        
        m, n = len(maze), len(maze[0])
        # down direction
        row += 1
        while row < m:
            if maze[row][col] in [1, 2, 3, 5, 7, 8, 9, 10]:
                break
            elif maze[row][col]== 4:
                maze[row][col] = 9
            elif maze[row][col]== 6:
                maze[row][col] = 10
            elif maze[row][col]== 0:
                total_spaces -= 1
                maze[row][col] = 5
                # print("removed ",row, col)
            row += 1 
        return maze, total_spaces
    
    def fill_left(self, row: int, col: int , maze:List[List[int]], total_spaces: int ):
        
        m, n = len(maze), len(maze[0])
        # left direction
        col -= 1
        while col>=0:
            if maze[row][col] in [1, 2, 4, 6, 7, 8, 9, 10]:
                break
            elif maze[row][col]== 3:
                maze[row][col] = 8
            elif maze[row][col]== 5:
                maze[row][col] = 10
            elif maze[row][col]== 0:
                total_spaces -= 1
                maze[row][col] = 6
                # print("removed ",row, col)
                
            col -= 1 
        return maze, total_spaces
            
    
    
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        
        maze= [[0]*n for _ in range(m)]
        
        total_spaces= m*n
        
        for wall in walls:
            maze[wall[0]][wall[1]]= 2
            total_spaces -= 1
            
        for guard in guards:
            maze[guard[0]][guard[1]]= 1
            total_spaces -= 1
            row, col= guard[0], guard[1]
            # print("removed ",row, col)
            
        for guard in guards:  
            
            row, col= guard[0], guard[1]
            
            # print(row, col)
            # go up
            maze, total_spaces= self.fill_up(row, col, maze, total_spaces)
            # go right
            maze, total_spaces= self.fill_right(row, col, maze, total_spaces)
            # go down
            maze, total_spaces= self.fill_down(row, col, maze, total_spaces)
            # go left
            maze, total_spaces= self.fill_left(row, col, maze, total_spaces)
            
        # for row in range(m):
            # print(maze[row])
        # print(total_spaces)
        return total_spaces