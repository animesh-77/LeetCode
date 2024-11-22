class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        # assume first col not flipped
        m_row, n_col= len(matrix), len(matrix[0])
        
        list_flip= ["0"]* m_row
        
        
        for row in range(m_row):
            for col in range(1, n_col):
                
                if matrix[row][col] == matrix[row][0]:
                    # no flip required
                    list_flip[row] += "0"
                    
                else:
                    list_flip[row] += "1"
        
        all_ops= {}
        max_rows= 0
        for op in list_flip:
            all_ops[op] = all_ops.get(op, 0)+ 1
            max_rows = all_ops[op] if (max_rows < all_ops[op]) else max_rows
            
        return max_rows
                    
                    
                    
                
                
        