class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        paths= triangle.copy()
        
        for pos in range(len(triangle)-2, -1, -1):
            
            for row_pos in range(len(triangle[pos])):
                paths[pos][row_pos] += min(paths[pos+1][row_pos], paths[pos+1][row_pos+1])
                
        # print(paths[0][0])
        return paths[0][0]