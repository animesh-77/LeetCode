class Solution:
    def climbStairs(self, n: int) -> int:
        
        ret1, ret2= 0, 1
        for m in range(n):
            
            a= ret1
            ret1= ret2
            ret2= ret2 + a
        
        return ret2
        