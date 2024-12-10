class Solution:
    def maximumLength(self, s: str) -> int:
        
        def checkSpecial(s:str)-> bool:
            
            c= s[0]
            for c2 in s[1:]:
                if c2 != c:
                    return False
            return True
        
        lenS= len(s)
        
        for subStrLen in range(lenS-2, 0, -1):
            
            # every substring will have lenght subStrLen
            subStrDict= {}
            for pos in range(0, lenS):
                
                subStr= s[pos: pos+subStrLen]
                if len(subStr) != subStrLen:
                    break
                
                if checkSpecial(subStr) is False:
                    continue
                    
                # print(f"{subStrLen=} {subStr=}")
                
                subStrDict[subStr] = subStrDict.get(subStr, 0)+1
                
                if subStrDict[subStr] == 3:
                    # print(f"{subStrLen=} {subStr=}")
                    return subStrLen
                
        return -1