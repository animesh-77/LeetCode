class Solution:
    def compressedString(self, word: str) -> str:
        
        comp= ""
        c_char= word[0]
        c_char_count= 1
        
        for n_char in word[1:]:
            
            if n_char == c_char:
                
                c_char_count += 1
                if c_char_count == 9:
                    comp += str(c_char_count)+c_char
                    c_char_count = 0
                    
                
            else: # n_char != c_char
                
                if c_char_count > 0:
                    comp += str(c_char_count)+c_char
                c_char= n_char
                c_char_count = 1
        
        else:
            if c_char_count > 0:
                comp += str(c_char_count)+c_char
            
        
        return comp