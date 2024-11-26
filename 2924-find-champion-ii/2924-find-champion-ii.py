class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        teams= [0]*n
        
        for strong, weak in edges:
            teams[weak] += 1
            
        strongest= None
        
        for pos,team in enumerate(teams):
            if team == 0:
                if strongest is None:
                    strongest = pos
                else:
                    return -1
            else:
                pass
        
        return strongest
                    
                
            
        