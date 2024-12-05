class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        
        start_LRs= [(c, i) for i,c in enumerate(start) if c!= 'X']
        result_LRs= [(c,i) for i,c in enumerate(result) if c!= 'X']
        
        if len(start_LRs) != len(result_LRs):
            return False
        
        for start_c, result_c in zip(start_LRs, result_LRs):
            if start_c[0] != result_c[0]:
                # Check both L or R
                return False
            # Now both are L or both are R
            elif result_c[0] == "L":
                if start_c[1] < result_c[1]:
                    return False
                
            elif result_c[0] == "R":
                if start_c[1] > result_c[1]:
                    return False
        
        return True
        