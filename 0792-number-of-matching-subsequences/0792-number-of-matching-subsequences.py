class Solution:
    
    def isSubsequence(self, s:str, t: str) -> int:
        
        pos= 0
        
        while len(s) > 0:
            
            if pos>= len(t):
                break
            
            if s[0] == t[pos]:
                s= s[1:]
                
            pos += 1
            
        else:
            return 1
        return 0
        
        
        
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        ret= 0
        already= {}
        for word in words:
            if word in already:
                ret+= already[word]
            else:
                already[word]=  self.isSubsequence(word, s)
                ret += already[word]
                
            
            
        return ret
        