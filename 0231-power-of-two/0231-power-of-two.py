class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        
        # print("ORG ", n)
        if  n <= 0:
            return False
        
        while (n>0):
            
            new_num = n>>1
            # print("new num", new_num,"   n", n)
            if new_num *2 != n and new_num != 0:
                return False
            
            n= new_num
        return True
            
        