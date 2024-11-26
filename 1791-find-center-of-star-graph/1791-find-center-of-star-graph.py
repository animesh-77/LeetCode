class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        n= len(edges)+ 1
        
        edge= [0]*(n+1)
        
        
        for p1, t1 in edges:
            
            edge[t1] += 1
            edge[p1] += 1
            
        for i in range(1, n+1):
            if edge[i] == n-1 :
                return i
        else:
            return -1
        