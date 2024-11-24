class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        matrix_sum= 0
        least_num= abs(matrix[0][0])
        total_neg= 0
        
        n= len(matrix)
        
        for row in range(n):
            for col in range(n):
                total_neg += 1 if (matrix[row][col]<0) else 0
                
                abs_num= abs(matrix[row][col])
                matrix_sum += abs_num
                
                least_num= abs_num if abs_num < least_num else least_num
                
                
        if total_neg%2 ==1:
            # odd number of negative number
            # make the smallest one in the matrix negative
            # print(least_num)
            matrix_sum -= (2*least_num)
        else:
            pass
        
        return matrix_sum