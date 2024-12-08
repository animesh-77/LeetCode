class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        import bisect 
        
        events.sort(key= lambda x: x[0])
        n= len(events)
        maxFromStartTime= [events[-1][2]]* n
        
        for pos in range(n-2, -1, -1):
            maxFromStartTime[pos]= max(maxFromStartTime[pos+1], events[pos][2])

        
        maxValue= 0
        
        for start, end, val in events:
            
            # first event that starts after current one ends
            idx= bisect.bisect_right(events, end, key= lambda x: x[0])
            
            if idx < n:
                # we found a suitable position
                combinedVal= val+ maxFromStartTime[idx]
            else:
                combinedVal= val
                
                
            maxValue= max(maxValue, combinedVal)
            
        return maxValue
                    
                                     