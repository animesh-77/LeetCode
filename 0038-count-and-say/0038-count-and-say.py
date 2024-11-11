class Solution:
    
    def get_RLE(self, s:str)-> str:
        
        c_char= s[0]
        c_char_count= 1
        RLE_str= ""
        
        for pos in range(1, len(s)):
            
            if s[pos] == c_char:
                c_char_count += 1
                
            else:
                RLE_str+= str(c_char_count)+c_char
                c_char = s[pos]
                c_char_count= 1
        else:
            RLE_str+= str(c_char_count)+c_char
        return RLE_str
    
    def countAndSay(self, n: int) -> str:
        
        if n==1:
            return "1"
        
        last_RLE_str= "1"
        # else n > 0
        for n_val in range(2, n+1):
            
            RLE_str= self.get_RLE(last_RLE_str)
            last_RLE_str= RLE_str
            
            # print(last_RLE_str)
        return RLE_str
            
        