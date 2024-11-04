class Solution:
    def reverseBits(self, n: int) -> int:
        
        
        num_str= "{0:0>32b}".format(n)
        
        # print(num_str, len(num_str))
       
        
        ret= 0
            
        for power, bit in enumerate(num_str):
            if bit == "1":
                ret = ret + (2**power)
            
        
        return ret