class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        
        # print("ORG ", n)
        if  n <= 0:
            return False
        
        while (n>0):
            
            # new_num = n>>1
            # print("new num", new_num,"   n", n)
            if (n>>1) *2 != n and (n>>1) != 0:
                return False
            
            n= n>>1
        return True
            
        