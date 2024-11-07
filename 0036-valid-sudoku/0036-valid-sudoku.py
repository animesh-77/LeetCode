class Solution:
    
    def get_block(self, i:int, j:int) -> int:
        
        if i<=2:
            if j <= 2:
                return 1
            
            elif j <= 5:
                return 2
            
            else:
                return 3
                
            
        elif i<=5:
            if j <= 2:
                return 4
            
            elif j <= 5:
                return 5
            
            else:
                return 6
        
        else:
            if j <= 2:
                return 7
            
            elif j <= 5:
                return 8
            
            else:
                return 9
            
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_check = {i:{} for i in range(9)}
        col_check = {j:{} for j in range(9)}
        block_check = {block:{} for block in range(1,10)}
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    # print(i, j, num, row_check)
                    
                    if num in row_check[i]:
                        # number already in row
                        # print("ROW fail", i, num)
                        return False
                    else:
                        row_check[i][num]= None
                    
                    if num in col_check[j]:
                        # print("COL fail", j)
                        return False
                    else:
                        col_check[j][num] = None
                        
                    block= self.get_block(i, j)
                    if num in block_check[block]:
                        # print("BLOCK fail", block)
                        return False
                    else:
                        block_check[block][num] = None
        
        return True 
        