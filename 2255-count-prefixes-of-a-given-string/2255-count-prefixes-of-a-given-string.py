class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        
        ret= 0
        
        for word in words:
            if word == s[0:len(word)]:
                ret += 1
                
        return ret