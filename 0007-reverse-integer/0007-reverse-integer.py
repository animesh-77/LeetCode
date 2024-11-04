class Solution:
    def reverse(self, x: int) -> int:
        
        if x<0:
            sign = -1
        else:
            sign = 1
        
        x = abs(x)
        ret= 0
        
        while x>0:
            
            ret = ret*10 + (x%10)
            
            if ret%10 != x%10 or ret > 2**31 -1:
                return 0
            
            x = x//10
            
            
        return ret*sign    
            
                