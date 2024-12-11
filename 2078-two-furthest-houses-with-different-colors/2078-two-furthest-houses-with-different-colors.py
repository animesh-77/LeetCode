class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        
        minColHouse= {}
        maxColHouse= {}
        
        for pos, color in enumerate(colors):
            
            minColHouse[color]= min(minColHouse.get(color, pos), pos)
            maxColHouse[color]= max(maxColHouse.get(color, pos), pos)
            
        uniqueCol= list(minColHouse.keys())
        maxDist= 0
        
        for pos, color in enumerate(colors):
            
            for othColor in uniqueCol:
                if othColor == color:
                    continue
                    
                distToMin= abs(pos- minColHouse[othColor]) 
                distToMax= abs(pos- maxColHouse[othColor])
                
                maxDist= max(maxDist, (max(distToMin, distToMax)))
        
                
        return maxDist
                
            
        