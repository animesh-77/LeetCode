class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        pos= 0
        while len(s) > 0:
            
            if pos>= len(t):
                break
                
            if s[0]== t[pos]:
                s=s[1:]
            
            pos += 1
                
        else:
            return True
        
        return False