class Solution:
   
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m, n= len(matrix), len(matrix[0])
        max_n= [[0]*n for _ in range(m)]
        
        max_n_len= 0 
        
        for row in range(m):
            max_n[row][0]= 1 if matrix[row][0]=="1" else 0
            max_n_len= max(max_n_len, max_n[row][0])
            
        for col in range(n):
            max_n[0][col]= 1 if matrix[0][col]=="1" else 0
            max_n_len= max(max_n_len, max_n[0][col])
        
        
            
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == "1":
                    if max_n[row-1][col]>0 and max_n[row][col-1]>0 and max_n[row-1][col-1]>0:
                        max_n[row][col]= min(min(max_n[row-1][col], max_n[row][col-1]), max_n[row-1][col-1])+1   
                        max_n_len= max(max_n_len, max_n[row][col])
                    else:
                        max_n[row][col]= 1
                        max_n_len= max(max_n_len, max_n[row][col])
                else:
                    max_n[row][col]= 0
        
        # print(max_n_len)
        
        return max_n_len**2