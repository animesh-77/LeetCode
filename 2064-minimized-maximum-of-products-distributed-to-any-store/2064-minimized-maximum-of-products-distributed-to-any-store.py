class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        import bisect
        import math
        
        def maxInOneStore(val: int):
            
            storesFilled= 0
            for quantity in quantities:
                
                L= int(math.ceil((quantity- val)/val))
                
                storesFilled += (L+1)
                
                if storesFilled > n:
                    break
                    
            return storesFilled <= n
        
        minVal, maxVal= 1, max(quantities)
        
        optVal= bisect.bisect_left(range(minVal, maxVal), True, key= maxInOneStore)+1
        
        return optVal