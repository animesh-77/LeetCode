class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        import numpy as np
        
        all_ways= np.zeros((m, n),)
        
        all_ways[:,-1]= 1
        all_ways[-1, :]= 1
        
        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                all_ways[row, col]= all_ways[row+1, col]+ all_ways[row, col+1]
        # print(all_ways)
        
        return int(all_ways[0,0])