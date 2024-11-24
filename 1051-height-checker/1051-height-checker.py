class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        
        height_sort= sorted(heights)
        total= 0
        
        for correct_height, height in zip(height_sort, heights):
            total += 1 if (correct_height != height) else 0
            
        return total
            
        