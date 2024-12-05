class Solution:
    def squareIt(self, n: int) -> int:
        ret= 0
        while n>0:
            ret += (n%10)**2
            n = n//10
        
        return ret
    def isHappy(self, n: int) -> bool:
        
        loop= {n: None}

        while n >= 1:
            n= self.squareIt(n)
            # print(n)
            
            if n== 1:
                return True
            
            if n in loop:
                return False
            
            
            
            loop[n]= None
            
                        
        