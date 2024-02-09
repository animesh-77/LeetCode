class Solution:
    def sum(self, num1: int, num2: int) -> int:
        # return num1+num2 # non optimal solution
        
        mask= 0b111111111 # 511

        a, b= num1& mask, num2&mask
        

        while b>0:
            
            carry= a&b
            a = (a^b) & mask
            
            b= (carry << 1) & mask
        
        if a>>8 & 1 == 1:
            # result is negative
            return -self.sum(~a, 1)
        return a