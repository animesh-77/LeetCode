class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        ret= 0
        for word in words:
            if word[0:len(pref)] == pref:
                ret += 1
                
        return ret