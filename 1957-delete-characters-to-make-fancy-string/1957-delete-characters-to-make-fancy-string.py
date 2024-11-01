class Solution:
    def makeFancyString(self, s: str) -> str:
        ret_str= s[0]
        last_char_dic= {s[0]:1}
        for c in s[1:]:
            ret_str += c
            if c in last_char_dic:
                last_char_dic[c] += 1
                
                if last_char_dic[c] == 3:
                    ret_str = ret_str[:-1]
                    last_char_dic[c]-=1
                    
            elif c not in last_char_dic:
                last_char_dic = {c: 1}
                
        return ret_str
                
            
        