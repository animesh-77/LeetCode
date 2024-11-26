class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        u0, v0= edges[0][0], edges[0][1]
        u1, v1= edges[1][0], edges[1][1]
        
        if u0 == u1 or u0== v1:
            return u0
        if v0 == u1 or v0 == v1:
            return v0
        
        
        