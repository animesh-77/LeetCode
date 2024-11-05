class Solution:
    def minChanges(self, s: str) -> int:
        
        changes= 0
        
        for p_char, c_char in zip(s[0::2], s[1::2]):
            if c_char != p_char:
                changes+= 1
                
        return changes
        