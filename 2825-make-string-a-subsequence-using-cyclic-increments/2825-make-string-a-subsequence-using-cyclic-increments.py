class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        same_char= {chr(i):chr(i) for i in range(97, 123)}
        
        prev_char= {chr(i+1):chr(i) for i in range(97, 122)}
        prev_char["a"]= "z"
        
        pos=0
        while len(str2) > 0:
            if pos >= len(str1):
                break
            if same_char[str2[0]]== str1[pos] or prev_char[str2[0]] == str1[pos]:
                str2= str2[1:]
            
            pos+=1
            
        else:
            return True
        
        return False
        
            
        