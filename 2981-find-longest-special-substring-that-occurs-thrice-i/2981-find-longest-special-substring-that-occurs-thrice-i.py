class Solution:
    def maximumLength(self, s: str) -> int:
        
        def checkSpecial(s:str)-> bool:
            
            c= s[0]
            for c2 in s[1:]:
                if c2 != c:
                    return False
            return True
        
        lenS= len(s)
        
        specialCandidates= set()
        
        special= s[0]
        for c in s[1:]:
            if c== special[-1]:
                special += c
            else:
                specialCandidates.add(special)
                special = c
        else:
            specialCandidates.add(special)
            
            
        newSpecialCandidates= set()
        
        for specialCandidate in specialCandidates:
            newSpecialCandidate = specialCandidate
            while len(newSpecialCandidate) >0 :
                newSpecialCandidates.add(newSpecialCandidate)
                
                newSpecialCandidate= newSpecialCandidate[1:]
                
        specialCandidates= list(newSpecialCandidates)
        specialCandidates.sort(key= lambda x: len(x))
        
        for specialCandidate in specialCandidates[::-1]:
            
            lenToRet= len(specialCandidate)
            counter= 0
            
            for pos in range(0, lenS):
                subStr= s[pos: pos+lenToRet]
                if len(subStr) != lenToRet:
                    break
                    
                if subStr == specialCandidate:
                    counter += 1
                    
                if counter == 3:
                    return lenToRet
        else:
            return -1