class Solution:
    def give_common(self, str1, str2) -> str:
        ret = ""
        for char1, char2 in zip(str1, str2):
            if char1 == char2:
                ret += char1
            else:
                return ret
        return ret
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
            return strs[0]
        
        ret= self.give_common(strs[0], strs[1])
        for next_word in strs[2:]:
            ret = self.give_common(ret, next_word)
            
            if ret == "":
                break
                
        return ret
        
        